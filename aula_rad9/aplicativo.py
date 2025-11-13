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

        tk.Button(btn_frame, text="Listar Usuarios", command=self.listar_usuarios).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Criar Usuario", command=self.criar_usuario).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Atualizar Usuario", command=self.atualizar_usuario).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Deletar Usuario", command=self.deletar_usuario).grid(row=0, column=3, padx=5)

        self.email_var = tk.StringVar()
        self.senha_var = tk.StringVar()
        self.novo_email_var = tk.StringVar()

        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Email: ").grid(row=0, column=0)
        tk.Entry(entry_frame, textvariable=self.email_var).grid(row=0, column=1)

        tk.Label(entry_frame, text="Senha: ").grid(row=1, column=0)
        tk.Entry(entry_frame, textvariable=self.senha_var).grid(row=1, column=1)

        tk.Label(entry_frame, text="Novo Email (atualizar): ").grid(row=2, column=0)
        tk.Entry(entry_frame, textvariable=self.novo_email_var).grid(row=2, column=1)

    def listar_usuarios(self):
        try:
            response = requests.get(f"{API_URL}/listar_usuarios")
            if response.status_code == 200:
                self.tree.delete(*self.tree.get_children())
                for usuario in response.json():
                    self.tree.insert("", "end", values=(usuario["id"], usuario["email"]))
            else:
                messagebox.showerror("Erro", "erro ao buscar usuarios.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na requisição: {e} ")

    def criar_usuario(self):
        email = self.email_var.get()
        senha = self.senha_var.get()
        if not email or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        payload = {"email": email, "password": senha}
        try:
            response = requests.post(f"{API_URL}/criar_usuarios", json=payload)
            if response.status_code == 201:
                messagebox.showinfo("Sucesso", "Usuario criado.")
                self.listar_usuarios()
            else:
                messagebox.showerror("Erro", response.json())
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na requisição: {e}")
    
    def atualizar_usuario(self):
        selecionar_item = self.tree.selection()
        novo_email = self.novo_email_var.get()

        if not selecionar_item or not novo_email:
            messagebox.showwarning("Aviso", "Selecione um usuario e insira o novo email.")
            return

        usuario_id = self.tree.item(selecionar_item[0])["values"][0]
        payload = {"email": novo_email}

        try:
            response = requests.put(f"{API_URL}/atualizar_usuarios/{usuario_id}", json=payload)
            if response.status_code == 200:
                messagebox.showinfo("Sucesso", "Email atualizado.")
                self.listar_usuarios()
            else:
                messagebox.showerror("Erro", "Erro ao atualizar.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na requisicao: {e}")
    
    def deletar_usuario(self):
        selecionar_item = self.tree.selection()
        if not selecionar_item:
            messagebox.showwarning("Aviso", "Selecione um usuario.")
            return

        usuario_id = self.tree.item(selecionar_item[0])["values"][0]

        try:
            response = requests.delete(f"{API_URL}/deleta_usuarios/{usuario_id}")
            if response.status_code == 200:
                messagebox.showinfo("Sucesso", "Usuario deletado.")
                self.listar_usuarios()
            else:
                messagebox.showerror("Erro", "Erro ao deletar o usuario.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na requisicao: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UsuarioApp(root)
    root.mainloop()