import requests
from datetime import datetime
import locale
import json
import sys
import sqlite3
import os
API_KEY ="trnsl.1.1.20190822T122346Z.56c731cbcdbda49a.c11be907a06454d65951478974febf9bca666b61"
URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"

class Translete():
    def __init__(self, *args, **kwargs):
        if kwargs.get("Word"):
            self.url = "{0}?key={1}&text={2}&ui=ru".format(URL, API_KEY, f"q={kwargs['Word']}")

    def get_date(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.date = response.json()
        else:
            self.date = {}


    def create_db(path):
        if not os.path.isfile(path):
            with open(path, "wb") as file:
                pass
        return

    def get_connect(path):
        connect = sqlite3.connect(path)
        return connect

    def create_table(connect):
        sql_translate = """CREATE TABLE IN NOT EXISTS "Translate" (
            "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "word_in" TEXT NOT NULL,
            "word_out" TEXT NOT NULL,
        );
        """
        cursor = connect.cursor()
        cursor.execute(sql_translate)
        connect.commit()

    def get_data(path):
    json_file = open(path, "r")
    data = json.load(json_file)
    json_file.close()
    return data

    def send_data(element, connect):
        sql = f"""INSERT INTO "Translate" (
            "word_in",
            "word_out",
        )
        VALUES (
            "{element['{2}']}",
            "{element['text']}",
        );
        """
        cursor = connect.cursor()
        cursor.execute(sql)
        connect.commit()

if __name__ == "__main__":
    obj = Translete(text= "Word")
    print(obj.url)
    obj.get_date()
    print(obj.date)
    obj.create_response()
