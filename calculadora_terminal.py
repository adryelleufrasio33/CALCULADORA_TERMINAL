import math

numeros = []
while True:

    print("Essa é sua calculadora de operações simples")
    print("Escolha umas das operações abaixo")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = input("Escolha uma das opçoes abaixo")

    if opcao == "1":
        while True:
          
          desejo_soma = input("Deseja inserir  numeros, para afirmativo s/ para negativo n").upper()
          if desejo_soma == "S":
             n = float(input("Digite seus valores"))
          elif desejo_soma == "N":
             print("Soma encerrada")
             print(numeros)
             break
          else:
             raise ValueError("Valor não encontrado")
             
       
          numeros.append(n)
          soma =  sum(numeros)
          print(soma)
    elif opcao == "2":
        while True:
          
           desejo_sub = input("Deseja realizar outra subtração S/N").upper()
           if desejo_sub == "S":
             print("Digite dois numeros para subtrair por vez")
             sub1 = float(input("Digite o primeiro valor"))
             sub2 = float(input("Digite o segundo valor"))
             subtracao = sub1 - sub2
             print(subtracao)
           elif desejo_sub == "N":
              print("Operação Encerrada ") 
              break
           else:
            raise ValueError("Valor não encontrado")
    elif opcao == "3":
       while True:
          opcao_multi = input("Deseja realizar multiplicação").upper()
          if opcao_multi == "S":
             multi = float(input("Digite o numero"))
            
          elif opcao_multi == "N":
             print("Operação encerrada")
             print(resultado)
             break
          else:
             print("Valor não encontrado")
             raise ValueError("Valor não encontrado")
          
          numeros.append(multi)
          resultado = math.prod(numeros)
          print(resultado)
    elif opcao == "4":
       
       while True:
          print("Digite dois numeros para dividir por vez")
          desejo_div =  input("Deseja realizar divisão S/N").upper()
          if desejo_div == "S":
             div_1 = float(input("Digite o primeiro número"))
             div_2 = float(input("Digite o segundo número"))
             divisao = div_1/div_2
             print(divisao)
          elif desejo_div == "N":
             print("Programa Encerrado")
             print(divisao)
             break
          else:
             print("Valor não encontrado")
             raise ValueError("Valor não encontrado") 
    elif opcao == "5":
       print("Programa encerrado")
       break
    else:
       print("Opção não encontrada")
       break       
          
          
          
           
           
        
        


           
        
       
        
