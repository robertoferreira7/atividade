def pertence_fibonacci(numero):
    anterior = 0
    proxima = 1
    
    for n in range(20): 
        if anterior == numero or proxima == numero:
            return f"{numero} pertence a sequência de fibonacci."
        
        soma = proxima + anterior
        anterior = proxima
        proxima = soma
    
    return f"{numero} nao pertence a sequência de fibonacci."

numero_informado = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero_informado)
print(resultado)