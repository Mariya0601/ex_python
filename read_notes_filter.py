import read_notes as rnf
from datetime import datetime
import csv


def read_notes_filter():
    from_date = datetime.strptime(input('Введите дату/время в формате ГГГГ-ММ-ДД ЧЧ:ММ (например, 2022-01-01 12:00): '), '%Y-%m-%d %H:%M')
    notes = rn.read_notes()
    notes_filter = [note for note in notes if datetime.strptime(notes['created_at'], '%Y-%m-%d %H:%M') >= from_date or note['updated_at'] and datetime.strptime(note['updated_at'], '%Y-%m-%d %H:%M') >= from_date]
    return notes_filter

    # changes_vol = input('введите  Дату записи в формате -> YYYY-MM-DD :   ')
    # df = rn.read_notes('notes.csv')
    # filtered_df = df[df['Время'].str.contains(changes_vol)]