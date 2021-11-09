#source code of censor_text
#-----------LOG------------
#version 1.0
#Project started:: 08-11-21
#Author:: Ankit Rana
#Github:: https://github.com/Ankit161001

import sqlite3
import os

def create():
    os.system('touch mydb.db')
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    query = "CREATE TABLE names (id varchar(4), name varchar(50));"
    cursor.execute(query)
    connection.commit()
    query = """INSERT INTO names (id, name) VALUES 
            ('EN01', 'shit'),
            ('EN02', 'damn'),
            ('EN03', 'goddamn'),
            ('EN04', 'fuck'),
            ('EN05', 'nigga'),
            ('EN06', 'nigger'),
            ('EN07', 'bitch'),
            ('EN08', 'ass'),
            ('EN09', 'asshole'),
            ('EN10', 'motherfucker'),
            ('EN11', 'cunt'),
            ('EN12', 'dick'),
            ('EN13', 'bastard'),
            ('EN14', 'faggot'),
            ('EN15', 'maggot'),
            ('EN16', 'whore');"""
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

def custom():
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM names WHERE id LIKE 'CS%';")
    results = cursor.fetchall()
    total_custom_words = len(results)
    #print(total_custom_words)
    code = 0
    if total_custom_words == 0:
        #print(code)
        return code
    else:
        last_custom = results[total_custom_words-1][0]
        #print(last_custom[3])
        custom_code = ""
        custom_code = custom_code + last_custom[2] + last_custom[3]
        code = int(custom_code)
        #print(code)
        return code

def censor(sentence):
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM names;")
    results = cursor.fetchall()
    #total_censored_words = len(results)
    words = sentence.split(' ')
    size = len(words)
    for p in range(0, len(words)):
        for q in range(0, len(results)):
            if words[p] == results[q][1]:
                size = len(words[p])
                temp = ""
                for s in range(size):
                    temp = temp + '*'
                words[p] = temp
    final =""
    for i in range(0, len(words)):
        final = final + words[i] + " "
    print(final)
    connection.commit()
    cursor.close()
    connection.close()

def add_words(words):
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM names;")
    #results = cursor.fetchall()
    #total_censored_words = len(results)
    add = words.split(" ")
    size = custom()
    query = "INSERT INTO names (id, name) VALUES (?, ?);"
    for i in range(0, len(add)):
        size = size + 1
        id_pass = ""
        if size <= 9:
            id_pass = "CS0" + str(size)
        else:
            id_pass = "CS" + str(size)
        #print(id_pass)
        cursor.execute(query, (id_pass, add[i]))
    connection.commit()
    cursor.close()
    connection.close()

def add_word(word):
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM names;")
    #results = cursor.fetchall()
    #total_censored_words = len(results)
    size = custom()
    query = "INSERT INTO names (id, name) VALUES (?, ?);"
    size = size + 1
    id_pass = ""
    if size <= 9:
        id_pass = "CS0" + str(size)
    else:
        id_pass = "CS" + str(size)
    #print(id_pass)
    cursor.execute(query, (id_pass, word))
    connection.commit()
    cursor.close()
    connection.close()

def remove_words(words):
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM names;")
    #results = cursor.fetchall()
    #total_censored_words = len(results)
    rem = words.split(" ")
    #size = total_censored_words
    query = "DELETE FROM names WHERE name = ?;"
    for i in range(0, len(rem)):
        #size = size - 1
        cursor.execute(query, [rem[i]])
    connection.commit()
    cursor.close()
    connection.close()

def remove_word(word):
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM names;")
    #results = cursor.fetchall()
    #total_censored_words = len(results)
    #size = total_censored_words
    query = "DELETE FROM names WHERE name = ?;"
    #size = size - 1
    cursor.execute(query, [word])
    connection.commit()
    cursor.close()
    connection.close()

def show_words():
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM names;")
    results = cursor.fetchall()
    #total_censored_words = len(results)
    for i in range(0, len(results)):
        print(results[i])
    cursor.close()
    connection.close()

def query(query):
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    #total_censored_words = len(results)
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)
    connection.commit()
    cursor.close()
    connection.close()

def default():
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    query = "DROP TABLE names;"
    cursor.execute(query)
    connection.commit()
    query = "CREATE TABLE names (id varchar(4), name varchar(50));"
    cursor.execute(query)
    connection.commit()
    query = """INSERT INTO names (id, name) VALUES 
            ('EN01', 'shit'),
            ('EN02', 'damn'),
            ('EN03', 'goddamn'),
            ('EN04', 'fuck'),
            ('EN05', 'nigga'),
            ('EN06', 'nigger'),
            ('EN07', 'bitch'),
            ('EN08', 'ass'),
            ('EN09', 'asshole'),
            ('EN10', 'motherfucker'),
            ('EN11', 'cunt'),
            ('EN12', 'dick'),
            ('EN13', 'bastard'),
            ('EN14', 'faggot'),
            ('EN15', 'maggot'),
            ('EN16', 'whore');"""
    cursor.execute(query)
    connection.commit()
    cursor.execute("SELECT * FROM names;")
    results = cursor.fetchall()
    #total_censored_words = len(results)
    print(results)
    connection.commit()
    cursor.close()
    connection.close()

def text_toxicity(sentence):
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM names;")
    results = cursor.fetchall()
    #total_censored_words = len(results)
    words = sentence.split(' ')
    #size = len(words)
    toxic_words = 0
    for p in range(0, len(words)):
        for q in range(0, len(results)):
            if words[p] == results[q][1]:
                toxic_words = toxic_words + 1
    toxicity = toxic_words / len(words) * 100
    connection.commit()
    cursor.close()
    connection.close()
    return toxicity

#cursor.close()
#connection.close()
