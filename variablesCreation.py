import pyodbc
import logging
import tkinter as tk


def create_ahu_analog_variables(master, dev_id, site_id):
    logging.basicConfig(filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    analog_variables_list = [
        "1,'Outside Air Temperature Transfer','°F'",
        "2,'Outside Air Humidity Transfer','%RH'",
        "3,'Outside Air Wetbulb Temperature Transfer','°F'",
        "4,'Outside Air CO2 Transfer','ppm'",
        "5,'Outside Air Enthalpy Transfer','BTU/lb'",
        "6,'Return Air Enthalpy','BTU/lb'",
        "21,'Supply Duct Static Pressure Setpoint','inWC'",
        "22,'Supply Discharge High Limit Static Pressure Setpoint','inWC'",
        "23,'Return Fan CFM Setpoint','CFM'",
        "24,'Return Plenum Static Pressure Low Limit Setpoint','inWC'",
        "25,'Building Static Pressure Setpoint','inWC'",
        "26,'Mixed Air Plenum Static Pressure Low Limit Setpoint','inWC'",
        "31,'Supply Air Heating Setpoint','°F'",
        "32,'Supply Air Cooling Setpoint','°F'",
        "33,'Return Air Temperature Setpoint','°F'",
        "34,'Preheat Air Temperature Setpoint','°F'",
        "35,'Mixed Air Temperature Setpoint','°F'",
        "36,'Mixed Air Low Limit Temperature Setpoint','°F'",
        "37,'Economizer Enable Setpoint','°F'",
        "41,'Humidifier Enable Setpoint','%RH'",
        "42,'Return Air Humidity Setpoint','%RH'",
        "43,'Space Humidity Setpoint','%RH'",
        "44,'Humidity High Limit Setpoint','%RH'",
        "45,'Dehumidification Setpoint','%RH'",
        "46,'Unoccupied Dehumidification Setpoint','%RH'",
        "51,'Minimum Outside Air CFM Setpoint','CFM'",
        "52,'Maximum Outside Air CFM Setpoint (CO2)','CFM'",
        "53,'Minimum Outside Air CFM Setpoint (CO2)','CFM'",
        "54,'Demand Ventilation CO2 Setpoint','ppm'",
        "61,'Occupied Space Temperature Setpoint','°F'",
        "62,'Active Space Heating Setpoint','°F'",
        "63,'Active Space Cooling Setpoint','°F'",
        "64,'Occupied Space Temperature Setpoint Deadband','°F'",
        "71,'Unoccupied Heating Setpoint','°F'",
        "72,'Unoccupied Cooling Setpoint','°F'",
        "73,'Unoccupied Space Temperature Setpoint Deadband','°F'",
        "77,'Average Space Temperature','°F'",
        "78,'Lowest Space Temperature','°F'",
        "79,'Highest Space Temperature','°F'",
        "81,'Hot Water Runaround Pump Enable Setpoint','°F'",
        "91,'Supply VFD Control Ramp','%'",
        "92,'Return VFD Control Ramp','%'",
        "93,'Damper Control Ramp','%'",
        "94,'Valve Control Ramp','%'",
        "95,'Fan Control Ramp','%'",
        "96,'Humidifier Control Ramp','%'"
    ]
    for row in range(len(analog_variables_list)):
        try:
            sql_statement = f"INSERT INTO OBJECT_V4_AV (DEV_ID, INSTANCE, Object_Name, Units, SITE_ID) " \
                                  f"VALUES ({dev_id},{analog_variables_list[row]},'{site_id}') "

            conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
            cursor = conn.cursor()
            cursor.execute(sql_statement)
            cursor.close()
            conn.close()
            label = tk.Label(master, text=f"{dev_id}, AV{analog_variables_list[row]}", bg='white')
            label.grid(column=0, sticky="w")
            logger.info(f"{dev_id}, AV{analog_variables_list[row]}")
        except:
            label = tk.Label(master, text=f"failed to create AV{analog_variables_list[row]}", bg='white')
            label.grid(column=0, sticky="w")
            logger.info(f"failed to create AV{analog_variables_list[row]}")


def create_ahu_binary_variables(master, dev_id, site_id):
    logging.basicConfig(filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    binary_variables_list = [
        "1,'AHU Enable','BDC7'",
        "2, 'AHU Fan Request', 'BDC5'",
        "3, 'Afterhours Override', 'BDC5'",
        "11, 'Hot Water Available', 'BDC5'",
        "21, 'Mechanical Cooling Available', 'BDC5'",
        "31, 'Economizer Mode Enable', 'BDC5'",
        "32, 'CO2 Demand Ventilation Mode Enable', 'BDC5'",
        "41, 'Humidifier Enable', 'BDC5'",
        "42, 'Dehumidification Enable', 'BDC5'",
        "51, 'Supply Fans Operational Status', 'BDC5'",
        "52, 'Return Fans Operational Status', 'BDC5'"
    ]
    for row in range(len(binary_variables_list)):
        try:
            sql_statement = f"INSERT INTO OBJECT_V4_BV (DEV_ID, INSTANCE, Object_Name, Type_Reference, SITE_ID) " \
                            f"VALUES ({dev_id},{binary_variables_list[row]},'{site_id}') "

            conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
            cursor = conn.cursor()
            cursor.execute(sql_statement)
            cursor.close()
            conn.close()
            label = tk.Label(master, text=f"{dev_id}, BV{binary_variables_list[row]}", bg='white')
            label.grid(column=0, sticky="w")
            logger.info(f"{dev_id}, BV{binary_variables_list[row]}")
        except:
            label = tk.Label(master, text=f"failed to create BV{binary_variables_list[row]}", bg='white')
            label.grid(column=0, sticky="w")
            logger.info(f"failed to create BV{binary_variables_list[row]}")


def create_ahu_mics(master, dev_id, site_id):
    logging.basicConfig(filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    mic_list = [
        "'Controller Modes', 'MIC21'",
        "'Controller Status', 'MIC22'"
    ]
    mic_state_texts = [
        
    ]

    for row in range(len(mic_list)):
        try:
            sql_statement = f"INSERT INTO OBJECT_V4_MIC (DEV_ID, Object_Name, Object_Identifier, SITE_ID)" \
                            f"VALUES ({dev_id}, {mic_list[row]}, '{site_id}')"
        except:
            label = tk.Label(master, text=f"failed to create MIC{mic_list[row]}", bg='white')
            label.grid(column=0, sticky="w")
            logger.info(f"failed to create MIC{mic_list[row]}")


def create_ahu_multistate_variables(master, dev_id, site_id):
    logging.basicConfig(filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    multistate_variables_list = [
        "'AHU Mode', 'MIC21'",
        "'AHU Status', 'MIC22'"
    ]
    for row in range(len(multistate_variables_list)):
        try:
            sql_statement = f"INSERT INTO OBJECT_V4_MV (DEV_ID, Object_Name, Type_Reference, SITE_ID) " \
                            f"VALUES ({dev_id},{multistate_variables_list[row]},'{site_id}') "

            conn = pyodbc.connect('DSN=Delta ODBC 4', autocommit=True)
            cursor = conn.cursor()
            cursor.execute(sql_statement)
            cursor.close()
            conn.close()
            label = tk.Label(master, text=f"{dev_id}, MV{multistate_variables_list[row]}", bg='white')
            label.grid(column=0, sticky="w")
            logger.info(f"{dev_id}, MV{multistate_variables_list[row]}")
        except:
            label = tk.Label(master, text=f"failed to create MV{multistate_variables_list[row]}", bg='white')
            label.grid(column=0, sticky="w")
            logger.info(f"failed to create MV{multistate_variables_list[row]}")