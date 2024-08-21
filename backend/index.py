from datetime import datetime, timedelta
import os
from flask import Flask, Response, request, session
from dotenv import load_dotenv
from connectors.mysql_connectors import connection
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text,select
from controllers.users import user_routes
from flask_login import LoginManager, current_user
# from flask_jwt_extended import JWTManager
from models.users import Users
from flask import Flask, Response, redirect, url_for, request, session, abort, g
from flask_cors import CORS
from controllers.product_management import products_list
from controllers.transaction_detail_management import trans_detail_bp
from controllers.transaction_management import trans_bp
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename

load_dotenv()

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__, static_folder='uploads')
cors = CORS(app)

project_root = os.path.abspath(os.path.dirname(__file__))
upload_folder = os.path.join(project_root, 'uploads/images')

# app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOADED_PHOTOS_DEST'] = upload_folder
app.config['UPLOAD_FOLDER'] = upload_folder
app.register_blueprint(user_routes)
app.register_blueprint(products_list)
app.register_blueprint(trans_detail_bp)
app.register_blueprint(trans_bp)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
# jwt=JWTManager(app) ##jason web token

##biar bisa login
# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     Session = sessionmaker(connection)
#     s = Session()
#     return s.query(Users).get(int(user_id))


if __name__ == '__main__':
    app.run(debug=True)

# @app.route("/")
# def hello_world():
        
#         return "Product inserted!"


# @app.before_request
# def before_request():
#     session.permanent = True
#     app.permanent_session_lifetime = timedelta(minutes=300)
#     session.modified = True
#     g.user = current_user

