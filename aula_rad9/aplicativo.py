import tkinter as tk
from tkinter import messagebox, ttk
import requests

API_URL = "http://127.0.0.1:5009"

class UsuarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Usuarios")
        self.root.geometry("600x400")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.tree = ttk.Treeview(self.frame, columns=("id", "email"), show='headings')
        self.tree.heading("id", text="ID")
        self.tree.heading("email", text="Email")
        self.tree.pack()

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Listar Usuarios", command=self.listar_usuarios).grid(row=0, column=5, padx=5)

    def listar_usuarios():
        ...

if __name__ == "__main__":
    root = tk.Tk()
    app = UsuarioApp(root)
    root.mainloop()