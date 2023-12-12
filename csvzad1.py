import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['Radek', 'coe', '3', 9]

dict2 = dict(zip(fields, row))
print(dict2)

dict_list = [
    {'name': 'Radek', 'branch': 'coe', 'year': '3', 'cgpa': 9},
    {'name': 'Tomek', 'branch': 'coe', 'year': '3', 'cgpa': 9},
    {'name': 'MArek', 'branch': 'coe', 'year': '2', 'cgpa': 9},
    {'name': 'Zenek', 'branch': 'coe', 'year': '1', 'cgpa': 9},

]
filename = 'records.csv'
# context manager
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
with open(filename, 'w', newline='') as csv_f:
    # csvwriter = csv.writer(csv_f)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=";")
    # csvwriter.writerow(row)

    csvwriter.writeheader()
    csvwriter.writerow(dict2)
    csvwriter.writerows(dict_list)  # zapisanie listy słowników
