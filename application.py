from flask import Flask,send_file,request
app = Flask(__name__)
import imutils
import cv2
import imutils.text

@app.route("/")
def hello():

    image = cv2.imread("images/bridge.jpg")
    text = request.args.get('text');
   
    imutils.text.put_centered_text(image,
                                text,
                                font_face=cv2.FONT_HERSHEY_SIMPLEX,
                                font_scale=1,
                                color=(0, 255, 0),
                                thickness=2)
    
    cv2.imwrite('images/image.jpg',image)

    return send_file('images/image.jpg', mimetype='image/gif')