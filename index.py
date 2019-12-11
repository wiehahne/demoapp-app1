from flask import send_file
@app.route('/summer')
def summer():
    filename = 'uploads\\cape-town-480x300.jpg'
    return send_file(filename, mimetype='image/jpg')