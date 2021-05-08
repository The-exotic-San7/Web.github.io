from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html') 
app.run(debug=False ,host="0.0.0.0",port=5000)
