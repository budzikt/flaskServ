
import numpy as np
import pandas as pd
from flask import Flask
print("Yeah")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'