import csv
import os
from os import path


data = (
    ['Pharma A, Vitamin C,100'],
    ['Drugstore XYZ,Penicilin, 20, pills'],
    ['Pharma X,Montelukast,10'],
    ['Drugstore ABC,Aspirin,60'],
)
file_path = 'pomoce/simple.csv'
if path.exists(file_path):
    print('File Exists')
else:
    with open(file_path, 'w', newline='') as file:
        write = csv.writer(file)
        for item in data:
            write.writerow(item)

with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    while True:
        try:
            row = next(csvreader)
            print(row)
        except StopIteration:
            print('Iteration over {} is over'.format(file_path))
            break