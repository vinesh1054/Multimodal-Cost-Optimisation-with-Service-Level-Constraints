import pandas as pd

class SheetCleaner:
    def __init__(self, df_dict):
        """
        Initialize with a dictionary of DataFrames.
        Args:
            df_dict (dict): Dictionary where keys are sheet names and values are DataFrames.
        """
        self.df_dict = df_dict

    def clean_all(self):
        """
        Clean all DataFrames in the dictionary.
        Returns:
            dict: Cleaned DataFrames with the same keys as input.
        """
        cleaned_dfs = {}
        for sheet_name, df in self.df_dict.items():
            cleaned_df = self.clean_sheet(df)
            cleaned_dfs[sheet_name] = cleaned_df
        return cleaned_dfs

    def clean_sheet(self, df):
        """
        Clean a single DataFrame.
        Steps:
            - Drop completely empty rows and columns
            - Strip whitespace from headers
            - Reset index
        Args:
            df (pd.DataFrame): Raw DataFrame
        Returns:
            pd.DataFrame: Cleaned DataFrame
        """
        # Drop completely empty rows and columns
        df = df.dropna(how='all')
        df = df.dropna(axis=1, how='all')

        # Strip whitespace from headers if they are strings
        df.columns = [col.strip() if isinstance(col, str) else col for col in df.columns]

        # Reset index
        df = df.reset_index(drop=True)

        # Additional cleaning steps can be added here

        return df

    def validate_sheet(self, df, required_columns):
        """
        Validate that required columns exist in the DataFrame.
        Args:
            df (pd.DataFrame): DataFrame to validate
            required_columns (list): List of columns that must be present
        Returns:
            bool: True if validation passes, raises ValueError otherwise
        """
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        return True

# Example usage:
# cleaner = SheetCleaner(df_dict)
# cleaned_dfs = cleaner.clean_all()
# for sheet, df in cleaned_dfs.items():
#     cleaner.validate_sheet(df, required_columns=['Column1', 'Column2'])
