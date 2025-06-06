from src.data_loader import DataLoader

def main():
    # Set the path to your Excel file
    data_path = 'D:\\01 VINESH_0\\Machine Learning\\Projects\\ML\\RouteOptimisation\\data\\Supply chain logistics problem.xlsx'
    
    # Initialize the DataLoader and load all sheets
    try:
        loader = DataLoader(data_path)
        raw_sheets = loader.load_sheets()
        
        # Print a preview of each sheet (for confirmation)
        for name, df in raw_sheets.items():
            print(f"\n--- {name} ---\n", df.head()git commit git commit -m "data" )
        
        # TODO: Pass these raw DataFrames to your cleaning functions in sheet_cleaner.py
        # Example:
        # from src import sheet_cleaner
        # cleaned_orderlist = sheet_cleaner.clean_orderlist(raw_sheets["OrderList"])
        # ... etc ...
        
    except Exception as e:
        print(f"[FATAL] Pipeline failed: {e}")

if __name__ == "__main__":
    main()
