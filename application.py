from flask import Flask,send_file,request
app = Flask(__name__)
import imutils
import cv2
import imutils.text

@app.route("/")
def hello():

    return "hello!"
