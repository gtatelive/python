#%%
# Simulate command line arguments using sys.argv
# Replace these with actual arguments when running the script standalone
simulated_argv = [
    'script_name.py', 
    '--output','database', 
    '--server', 'server.domain.com', 
    '--table',  'table', 
    '--port', '1433', 
    ]
# simulated_argv = [
#     'script_name.py', 
#     '--output','csv', 
#     '--fileName', 'somefile.csv',
#     '--filePath', 'c:\\temp\\'
#     ]




#%%

# Define the ArgumentParser
parser = argparse.ArgumentParser(description="Export Data to Database or CSV")

# Add Main Arguments
parser.add_argument("--output", type=str, choices=['database', 'csv'], help="Choose output type: database or csv", required=True)

# Sub-parameter for csv
parser.add_argument("--fileName", type=str, help="Name of the CSV file")
parser.add_argument("--filePath", type=str, help="Path to save the CSV file")


# Sub-parameters for database
parser.add_argument("--server", type=str, help="FQDN of Database Server")
parser.add_argument("--table", type=str, help="Name of the database table")
parser.add_argument("--port", type=str, help="Database port")




# Temporarily replace sys.argv for testing purposes
original_argv = sys.argv
sys.argv = simulated_argv
args = parser.parse_args()

# Restore sys.argv to its original state
sys.argv = original_argv

# Assume df is a pandas DataFrame you want to export
df = pd.DataFrame({ 'A': ['foo', 'bar', 'baz'], 'B': ['one', 'two', 'three'] })

if args.output == 'database':
    if args.server is None or args.table is None or args.port is None:
        print("Database connection details are missing.")
    else:
        print(f"Exporting data to database at {args.server}/{args.table} on port {args.port}")
        # Implement code to export dataframe df to specified database
        
elif args.output == 'csv':
    if args.fileName is None:
        print("CSV file location is missing.")
    else:
        print(f"Exporting data to CSV at {args.fileName}")
        # Implement code to export dataframe df to specified CSV path
else:
    print("Invalid output type chosen.")
# %%
