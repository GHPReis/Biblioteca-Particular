# Variáveis globais
lista_livro = [] # Lista de dicionário para armazenar os livros
id_global = 0 # Variável global para controlar o ID dos livros

# Função pra cadastrar um livro
def cadastrar_livro(id):
    print('-'*19, 'CADASTRAR LIVRO', '-'*20)
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o nome do autor: ')
    editora = input('Digite o nome da editora: ')
    print('-'*56)
    livro = {
        'ID': id,
        'Nome': nome,
        'Autor': autor,
        'Editora': editora    
    }
    
    lista_livro.append(livro)

#Função para consultar livros
def consultar_livro():
    while True:
        print('-'*19, 'CONSULTAR LIVRO', '-'*20)
        print('Escolha a opção desejada')
        print('1 - Consultar todos os livros')
        print('2 - Consultar livro por ID')
        print('3 - Consultar livro por autor')
        print('4 - Retornar ao menu principal')
        print()
        opcao = input('Escolha uma opção: ')
        print('-'*56)
        
        if opcao == '1':
            for livro in lista_livro:
                print("ID:", livro["ID"])
                print("Nome:", livro["Nome"])
                print("Autor:", livro["Autor"])
                print("Editora:", livro["Editora"])
                print('-'*56)
        elif opcao == '2':
            id_busca = int(input('Digite o ID do livro que deseja consultar: '))
            for livro in lista_livro:
                if livro["ID"] == id_busca:
                    print("ID:", livro["ID"])
                    print("Nome:", livro["Nome"])
                    print("Autor:", livro["Autor"])
                    print("Editora:", livro["Editora"])
                    print('-'*56)
                    break
            else:
                print('Livro não encontrado.')
        elif opcao == '3':
                autor_busca = input('Digite o nome do autor que deseja consultar: ')
                for livro in lista_livro:
                    if livro['Autor'] == autor_busca:
                        print("ID:", livro["ID"])
                        print("Nome:", livro["Nome"])
                        print("Autor:", livro["Autor"])
                        print("Editora:", livro["Editora"])
                        print('-'*56)
        elif opcao == '4':
            break
        else:
            print('Opção inválida')
                
# Função para remover um livro
def remover_livro():
    print('-'*20, 'REMOVER LIVRO', '-'*21)
    id_remover = int(input('Digite o ID do livro que deseja remover: '))
    print()
    for livro in lista_livro:
        if livro['ID'] == id_remover:
            lista_livro.remove(livro)
            print('Livro removido com sucesso.')
            print('-'*56)
            return
    print('Livro não encontrado.')

# Função principal

def main():
    print ('Bem-vindo ao controle de livros do Gabriel Henrique de Paula Reis')
    print()
    
    while True:
        print('-'*20, 'MENU PRINCIPAL', '-'*20)
        print('1 - Cadastrar livro')
        print('2 - Consultar livro')
        print('3 - Remover livro')
        print('4 - Encerrar programa')
        print()
        
        opcao = input('Escolha uma opção: ')
        print('-'*56)
        
        if opcao == '1':
            global  id_global
            id_global += 1
            cadastrar_livro(id_global)
        elif opcao == '2':
            consultar_livro()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            break
        else:
            print('opção inválida')
    print('Encerrando programa...')
    
if __name__ == '__main__':
    main()