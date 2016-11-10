import sqlite3
import sqlalchemy


def insertNewLab(nome, local, responsavel):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO labs_unifacs (nome_lab, local_lab, responsavel_lab) VALUES (?, ?, ?)''', (nome, local, responsavel))
    db.commit()
    db.close()

def retriveLab():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('''SELECT nome_lab, local_lab, responsavel_lab FROM labs_unifacs''')
    labs = cursor.fetchall()
    db.close()
    return labs

def updateResponsavelLab(nome, local, new_responsavel):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('''UPDATE labs_unifacs SET responsavel_lab = ? WHERE nome_lab = ? AND local_lab = ?''', (new_responsavel, nome, local))
    db.commit()
    db.close()

def deleteLab (nome, local):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('''DELETE FROM labs_unifacs WHERE nome_lab = ? AND local_lab = ?''', (nome, local))
    db.commit()
    db.close()

def LabExists(nome, local):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    result = False
    cursor.execute('''SELECT nome_lab, local_lab FROM labs_unifacs''')
    labs = cursor.fetchall()
    for lab in labs:
        if (nome == lab[0]) and (local == lab[1]):
            result = True
    else:
        return result