from flask import send_file
@app.route('/get_image')
def get_image():
    filename = 'uploads\\cape-town-480x300.jpg'
    return send_file(filename, mimetype='image/jpg')