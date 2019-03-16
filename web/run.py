# run.py
# Invoked at from docker compose/ standalone
from flask_cors import CORS

from project import app
CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)

