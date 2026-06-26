from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Azure App Service Demo</h1>
    <p>The Python Flask application deployed successfully from GitHub.</p>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}, 200
