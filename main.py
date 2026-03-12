historico = []

print("Calculadora Python") 

while True:
    print("Digite 'sair' para encerrar ou 'historico' para ver as operações.")
    entrada = input("Digite o primeiro número (ou comando): ")

    if entrada.lower() == "sair":
        print("Calculadora encerrada.")
        break

    if entrada.lower() == "historico": 
        print("\nHistórico de operações:") 
        for item in historico:
            print(item)
        print()
        continue

    try:
        num1 = float(entrada)
    except ValueError:
        print("Entrada inválida.\n")
        continue

    operador = input("Digite o operador (+, -, *, /): ")

    try:
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Número inválido.\n")
        continue

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            print("Erro: divisão por zero.\n")
            continue
        resultado = num1 / num2
    else:
        print("Operador inválido.\n")
        continue

    operacao = f"{num1} {operador} {num2} = {resultado}"
    historico.append(operacao)

    print("Resultado:", resultado)
    print()