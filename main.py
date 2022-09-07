import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/")
def test():
    return render_template('tracker.html')
app.run(host='0.0.0.0', port=3000)