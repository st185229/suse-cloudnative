import json
import logging

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    logging.debug("Hello")
    return "Hello World!"


@app.route("/status")
def status():
    logging.debug("status")
    data = {"result": "OK - healthy"}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/metrics")
def metrics():
    logging.debug("metrics")
    data = {"UserCount": 140, "UserCountActive": 23}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    logging.basicConfig(filename='longname.txt', filemode='a',
                        format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S', level=logging.DEBUG)
    app.run(host='0.0.0.0')
