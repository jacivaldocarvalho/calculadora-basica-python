def calculadora(num1, num2, operacao):
    if operacao == 1:  # Soma
        return num1 + num2
    elif operacao == 2:  # Subtração
        return num1 - num2
    elif operacao == 3:  # Multiplicação
        return num1 * num2
    elif operacao == 4:  # Divisão
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:  # Operação inválida
        return 0


def main():

    # Exemplos de uso
    print("Resultados da Calculadora:")
    print("1. Soma -> 10 + 5 = ", calculadora(10, 5, 1))  # Saída: 15
    print("2. Subtração -> 10 - 5 = ", calculadora(10, 5, 2))  # Saída: 5
    print("3. Multiplicação -> 10 * 5 = ", calculadora(10, 5, 3))  # Saída: 50
    print("4. Divisão -> 10 / 5 = ", calculadora(10, 5, 4))  # Saída: 2.0
    print("4. Divisão -> 10 / 0 = ", calculadora(10, 0, 4))  # Divisão por 0!
    print("Operação inválida:", calculadora(10, 5, 5))  # Saída: 0


if __name__ == "__main__":
    main()
