from flask import Flask, render_template, send_from_directory
import os, getStats

getStats.downloadSetup()
def create_app():
    app = Flask(__name__)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
    @app.route("/")
    def test():
        return render_template('tracker.html')
    return app