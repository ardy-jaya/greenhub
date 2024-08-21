from flask import Blueprint, jsonify, request
from flask_login import login_required
from connectors.mysql_connectors import connection
from models.transaction_detail import trans_detail
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models.product import CartItem, product_list  # Adjust the import based on your project structure

trans_detail_bp = Blueprint('trans_detail', __name__)

@trans_detail_bp.route('/transaction-details/', methods=['GET'])
# @login_required
def get_transaction_detail():
    session = sessionmaker(connection)
    s = session()
  
    try:
        transactions = s.query(trans_detail).filter(trans_detail.transaction_id == None, trans_detail.user_id == 1).all()
        transaction_list = []
        for trans in transactions:
            trans_data = {
                'transaction_detail_id': trans.transaction_detail_id,
                'product_id': trans.product_id,
                'price': trans.price,
                'quantity': trans.quantity,
                'user_id': trans.user_id,
                'transaction_id': trans.transaction_id
            }
            transaction_list.append(trans_data)
        return jsonify(transaction_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        s.close()

@trans_detail_bp.route('/transaction-details/', methods=['POST'])
# @login_required
def create_transaction_detail():
    session = sessionmaker(connection)
    s = session()

    try:
        # Get the request data
        data = request.get_json()
        # Check if the transaction detail already exists for the user
        existing_trans_detail = s.query(trans_detail).filter_by(user_id=data.get('user_id', 1), product_id=data['product_id'], transaction_id=None).first()
        new_trans_detail = None

        if existing_trans_detail:
            # Update the product_id and quantity
        
            existing_trans_detail.quantity += data['quantity']
        else:
            # Create a new transaction detail object
            new_trans_detail = trans_detail(
                product_id=data['product_id'],
                price=data['price'],
                quantity=data['quantity'],
                user_id=data.get('user_id', 1),
                transaction_id=data.get('transaction_id', None)
            )
            # Add the new transaction detail to the session
            s.add(new_trans_detail)
        s.commit()

        transDetail= new_trans_detail if new_trans_detail else existing_trans_detail

        # Return the created transaction detail
        return jsonify({
            # 'transaction_detail_id': new_trans_detail.transaction_detail_id,
            'product_id': transDetail.product_id,
            'price': transDetail.price,
            'quantity': transDetail.quantity,
            'user_id': transDetail.user_id,
            'trasaction_id': transDetail.transaction_id
        }), 201
    except Exception as e:
        # Handle any exceptions and return an error response
        return jsonify({"error": str(e)}), 500
    finally:
        s.close()

@trans_detail_bp.route('/transaction-details/<int:transaction_detail_id>', methods=['DELETE'])
# @login_required
def delete_transaction_detail(transaction_detail_id):
    session = sessionmaker(connection)
    s = session()

    try:
        # Find the transaction detail to delete
        transaction_detail = s.query(trans_detail).filter_by(transaction_detail_id=transaction_detail_id).first()

        if transaction_detail is None:
            return jsonify({"error": "Transaction detail not found"}), 404

        # Delete the transaction detail
        s.delete(transaction_detail)
        s.commit()

        return jsonify({"message": "Transaction detail deleted successfully"}), 200
    except Exception as e:
        # Handle any exceptions and return an error response
        return jsonify({"error": str(e)}), 500
    finally:
        s.close()

@trans_detail_bp.route('/transaction-details/<int:transaction_detail_id>', methods=['PUT'])
# @login_required
def update_transaction_detail(transaction_detail_id):
    session = sessionmaker(connection)
    s = session()

    try:
        # Get the request data
        data = request.get_json()

        # Find the transaction detail to update
        transaction_detail = s.query(trans_detail).filter_by(transaction_detail_id=transaction_detail_id).first()

        if transaction_detail is None:
            return jsonify({"error": "Transaction detail not found"}), 404

        # Update the transaction detail attributes
        transaction_detail.transaction_detail_id = data['transaction_detail_id']
        transaction_detail.product_id = data['product_id']
        transaction_detail.price = data['price']
        transaction_detail.quantity = data['quantity']
        transaction_detail.user_id = data['user_id']
        transaction_detail.transaction_id = data['transaction_id']

        # Commit the changes
        s.commit()

        return jsonify({
            'transaction_detail_id': transaction_detail.transaction_detail_id,
            'transaction_id': transaction_detail.transaction_id,
            'product_id': transaction_detail.product_id,
            'price': transaction_detail.price,
            'quantity': transaction_detail.quantity,
            'user_id': transaction_detail.user_id
        }), 200
    except Exception as e:
        # Handle any exceptions and return an error response
        return jsonify({"error": str(e)}), 500
    finally:
        s.close()


@trans_detail_bp.route('/transaction-cart', methods=['POST'])
def add_to_cart():
    session = sessionmaker(connection)
    s = session()

    try:
        data = request.get_json()
        product_id = data['product_id']
        quantity = data['quantity']

        # Check if the product exists
        product = s.query(Product).filter_by(product_id=product_id).first()
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Check if the item is already in the cart
        cart_item = s.query(CartItem).filter_by(product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(product_id=product_id, quantity=quantity)
            s.add(cart_item)

        s.commit()
        return jsonify({"message": "Item added to cart"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        s.close()