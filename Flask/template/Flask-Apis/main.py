from flask import Flask,jsonify
app = Flask(__name__)
@app.route("/")
def json():
    details = [
        {"name": "Bhumika", "age": 19, "profession": "Software Engineer"},
        {"name": "Divya", "age": 20, "profession": "Electronics Engineer"},
        {"name": "Chaitali", "age": 20, "profession": "Chemical Engineer"},
        {"name": "Anushka", "age": 19, "profession": "Electronics Engineer"}
    ]

    return jsonify(details)
app.run(debug=True)