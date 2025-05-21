from db import Session
from models import Transaction, Category
from datetime import datetime
from sqlalchemy import func

def get_transactions(start_date, end_date, tx_type=None):
    session = Session()
    start = datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.strptime(end_date, '%Y-%m-%d').date()
    query = session.query(Transaction).filter(
        Transaction.date >= start,
        Transaction.date <= end
    )
    if tx_type in ('income', 'expense'):
        query = query.filter_by(type=tx_type)
    results = query.all()
    session.close()
    return results

def summary_by_category(start_date, end_date, tx_type='expense'):
    session = Session()
    start = datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.strptime(end_date, '%Y-%m-%d').date()
    data = session.query(
        Transaction.category_id if tx_type=='expense' else Transaction.source_id,
        func.sum(Transaction.amount)
    ).filter(
        Transaction.type == tx_type,
        Transaction.date >= start,
        Transaction.date <= end
    ).group_by(
        Transaction.category_id if tx_type=='expense' else Transaction.source_id
    ).all()
    summary = []
    for idx, total in data:
        if tx_type=='expense':
            name = session.query(Category).get(idx).name
        else:
            name = session.query(Category).get(idx).name if tx_type=='expense' else session.query(Category).get(idx).name  # placeholder for IncomeSource
        summary.append((name, total))
    session.close()
    return summary

def summary_by_details(start_date, end_date, category_name):
    session = Session()
    start = datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.strptime(end_date, '%Y-%m-%d').date()
    data = session.query(
        Transaction.details,
        func.sum(Transaction.amount)
    ).join(Transaction.category).filter(
        Category.name == category_name,
        Transaction.type == 'expense',
        Transaction.date >= start,
        Transaction.date <= end
    ).group_by(Transaction.details).all()
    session.close()
    return data

def get_totals(start_date, end_date):
    session = Session()
    start = datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.strptime(end_date, '%Y-%m-%d').date()
    total_income = session.query(func.coalesce(func.sum(Transaction.amount), 0.0)) \
        .filter(Transaction.type=='income', Transaction.date>=start, Transaction.date<=end).scalar()
    total_expense = session.query(func.coalesce(func.sum(Transaction.amount), 0.0)) \
        .filter(Transaction.type=='expense', Transaction.date>=start, Transaction.date<=end).scalar()
    session.close()
    return total_income, total_expense
