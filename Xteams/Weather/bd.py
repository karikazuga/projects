import json
import sys
import sqlite3
import os


def create_db(path):
    if not os.path.isfile(path):
        with open(path, "wb") as file:
            pass
    return

def get_connect(path):
    connect = sqlite3.connect(path)
    return connect

def create_table(connect):
    sql = f"""CREATE TABLE IF NOT EXISTS "location" (
    	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    	"country_name"	TEXT  UNIQUE,
    	"city_name"	TEXT ,
    	"country_code"	TEXT NOT NULL UNIQUE,
    	"city"	TEXT NOT NULL,
    	"lat"	REAL NOT NULL,
    	"lon"	REAL NOT NULL
    );"""
    cursor = connect.cursor()
    cursor.execute(sql)
    connection.commit()

def get_date(path):
    json_file = open(path, "r")
    data = json.load(json_file)
    json_file.close()
    return data

def send_data(element):
    sql = f"""INSERT INTO "location" (
    "country_code",
    "city",
    "lat",
    "lon")
    VALUE ("{element['country']}", "{element['name']}", {element['coord']['lat']}, {element['coord']['lon']})"""
    print(sql)
if __name__=="__main__":
    if len(sys.argv) > 2:
        path = os.path.join(sys.argv[1], sys.argv[2])
        create_db(path)
        connection = get_connect(path)
        create_table(connection)
        data = get_date("city.list.json")
        for element in data[:2]:
            send_data(element)
        print("OK")
    else:
        print("Not arguments")
    # if len(sys.argv) > 1:
    #     file = open("city.list.json", "r")
    #     cities = json.load(file)
    #     print(len(cities))
    #     print(cities[0])
    # else:
    #     print("НЕТ аргументов")
    #     exit()
