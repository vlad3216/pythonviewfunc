from utils import execute_query, unwrapper

from typing import List


def get_employees() -> List:
    '''
    Get employees
    :return: changes list
    '''
    query_sql = '''
        SELECT *
          FROM employees;
    '''
    return execute_query(query_sql)


# unwrapper(get_employees())


def get_filtered_customers(city=None,
                           state=None) -> List:
    '''
    customers return
    :param city: city, str
    :param state: state, str
    :return: customers list
    '''
    query_sql = '''
        SELECT *
          FROM customers
    '''
    if city and state:
        query_sql += f" WHERE City = '{city}' AND State = '{state}';"
    elif city:
        query_sql += f" WHERE City = '{city}';"
    elif state:
        query_sql += f" WHERE State = '{state}';"
    return execute_query(query_sql)


# unwrapper(get_filtered_customers(state='SP', city='São Paulo'))


def get_unique_customers_by_sql() -> List:
    query_sql = '''
        SELECT distinct FirstName
          FROM customers;
    '''
    return execute_query(query_sql)


# unwrapper(get_unique_customers_by_sql())


def get_unique_customers_by_python() -> List:
    query_sql = '''
            SELECT distinct FirstName
              FROM customers;
    '''
    records = execute_query(query_sql)
    unique_names = set()
    for record in records:
        unique_names.add(record[0])
    return list(unique_names)


# unwrapper(get_unique_customers_by_python())

def get_count_of_firstname() -> List:
    '''
    unique names
    '''
    query_sql = '''
                SELECT FirstName, COUNT(FirstName)
                FROM customers
                GROUP BY FirstName;
    '''
    return execute_query(query_sql)


def get_all_profit() -> float:
    '''
    orders summ from invoice_items
    '''
    query_sql = '''
                SELECT SUM(UnitPrice * Quantity)
                FROM invoice_items;
    '''
    return execute_query(query_sql)