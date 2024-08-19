from flask import Blueprint, jsonify, request, current_app
from flask_login import login_required
from connectors.mysql_connectors import connection
from models.product import product_list
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from flask_uploads import UploadSet, IMAGES
from werkzeug.utils import secure_filename
import os

# # Create the UPLOAD_FOLDER directory if it doesn't exist
# UPLOAD_FOLDER = 'backend/uploads/images'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

photos = UploadSet('photos', IMAGES)

products_list = Blueprint('product_list', __name__)

@products_list.route('/products/', methods=['GET'])
# @login_required
def get_product():
    session = sessionmaker(connection)
    s = session()
    try:
        products = s.query(product_list).all()
        products_list = []
        for prod in products:
            product_data = {
                'product_id': prod.product_id,
                'seller_id': prod.seller_id,
                'name': prod.name,
                'price': prod.price,
                'description': prod.description,
                'stock': prod.stock,
                'product_category': prod.product_category,
                'product_grade': prod.product_grade,
                'product_type': prod.product_type,
                'product_image': prod.product_image
            }
            products_list.append(product_data)
        return jsonify(products_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        s.close()

@products_list.route('/products/', methods=['POST'])
# @login_required
def create_product():
    session = sessionmaker(connection)
    s = session()
    s.begin()

    try:
         # Debugging statements
        print("Request files:", request.files)
        print("Request form:", request.form)

        if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
            os.makedirs(current_app.config['UPLOAD_FOLDER'])

        # Check for file part in the request
        if 'product_image' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['product_image']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        
        # Retrieve other form data
        product_id = request.form.get('product_id')
        seller_id = request.form.get('seller_id', 1)
        name = request.form.get('name')
        price = request.form.get('price')
        description = request.form.get('description')
        stock = request.form.get('stock')
        product_category = request.form.get('product_category')
        product_grade = request.form.get('product_grade')
        product_type = request.form.get('product_type')
        product_image = filename  # Use the saved filename

        # Create new product
        new_product = product_list(
            product_id=product_id,
            seller_id=seller_id,
            name=name,
            price=price,
            description=description,
            stock=stock,
            product_category=product_category,
            product_grade=product_grade,
            product_type=product_type,
            product_image=product_image
        )
        s.add(new_product)
        s.commit()
        return jsonify({"message": "Product created successfully", "product_id": new_product.product_id}), 201

    except Exception as e:
        s.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        s.close()


# @products_list.route('/products/', methods=['POST'])
# # @login_required
# def create_product():
#     session = sessionmaker(connection)
#     s = session()
#     s.begin()

#     try:
#         data = request.get_json()
#         if data is None or not isinstance(data, dict):
#             return jsonify({"error": "Missing or invalid JSON data"}), 400

#         if 'file' not in request.files:
#             return 'No file part'
#         file = request.files['file']
#         if file.filename == '':
#             return 'No selected file'
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             data['product_image'] = filename 
#             return 'File successfully uploaded'    

#         new_product = product_list(
#             product_id=data.get('product_id'),
#             seller_id=data.get('seller_id') if data.get('seller_id') else 1,
#             name=data.get('name'),
#             price=data.get('price'),
#             description=data.get('description'),
#             stock=data.get('stock'),
#             product_category=data.get('product_category'),
#             product_grade=data.get('product_grade'),
#             product_type=data.get('product_type'),
#             product_image=data.get('product_image')
#         )
#         s.add(new_product)
#         s.commit()
#         return jsonify({"message": "Product created successfully", "product_id": new_product.product_id}), 201

#     except Exception as e:
#         s.rollback()
#         return jsonify({"error": str(e)}), 500

#     finally:
#         s.close()




# @account.route('/accounts/', methods=['POST'])
# @login_required
# def create_account():
#     session = sessionmaker(bind=connection)
#     s = session()
#     try:
        
#         data = request.get_json()
#         if data is None or not isinstance(data, dict):
#             return jsonify({"error": "Missing or invalid JSON data"}), 400

#         new_account = Accounts(
#             id=data.get('id'),
#             user_id=data.get('user_id'),
#             account_type=data.get('account_type'),
#             account_number=data.get('account_number'),
#             balance=data.get('balance', 0),
#             created_at=datetime.utcnow(),
#             updated_at=datetime.utcnow()
#         )
#         s.add(new_account)
#         s.commit()
#         return jsonify({"message": "Account created successfully", "account_id": new_account.id}), 201

#     except Exception as e:
#         s.rollback()
#         return jsonify({"error": str(e)}), 500

#     finally:
#         s.close()

# @account.route('/accounts/<int:account_id>', methods=['PUT'])
# @login_required
# def update_account(account_id):
#     session = sessionmaker(bind=connection)
#     s = session()
#     try:
#         account = s.query(Accounts).filter_by(id=account_id).first()
#         if account is None:
#             return jsonify({"error": "Account not found"}), 404

#         data = request.get_json()
#         if data is None or not isinstance(data, dict):
#             return jsonify({"error": "Missing or invalid JSON data"}), 400

#         account.account_type = data.get('account_type', account.account_type)
#         account.account_number = data.get('account_number', account.account_number)
#         account.balance = data.get('balance', account.balance)
#         account.updated_at = datetime.utcnow()
#         s.commit()
#         return jsonify({"message": "Account updated successfully"}), 200
#     except Exception as e:
#         s.rollback()
#         return jsonify({"error": str(e)}), 500
#     finally:
#         s.close()

# @account.route('/accounts/<int:account_id>', methods=['DELETE'])
# @login_required
# def delete_account(account_id):
#     session = sessionmaker(bind=connection)
#     s = session()
#     try:
#         account = s.query(Accounts).filter_by(id=account_id).first()
#         if account is None:
#             return jsonify({"error": "Account not found"}), 404
#         s.delete(account)
#         s.commit()
#         return jsonify({"message": "Account deleted successfully"}), 200
#     except Exception as e:
#         s.rollback()
#         return jsonify({"error": str(e)}), 500
#     finally:
#         s.close()