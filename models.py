from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class IncomeSource(Base):
    __tablename__ = 'income_source'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    incomes = relationship('Transaction', back_populates='source')

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    expenses = relationship('Transaction', back_populates='category')

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # 'income' or 'expense'
    source_id = Column(Integer, ForeignKey('income_source.id'), nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    details = Column(String)
    source = relationship('IncomeSource', back_populates='incomes')
    category = relationship('Category', back_populates='expenses')
