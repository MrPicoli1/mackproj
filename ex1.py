acao = "x"

while acao != 0 :
  print("Digite + para fazer a soma de dois numeros")
  print("Digite - para fazer a subtracao de dois numeros")
  print("Digite / para fazer a divisao de dois numeros")
  print("Digite * para fazer a multiplicacao de dois numeros")
  acao = input()
  if acao == "+":
    a = float(input("Digite o primeiro numero"))
    b = float(input("Digite o segundo numero"))
    c = a+b
    print(a," + ",b, " = ", c)
  elif acao == "-":
    a = float(input("Digite o primeiro numero"))
    b = float(input("Digite o segundo numero"))
    c = a-b
    print(a," - ",b, " = ", c)
  elif acao == "/":
    a = float(input("Digite o primeiro numero"))
    b = float(input("Digite o segundo numero"))
    c = a/b
    print(a," / ",b, " = ", c)
  elif acao == "*":
    a = float(input("Digite o primeiro numero"))
    b = float(input("Digite o segundo numero"))
    c = a*b
    print(a," * ",b, " = ", c)
  elif acao == 0:
    print ("O programa acabou")
  else:
    print("Entra invalida")