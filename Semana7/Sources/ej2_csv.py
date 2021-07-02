import csv

file_name="Tabla.csv"
with open(file_name, 'a', newline='') as csv_file:
    escribir=csv.writer(csv_file)
    escribir.writerows([['Egipto', 'El cairo'], ['Colombia','Bogota'], ["Australia", "Canberra"]])



