from flask import Flask, render_template
import os

apprun = Flask(__name__)


@apprun.route("/")
def root():
    return render_template("index.html")


#--------Main------------------
if __name__ == "__main__":
    apprun.run(host="0.0.0.0", port=8080)
