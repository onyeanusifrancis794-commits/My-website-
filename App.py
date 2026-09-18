from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Francez - Web Developer</title></head>
    <body style="font-family: Arial; text-align: center; margin-top: 80px;">
        <h1>Hello, I am Francez</h1>
        <p>Welcome to my personal website!</p>
        <p>Web Developer from Port Harcourt</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
