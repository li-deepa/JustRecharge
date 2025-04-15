from flask import Flask, render_template, request, jsonify
import pandas as pd
import re
from collections import defaultdict

app = Flask(__name__)

# Parse the log file and prepare data
def parse_log_file(log_file_path):
    data = []
    with open(log_file_path, "r") as log_file:
        for line in log_file:
            match = re.search(r"(\d{4}-\d{2}-\d{2}) .* :INFO :(test_\w+) :(.*)", line)
            if match:
                date, test_name, message = match.groups()
                year = date.split("-")[0]
                data.append({"date": date, "year": year, "test_name": test_name, "message": message})
    return pd.DataFrame(data)

# Load log data
log_file_path = "logfile.log"  # Path to your log file
log_data = parse_log_file(log_file_path)

@app.route("/")
def index():
    # Get unique tests and years for dropdowns
    tests = log_data["test_name"].unique().tolist()
    years = log_data["year"].unique().tolist()
    return render_template("dashboard.html", tests=tests, years=years)

@app.route("/get_chart_data", methods=["POST"])
def get_chart_data():
    # Get selected test and year from the frontend
    selected_test = request.json.get("test")
    selected_year = request.json.get("year")

    # Filter data based on the selection
    filtered_data = log_data[(log_data["test_name"] == selected_test) & (log_data["year"] == selected_year)]

    # Count passed and failed occurrences
    passed_count = len(filtered_data[~filtered_data["message"].str.contains("error|failed", case=False)])
    failed_count = len(filtered_data[filtered_data["message"].str.contains("error|failed", case=False)])

    return jsonify({"passed": passed_count, "failed": failed_count})

if __name__ == "__main__":
    app.run(debug=True)