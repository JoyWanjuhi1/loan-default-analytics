import pandas as pd

# Paste your exact Windows file path here (the 'r' before the string handles the backslashes)
file_path = r"C:\Users\user\loan-default-analytics\Default_Fin.csv"

print(f"Loading dataset from: {file_path}\n" + "="*50)

try:
    # Load the data
    df = pd.read_csv(file_path)
    
    # Display dataset details
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
    print("Columns and Data Types:")
    print(df.dtypes)
    print("\nFirst 5 Rows:")
    print(df.head())

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}. Double-check the folder and file name!")