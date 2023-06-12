import csv
from datetime import datetime

# чтение заметок из файла

def read_notes():
    notes = []
    with open('notes.csv','r',encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            row['id'] = int(row['id'])
            notes.append(row)
    return notes