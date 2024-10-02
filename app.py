nomes = ["Ana", "Carlos", "Fernanda", "Gustavo", "Juliana", "Lucas", "Mariana", "Roberto", "Sofia", "Thiago"]

#exebir a lista 
for i in range(len(nomes)):
    print(f"Índice {i}: {nomes[i]}.")
try:
    #usuário informa o índice
    indice = int(input("Informe o índice que deseja alterar: "))
    confirmacao = input(f"Deseja alterar o nome {nomes[indice]}? Digite 'SIM' para confirmar. ")
    if confirmacao == "sim":
        novo_nome = input("Informe o novo nome: ")
        nomes[indice] = novo_nome
        for i in range(len(nomes)):
            print(f"Índice {i}: {nomes[i]}.")
            
    indice = int(input("Informe o índice do nome que deseja excluir: "))
    confirmacao = input(f"Deseja excluir o nome {nomes[indice]}? Digite 'SIM' para confirmar. ")
    if confirmacao == "sim":
        del(nomes[indice])
        print("nome deletado com sucesso.")
    else:
        ...
except Exception as e:
    print(f"Não foi possível deletar o nome. {e}.")
finally:
    #exebir a lista
    for i in range(len(nomes)):
        print(f"Índice {i}: {nomes[i]}.")
    
    confirmacao = input(f"Deseja sair do programa? Digite 'SIM' para confirmar. ")
    if confirmacao == "sim":
        print("Obrigado volte sempre!")
    

   
        
        
      

    