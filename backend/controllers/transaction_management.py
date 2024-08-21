from flask import Blueprint, jsonify, request
from flask_login import login_required
from connectors.mysql_connectors import connection
from models.transaction import Transaction
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from werkzeug.utils import secure_filename
import random
import string
from models.transaction_detail import trans_detail

trans_bp = Blueprint('Transaction', __name__)

@trans_bp.route('/transaction/', methods=['GET'])
# @login_required
def get_transaction():
    session = sessionmaker(connection)
    s = session()  
    try:
        transactions = s.query(Transaction).all()
        transaction_list = []
        for trans in transactions:
            trans_data = {
                'transaction_id': trans.transaction_id,
                'invoice_number': trans.invoice_number,
                'total_price': trans.total_price,
                'status': trans.status,
                'created_at': trans.created_at,
                'shipping_address': trans.shipping_address,
                'user_id': trans.user_id,
                'voucher_id': trans.voucher_id
            }
            transaction_list.append(trans_data)
        return jsonify(transaction_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        s.close()

@trans_bp.route('/transaction/', methods=['POST'])
# @login_required
def create_transaction():
    session = sessionmaker(connection)
    s = session()

    try:
        # Get the request data
        data = request.get_json()

        # Create a new transaction object
        new_trans = Transaction(
            invoice_number=generate_invoice_number(),
            total_price=data['total_price'],
            status='paid',
            shipping_address=data.get('shipping_address', None),
            user_id=data.get('user_id', 1),
            voucher_id=data.get('voucher_id', None)
        )
        s.add(new_trans)
       
        transaction_details = s.query(trans_detail).filter_by(user_id=1, transaction_id=None).all()
        for transaction_detail in transaction_details:
            transaction_detail.transaction_id = new_trans.transaction_id
        s.commit()
        return jsonify({
            'invoice_number' : new_trans.invoice_number,
            'total_price': new_trans.total_price,
            'status': new_trans.status,
            'created_at': new_trans.created_at,
            'shipping_address': new_trans.shipping_address,
            'user_id': new_trans.user_id,
            'voucher_id': new_trans.voucher_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        s.close()

def generate_invoice_number():
    letters = string.ascii_uppercase
    numbers = string.digits
    invoice_number = ''.join(random.choice(letters + numbers) for _ in range(8))
    return invoice_number










# @trans_detail_bp.route('/transaction-details/', methods=['POST'])
# # @login_required
# def create_transaction_detail():
#     session = sessionmaker(connection)
#     s = session()

#     try:
#         # Get the request data
#         data = request.get_json()

#         # Create a new transaction detail object
#         new_trans_detail = trans_detail(
#             transaction_detail_id=data['transaction_detail_id'],
#             product_id=data['product_id'],
#             price=data['price'],
#             quantity=data['quantity'],
#             user_id=data['user_id'],
#             transaction_id=data['transaction_id']
#         )

#         # Add the new transaction detail to the session
#         s.add(new_trans_detail)
#         s.commit()

#         # Return the created transaction detail
#         return jsonify({
#             'transaction_detail_id': new_trans_detail.transaction_detail_id,
#             'product_id': new_trans_detail.product_id,
#             'price': new_trans_detail.price,
#             'quantity': new_trans_detail.quantity,
#             'user_id': new_trans_detail.user_id,
#             'trasaction_id': new_trans_detail.transaction_id
#         }), 201
#     except Exception as e:
#         # Handle any exceptions and return an error response
#         return jsonify({"error": str(e)}), 500
#     finally:
#         s.close()


# @trans_detail_bp.route('/transaction-details/<int:transaction_detail_id>', methods=['PUT'])
# # @login_required
# def update_transaction_detail(transaction_detail_id):
#     session = sessionmaker(connection)
#     s = session()

#     try:
#         # Get the request data
#         data = request.get_json()

#         # Find the transaction detail to update
#         transaction_detail = s.query(trans_detail).filter_by(transaction_detail_id=transaction_detail_id).first()

#         if transaction_detail is None:
#             return jsonify({"error": "Transaction detail not found"}), 404

#         # Update the transaction detail attributes
#         transaction_detail.transaction_detail_id = data['transaction_detail_id']
#         transaction_detail.product_id = data['product_id']
#         transaction_detail.price = data['price']
#         transaction_detail.quantity = data['quantity']
#         transaction_detail.user_id = data['user_id']
#         transaction_detail.transaction_id = data['transaction_id']

#         # Commit the changes
#         s.commit()

#         return jsonify({
#             'transaction_detail_id': transaction_detail.transaction_detail_id,
#             'transaction_id': transaction_detail.transaction_id,
#             'product_id': transaction_detail.product_id,
#             'price': transaction_detail.price,
#             'quantity': transaction_detail.quantity,
#             'user_id': transaction_detail.user_id
#         }), 200
#     except Exception as e:
#         # Handle any exceptions and return an error response
#         return jsonify({"error": str(e)}), 500
#     finally:
#         s.close()