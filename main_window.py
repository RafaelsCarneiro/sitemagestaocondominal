import tkinter as tk
from cadastro_window import CadastroWindow
from consulta_visitantes_window import ConsultaVisitantesWindow
from consulta_window import ConsultaWindow
from visitantes_window import VisitantesWindow

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Janela Principal")
        self.geometry("500x400")
        self.setup_ui()

    def setup_ui(self):
        self.configure(bg="#B0B0B2")  # Cor ligeiramente mais clara

        frame = tk.Frame(
            self, width=500, height=400, bg="#B0B0B2"
        )
        frame.pack(expand=True, fill='both', padx=20, pady=20)

        label_welcome = tk.Label(frame, text="Bem-vindo ao seu sistema de \n gestão condominal", font=('Helvetica', 16, 'bold'), bg="#B0B0B2", fg="#000")
        label_welcome.pack(pady=20)

        btn_consulta = tk.Button(frame, text="Consulta de Moradores", bg="#fff", fg="#000", command=self.abrir_consulta, font=('Helvetica', 12), width=40)
        btn_consulta.pack(pady=10)

        btn_cadastro = tk.Button(frame, text="Cadastro de Novo Morador", bg="#fff", fg="#000", command=self.abrir_cadastro, font=('Helvetica', 12), width=40)
        btn_cadastro.pack(pady=10)

        btn_cadastrov = tk.Button(frame, text="Cadastro de Visitantes", bg="#fff", fg="#000", command=self.abrir_cadastro_visitantes, font=('Helvetica', 12), width=40)
        btn_cadastrov.pack(pady=10)

        btn_consultav = tk.Button(frame,text="Consulta de Visitantes", bg="#fff", fg="#000", command=self.abrir_consulta_visitantes, font=('Helvetica', 12), width=40)
        btn_consultav.pack(pady=10)

    def abrir_cadastro(self):
        cadastro_window = CadastroWindow(self.update_fields)

    def abrir_consulta(self):
        ConsultaWindow()

    def abrir_cadastro_visitantes(self):
        VisitantesWindow()

    def abrir_consulta_visitantes(self):
        ConsultaVisitantesWindow()

    def update_fields(self):
        # Adicionar qualquer lógica adicional necessária após o cadastro
        print("Campos atualizados na janela principal")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow()
    root.mainloop()
