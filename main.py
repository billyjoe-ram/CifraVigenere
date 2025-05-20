from cifra_vigenere import CifraVigenere

def main():
    mensagem = input("Digite a mensagem a ser codificada: ")
    palavra_chave = input("Digite a palavra-chave: ")

    cifra = CifraVigenere(palavra_chave)
    mensagem_codificada = cifra.codificar(mensagem)

    print("Mensagem codificada:", mensagem_codificada)

if __name__ == "__main__":
    main()
