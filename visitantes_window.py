import tkinter as tk
from tkinter import ttk, Text
import sqlite3

class VisitantesWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Janela de Visitantes")
        self.geometry("900x600")

        self.connection = sqlite3.connect("visitantes.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS visitantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nomem TEXT,
                contatom TEXT,
                numero_casam TEXT,
                ruam TEXT,
                observacoesm TEXT,
                placam TEXT,
                filiacaom TEXT,
                datam TEXT
            )
        """
        )
        self.connection.commit()

        self.setup_ui()

    def setup_ui(self):
        self.configure(bg="#B0B0B2")  # Cor ligeiramente mais clara
        
      

        title = tk.Label(
            self,
            text="Sistema de Cadastro de Novos Visitantes",
            font=("Helvetica", 24, "bold"),
            fg="#000",
            bg="#B0B0B2",
        )
        title.place(x=150, y=10)

        self.style = ttk.Style()
        self.style.configure("My.TFrame", background="#B0B0B2")  # Cor ligeiramente mais clara

        self.namev_value = tk.StringVar()
        self.contactv_value = tk.StringVar()
        self.numero_casav_value = tk.StringVar()
        self.ruav_value = tk.StringVar()
        self.placav_value = tk.StringVar()
        self.filiacao_value = tk.StringVar()
        self.data_hora_value = tk.StringVar()

        tk.Entry(
            self,
            textvariable=self.namev_value,
            font=("Century Gothic bold", 16),
        ).place(x=50, y=130)

        tk.Entry(
            self,
            textvariable=self.contactv_value,
            font=("Century Gothic bold", 16),
        ).place(x=320, y=130)

        tk.Entry(
            self,
            textvariable=self.placav_value,
            font=("Century Gothic bold", 16),
        ).place(x=600, y=130)

        tk.Entry(
            self,
            textvariable=self.filiacao_value,
            font=("Century Gothic bold", 16),
        ).place(x=600, y=220)

        tk.Entry(
            self,
            textvariable=self.ruav_value,
            font=("Century Gothic bold", 16),
        ).place(x=320, y=220)

        tk.Entry(
            self,
            textvariable=self.numero_casav_value,
            font=("Century Gothic bold", 16),
        ).place(x=50, y=220)

        tk.Entry(
            self,
            textvariable=self.data_hora_value,
            font=("Century Gothic bold", 16),
        ).place(x=600, y=290)

        self.obs_entry = Text(
            self, font=("Century Gothic bold", 16), height=5, width=40
        )
        self.obs_entry.place(x=50, y=290)

        tk.Label(
            self,
            text="Data e Horário de Entrada",
            font=("Century Gothic bold", 16),
            fg="#000",
            bg="#B0B0B2",  # Cor ligeiramente mais clara
        ).place(x=600, y=260)

        tk.Label(
            self,
            text="Nome Completo",
            font=("Century Gothic bold", 16),
            fg="#000",
            bg="#B0B0B2",  # Cor ligeiramente mais clara
        ).place(x=50, y=100)

        tk.Label(
            self,
            text="Contato",
            font=("Century Gothic bold", 16),
            fg="#000",
            bg="#B0B0B2",  # Cor ligeiramente mais clara
        ).place(x=320, y=100)

        tk.Label(
            self,
            text="Placa do Veículo",
            font=("Century Gothic bold", 16),
            fg="#000",
            bg="#B0B0B2",  # Cor ligeiramente mais clara
        ).place(x=600, y=100)

        tk.Label(
            self,
            text="Filiação",
            font=("Century Gothic bold", 16),
            fg="#000",
            bg="#B0B0B2",  # Cor ligeiramente mais clara
        ).place(x=600, y=190)

        tk.Label(
            self,
            text="Rua",
            font=("Century Gothic bold", 16),
            fg="#000",
            bg="#B0B0B2",  # Cor ligeiramente mais clara
        ).place(x=320, y=190)

        tk.Label(
            self,
            text="Número da Casa",
            font=("Century Gothic bold", 16),
            fg="#000",
            bg="#B0B0B2",  # Cor ligeiramente mais clara
        ).place(x=50, y=190)

        tk.Label(
            self,
            text="Observações",
            font=("Century Gothic bold", 16),
            fg="#000",
            bg="#B0B0B2",  # Cor ligeiramente mais clara
        ).place(x=50, y=260)

        tk.Button(
            self,
            text="Salvar Dados".upper(),
            command=self.submitv,
            font=("Century Gothic bold", 14),
            bg="#B0B0B2",
            fg="#000",
        ).place(x=50, y=420)

        tk.Button(
            self, text="Limpar Campos".upper(),
            command=self.clear,
            font=("Century Gothic bold", 14),
            bg="#B0B0B2",
            fg="#000",
        ).place(x=430, y=420)

        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def submitv(self):
        namem = self.namev_value.get()
        contactm = self.contactv_value.get()
        ruam = self.ruav_value.get()
        numero_casam = self.numero_casav_value.get()
        placam = self.placav_value.get()
        obsm = self.obs_entry.get(1.0, tk.END).strip()
        filiacaom = self.filiacao_value.get()
        data_horam = self.data_hora_value.get()

        print("Nome:", namem)
        print("Contato:", contactm)
        print("Rua:", ruam)
        print("Número da Casa:", numero_casam)
        print("Placa:", placam)
        print("Observações:", obsm)
        print("Filiação:", filiacaom)
        print("Data e Hora:", data_horam)

        self.cursor.execute(
            """
            INSERT INTO visitantes (nomem, contatom, numero_casam, ruam, observacoesm, placam, filiacaom, datam)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (namem, contactm, numero_casam, ruam, obsm, placam, filiacaom, data_horam)
        )

        self.connection.commit()

    def clear(self):
        self.namev_value.set("")
        self.contactv_value.set("")
        self.numero_casav_value.set("")
        self.ruav_value.set("")
        self.obs_entry.delete(1.0, tk.END)
        self.filiacao_value.set("") 
        self.data_hora_value.set("")

    def close_window(self):
        self.connection.close()
        self.destroy()

if __name__ == "__main__":
    visitantes_window = VisitantesWindow()
    visitantes_window.mainloop()
