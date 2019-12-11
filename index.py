from flask import send_file
@app.route('/summer')
def summer():
    if request.args.get('type') == '1':
       filename = 'cape-town-480x300.jpg'
    else:
       filename = 'cape-town-480x300.jpg'
    return send_file(filename, mimetype='image/gif')