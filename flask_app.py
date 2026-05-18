from flask import Flask, render_template, jsonify
from tester.runner import run_tests
from storage import init_db, save_run, get_runs

app = Flask(__name__)

init_db()

@app.get("/")
def home():
    return render_template("dashboard.html", runs=get_runs())

@app.get("/run")
def run():
    result = run_tests()
    save_run(result)
    return jsonify(result)

@app.get("/api/runs")
def api_runs():
    return jsonify(get_runs())