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
    stock = Column(Integer, nullable=False)
    product_category = Column(String(100), nullable=False)
    product_grade = Column(String(100), nullable=False)
    product_type = Column(String(100), nullable=False)
    product_image = Column(String(255), nullable=True)