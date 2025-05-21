import matplotlib.pyplot as plt

def plot_expense_pie(data):
    labels = [item[0] for item in data]
    sizes = [item[1] for item in data]
    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Витрати за категоріями')
    plt.show()

def plot_expense_bar(data):
    labels = [item[0] for item in data]
    amounts = [item[1] for item in data]
    plt.figure()
    plt.bar(labels, amounts)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Сума')
    plt.title('Витрати за категоріями')
    plt.tight_layout()
    plt.show()

def plot_category_vs_total(summary):
    """
    Для кожної категорії (або джерела) малює окрему кругову діаграму:
    частка цієї категорії проти всіх інших.
    summary: список кортежів (назва, сума)
    """
    total = sum(amount for _, amount in summary)
    for name, amount in summary:
        other = total - amount
        labels = [name, 'інші']
        sizes = [amount, other]
        plt.figure()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title(f"{name}: {amount:.2f} vs інші {other:.2f}")
        plt.show()


def plot_income_expense(total_income, total_expense):
    """Малює стовпчикову діаграму порівняння надходжень та витрат."""
    labels = ['надходження', 'витрати']
    values = [total_income, total_expense]
    plt.figure()
    plt.bar(labels, values)
    plt.title(f"Надходження vs Витрати: {total_income:.2f} / {total_expense:.2f}")
    plt.ylabel('Сума')
    plt.tight_layout()
    plt.show()