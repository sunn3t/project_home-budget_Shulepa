from db import Session
from models import Category, Transaction
from datetime import datetime

def add_expense(date_str, amount, category_name, details):
    session = Session()
    cat = session.query(Category).filter_by(name=category_name).first()
    if not cat:
        cat = Category(name=category_name)
        session.add(cat)
        session.commit()
    tx = Transaction(
        date=datetime.strptime(date_str, '%Y-%m-%d').date(),
        amount=amount,
        type='expense',
        category=cat,
        details=details
    )
    session.add(tx)
    session.commit()
    session.close()