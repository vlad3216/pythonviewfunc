import sqlite3
import os

from typing import List


def execute_query(query_sql: str) -> List:
    '''
    main func
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    '''
    result func
    '''
    for record in records:
        print(*record)