from sqlalchemy import create_engine, Column, String, MetaData
from sqlalchemy.orm import sessionmaker

# Create an engine
engine = create_engine('sqlite:///ars_draft2.db')

# Connect to the database
conn = engine.connect()

# Create a metadata object
metadata = MetaData()

# Reflect the tables from the database
metadata.reflect(bind=engine)

# Loop through the tables and print the contents
for table_name, table in metadata.tables.items():
    print(f"Table: {table_name}")
    print("-" * 50)

    # Select all rows from the table
    select_query = table.select()
    result = conn.execute(select_query)
    column_names = table.columns.keys()
    print("Column names: ")
    print(column_names)
    # Fetch and print the data
    for row in result:
        print(row)
        for each_ in row:
            print(each_)
        print("\n")


# Close the connection
conn.close()
