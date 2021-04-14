from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def project():
    return render_template("project.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
