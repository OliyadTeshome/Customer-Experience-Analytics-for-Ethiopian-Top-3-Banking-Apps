# src/database.py
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def get_engine():
    user = "bankapp_user"
    password = "pa55w0rd"
    host = "localhost"
    port = 1521
    service_name = "XEPDB1"

    oracle_url = f"oracle+oracledb://{user}:{password}@{host}:{port}/?service_name={service_name}"
    engine = create_engine(oracle_url)
    return engine

def insert_dataframe(df, table_name, engine, if_exists="append"):
    """
    Insert a pandas DataFrame into an Oracle table with commit handling.

    Args:
        df (pd.DataFrame): DataFrame to insert.
        table_name (str): Target table name.
        engine: SQLAlchemy engine.
        if_exists (str): 'append', 'replace', or 'fail'.
    """
    try:
        with engine.begin() as connection:  # begin() handles commit/rollback
            df.to_sql(name="bank_reviews_cleaned", con=connection, if_exists=if_exists, index=False)
        print(f"Data inserted successfully into '{table_name}'.")
    except SQLAlchemyError as e:
        print(f"Error inserting data into '{table_name}': {e}")