from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World :)</h1>"

@app.route("/greet")
@app.route("/greet/<name>")
def greet(name=""):
    return f"Hello {name}"

def c_to_f(celsius: float) -> float:
    return celsius * 9.0 / 5 + 32

@app.route("/f/<float:celsius>")
def to_fahrenheit(celsius):
    return f"{c_to_f(celsius):.2f}"


if __name__ == "__main__":
    app.run(debug=True)
