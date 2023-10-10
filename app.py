# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request
from Model.Vinyl.Record import *
from datetime import time
import mysql.connector

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user="postgres",
  password="test123!",
  database="Plattenspass"
)

app = Flask(__name__)

record = Record(title="Schnarr", artist="Muh")
record.add_track(Track(title="Niau", length=time(minute=5, second=23)))
print(record.dict())

a = float('inf') * -1
print(a)
