from decimal import Decimal
from .base import Base
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from models.transaction import Transaction
# from models.bills import Bills


db = SQLAlchemy()

class Transaction(Base):
    __tablename__ = 'transaction'
    transaction_id = Column(Integer, primary_key=True, nullable=True)
    invoice_number = Column(String(50), nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)
    status = Column(String(100), nullable=False)
    created_at = Column(Date, default=datetime.utcnow().date, nullable=False)
    user_id = Column(Integer, nullable=False)
    voucher_id = Column(Integer, nullable=True)
    shipping_address = Column(String(255), nullable=True)