import sqlite3
from sqlite3 import Error
from datetime import datetime
import time



class Database:
    '''
    Class made to connect to sqlite3 database so messages can be 
    written to and read from the databse.
    '''
    def __init__(self):
        '''
        starts up the database and use a cursor, similar to an identifier
        '''
        self.connection = None
        try:
            self.connection = sqlite3.connect("messages.db")
            
        except Error as e:
            print("Error: ")

        
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        '''
        Checks to see if a table exists. If it does not exists then,
        table is created
        '''
        messages_table = """ CREATE TABLE IF NOT EXISTS Messages (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        msg text,
                                        time Date
                                    ); """
        self.cursor.execute(messages_table)
        self.connection.commit()

    def save_message(self, name, msg):
        '''
        Saves the given message into the database
        '''
        insert = f"INSERT INTO Messages VALUES (?, ?, ?, ?)"
        self.cursor.execute(insert, (None,name, msg, datetime.now()))
        self.connection.commit()

    def get_all_msg(self, limit=100, name=None):
        '''
        Gets all the messages
        '''
        if not name:
            check = f"SELECT * FROM Messages"
            self.cursor.execute(check)
        else:
            check = f"SELECT * FROM Messages WHERE NAME = ?"
            self.cursor.execute(check, (name,))

        result = self.cursor.fetchall()

        # return messages in sorted order by date
        results = []
        for r in sorted(result, key=lambda x: x[3], reverse=True)[:limit]:
            name, content, date, _id = r
            data = {"name":name, "message":content, "time":str(date)}
            results.append(data)

        return list(reversed(results))

    def get_msg_name(self, name, limit=100):
        '''
        uses the get_all_msg with a given name
        '''
        return self.get_all_msg(limit, name)
    
    def close(self):
        '''
        Closes the database
        '''
        self.connnection.close()

    