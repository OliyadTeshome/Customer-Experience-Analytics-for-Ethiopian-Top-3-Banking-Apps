# src/database.py

import pandas as pd
import oracledb
from src.utils import log_step

def check_or_create_table(table_name, conn_str):
    """
    Ensures that the target table exists in Oracle DB.
    If it does not, creates it.

    Args:
        table_name (str): Name of the target table.
        conn_str (str): Oracle connection string.
    """
    create_sql = f"""
    BEGIN
        EXECUTE IMMEDIATE '
            CREATE TABLE {table_name} (
                id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                review CLOB,
                rating NUMBER,
                review_date DATE,
                app_name VARCHAR2(100)
            )
        ';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -955 THEN
                RAISE;
            END IF;
    END;
    """

    try:
        with oracledb.connect(conn_str) as connection:
            with connection.cursor() as cursor:
                cursor.execute(create_sql)
                log_step(f"Table '{table_name}' is ready.")
    except Exception as e:
        log_step(f"Error ensuring table: {e}")
        raise

def insert_reviews_to_oracle(df: pd.DataFrame, table_name: str, conn_str: str):
    """
    Inserts a DataFrame of reviews into Oracle DB.

    Args:
        df (pd.DataFrame): DataFrame containing review data.
        table_name (str): Oracle table name.
        conn_str (str): Oracle connection string.
    """
    insert_sql = f"""
    INSERT INTO {table_name} (review, rating, review_date, app_name)
    VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)
    """

    data = [
        (row['review'], row['rating'], row['date'], row['app_name'])
        for _, row in df.iterrows()
    ]

    try:
        with oracledb.connect(conn_str) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(insert_sql, data)
                connection.commit()
                log_step(f"Inserted {len(df)} rows into '{table_name}'.")
    except Exception as e:
        log_step(f"Error inserting data: {e}")
        raise