import unittest
from cifra_vigenere import CifraVigenere

class TestCifraVigenere(unittest.TestCase):

    def test_criptografia_basica(self):
        cifra = CifraVigenere("macaco")
        resultado = cifra.codificar("bom dia")
        self.assertEqual(resultado.replace(" ", ""), "NOODKO")

    def test_criptografia_chave_curta(self):
        cifra = CifraVigenere("limao")
        resultado = cifra.codificar("ATACARBASESUL")
        self.assertEqual(resultado, "LMLMORFIMVWIQ")

    def test_criptografia_chave_longa(self):
        cifra = CifraVigenere("SEGURANCA")
        resultado = cifra.codificar("BOMDIA")
        self.assertEqual(resultado, "TCTXNL")

    def test_criptografia_com_espacos(self):
        cifra = CifraVigenere("macaco")
        resultado = cifra.codificar("ataque ao amanhecer")
        self.assertEqual(resultado.replace(" ", ""), "MVMGCWKMMLWQPGSXI")

    def test_criptografia_com_caracteres_invalidos(self):
        cifra = CifraVigenere("macaco")
        with self.assertRaises(ValueError) as cm:
            cifra.codificar("ataque em 3...")
        self.assertEqual(str(cm.exception), "Não utilize caracteres especiais!")

    def test_criptografia_com_numeros_por_extenso(self):
        cifra = CifraVigenere("macaco")
        with self.assertRaises(ValueError) as cm:
            cifra.codificar("ataque tres")
        # Como números por extenso são permitidos, não deve lançar erro.
        self.assertEqual(cifra.codificar("ataque tres").replace(" ", "").isalpha(), True)

    def test_maiusculas_minusculas(self):
        cifra = CifraVigenere("MaCaCo")
        resultado = cifra.codificar("Bom Dia")
        self.assertEqual(resultado.replace(" ", ""), "NOODKO")

    def test_texto_vazio(self):
        cifra = CifraVigenere("macaco")
        with self.assertRaises(ValueError) as cm:
            cifra.codificar("")
        self.assertEqual(str(cm.exception), "Forneça um texto para ser criptografado")

    def test_chave_vazia(self):
        with self.assertRaises(ValueError) as cm:
            CifraVigenere("")
        self.assertEqual(str(cm.exception), "Forneça uma chave para criptografar")

    def test_chave_com_caracteres_invalidos(self):
        with self.assertRaises(ValueError) as cm:
            CifraVigenere("123@#")
        self.assertEqual(str(cm.exception), "Forneça uma chave sem caracteres não-alfabéticos")

    def test_descriptografia_basica(self):
        cifra = CifraVigenere("macaco")
        texto_cifrado = cifra.codificar("bom dia")
        texto_decifrado = cifra.decodificar(texto_cifrado)
        self.assertEqual(texto_decifrado.replace(" ", ""), "BOMDIA")

    def test_descriptografia_com_espacos(self):
        cifra = CifraVigenere("macaco")
        texto_cifrado = "NOO DKO"
        texto_decifrado = cifra.decodificar(texto_cifrado)
        self.assertEqual(texto_decifrado.replace(" ", ""), "BOMDIA")

    def test_descriptografia_com_caracteres_invalidos(self):
        cifra = CifraVigenere("macaco")
        with self.assertRaises(ValueError) as cm:
            cifra.decodificar("N00 D@K")
        self.assertEqual(str(cm.exception), "Forneça uma palavra sem caracteres especiais!")

    def test_descriptografia_texto_vazio(self):
        cifra = CifraVigenere("macaco")
        with self.assertRaises(ValueError) as cm:
            cifra.decodificar("")
        self.assertEqual(str(cm.exception), "Forneça uma palavra válida!")

    def test_descriptografia_chave_vazia(self):
        with self.assertRaises(ValueError) as cm:
            CifraVigenere("").decodificar("NOODKO")
        self.assertEqual(str(cm.exception), "Forneça uma chave para criptografar")

    def test_end_to_end(self):
        texto_original = "bom dia"
        chave = "macaco"
        cifra = CifraVigenere(chave)
        criptografado = cifra.codificar(texto_original)
        descriptografado = cifra.decodificar(criptografado)
        self.assertEqual(descriptografado.replace(" ", ""), "BOMDIA")

if __name__ == "__main__":
    unittest.main()
