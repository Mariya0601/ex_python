import csv
from datetime import datetime

# запись заметок в файл

def write_notes(notes):
    with open('notes.csv','w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['id','title','body','created_at','update_at'], delimiter=',')
        writer.writeheader()
        for note in notes:
            writer.writerow(note)