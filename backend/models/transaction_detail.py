from decimal import Decimal
from .base import Base
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from models.transaction import Transaction
# from models.bills import Bills


db = SQLAlchemy()

class trans_detail(Base):
    __tablename__ = 'transaction_detail'
    transaction_detail_id = Column(Integer, autoincrement=True, primary_key=True, nullable=True)
    product_id = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    user_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    transaction_id = Column(Integer, nullable=True)