import tkinter as tk

# 1 Janela principal 
janela = tk.Tk()
janela.title("Logo da empresa")
janela.geometry("400x550")
janela.configure(bg="white") # --> Background na pagina

# 2 logo
imagem_logo = tk.PhotoImage(file="logo.png")
logo = tk.Label(janela, image=imagem_logo, bg="#ffffff")
logo.pack(pady=(20, 40))

# 3 campo do email
campo_email = tk.Entry(janela, bg="#f0f0f0", fg="#515151", font=("Arial", 12), highlightbackground="#2ecc71", highlightthickness=1)
campo_email.insert(0, "E-mail")
campo_email.pack(pady=10, ipadx=50, ipady=8)

# 4 campo senha
campo_senha = tk.Entry(janela, bg="#f0f0f0", fg="#515151", font=("Arial", 12), highlightbackground="#e74c3c", highlightthickness=1)
campo_senha.insert(0, "Senha")
campo_senha.pack(pady=10, ipadx=50, ipady=8)

# 5 Adicionar um botao

botao = tk.Label(janela, text="Acessar", bg="#2980b9", fg="#ffffff", font=("Arial", 11, "bold"))
botao.pack(pady=(20, 15), ipadx=105, ipady=10)

janela.mainloop()