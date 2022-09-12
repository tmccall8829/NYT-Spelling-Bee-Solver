from flask import Flask, request
import os

from fast import process_matches

app = Flask(__name__)

@app.route("/fast", methods=["GET"])
def fast_solver():
    letters = request.args.get("letters")
    if len(letters) != 7:
        return f"Invalid number of supplied letters: {len(letters)}", 400
    center_letter = request.args.get("center_letter")
    if len(center_letter) != 1:
        return f"Need one and only one center letter, got: {center_letter}", 400

    matches = process_matches(letters=letters, center_letter=center_letter)

    return ", ".join(matches), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    