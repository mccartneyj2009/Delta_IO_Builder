import pyodbc
import logging
import tkinter as tk


def create_analog_variables(master, dev_id, site_id):
    logging.basicConfig(filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    analog_variables_list = [
        "1,'Outside Air Temperature Transfer','°F'"
    ]
    print(analog_variables_list[0])
    sql_statement = f"INSERT INTO OBJECT_V4_AV (DEV_ID, INSTANCE, Object_Name, Units, SITE_ID) " \
                          f"VALUES ({dev_id},{analog_variables_list[0]}, '{site_id}') "
    print(sql_statement)

    conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
    cursor = conn.cursor()
    cursor.execute(sql_statement)
    cursor.close()
    conn.close()
    label = tk.Label(master, text=analog_variables_list[0], bg='white')
    label.grid(column=0, sticky="w")
    logger.info(analog_variables_list[0])

    pass
