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
        finalized_list = prepare_points_list(points_list)
    return finalized_list


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
    prepared_list =[]
    for item in pl:
        item.pop()
        prepared_list.append(item)
    for i in prepared_list:
        object_identifier = i[0] + i[1]
        type = determine_point_type(object_identifier)

    #return prepared_list



read_csv_file()