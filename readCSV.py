import csv
import tkinter as tk
from tkinter import filedialog


def read_csv_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        points_list = []
        next(reader)
        next(reader)
        for row in reader:
            points_list.append(row)
        print(points_list)
        finalized_list = prepare_points_list(points_list)

    return points_list


def determine_point_type(point):
    if point.find('AI') != -1:
        return 'AI'
    elif point.find('AO') != -1:
        return 'AO'
    elif point.find('BI') != -1:
        return 'BI'
    elif point.find('BO') != -1:
        return 'BO'
    elif point.find('AV') != -1:
        return 'AV'
    elif point.find('BV') != -1:
        return 'BV'
    else:
        print("Unrecognized point type.")

def prepare_points_list(pl):
    #(DEV_ID, Object_Identifier, Object_Name, Type_Reference)
    id = input('BACnet address: ')
    start_list = []
    for item in pl:
        item.pop()
        start_list.append(item)
    for i in start_list:
        object_name = i[2]
        object_identifier = i[0] + i[1]
        type = determine_point_type(object_identifier)
        if type == 'AI':
            type_reference = 'AIC' + i[3]
        elif type == 'AO':
            type_reference = 'AOC' + i[3]
        elif type == 'BI' or type == 'BO':
            type_reference = 'BDC' + i[3]
        inter_list = [id,object_identifier,object_name,type_reference]


    #return prepared_list



read_csv_file()