import tkinter as tk
from tkinter import ttk, Text
import sqlite3

class CadastroWindow(tk.Toplevel):
    def __init__(self, update_main_window_callback):
        tk.Toplevel.__init__(self)
        self.update_main_window = update_main_window_callback
        self.title("Cadastro Window")
        self.geometry("900x600")

        self.connection = sqlite3.connect("dados_moradores.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS moradores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                contato TEXT,
                numero_casa TEXT,
                rua TEXT,
                observacoes TEXT,
                placa TEXT
            )
        """)
        self.connection.commit()

        self.name_var = tk.StringVar()
        self.contact_var = tk.StringVar()
        self.street_var = tk.StringVar()
        self.house_number_var = tk.StringVar()
        self.plate_var = tk.StringVar()
        self.obs_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        frame = tk.Frame(self, width=900, height=600, bg="#B0B0B2")  # Cor ligeiramente mais clara
        frame.place(x=0, y=0)

        style = ttk.Style()
        style.configure("Title.TLabel", font=('Helvetica', 24, 'bold'), background="#B0B0B2")
        style.configure("Label.TLabel", font=("Century Gothic bold", 14), background="#B0B0B2")

        title_label = ttk.Label(frame, text="Sistema de cadastro de novos Moradores", style="Title.TLabel")
        title_label.place(x=150, y=20)

        labels = [
            ("Nome:", 50, 100),
            ("Contato:", 320, 100),
            ("Placa:", 600, 100),
            ("Rua:", 320, 190),
            ("Número da Casa:", 50, 190),
            ("Observações:", 50, 260)
        ]

        entries = [
            (self.name_var, 50, 130),
            (self.contact_var, 320, 130),
            (self.plate_var, 600, 130),
            (self.street_var, 320, 220),
            (self.house_number_var, 50, 220)
        ]

        for label_text, x, y in labels:
            label = ttk.Label(frame, text=label_text, style="Label.TLabel")
            label.place(x=x, y=y)

        obs_label = ttk.Label(frame, text="Observações:", style="Label.TLabel")
        obs_label.place(x=50, y=260)

        for var, x, y in entries:
            entry = ttk.Entry(frame, textvariable=var, font=("Century Gothic bold", 16))
            entry.place(x=x, y=y)

        obs_entry = Text(frame, font=("Century Gothic bold", 16), height=5, width=40)
        obs_entry.place(x=50, y=290)

        btn_submit = ttk.Button(frame, text="Salvar dados".upper(), command=self.submit)
        btn_submit.place(x=50, y=420)

        btn_clear = ttk.Button(frame, text="Limpar campos".upper(), command=self.clear)
        btn_clear.place(x=430, y=420)

    def submit(self):
        name = self.name_var.get()
        contact = self.contact_var.get()
        street = self.street_var.get()
        house_number = self.house_number_var.get()
        plate = self.plate_var.get()
        obs = self.obs_var.get()

        self.cursor.execute("""
            INSERT INTO moradores (nome, contato, numero_casa, rua, observacoes, placa)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, contact, house_number, street, obs, plate))

        self.connection.commit()
        print("Dados inseridos com sucesso!")

        self.clear()

        # Chama a função de callback para atualizar os campos na janela principal
        self.update_main_window()

    def clear(self):
        self.name_var.set("")
        self.contact_var.set("")
        self.house_number_var.set("")
        self.street_var.set("")
        self.plate_var.set("")
        self.obs_var.set("")

# Exemplo de uso
