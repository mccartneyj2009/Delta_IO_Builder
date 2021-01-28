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
        for row in reader:
            points_list.append(row)
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
