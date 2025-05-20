class CifraVigenere:
    def __init__(self, palavra_chave):
        if not palavra_chave:
            raise ValueError("Forneça uma chave para criptografar")
        if not palavra_chave.isalpha():
            raise ValueError("Forneça uma chave sem caracteres não-alfabéticos")
        self.palavra_chave = palavra_chave.upper()
        self.alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __repetir_chave(self, texto):
        chave_repetida = ''
        indice = 0
        for c in texto:
            if c.isalpha():
                chave_repetida += self.palavra_chave[indice % len(self.palavra_chave)]
                indice += 1
            else:
                chave_repetida += c
        return chave_repetida

    def __validar_texto(self, texto, criptografar=True):
        if not texto:
            raise ValueError("Forneça um texto para ser criptografado" if criptografar else "Forneça uma palavra válida!")
        if any(c.isdigit() for c in texto):
            raise ValueError("Escreva os números por extenso")
        if any(not c.isalpha() and not c.isspace() for c in texto):
            raise ValueError("Não utilize caracteres especiais!" if criptografar else "Forneça uma palavra sem caracteres especiais!")

    def codificar(self, mensagem):
        self.__validar_texto(mensagem)
        mensagem = mensagem.upper().replace(" ", "")
        chave = self.__repetir_chave(mensagem)
        resultado = ''
        for i, letra in enumerate(mensagem):
            idx = (self.alfabeto.index(letra) + self.alfabeto.index(chave[i])) % 26
            resultado += self.alfabeto[idx]
        return resultado

    def decodificar(self, mensagem_codificada):
        self.__validar_texto(mensagem_codificada, criptografar=False)
        mensagem_codificada = mensagem_codificada.upper().replace(" ", "")
        chave = self.__repetir_chave(mensagem_codificada)
        resultado = ''
        for i, letra in enumerate(mensagem_codificada):
            idx = (self.alfabeto.index(letra) - self.alfabeto.index(chave[i])) % 26
            resultado += self.alfabeto[idx]
        return resultado
