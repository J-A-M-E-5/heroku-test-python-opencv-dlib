import platform

from flask import Flask
import cv2
import dlib


# Configure verbose in all the app
verbose = False

# FLASK #
app = Flask(__name__)

@app.route('/')
def hello_world():
    html =  '<strong>Python version: </strong>%s<br/>' % platform.python_version()
    html += '<strong>OpenCV version: </strong>%s<br/>' % cv2.__version__
    html += '<strong>Dlib version: </strong>%s<br/>' % dlib.__version__
    html += '<hr><strong>OpenCV Functions:</strong><br/>%s' % str(dir(cv2))
    html += '<hr><strong>DLib Functions:</strong><br/>%s' % str(dir(dlib))
    html += '<hr>El fin :)'
    return html
