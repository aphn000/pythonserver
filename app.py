
import json
from pathlib import Path
from flask import Flask, request, render_template

app = Flask(__name__)
dictionaty_path = Path(__file__).with_name("dictionary.json")

with dictionaty_path.open(encoding="utf-8") as file:
    dictionary = json.load(file)

@app.route("/", methods=["GET", "POST"])
def translate():
    text = ""
    result = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            result = dictionary.get(text.lower(),"Word not found")
        else:
            result = "Enter a word"

    return render_template("index.html", text=text, result=result)

if __name__ == "__main__":
    app.run()