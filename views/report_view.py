import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from controllers.report_controller import summary_by_category, get_totals
import charts

class ReportView(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        # Фільтри дат
        tk.Label(self, text="Початок (YYYY-MM-DD):").grid(row=0, column=0, sticky='e')
        self.start_entry = tk.Entry(self)
        self.start_entry.grid(row=0, column=1)

        tk.Label(self, text="Кінець (YYYY-MM-DD):").grid(row=1, column=0, sticky='e')
        self.end_entry = tk.Entry(self)
        self.end_entry.grid(row=1, column=1)

        # Тип звіту
        tk.Label(self, text="Що показати:").grid(row=2, column=0, sticky='e')
        options = ["витрати", "надходження", "обидва"]
        self.type_var = tk.StringVar(value=options[0])
        ttk.OptionMenu(self, self.type_var, options[0], *options).grid(row=2, column=1, sticky='we')

        # Кнопка показу
        tk.Button(self, text="Показати", command=self.show).grid(row=3, column=0, columnspan=2, pady=5)
        # Текстове вікно
        self.text_area = scrolledtext.ScrolledText(self, width=60, height=10)
        self.text_area.grid(row=4, column=0, columnspan=2)

    def show(self):
        sd = self.start_entry.get()
        ed = self.end_entry.get()
        rtype = self.type_var.get()
        self.text_area.delete('1.0', tk.END)
        try:
            if rtype == "витрати":
                summary = summary_by_category(sd, ed, tx_type='expense')
                if not summary:
                    messagebox.showinfo("Інфо", "Немає витрат у цьому періоді")
                    return
                # окремі кругові діаграми для кожної категорії витрат
                charts.plot_category_vs_total(summary)
            elif rtype == "надходження":
                summary = summary_by_category(sd, ed, tx_type='income')
                if not summary:
                    messagebox.showinfo("Інфо", "Немає надходжень у цьому періоді")
                    return
                # окремі кругові діаграми для кожного джерела надходжень
                charts.plot_category_vs_total(summary)
            else:
                income_sum, expense_sum = get_totals(sd, ed)
                self.text_area.insert(tk.END, f"Загальні надходження: {income_sum:.2f}\nЗагальні витрати: {expense_sum:.2f}\n")
                charts.plot_income_expense(income_sum, expense_sum)
        except Exception as e:
            messagebox.showerror("Помилка", str(e))
