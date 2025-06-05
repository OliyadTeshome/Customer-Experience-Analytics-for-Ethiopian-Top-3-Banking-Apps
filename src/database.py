from sqlalchemy import create_engine
import pandas as pd

def store_to_oracle(df, table_name, user, password, dsn):
    engine = create_engine(f'oracle+cx_oracle://{user}:{password}@{dsn}')
    df.to_sql(table_name, con=engine, if_exists='append', index=False)