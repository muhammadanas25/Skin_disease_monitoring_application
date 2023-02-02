
import sqlite3
from sqlite3 import Connection
from db.queries import CREATE_TABLE, INSERT_DUMMY_ENTRIES
import streamlit as st
import pandas as pd
import os

URI_SQLITE_DB = os.environ.get("DB_NAME", "test_db")


@st.cache(hash_funcs={Connection: id})
def get_connection(path: str):
    """Put the connection in cache to reuse if path does not change between Streamlit reruns.
    """
    return sqlite3.connect(path, check_same_thread=False)


def init_db(conn: Connection = get_connection(URI_SQLITE_DB)):
    conn.execute(CREATE_TABLE)
    conn.commit()
    
def populate_db(conn: Connection = get_connection(URI_SQLITE_DB)):
    conn.execute(INSERT_DUMMY_ENTRIES)
    conn.commit()
    return True


conn = get_connection(URI_SQLITE_DB)

def get_data(query, conn: Connection = get_connection(URI_SQLITE_DB)):
    return pd.read_sql(query, con=conn)

def insert_data(query, conn: Connection = get_connection(URI_SQLITE_DB)):
    conn.execute(query)
    conn.commit()
    return True