#Crie um programa que receba 2 números, some-os, e retorne o resultado ao Usúario

#Instale a biblioteca "tk" antes de usar
import tkinter as tk

# Funções de Lógica
def clicar(valor):
    atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, atual + str(valor))

def limpar():
    visor.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except Exception:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Calculadora Python")
janela.geometry("320x450")
janela.configure(bg="#1c1c1c") # Fundo Grafite Escuro
janela.resizable(False, False)

# Estilização do Visor
visor = tk.Entry(janela, width=15, font=("Arial", 28), bg="#1c1c1c", 
                 fg="#ffffff", borderwidth=0, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=30, sticky="nsew")

# Configurações de cores para os botões
estilo_num = {"bg": "#333333", "fg": "#ffffff", "font": ("Arial", 14), "borderwidth": 0}
estilo_op = {"bg": "#ff9f0a", "fg": "#ffffff", "font": ("Arial", 14, "bold"), "borderwidth": 0}
estilo_esp = {"bg": "#a5a5a5", "fg": "#000000", "font": ("Arial", 14), "borderwidth": 0}

# Lista de botões: (Texto, Linha, Coluna, Estilo)
botoes = [
    ('C', 1, 0, estilo_esp), ('/', 1, 3, estilo_op),
    ('7', 2, 0, estilo_num), ('8', 2, 1, estilo_num), ('9', 2, 2, estilo_num), ('*', 2, 3, estilo_op),
    ('4', 3, 0, estilo_num), ('5', 3, 1, estilo_num), ('6', 3, 2, estilo_num), ('-', 3, 3, estilo_op),
    ('1', 4, 0, estilo_num), ('2', 4, 1, estilo_num), ('3', 4, 2, estilo_num), ('+', 4, 3, estilo_op),
    ('0', 5, 0, estilo_num), ('.', 5, 2, estilo_num), ('=', 5, 3, estilo_op),
]

# Criar e posicionar os botões dinamicamente
for (texto, linha, col, estilo) in botoes:
    # Ajuste para o botão '0' e 'C' ocuparem mais espaço se necessário
    colspan = 2 if texto == '0' else 1
    if texto == 'C': colspan = 3
    
    # Definir comando do botão
    if texto == '=':
        comando = calcular
    elif texto == 'C':
        comando = limpar
    else:
        comando = lambda t=texto: clicar(t)
        
    btn = tk.Button(janela, text=texto, command=comando, **estilo)
    btn.grid(row=linha, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Configurar o peso das colunas e linhas para os botões expandirem
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()