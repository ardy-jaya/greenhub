from decimal import Decimal
from .base import Base
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from models.transaction import Transaction
# from models.bills import Bills


db = SQLAlchemy()

class product_list(Base):
    __tablename__ = 'product_list'
    product_id = Column(Integer,primary_key=True, autoincrement=True)
    seller_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    description = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    product_category = Column(String(100), nullable=False)
    product_grade = Column(String(100), nullable=False)
    product_type = Column(String(100), nullable=False)
    product_image = Column(String(255), nullable=True)

class CartItem(Base):
    __tablename__ = 'cart_items'
    cart_item_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product_list.product_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    product = relationship('product_list')