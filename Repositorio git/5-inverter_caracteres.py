def inverter_string(texto):
    
    invertida = ""
    
    
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    
    return invertida


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Ver um exemplo de texto invertido")
        print("2 - inverta seu texto")
        print("0 - Sair")
        
        opcao = input("Digite 1, 2 ou 0: ")
        
        if opcao == "1":
            
            texto_original_exemplo = "o rato roeu a roupa do rei de roma"
            texto_invertido_exemplo = inverter_string(texto_original_exemplo)
            print("\nTexto original (predefinido):", texto_original_exemplo)
            print("Texto invertido (predefinido):", texto_invertido_exemplo)
        
        elif opcao == "2":
            
            texto_original_usuario = input("\nDigite uma string: ")
            texto_invertido_usuario = inverter_string(texto_original_usuario)
            print("\nTexto original (usuário):", texto_original_usuario)
            print("Texto invertido (usuário):", texto_invertido_usuario)
        
        elif opcao == "0":
            print("Saindo do programa...")
            break  
        
        else:
            print("\nOpção inválida. Tente novamente.")


main()