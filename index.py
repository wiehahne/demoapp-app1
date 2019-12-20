from flask import Flask
from flask import send_file
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
app = Flask(__name__)
xray_recorder.configure(service='xray-service')
XRayMiddleware(app, xray_recorder)
@app.route('/summer')
def summer():
    return "Summer App"
@app.route('/summer/capetown')
def capetown():
    filename = 'cape-town-480x300.jpg'
    return send_file(filename, mimetype='image/gif')
@app.route('/summer/keywest')
def keywest():
    filename = 'key-west-480x300.jpg'
    return send_file(filename, mimetype='image/gif')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)