#%%
import argparse
import pandas as pd
import sys

#%%
# Sample DataFrame to export
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'score': [85, 90, 78],
}
df = pd.DataFrame(data)

#%%
# Simulate command line arguments
sys.argv = [
    'export_data.py',  # Script name (typically ignored)
    'csv',
    '--file', 'somepath.csv'
    # 'database',        # Subcommand (either 'csv' or 'database')
    # '--type', 'sqlite',
    # '--name', 'simulated_database.db',
    # '--table', 'simulated_table'
]

#%%

# Set up argument parser
parser = argparse.ArgumentParser(description="Export data to either a database or a CSV file.")
subparsers = parser.add_subparsers(dest='output', required=True, help="Output format")

# CSV output subparser
csv_parser = subparsers.add_parser('csv', help="Export to a CSV file")
csv_parser.add_argument('--file', required=True, help="Path to the CSV file")

# Database output subparser
db_parser = subparsers.add_parser('database', help="Export to a database")
db_parser.add_argument('--type', required=True, choices=['sqlite', 'postgres'], help="Type of database")
db_parser.add_argument('--name', required=True, help="Name of the database or connection string")
db_parser.add_argument('--table', required=True, help="Name of the table to export data into")

# Parse arguments
args = parser.parse_args()

# Handle CSV output
if args.output == 'csv':
    output_file = args.file
    # df.to_csv(output_file, index=False)
    print(f"Data successfully exported to CSV file: {output_file}")

# Handle Database output
elif args.output == 'database':
    if args.type == 'sqlite':
        db_path = args.name
        # conn = sqlite3.connect(db_path)
        # df.to_sql(args.table, conn, if_exists='replace', index=False)
        # conn.close()
        print(f"Data successfully exported to SQLite database: {db_path}, table: {args.table}")
    elif args.type == 'postgres':
        #import psycopg2
        from sqlalchemy import create_engine
        
        # Assuming args.name contains a full connection string for PostgreSQL
        db_url = args.name
        # engine = create_engine(db_url)
        # df.to_sql(args.table, engine, if_exists='replace', index=False)
        print(f"Data successfully exported to PostgreSQL database: {db_url}, table: {args.table}")# %%

# %%
