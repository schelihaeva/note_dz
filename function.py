import file_operation
import Notepad
import ui

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Notepad.Note.get_id(note) == Notepad.Note.get_id(notes):
            Notepad.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Notepad.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Notepad.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Notepad.Note.get_date(notes):
                print(Notepad.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Notepad.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Notepad.Note.set_title(notes, note.get_title())
                Notepad.Note.set_body(notes, note.get_body())
                Notepad.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Notepad.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operation.write_file(array, 'a')