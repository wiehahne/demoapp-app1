from flask import send_file
app = Flask(__name__)
@app.route("/summer")
def get_image():
    filename = 'cape-town-480x300.jpg'
    return send_file(filename, mimetype='image/jpg')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)