from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel
from main_window import MainWindow
import tkinter as tk
from PIL import Image, ImageTk

class LoginWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x200")

        # Carregar a imagem de fundo
        original_image = Image.open("sistema de segurança condominal.png")  # Substitua pelo caminho da sua imagem
        resized_image = original_image.resize((400, 200))
        self.background_image = ImageTk.PhotoImage(resized_image)

        # Criar um Canvas que cobre toda a janela
        self.background_canvas = tk.Canvas(self, width=400, height=200)
        self.background_canvas.pack()

        # Exibir a imagem de fundo
        self.background_canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # Elementos da interface
        self.username_label = CTkLabel(self.background_canvas, text="Usuário:", fg_color="white", bg_color="#373739")
        self.username_label.place(x=30, y=95,)
        

        self.username_entry = CTkEntry(self.background_canvas)
        self.username_entry.place(x=30, y=115)

        self.password_label = CTkLabel(self.background_canvas, text="Senha:", fg_color="#FFFFFF", bg_color="#373739")
        self.password_label.place(x=230, y=95)

        self.password_entry = CTkEntry(self.background_canvas, show="*")
        self.password_entry.place(x=230, y=115)

        self.login_button = CTkButton(self.background_canvas, text="Entrar", fg_color="white", bg_color=None, command=self.login)
        self.login_button.place(x=155, y=145)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Implemente a lógica de verificação de usuário e senha
        # Aqui você pode comparar com um usuário/senha fixo ou verificar em um banco de dados
        if username == "admin" and password == "admin":
            self.after(1000, self.close_login_window)  # Aguarda 1000 milissegundos (1 segundo) e fecha a janela de login
        else:
            # Mostra uma mensagem de erro
            self.show_error_message("Usuário ou senha incorretos")

    def show_error_message(self, message):
        # Mostra uma mensagem de erro
        tk.messagebox.showerror("Erro", message)

    def close_login_window(self):
        self.withdraw()  # Oculta a janela de login
        MainWindow().mainloop()  # Abre a janela principal

if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
