def seq_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False''''''

while True:
    
    numero = int(input("Informe um número (ou -1 para sair): "))
    
    
    if numero == -1:
        print("Saindo do programa.")
        break

    
    if seq_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")