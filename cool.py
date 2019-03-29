import xmltodict, marshmallow
import sqlite3
import time
import datetime
import random


def read_xml():
    cool_xml = None

    with open("cool.xml", "r") as f:
        cool_xml = f.read()

    my_cool_dict = xmltodict.parse(cool_xml)

    marshmallow.pprint(my_cool_dict)


def create_table(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)"
    )


def data_entry(cursor):
    cursor.execute(
        "INSERT INTO stuffToPlot VALUES(145, '2016-01-01', 'Python', 5)")


def dynamic_data_entry(cursor):
    unix = time.time()
    date = str(
        datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
    keyword = 'Python'
    value = random.randrange(0, 10)
    cursor.execute(
        "INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
        (unix, date, keyword, value))


def read_from_db(cursor):
    cursor.execute("SELECT * FROM stuffToPlot")
    data = cursor.fetchall()
    print(data)


if __name__ == "__main__":
    conn = sqlite3.connect("tutorial.db")
    c = conn.cursor()

    create_table(c)

    data_entry(c)
    dynamic_data_entry(c)
    conn.commit()

    read_from_db(c)

    c.close()
    conn.close()
