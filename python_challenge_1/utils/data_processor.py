import pandas as pd
import os

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None


    def read_file(self):
            while True:
                try:
                    file_path = input("Enter file path: ")
                    if os.path.isfile(file_path):
                        self.file_path = file_path
                        if self.file_path.endswith('.csv'):
                            self.data = pd.read_csv(self.file_path)
                        elif self.file_path.endswith('.parquet'):
                            self.data = pd.read_parquet(self.file_path)
                        elif self.file_path.endswith('.xlsx'):
                            self.data = pd.read_excel(self.file_path)
                        else:
                            print(
                                "Unsupported file format. Please provide a file with format .csv, .parquet, or .xlsx.")
                            continue
                        break
                    else:
                        print("Invalid file path. Please enter a valid file path.")
                except Exception as e:
                    print(f"Error reading file: {e}")
    def detect_schema(self):
        try:
            print(self.data.dtypes)
        except Exception as e:
            print(f"Error detecting schema: {e}")

    def transform_to_table(self):
        try:
            return pd.DataFrame(self.data)
        except Exception as e:
            print(f"Error transforming data to table: {e}")

    def choose_storage_format(self):
        while True:
            try:
                choice = input(
                    "Choose storage format (CSV, Parquet, or Excel): ").lower()
                if choice in ['csv', 'parquet', 'excel']:
                    return choice
                else:
                    print("Invalid choice. Please choose from CSV, Parquet, or Excel.")
            except Exception as e:
                print(f"Error choosing storage format: {e}")

    def upload_file(self, storage_format):
        try:
            if storage_format == 'csv':
                self.data.to_csv(r'output\output.csv', index=False)
            elif storage_format == 'parquet':
                self.data.to_parquet(r'output\output.parquet', index=False)
            elif storage_format == 'excel':
                self.data.to_excel(r'output\output.xlsx', index=False)
            print("File uploaded successfully.")
        except Exception as e:
            print(f"Error uploading file: {e}")
