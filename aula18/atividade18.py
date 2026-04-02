import tkinter as tk


def enviar():
    print("Nome:", nome.get())
    print("Idade:", idade.get())
    print("Email:", email.get())
    print("Endereço:", endereco.get())
    print("Celular:", celular.get())
    print("CEP:", cep.get())
    print("Cidade:", cidade.get())
    print("Cursos:", cursos.get())
    print("------------------------")


janela = tk.Tk()
janela.title("Cadastro")
janela.geometry("1700x750")


tk.Label(janela, text="Nome").pack()
nome = tk.Entry(janela)
nome.pack()

tk.Label(janela, text="Idade").pack()
idade = tk.Entry(janela)
idade.pack()

tk.Label(janela, text="Email").pack()
email = tk.Entry(janela)
email.pack()

tk.Label(janela, text="Endereço").pack()
endereco = tk.Entry(janela)
endereco.pack()

tk.Label(janela, text="Celular").pack()
celular = tk.Entry(janela)
celular.pack()

tk.Label(janela, text="CEP").pack()
cep = tk.Entry(janela)
cep.pack()

tk.Label(janela, text="Cidade").pack()
cidade = tk.Entry(janela)
cidade.pack()

tk.Label(janela, text="Cursos").pack()
cursos = tk.Entry(janela)
cursos.pack()


tk.Button(janela, text="Enviar", command=enviar).pack(pady=10)

janela.mainloop()