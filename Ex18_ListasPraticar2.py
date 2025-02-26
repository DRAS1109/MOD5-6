"""
Programa para gerir livros de uma biblioteca e os seus emprestimos
- Ler o titulo do livro a emprestar
- Remover da lista de livros para a lista de emprestimo
- Mostrar os livros e emprestimos
- O programa deve terminar quando é inserido um título em branco ou quando não há mais livros para emprestar
- Avisar o utilizador quando o livro ja esta emprestado
"""

Livros = ["Livro 1", "Livro 2", "Livro 3", "Livro 4"]
Emprestados = []

while True:
    #Ler o titulo do livro a emprestar
    Livro = input("Qual livro pretende emprestar? ")

    #Terminar programa
    if Livro != "" and len(Livros) > 0:

        #Emprestar
        if Livro in Livros:
            print("Livro emprestado :D \n")
            Emprestados.append(Livro)
            Livros.remove(Livro)

        #Avisar se ja está emprestado
        elif Livro in Emprestados:
            print("Esse livro ja está emprestado x_X \n")

        #Avisar se o livro não existe
        else:
            print("O livro não está na base de dados \n")

    else:
        #Mostrar os livros e emprestimos
        print("Livros por emprestar:")
        for Livro in Livros:
            print(Livro)
        print("")

        print("Livros emprestados:")
        for Livro in Emprestados:
            print(Livro)
        print("")

        break