import pyodbc
import sys
import readCSV
import os
import tkinter as tk


def open_driver():
    os.startfile('C:\Windows\SysWOW64\odbcad32.exe',)


def verify_dsn_source():
    sources = pyodbc.dataSources()
    dsns = sources.keys()
    data_source_list = []
    for key in dsns:
        data_source_list.append(key)
    if data_source_list.count("Delta ODBC 4") == 1:
        return True
    elif data_source_list.count("Delta ODBC 4") == 0:
        return False


def create_points(dev_id, master):
    points_list = readCSV.read_csv_file(dev_id)
    sql_list = []

    # Loop thru points list and execute sql statements
    for row in range(len(points_list)):
        try:
            point = readCSV.determine_point_type(points_list[row][1])
            sql_list = points_list[row]
            if sql_list[3] != '' and (point == "AO" or point == "AI" or point == "BO" or point == "BI"):
                sql = f"INSERT INTO OBJECT_V4_{point} (DEV_ID, Object_Identifier, Object_Name, Type_Reference) " \
                      f"VALUES ({sql_list[0]},'{sql_list[1]}','{sql_list[2]}','{sql_list[3]}') "
                conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
                cursor = conn.cursor()
                cursor.execute(sql)
                cursor.close()
                conn.close()
                label = tk.Label(master, text=sql_list, bg='white')
                label.grid(column=0, sticky="w")
            elif sql_list[3] != '' and point == "AV":
                sql = f"INSERT INTO OBJECT_V4_{point} (DEV_ID, Object_Identifier, Object_Name, Units) " \
                      f"VALUES ({sql_list[0]},'{sql_list[1]}','{sql_list[2]}','{sql_list[3]}') "
                conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
                cursor = conn.cursor()
                cursor.execute(sql)
                cursor.close()
                conn.close()
                label = tk.Label(master, text=sql_list, bg='white')
                label.grid(column=0, sticky="w")
            else:
                sql_list.pop()
                sql = f"INSERT INTO OBJECT_V4_{point} (DEV_ID, Object_Identifier, Object_Name) " \
                      f"VALUES ({sql_list[0]},'{sql_list[1]}','{sql_list[2]}') "
                conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
                cursor = conn.cursor()
                cursor.execute(sql)
                cursor.close()
                conn.close()
                label = tk.Label(master, text=sql_list, bg='white')
                label.grid(column=0, sticky="w")
        except:
            label = tk.Label(master, text=f"failed to create {sql_list[1]} ,{sql_list[2]}", bg='white')
            label.grid(column=0, sticky="w")
    return


def view_controller_points(dev_id):
    pl = []
    sql_list = [
        f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AI WHERE DEV_ID = {dev_id}",
        f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AO WHERE DEV_ID = {dev_id}",
        f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_BI WHERE DEV_ID = {dev_id}",
        f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_BO WHERE DEV_ID = {dev_id}",
        f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AV WHERE DEV_ID = {dev_id}",
        f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_BV WHERE DEV_ID = {dev_id}",
        f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AIC WHERE DEV_ID = {dev_id}",
        f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AOC WHERE DEV_ID = {dev_id}",
        f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_BDC WHERE DEV_ID = {dev_id}"
        ]

    for i in range(len(sql_list)):
        conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
        cursor = conn.cursor()
        cursor.execute(sql_list[i])
        for row in cursor.fetchall():
            pl.append(row)

        cursor.close()
        conn.close()

    if not pl:
        print("Device does not exist.\n")
    else:
        for i in range(len(pl)):
            print(pl[i])
    return

def delete_points():
    pass
