import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ConsultaWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Consulta de Moradores")
        self.geometry("1000x600")
        self.configure(bg="#B0B0B2")  # Cor de fundo da janela

        self.create_widgets()

    def create_widgets(self):
        filter_frame = tk.Frame(self, bg="#B0B0B2")  # Cor de fundo do frame
        filter_frame.pack(pady=10)

        label_style = ("Century Gothic bold", 12)

        lb_filter_placa = tk.Label(filter_frame, text="Filtrar por Placa:", font=label_style, bg="#B0B0B2", fg="black")
        lb_filter_placa.grid(row=0, column=0, padx=5)

        self.filter_placa_var = tk.StringVar()
        entry_filter_placa = tk.Entry(filter_frame, textvariable=self.filter_placa_var, font=label_style, bg="lightgray")  # Cor de fundo da Entry
        entry_filter_placa.grid(row=0, column=1, padx=5)

        btn_consulta_placa = tk.Button(filter_frame, text="Consultar Placa", command=self.consultar_por_placa, bg="white", relief=tk.FLAT, width=15)  # Ajuste na assimetria
        btn_consulta_placa.grid(row=0, column=2, padx=5, pady=5)

        lb_filter_nome = tk.Label(filter_frame, text="Filtrar por Nome:", font=label_style, bg="#B0B0B2", fg="black")
        lb_filter_nome.grid(row=1, column=0, padx=5)

        self.filter_nome_var = tk.StringVar()
        entry_filter_nome = tk.Entry(filter_frame, textvariable=self.filter_nome_var, font=label_style, bg="lightgray")  # Cor de fundo da Entry
        entry_filter_nome.grid(row=1, column=1, padx=5)

        btn_consulta_nome = tk.Button(filter_frame, text="Consultar Nome", command=self.consultar_por_nome, bg="white", relief=tk.FLAT, width=15)  # Ajuste na assimetria
        btn_consulta_nome.grid(row=1, column=2, padx=5, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Century Gothic bold", 12))
        style.configure("Treeview", font=("Century Gothic", 11))

        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Contato", "Número da Casa", "Rua", "Observações", "Placa"), style="Treeview")
        self.tree.heading("#0", text="ID")  # Oculta a coluna
        self.tree.heading("ID", text="ID", anchor=tk.W)
        self.tree.heading("Nome", text="Nome", anchor=tk.W)
        self.tree.heading("Contato", text="Contato", anchor=tk.W)
        self.tree.heading("Número da Casa", text="Número da Casa", anchor=tk.W)
        self.tree.heading("Rua", text="Rua", anchor=tk.W)
        self.tree.heading("Observações", text="Observações", anchor=tk.W)
        self.tree.heading("Placa", text="Placa", anchor=tk.W)

        self.tree.column("#0", width=0, stretch=tk.NO)  # Ajusta a largura da coluna oculta
        self.tree.column("ID", width=40)
        self.tree.column("Nome", width=120)
        self.tree.column("Contato", width=80)
        self.tree.column("Número da Casa", width=80)
        self.tree.column("Rua", width=80)
        self.tree.column("Observações", width=120)
        self.tree.column("Placa", width=80)

        self.tree.pack(expand=True, fill='both', side='left')

        self.no_results_label = tk.Label(self, text="Nenhum resultado encontrado", font=label_style, bg="#B0B0B2", fg="red")

    def consultar_por_placa(self):
        self.realizar_consulta("placa", self.filter_placa_var.get())

    def consultar_por_nome(self):
        self.realizar_consulta("nome", self.filter_nome_var.get())

    def realizar_consulta(self, campo, valor):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.no_results_label.pack_forget()  # Esconde a mensagem de "Nenhum resultado encontrado" ao iniciar nova consulta

        try:
            connection = sqlite3.connect("dados_moradores.db")
            self.cursor = connection.cursor()

            if campo == "placa":
                self.cursor.execute("SELECT * FROM moradores WHERE placa LIKE ?", ('%' + valor + '%',))
            elif campo == "nome":
                self.cursor.execute("SELECT * FROM moradores WHERE nome LIKE ?", ('%' + valor + '%',))

            rows = self.cursor.fetchall()

            if not rows:
                self.no_results_label.pack()  # Exibe a mensagem de "Nenhum resultado encontrado" se não houver resultados
            else:
                for row in rows:
                    self.tree.insert("", "end", values=row, tags=("data_row",))
                self.tree.update_idletasks()

        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao consultar o banco de dados: {e}")

        finally:
            if connection:
                connection.close()

    def show(self):
        self.mainloop()

if __name__ == "__main__":
    app = ConsultaWindow()
    app.show()
