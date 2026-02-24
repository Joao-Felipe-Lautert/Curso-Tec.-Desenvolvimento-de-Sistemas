#Importe as duas bibliotecas, para funcionalidade completa (somente a "tk" é essencial)
import tkinter as tk
import math # Importante para funções avançadas

# Funções de Lógica
def clicar(valor):
    atual = visor.get()
    # Se o visor tiver um erro, limpamos antes de digitar
    if atual == "Erro":
        visor.delete(0, tk.END)
        atual = ""
    visor.insert(tk.END, str(valor))

def limpar():
    visor.delete(0, tk.END)

def calcular():
    try:
        # O eval() executa a string como código Python
        expressao = visor.get()
        # Substituímos o símbolo de porcentagem por /100 para o eval entender
        expressao = expressao.replace('%', '/100')
        
        resultado = eval(expressao)
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except Exception:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# Janela Principal
janela = tk.Tk()
janela.title("Calculadora Pro")
janela.geometry("380x550") # Aumentei um pouco para caber os botões novos
janela.configure(bg="#1c1c1c")
janela.resizable(False, False)

# Visor
visor = tk.Entry(janela, font=("Arial", 24), bg="#1c1c1c", fg="#ffffff", borderwidth=0, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=30, sticky="nsew")

# Estilos
estilo_num = {"bg": "#333333", "fg": "#ffffff", "font": ("Arial", 12), "borderwidth": 0}
estilo_op = {"bg": "#ff9f0a", "fg": "#ffffff", "font": ("Arial", 12, "bold"), "borderwidth": 0}
estilo_esp = {"bg": "#a5a5a5", "fg": "#000000", "font": ("Arial", 12, "bold"), "borderwidth": 0}
estilo_cient = {"bg": "#ff9f0a", "fg": "#ffffff", "font": ("Arial", 12, "bold"), "borderwidth": 0}

#Layout de botões da calculadora
botoes = [
    # Linha 1: Funções de Limpeza, Parênteses e divisão
    ('C', 1, 0, estilo_esp, 'C'), ('(', 1, 1, estilo_esp, '('), (')', 1, 2, estilo_esp, ')'), ('/', 1, 3, estilo_op, '/'),
    # Linha 2: Raiz, Potências e Fatorial
    ('sqrt', 2, 0, estilo_cient, 'math.sqrt('), ('x²', 2, 1, estilo_cient, '**2'), ('^', 2, 2, estilo_cient, '**'), ('n!', 2, 3, estilo_cient, 'math.factorial('),
    # Linha 3: PI, porcentagem, multiplicação e subtração
    ('pi', 3, 0, estilo_cient, 'math.pi'), ('%', 3, 1, estilo_cient, '%'), ('*', 3, 2, estilo_op, '*'), ('-', 3, 3, estilo_op, '-'),
    # Linha 4: Teclado 7-8-9 e soma
    ('7', 4, 0, estilo_num, '7'), ('8', 4, 1, estilo_num, '8'), ('9', 4, 2, estilo_num, '9'), ('+', 4, 3, estilo_op, '+'),
    # Linha 5: Teclado 4-5-6 e "="
    ('4', 5, 0, estilo_num, '4'), ('5', 5, 1, estilo_num, '5'), ('6', 5, 2, estilo_num, '6'), ('=', 5, 3, estilo_op, '='),
    # Linha 6: Teclado 1-2-3 e 0
    ('1', 6, 0, estilo_num, '1'), ('2', 6, 1, estilo_num, '2'), ('3', 6, 2, estilo_num, '3'), ('0', 6, 3, estilo_num, '0'),
    # Linha 7: Ponto decimal
    ('.', 7, 0, estilo_num, '.')
]

for (texto, linha, col, estilo, valor_real) in botoes:
    colspan = 1
    if texto == '=': 
        comando = calcular
    elif texto == 'C': 
        comando = limpar
    else:
        # Aqui passamos o 'valor_real' para a função clicar
        comando = lambda v=valor_real: clicar(v)
        
    btn = tk.Button(janela, text=texto, command=comando, **estilo)
    btn.grid(row=linha, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

# Configuração de expansão das colunas/linhas
for i in range(8): janela.grid_rowconfigure(i, weight=1)
for i in range(4): janela.grid_columnconfigure(i, weight=1)

janela.mainloop()
