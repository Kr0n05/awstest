import time
time.sleep(15)

from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
	return "Hello There!"

if __name__ == "__main__":
	application.run(host='0.0.0.0')