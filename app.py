# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request
from datetime import time
from Routes.Auth import *
from Routes.Article import *
from Model.Vinyl.Record import *

app = Flask(__name__)

record = Record(title="Schnarr", artist="Muh")
record.add_track(Track(title="Niau", length=time(minute=5, second=23)))
print(record.dict())
