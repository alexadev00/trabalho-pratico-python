saida = ''

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    return num1 / num2

def calculadora(num1, num2, operacao):
    if operacao in ('+', 'soma'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtracao'):
        resultado = subtracao(num1, num2)
    elif operacao in ('*', 'multiplicacao'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisao'):
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    
    return resultado

while saida.lower() != 'n':
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação (+, -, *, soma, subtracao, multiplicacao, divisao): ')
        
        resultado = calculadora(num1, num2, operacao)
        print('Resultado da operação:', resultado)
        
        saida = input('Deseja continuar? (s/n): ')
    except ValueError:
        print('Erro: Entrada inválida. Por favor, insira números válidos.')
