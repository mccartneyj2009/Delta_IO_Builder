import pyodbc
import readCSV
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def open_driver():
    os.startfile('C:\Windows\SysWOW64\odbcad32.exe')


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


def query_for_sites():
    conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
    cursor = conn.cursor()
    cursor.execute('Select SITE_ID from OBJECT_V4_NET')
    start_list_sites = []
    inter_list_sites = []
    final_list_sites = []
    for row in cursor.fetchall():
        start_list_sites.append(row)
    for i in start_list_sites:
        if i not in inter_list_sites:
            inter_list_sites.append(i)
    for site in inter_list_sites:
        final_list_sites.append(site[0])

    cursor.close()
    conn.close()
    return final_list_sites


def create_points(dev_id, master, site_id):
    if site_id != '':
        points_list = readCSV.read_csv_file(dev_id)
        sql_list = []

        time = datetime.now().strftime("%H:%M:%S")
        start_label = tk.Label(master, text=f"*****Points creation started for site {site_id}. {time}*****", bg='white')
        start_label.grid(column=0, sticky="w")

        # Loop thru points list and execute sql statements
        for row in range(len(points_list)):
            try:
                point = readCSV.determine_point_type(points_list[row][1])
                sql_list = points_list[row]
                if sql_list[3] != '' and (
                        point == "AO" or point == "AI" or point == "BO" or point == "BI") and site_id != '':
                    sql = f"INSERT INTO OBJECT_V4_{point} (DEV_ID, Object_Identifier, Object_Name, Type_Reference, " \
                          f"SITE_ID) " \
                          f"VALUES ({sql_list[0]},'{sql_list[1]}','{sql_list[2]}','{sql_list[3]}', '{site_id}') "
                    conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
                    cursor = conn.cursor()
                    cursor.execute(sql)
                    cursor.close()
                    conn.close()
                    label = tk.Label(master, text=sql_list, bg='white')
                    label.grid(column=0, sticky="w")
                elif sql_list[3] != '' and point == "AV" and site_id != '':
                    sql = f"INSERT INTO OBJECT_V4_{point} (DEV_ID, Object_Identifier, Object_Name, Units, SITE_ID) " \
                          f"VALUES ({sql_list[0]},'{sql_list[1]}','{sql_list[2]}','{sql_list[3]}', '{site_id}) "
                    conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
                    cursor = conn.cursor()
                    cursor.execute(sql)
                    cursor.close()
                    conn.close()
                    label = tk.Label(master, text=sql_list, bg='white')
                    label.grid(column=0, sticky="w")
                else:
                    sql_list.pop()
                    sql = f"INSERT INTO OBJECT_V4_{point} (DEV_ID, Object_Identifier, Object_Name, SITE_ID) " \
                          f"VALUES ({sql_list[0]},'{sql_list[1]}','{sql_list[2]}', '{site_id}') "
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
    else:
        messagebox.showinfo("Error", "No site selected.")
    return


def view_controller_points(dev_id, master, site_id):
    if site_id != '':
        time = datetime.now().strftime("%H:%M:%S")
        start_label = tk.Label(master, text=f"*****Points Query for site: {site_id} {time}*****", bg='white')
        start_label.grid(column=0, sticky="w")

        pl = []
        sql_list = [
            f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AI WHERE DEV_ID = {dev_id} and SITE_ID = '{site_id}'",
            f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AO WHERE DEV_ID = {dev_id} and SITE_ID ="
            f" '{site_id}'",
            f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_BI WHERE DEV_ID = {dev_id} and SITE_ID = '{site_id}'",
            f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_BO WHERE DEV_ID = {dev_id} and SITE_ID = '{site_id}'",
            f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AV WHERE DEV_ID = {dev_id} and SITE_ID = '{site_id}'",
            f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_BV WHERE DEV_ID = {dev_id} and SITE_ID = '{site_id}'",
            f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AIC WHERE DEV_ID = {dev_id} and SITE_ID = '{site_id}'",
            f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_AOC WHERE DEV_ID = {dev_id} and SITE_ID = '{site_id}'",
            f"SELECT DEV_ID, Object_Identifier, Object_Name FROM OBJECT_V4_BDC WHERE DEV_ID = {dev_id} and SITE_ID = '{site_id}'"
            ]

        for i in range(len(sql_list)):
            conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
            cursor = conn.cursor()
            cursor.execute(sql_list[i])
            for row in cursor.fetchall():
                pl.append(row)

        if not pl:
            label = tk.Label(master, text=f"Device {dev_id} does not exist.\n", bg='white')
            label.grid(column=0, sticky="w")
        else:
            for i in range(len(pl)):
                label = tk.Label(master, text=pl[i], bg='white')
                label.grid(column=0, sticky="w")
        cursor.close()
        conn.close()
    else:
        messagebox.showinfo("Error", "No site selected.")
    return


def delete_points():
    pass
