# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.

import json
import os
from datetime import datetime


# Функция для создания новой заметки
def create_note():
    notes = load_notes()
    new_note = {}
    new_note["id"] = len(notes) + 1
    new_note["title"] = input("Введите заголовок заметки: ")
    new_note["body"] = input("Введите текст заметки: ")
    new_note["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно создана!")


# Функция для загрузки списка заметок
def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []
