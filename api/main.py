from flask import Flask
from routes.auth import routes_auth
from dotenv import load_dotenv
import jwt

class chatMainPoint():
    print("Maybe yes...")
    app = Flask(__name__)
    app.register_blueprint(routes_auth, url_prefix="/api")
    if __name__ == '__main__':
        load_dotenv()
        app.run(debug=True)
        print("...I don´t know")
