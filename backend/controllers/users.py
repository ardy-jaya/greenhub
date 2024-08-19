from datetime import timedelta
from flask import Blueprint, Response, app, jsonify, request
from sqlalchemy import null
# from flask_jwt_extended import create_access_token
from connectors.mysql_connectors import engine
from sqlalchemy.orm import sessionmaker
from models.users import Users
from flask_login import login_required, login_user, logout_user, current_user
user_routes = Blueprint("user_routes", __name__)


##create new user
@user_routes.route('/users', methods=['POST'])
##cuman boleh yang gada login 
def register_user():

    Session = sessionmaker(engine)
    s = Session()
    s.begin()
    input_email = request.json['email'] 
    check_email_existing_query = s.query(Users).where(Users.email == input_email).first()
    input_same_email_query = s.query(Users).where(Users.email == input_email).first()
    try:
        if check_email_existing_query:
            return { "message": "Email already exists please use a different one" }, 400
        ##kalo email nya sama, terus punya dia, can just update email

        NewUser = Users(
            email=request.json['email'],
        )
        NewUser.set_password(request.json['password'])

        s.add(NewUser)
        s.commit()
    except Exception as e:
        print(e)
        s.rollback()
        return { "message": "Failed to register new user" }, 500

    return { 'message': 'Successfully created new user'}, 200

##get the current user
@user_routes.route("/users/me", methods=['GET'])
@login_required

def get_current_user():
    Session = sessionmaker(engine)
    s = Session()
    # with Session() as s:
    try:
        # Logic Apps
        me=[]
        user_query= s.query(Users).where(Users.email == current_user.email,  Users.id == current_user.id)
        results = s.execute(user_query)
        for row in results.scalars():
            me.append({
                'email': row.email,
                'email': row.email,
            })
        
        return { 'message': 'Successfully fetch current user', 'users':me}, 200
    except Exception as e:
        # Rollback
        print(e)
        
        # Kirim Error Message
        return { 'message': 'Unexpected Error' }, 500

##modify current user
@user_routes.route('/users/me', methods=['PUT'])
@login_required
def users_update():
    Session = sessionmaker(engine)
    s = Session()
    s.begin()
    input_email = request.json['email'] 
    input_email =request.json['email']
    check_email_existing_query = s.query(Users).where(Users.email == input_email, Users.id != current_user.id).first()
    input_same_email_query = s.query(Users).where(Users.email == input_email, Users.id == current_user.id).first()
    check_email_existing_query = s.query(Users).where(Users.email == input_email, Users.id != current_user.id).first()
    try:
        user = s.query(Users).filter(Users.id == current_user.id).first()
        ##kalo email exist terus tapi bukan punya dia
        if check_email_existing_query and check_email_existing_query:
            return { "message": "Email and email already exists please use a different one" }, 400
        if check_email_existing_query:
            return { "message": "Email already exists please use a different one" }, 400
        ##kalo email nya sama, terus punya dia, can just update email
        if check_email_existing_query:
            return { "message": "email already exists please use a different one" }, 400
        if input_same_email_query:
            user.email = request.json['email']
        if not input_same_email_query:
            user.email = request.json['email']
            user.email = request.json['email'] 
        # if request.json['email'] and request.json['email']:
        #     user.email = request.json['email']
        #     user.email = request.json['email']
        #     print('changing email and email' + str(Users.id))

        # elif request.json['email'] is null:
        #     user.email = request.json['email']
        #     print('changing email only' + str(user.email))
        # elif request.json['email']:
        #     user.email = request.json['email']
        #     print('changing email only' + str(user.email))

        s.commit()
    except Exception as e:
        print(e)
        s.rollback()
        return { "message": "Failed to Update" }, 500

    return { 'message': 'Your email and email has been changed to email:' +" "+user.email+" email:"+ user.email}, 200

@user_routes.route('/users/login', methods=['POST'])
def logging_in():
    
    Session = sessionmaker(engine)
    s = Session()
    s.begin()
    
    try:
        email = request.json['email']
        user = s.query(Users).filter(Users.email == email).first()

        if user == None:
            return { "message": "User not found" }, 403
        if not user.check_password(request.json['password']):
            return { "message": "Invalid password" }, 403
        
        #kalo diatas dilewatin berarti bisa login, dibawah biar dipass ke login manager
        login_user(user)

        # harus get session id -> kalo pake postman. kalo di browser gausah 
        session_id = request.cookies.get('session')
        # session_id.cookie_age =5
        return {
            "session_id": session_id,
             "message": "Login successful"}, 200
        
    except Exception as e:
        print(e)
        s.rollback()
        return { "message": "Incorrect email or Password" }, 500

@user_routes.route('/logout', methods=['GET'])
@login_required

def user_logout():
    Session = sessionmaker(engine)
    s = Session()
    s.begin()
    user_query= s.query(Users.email).where(Users.email == current_user.email,  Users.id == current_user.id)
    current_email = s.execute(user_query).scalar()
    logout_user()
    return { "message": "Successfully logged out, see you later! " + current_email}


# @user_routes.route('/product/<id>', methods=['DELETE'])
# def product_delete(id):
#     Session = sessionmaker(connection)
#     s = Session()
#     s.begin()
#     try:
#         product = s.query(Product).filter(Product.id == id).first()
#         s.delete(product)
#         s.commit()
#     except Exception as e:
#         print(e)
#         s.rollback()
#         return { "message": "Fail to Delete" }, 500

#     return { 'message': 'Success delete product data'}, 200

# @product_routes.route('/product/<id>', methods=['PUT'])
# def product_update(id):
    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        product = s.query(Product).filter(Product.id == id).first()

        product.name = request.json['name']
        product.price = request.json['price']
        product.description = request.json['description']

        s.commit()
    except Exception as e:
        print(e)
        s.rollback()
        return { "message": "Fail to Update" }, 500

    return { 'message': 'Success update product data'}, 200