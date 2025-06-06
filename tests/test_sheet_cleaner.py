import pandas as pd
import pytest
from src.sheet_cleaner import SheetCleaner

def test_clean_sheet_removes_empty_rows_and_columns():
    # Create a DataFrame with empty rows and columns
    df = pd.DataFrame({
        'A': [1, None, 3],
        'B': [None, None, None],
        'C': [4, None, 6]
    })
    df.loc[3] = [None, None, None]  # Add an empty row

    cleaner = SheetCleaner({'test': df})
    cleaned = cleaner.clean_sheet(df)

    # B should be dropped (all None), row 3 should be dropped
    assert 'B' not in cleaned.columns
    assert cleaned.shape[0] == 2  # Only rows 0 and 2 remain

def test_clean_sheet_strips_column_headers():
    df = pd.DataFrame({' Col A ': [1, 2], 'Col B': [3, 4]})
    cleaner = SheetCleaner({'test': df})
    cleaned = cleaner.clean_sheet(df)
    assert 'Col A' in cleaned.columns
    assert ' Col A ' not in cleaned.columns

def test_validate_sheet_passes_for_required_columns():
    df = pd.DataFrame({'A': [1], 'B': [2]})
    cleaner = SheetCleaner({'test': df})
    assert cleaner.validate_sheet(df, ['A', 'B']) is True

def test_validate_sheet_raises_for_missing_columns():
    df = pd.DataFrame({'A': [1], 'B': [2]})
    cleaner = SheetCleaner({'test': df})
    with pytest.raises(ValueError):
        cleaner.validate_sheet(df, ['A', 'C'])  # 'C' is missing

def test_clean_all_cleans_multiple_sheets():
    df1 = pd.DataFrame({'A': [1, None], 'B': [None, None]})
    df2 = pd.DataFrame({'X ': [2], ' Y': [3]})
    df_dict = {'sheet1': df1, 'sheet2': df2}
    cleaner = SheetCleaner(df_dict)
    cleaned = cleaner.clean_all()
    assert 'B' not in cleaned['sheet1'].columns
    assert 'X' in cleaned['sheet2'].columns
    assert ' Y' not in cleaned['sheet2'].columns

