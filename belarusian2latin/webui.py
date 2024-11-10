from flask import Flask, render_template, request
import belarusian2latin

app = Flask(__name__)

@app.route("/display", methods=["POST"])
def display():
    content = request.form["input"]
    output = belarusian2latin.latinize(content)
    return {"output": output}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form["input"]
        output = belarusian2latin.latinize(content)
        return render_template("index.html", user_input=content, output=output)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
