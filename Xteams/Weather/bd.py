#!/usr/bin/python3
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
    	"country_name"	TEXT,
    	"city_name"	TEXT ,
    	"country_code"	TEXT NOT NULL,
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

def send_data(element, connect):
    sql = f"""INSERT INTO "location" (
    "country_code",
    "city",
    "lat",
    "lon")
    VALUES ("{element['country']}", "{element['name']}", {element['coord']['lat']}, {element['coord']['lon']})"""
    cursor = connect.cursor()
    cursor.execute(sql)
    # connect.commit()


if __name__=="__main__":
    if len(sys.argv) > 2:
        path = os.path.join(sys.argv[1], sys.argv[2])
        create_db(path)
        connection = get_connect(path)
        create_table(connection)
        data = get_date("city.list.json")
        len_date = len(data)
        for id, element in enumerate(data, 1):
            print(f"{id} from {len_date}", end="\r")
            try:
                send_data(element, connection)
            except Exception as e:
                print("Error SQL")
                print(element)
                print(e)
        connection.commit()
        print("/nOK")
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
