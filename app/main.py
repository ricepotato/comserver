import subprocess
import argparse
from flask import Flask

app = Flask(__name__)


def subprocess_checkoutput(args):
    subprocess.check_output(args)


@app.route("/")
def index():
    return "hello"


@app.route("/linux/shutdown")
def linux_shutdown():
    args = ["shutdown", "now"]
    subprocess_checkoutput(args)
    return "OK"


@app.route("/win/shutdown/<int:seconds>")
def win_shutdown(seconds):
    args = ["shutdown", "-s", "-t", f"{seconds}"]
    subprocess_checkoutput(args)
    return "OK"


@app.route("/win/cancel")
def cancel():
    args = ["shutdown", "-a"]
    subprocess_checkoutput(args)
    return "OK"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", default=False, help="debug")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=1209, debug=args.debug)


if __name__ == "__main__":
    main()
