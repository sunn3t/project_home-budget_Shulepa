import tkinter as tk
from tkinter import messagebox
from controllers.expense_controller import add_expense
import datetime

class ExpenseView(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        tk.Label(self, text="Дата (YYYY-MM-DD):").grid(row=0, column=0, sticky='e')
        self.date_entry = tk.Entry(self)
        self.date_entry.insert(0, datetime.date.today().strftime('%Y-%m-%d'))
        self.date_entry.grid(row=0, column=1)

        tk.Label(self, text="Сума:").grid(row=1, column=0, sticky='e')
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=1, column=1)

        tk.Label(self, text="Категорія:").grid(row=2, column=0, sticky='e')
        categories = ["їжа", "комунальні витрати", "транспорт", "розваги", "інше"]
        self.category_var = tk.StringVar(value=categories[0])
        tk.OptionMenu(self, self.category_var, *categories).grid(row=2, column=1, sticky='we')

        tk.Label(self, text="Примітки:").grid(row=3, column=0, sticky='e')
        self.details_entry = tk.Entry(self)
        self.details_entry.grid(row=3, column=1)

        tk.Button(self, text="Додати витрату", command=self.submit).grid(row=4, column=0, columnspan=2, pady=5)

    def submit(self):
        d = self.date_entry.get()
        try:
            amt = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Помилка", "Некоректна сума")
            return
        cat = self.category_var.get()
        det = self.details_entry.get()
        add_expense(d, amt, cat, det)
        messagebox.showinfo("Успіх", "Витрату додано")
        self.amount_entry.delete(0, tk.END)
        self.details_entry.delete(0, tk.END)