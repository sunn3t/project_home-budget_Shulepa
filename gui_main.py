import tkinter as tk
from db import init_db
from views.income_view import IncomeView
from views.expense_view import ExpenseView
from views.report_view import ReportView

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Домашній бюджет")
        init_db()
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.frames = {}
        for F in (IncomeView, ExpenseView, ReportView):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(IncomeView)

        menubar = tk.Menu(self)
        menubar.add_command(label="Надходження", command=lambda: self.show_frame(IncomeView))
        menubar.add_command(label="Витрати", command=lambda: self.show_frame(ExpenseView))
        menubar.add_command(label="Звіти", command=lambda: self.show_frame(ReportView))
        self.config(menu=menubar)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()
