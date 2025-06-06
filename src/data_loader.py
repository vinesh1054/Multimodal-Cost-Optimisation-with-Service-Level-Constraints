import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("data_loader.log"),
        logging.StreamHandler()
    ]
)

class DataLoader:
    """
    Loads all relevant sheets from the supply chain Excel workbook as raw DataFrames.
    """

    SHEET_NAMES = [
        "OrderList",
        "FreightRates",
        "PlantPorts",
        "ProductsPerPlant",
        "VmiCustomers",
        "WhCapacities",
        "WhCosts"
    ]

    def __init__(self, file_path):
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")
        self.file_path = file_path

    def load_sheets(self):
        """
        Loads all defined sheets as raw DataFrames.
        Returns:
            dict: {sheet_name: DataFrame}
        """
        logging.info("Loading Excel sheets: %s", self.SHEET_NAMES)  
        try:
            # Use pandas ExcelFile context for efficiency if loading multiple sheets[2][1]
            with pd.ExcelFile(self.file_path) as xls:
                data = {name: pd.read_excel(xls, sheet_name=name) for name in self.SHEET_NAMES}
            logging.info("Sheets loaded: %s", list(data.keys()))
            return data
        except Exception as e:
            logging.error(f"Failed to load Excel: {e}")
            raise

# Example usage for testing
if __name__ == "__main__":
    data_path = os.path.join("..", "data", "Supply chain logistics problem.xlsx")
    try:
        loader = DataLoader(data_path)
        sheets = loader.load_sheets()
        for name, df in sheets.items():
            print(f"\n--- {name} ---\n", df.head())
    except Exception as e:
        logging.error(f"Data loading failed: {e}")
