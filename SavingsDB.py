import sqlite3
import datetime
import tkinter as tk

class entry_savings:
    
    def create_table(self):

             conn = sqlite3.connect('Users_data.db')
             c = conn.cursor()

             c.execute("""CREATE TABLE IF NOT EXISTS Savings(
          
           id integer PRIMARY KEY,
           Saving real ,
           Spending real ,
           Budget real,
           Date textL
          
          
          
            )""")
             conn.commit()  