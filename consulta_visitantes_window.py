import tkinter as tk
from tkinter import ttk, END
import sqlite3

class ConsultaVisitantesWindow:
    def __init__(self):
        self.consulta_visitantes_window = tk.Toplevel()
        self.consulta_visitantes_window.title("Consulta de Visitantes")
        self.consulta_visitantes_window.geometry("1000x600")
        self.consulta_visitantes_window.configure(bg="#B0B0B2")  # Cor de fundo da janela

        self.create_widgets()

    def create_widgets(self):
        filterv_frame = tk.Frame(self.consulta_visitantes_window, bg="#B0B0B2")  # Cor de fundo do frame
        filterv_frame.pack(pady=10)

        label_style = ("Century Gothic bold", 12)

        lb_filter_placa = tk.Label(filterv_frame, text="Filtrar por Placa:", font=label_style, bg="#B0B0B2", fg="black")
        lb_filter_placa.grid(row=0, column=0, padx=5)

        self.filter_placa_var = tk.StringVar()
        entry_filter_placa = tk.Entry(filterv_frame, textvariable=self.filter_placa_var, font=label_style, bg="lightgray")  # Cor de fundo da Entry
        entry_filter_placa.grid(row=0, column=1, padx=5)

        btnv_consulta_placa = tk.Button(filterv_frame, text="Consultar por Placa", command=self.consultar_por_placa, fg="black", relief=tk.FLAT, bg="white")
        btnv_consulta_placa.grid(row=0, column=2, padx=5, pady=5)  # Ajuste na assimetria

        lb_filter_nomev = tk.Label(filterv_frame, text="Filtrar por Nome:", font=label_style, bg="#B0B0B2", fg="black")
        lb_filter_nomev.grid(row=1, column=0, padx=5)

        self.filter_nomev_var = tk.StringVar()
        entry_filter_nomev = tk.Entry(filterv_frame, textvariable=self.filter_nomev_var, font=label_style, bg="lightgray")  # Cor de fundo da Entry
        entry_filter_nomev.grid(row=1, column=1, padx=5)

        btn_consulta_nomev = tk.Button(filterv_frame, text="Consultar por Nome", command=self.consultar_por_nome, fg="black", relief=tk.FLAT, bg="white")
        btn_consulta_nomev.grid(row=1, column=2, padx=5, pady=5)  # Ajuste na assimetria

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Century Gothic bold", 12))
        style.configure("Treeview", font=("Century Gothic", 11))

        self.tree = ttk.Treeview(self.consulta_visitantes_window, columns=("ID", "Nome", "Contato", "Data Visita", "Observações"), style="Treeview")
        self.tree.heading("#0", text="ID")
        self.tree.heading("ID", text="ID", anchor=tk.W)
        self.tree.heading("Nome", text="Nome", anchor=tk.W)
        self.tree.heading("Contato", text="Contato", anchor=tk.W)
        self.tree.heading("Data Visita", text="Data Visita", anchor=tk.W)
        self.tree.heading("Observações", text="Observações", anchor=tk.W)

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", width=40)
        self.tree.column("Nome", width=120)
        self.tree.column("Contato", width=80)
        self.tree.column("Data Visita", width=120)
        self.tree.column("Observações", width=120)

        self.tree.pack(expand=True, fill='both', side='left')

    def consultar_por_placa(self):
        self.realizar_consultav("placa", self.filter_placa_var.get())

    def consultar_por_nome(self):
        self.realizar_consultav("nome", self.filter_nomev_var.get())

    def realizar_consultav(self, campo, valor):
        for item in self.tree.get_children():
            self.tree.delete(item)

        connection = sqlite3.connect("visitantes.db")
        self.cursor = connection.cursor()

        if campo == "placa":
            self.cursor.execute("SELECT * FROM visitantes WHERE placam LIKE ?", ('%' + valor + '%',))
        elif campo == "nome":
            self.cursor.execute("SELECT * FROM visitantes WHERE nomem LIKE ?", ('%' + valor + '%',))

        rows = self.cursor.fetchall()

        for row in rows:
            self.tree.insert("", END, values=row, tags=("data_row",))
        self.tree.update_idletasks()

    def show(self):
        self.consulta_visitantes_window.mainloop()

if __name__ == "__main__":
    app = ConsultaVisitantesWindow()
    app.show()
