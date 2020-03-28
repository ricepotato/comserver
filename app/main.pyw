import subprocess
import argparse
from flask import Flask, render_template

app = Flask(__name__)


def subprocess_checkoutput(args):
    subprocess.check_output(args)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shutdown/<int:seconds>")
def shutdown(seconds):

    args = ["shutdown", "-s", "-t", f"{seconds}"]
    subprocess_checkoutput(args)
    return render_template("index.html")


@app.route("/cancel")
def cancel():
    args = ["shutdown", "-a"]
    subprocess_checkoutput(args)
    return render_template("index.html")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", default=False, help="debug")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=1209, debug=args.debug)


if __name__ == "__main__":
    main()
