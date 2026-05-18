from flask import Flask, render_template, jsonify
from tester.runner import run_all_tests
from storage import init_db, save_run

app = Flask(__name__)
init_db()


@app.route("/")
def home():
    return render_template("consignes.html")


@app.route("/run")
def run():
    result = run_all_tests()
    save_run(result)
    return jsonify(result)


@app.route("/health")
def health():
    return jsonify({"status": "OK"})


@app.route("/dashboard")
def dashboard():
    result = run_all_tests()
    return render_template("dashboard.html", data=result)


if __name__ == "__main__":
    app.run(debug=True)