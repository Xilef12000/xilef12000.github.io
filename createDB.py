import os
import sqlite3 as sl

os.system("rm content.db")
con = sl.connect("content.db", check_same_thread=False)

with con:
    con.execute("""
            CREATE TABLE CONTENT (
                id TEXT PRIMARY KEY,
                title TEXT,
                head TEXT,
                header TEXT,
                body TEXT,
                footer TEXT
            );
            """)