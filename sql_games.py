import sqlite3
import json


SQL_commands = {
    'create': """CREATE TABLE sample_table (
                 ID INTEGER primary key,
                 FULLNAME TEXT,
                 AGE INTEGER,
                 INFO TEXT);""",
    'insert': """INSERT INTO sample_table
                 (ID, FULLNAME, AGE, INFO)
                 VALUES
                 (?, ?, ?, ?)""",
    'update': """UPDATE sample_table set INFO = ? where ID = ?""",
    'delete': """DELETE from sample_table where ID = ?""",
    'select': """SELECT * from sample_table"""
                }


SQL_coloumns = ('ID', 'FULLNAME', 'AGE', 'INFO')
SQL_dict = dict()


try:
    connection = sqlite3.connect('database_sample.db')
    cursor = connection.cursor()
    print('SQL Connected')

    cursor.execute(SQL_commands['select'])
    data_fromSQL = cursor.fetchall()
    for id, data in enumerate(data_fromSQL, 1):
        SQL_dict[id] = {column: value for column, value in zip(SQL_coloumns, data)}

    cursor.close()
    connection.commit()
    print('Read Data from SQL')
except sqlite3.Error as err:
    print('Error:', err)
finally:
    connection.close()
    print('SQL Disconnected \n')


with open('data_from_SQL.json', 'w', encoding='UTF-8') as json_file:
    json.dump(SQL_dict, json_file, ensure_ascii=True, indent=4)
    print('JSON file with data from SQL created \n')


with open('data_from_SQL.json', 'r', encoding='UTF-8') as json_file:
    data_from_json_file = json.load(json_file)  # is a dict
    print('Data from JSON file loaded and represented as a dict "data_from_json_file":')
    print(data_from_json_file, '\n')


print('USERS DATA from SQL\JSON:\n---')
for userdata in data_from_json_file.values():
    for key, value in userdata.items():
        print(f'{key} == {value}')
    print('---')
print('END OF USERS DATA')