from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def main():
    return "how are you"

if __name__ =="main":
    app.run()