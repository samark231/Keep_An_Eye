import sys
import os
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(main_dir)
from flask import Flask, request, jsonify
from app.services.fetch_curated_data import fetch_curated_data
app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_home():
    return "welcome"

@app.route("/company", methods=["GET"])
def get_curated_news_data():
    company = request.args.get("company")
    
    if not company:
        return jsonify({"error": "Company name is required"}), 400  # Bad Request

    curated_data, error = fetch_curated_data(company)

    if error:  # If there's an error, return 500 Internal Server Error
        return jsonify({"error": "Internal Server Error", "details": error}), 500

    return jsonify(curated_data), 200  # Success
