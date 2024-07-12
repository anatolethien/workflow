import sqlite3


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def save(
    df: pd.DataFrame,
    table_name: str,
):
    conn = sqlite3.connect("data/db.sqlite3")
    df.to_sql(
        name=table_name,
        con=conn,
        index=False,
        if_exists="replace",
    )
    conn.close()
