def calculadora(num1,num2, operacao):
    if(operacao == 1):
        return num1 + num2
    elif(operacao == 2):
        return num1 - num2
    elif(operacao == 3):
        return num1 * num2
    elif(operacao == 4):
        return num1 / num2
    else:
        return 0


    
operacao =  -1


while (operacao != 0):


    valor1 = float(input("Informe o 1º Valor: "))
    valor2 = float(input("Informe o 2º Valor: "))


    print("Escolha uma opção da calculadora: ")
    print("1 - Soma ")
    print("2 - Subtração")
    print("3 - Multiplicação ")
    print("4 - Divisão")
    print("0 - Sair ")
    operacao = int(input("Informe a opção: "))
    if(operacao < 0) or (operacao > 4):
        print("Opção Invalida")


    elif(operacao == 0):
        print ("Ao informar zero você sai da calculadora")
        break
    else:
        resultado = calculadora(valor1,valor2,operacao)
    print("O resultado é: ", resultado)




