from db import Session
from models import IncomeSource, Transaction
from datetime import datetime

def add_income(date_str, amount, source_name, details):
    session = Session()
    src = session.query(IncomeSource).filter_by(name=source_name).first()
    if not src:
        src = IncomeSource(name=source_name)
        session.add(src)
        session.commit()
    tx = Transaction(
        date=datetime.strptime(date_str, '%Y-%m-%d').date(),
        amount=amount,
        type='income',
        source=src,
        details=details
    )
    session.add(tx)
    session.commit()
    session.close()