from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("Index.html")

@app.route('/aboutus')
def aboutUs():
    return render_template("about.html")

@app.route("/donate")
def donate():
    return render_template("Donate.html")

@app.route("/gallery")
def photoGallery():
    return render_template("Gallery.html")

if __name__ == "__main__":
    app.run(debug=True)
