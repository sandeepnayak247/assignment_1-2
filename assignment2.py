import pandas as pd
from sqlalchemy import create_engine, types
import pymysql

DB_USERNAME = 'root'
DB_PASSWORD = 'Sandeep@9524'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_DATABASE = 'db_2'

CSV_FILE_PATH = 'path/to/your/large_file.csv'

connection_str = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'

engine = create_engine(connection_str)

def create_table():
    
    table_schema = {
        'column1': types.Integer(),
        'column2': types.String(length=100),
        'column3': types.Float(),
        'column4': types.DateTime()
    }
    
    with engine.connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS your_table_name (
                column1 INT,
                column2 VARCHAR(100),
                column3 FLOAT,
                column4 DATETIME
                -- Define more columns as needed
            )
        """)

def insert_data(chunk):
    chunk.to_sql('your_table_name', con=engine, if_exists='append', index=False)

def main():
    
    create_table()

    chunk_size = 100000  
    csv_reader = pd.read_csv(CSV_FILE_PATH, chunksize=chunk_size)

    for i, chunk in enumerate(csv_reader):
        print(f'Processing chunk {i+1}')
        insert_data(chunk)

    print('Data insertion completed.')

if __name__ == '__main__':
    main()
