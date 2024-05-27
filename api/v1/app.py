#!/usr/bin/python3
# create a variable app, instance of Flask

from models import storage
import app_views from api.v1.views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
""" closes a database"""

    storage.close()

if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')

    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'

    app.run(host = host, port = port, threaded=True)
