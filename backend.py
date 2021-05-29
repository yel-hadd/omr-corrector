from flask import Flask
import cv2
import main

path = './5.png'
ans = [[1, 0, 0, 0, 0],
       [1, 0, 0, 1, 0],
       [1, 0, 0, 1, 0],
       [1, 1, 0, 0, 0],
       [0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0],
       [0, 0, 0, 1, 1],
       [0, 0, 0, 0, 1],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1],
       [0, 1, 0, 0, 1],
       [0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0]]

bareme = [0.5, 1.5, 0.5, 1.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5, 1, 0.5]

result = main.correctExam(cv2.imread(path), ans, 20, 5, bareme)
app = Flask(__name__)
@app.route('/')


def home():
    return f'the result is {result}'

app.run(port=5000)