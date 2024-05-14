
#%%
import argparse
import pandas as pd
import sys

#%%
# Simulate command line arguments using sys.argv
# Replace these with actual arguments when running the script standalone
# simulated_argv = [
#     'script_name.py', 
#     '--output','database', 
#     '--db_host', 'localhost', 
#     '--db_name', 'mydb', 
#     '--db_user', 'user', 
#     '--db_password', 'password'
#     ]
simulated_argv = [
    'script_name.py', 
    '--output','csv', 
    '--csv_path', 'somefile.csv'
    ]




#%%

# Define the ArgumentParser
parser = argparse.ArgumentParser(description="Export Data to Database or CSV")

# Add Main Arguments
parser.add_argument("--output", type=str, choices=['database', 'csv'], help="Choose output type: database or csv", required=True)

# Sub-parameters for database
parser.add_argument("--db_host", type=str, help="Database host address")
parser.add_argument("--db_name", type=str, help="Name of the database")
parser.add_argument("--db_user", type=str, help="Database user name")
parser.add_argument("--db_password", type=str, help="Database password")

# Sub-parameter for csv
parser.add_argument("--csv_path", type=str, help="Path to save the CSV file")


# Temporarily replace sys.argv for testing purposes
original_argv = sys.argv
sys.argv = simulated_argv
args = parser.parse_args()

# Restore sys.argv to its original state
sys.argv = original_argv

# Assume df is a pandas DataFrame you want to export
df = pd.DataFrame({ 'A': ['foo', 'bar', 'baz'], 'B': ['one', 'two', 'three'] })

if args.output == 'database':
    if args.db_host is None or args.db_name is None or args.db_user is None or args.db_password is None:
        print("Database connection details are missing.")
    else:
        print(f"Exporting data to database at {args.db_host}/{args.db_name} as user {args.db_user}")
        # Implement code to export dataframe df to specified database
        
elif args.output == 'csv':
    if args.csv_path is None:
        print("CSV file location is missing.")
    else:
        print(f"Exporting data to CSV at {args.csv_path}")
        # Implement code to export dataframe df to specified CSV path
else:
    print("Invalid output type chosen.")
# %%
