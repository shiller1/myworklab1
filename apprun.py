from flask import Flask, render_template
import os

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("index.html")


#--------Main------------------
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
