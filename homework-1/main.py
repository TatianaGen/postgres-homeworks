import csv
import os
import psycopg2

bd = ['employees_data.csv', 'customers_data.csv', 'orders_data.csv']
bd_name = ['employees', 'customers', 'orders']


def add_data_in_bd(database, database_name):
    """Скрипт для заполнения данными таблиц в БД Postgres."""
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='qwer')
    try:
        with conn:
            with conn.cursor() as cur:

                for item in range(len(bd)):
                    with open(os.path.join('north_data', database[item]), 'r') as csvfile:
                        header = next(csvfile)
                        csvreader = csv.reader(csvfile)
                        for row in csvreader:
                            values = '%s, ' * len(row)
                            cur.execute(f"INSERT INTO {database_name[item]} VALUES ({values[:-2]})", row)
                        conn.commit()
    finally:
        conn.close()


if __name__ == '__main__':
    add_data_in_bd(bd, bd_name)
