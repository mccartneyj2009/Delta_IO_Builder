from delta_connection import Delta_Connection
from __variables_creation import Variables
import logging
import tkinter as tk


class Ahu_Variables(Variables):
    def __init__(self, master, dev_id, site_id):
        super().__init__(master, dev_id, site_id)
        self.analog_variables_list = [
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
        self.binary_variables_list = [
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
        self.multistate_variables_list = [
            "'AHU Mode', 'MIC21'",
            "'AHU Status', 'MIC22'"
        ]
        self.mic_list = [
            ['Controller Modes', 'MIC21'],
            ['Controller Status', 'MIC22']
        ]
        self.mic_state_text_list = [
            ['MIC21', 1, 'Unoccupied', 21],
            ['MIC21', 2, 'Occupied', 21],
            ['MIC21', 3, 'Warmup', 21],
            ['MIC21', 4, 'Unoccupied Override', 21],
            ['MIC21', 5, 'Autozero', 21],
            ['MIC21', 6, 'Unoccupied Heat_Cool', 21],
            ['MIC21', 7, 'Unoccupied Dehumid', 21],
            ['MIC21', 8, 'Cooldown', 21],
            ['MIC21', 9, 'Airflow Calibration', 21],
            ['MIC22', 1, 'Heating', 22],
            ['MIC22', 1, 'Cooling', 22],
            ['MIC22', 1, 'Deadband', 22],
            ['MIC22', 1, 'Zero Calibration', 22],
            ['MIC22', 1, 'Smoke Evacuation', 22]
        ]

    def create_analog_variables(self):
        logging.basicConfig(filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        for row in range(len(self.analog_variables_list)):
            try:
                sql_statement = f"INSERT INTO OBJECT_V4_AV (DEV_ID, INSTANCE, Object_Name, Units, SITE_ID) " \
                                    f"VALUES ({self.dev_id},{self.analog_variables_list[row]},'{self.site_id}') "

                connection = Delta_Connection(sql_statement)
                connection.close_conn_cursor()
                label = tk.Label(self.master, text=f"{self.dev_id}, AV{self.analog_variables_list[row]}", bg='white')
                label.grid(column=0, sticky="w")
                logger.info(f"{self.dev_id}, AV{self.analog_variables_list[row]}")
            except:
                label = tk.Label(self.master, text=f"failed to create AV{self.analog_variables_list[row]}", bg='white')
                label.grid(column=0, sticky="w")
                logger.info(f"failed to create AV{self.analog_variables_list[row]}")

    def create_binary_variable(self):
        logging.basicConfig(filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        for row in range(len(self.binary_variables_list)):
            try:
                sql_statement = f"INSERT INTO OBJECT_V4_BV (DEV_ID, INSTANCE, Object_Name, Type_Reference, SITE_ID) " \
                                f"VALUES ({self.dev_id},{self.binary_variables_list[row]},'{self.site_id}') "

                connection = Delta_Connection(sql_statement)
                connection.close_conn_cursor()
                label = tk.Label(self.master, text=f"{self.dev_id}, BV{self.binary_variables_list[row]}", bg='white')
                label.grid(column=0, sticky="w")
                logger.info(f"{self.dev_id}, BV{self.binary_variables_list[row]}")
            except:
                label = tk.Label(self.master, text=f"failed to create BV{self.binary_variables_list[row]}", bg='white')
                label.grid(column=0, sticky="w")
                logger.info(f"failed to create BV{self.binary_variables_list[row]}")

    def create_multistate_variables(self):
        logging.basicConfig(filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        for row in range(len(self.multistate_variables_list)):
            try:
                sql_statement = f"INSERT INTO OBJECT_V4_MV (DEV_ID, Object_Name, Type_Reference, SITE_ID) " \
                                f"VALUES ({self.dev_id},{self.multistate_variables_list[row]},'{self.site_id}') "

                connection = Delta_Connection(sql_statement)
                connection.close_conn_cursor()
                label = tk.Label(self.master, text=f"{self.dev_id}, MV {self.multistate_variables_list[row][0]}",
                                 bg='white')
                label.grid(column=0, sticky="w")
                logger.info(f"{self.dev_id}, MV {self.multistate_variables_list[row][0]}")
            except:
                label = tk.Label(self.master, text=f"failed to create MV {self.multistate_variables_list[row][0]}",
                                 bg='white')
                label.grid(column=0, sticky="w")
                logger.info(f"failed to create MV {self.multistate_variables_list[row][0]}")

    def create_mics(self):
        logging.basicConfig(filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        for row in range(len(self.mic_list)):
            try:
                sql_statement = f"INSERT INTO OBJECT_V4_MIC (DEV_ID, Object_Name, Object_Identifier, SITE_ID)" \
                                f"VALUES ({self.dev_id}, {self.mic_list[row]}, '{self.site_id}')"

                connection = Delta_Connection(sql_statement)
                connection.close_conn_cursor()
                label = tk.Label(self.master, text=f"{self.dev_id}, MIC{self.mic_list[row]}", bg='white')
                label.grid(column=0, sticky="w")
                logger.info(f"{self.dev_id}, MIC{self.mic_list[row]}")
            except:
                label = tk.Label(self.master, text=f"failed to create MIC{self.mic_list[row]}", bg='white')
                label.grid(column=0, sticky="w")
                logger.info(f"failed to create MIC{self.mic_list[row]}")

        for row in range(len(self.mic_state_text_list)):
            idx = self.mic_state_text_list[row][1]
            state_text = self.mic_state_text_list[row][2]
            mic_instance = self.mic_state_text_list[row][3]

            try:
                sql_statement = f"Insert Into ARRAY_V4_MIC_STATE_TEXT (DEV_ID, IDX, State_Text, INSTANCE, SITE_ID)" \
                                f"Values({self.dev_id}, {idx}, '{state_text}',{mic_instance}, '{self.site_id}')"
                connection = Delta_Connection(sql_statement)
                connection.close_conn_cursor()
            except:
                pass