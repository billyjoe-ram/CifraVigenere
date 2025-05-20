# 🔐 Cifra de Vigenère em Python

Implementação simples e robusta da **Cifra de Vigenère**, uma técnica de criptografia por substituição polialfabética, desenvolvida com foco em clareza, testes e validações de entrada.

---

## 📖 Sumário

1. [Descrição do Projeto](#descrição-do-projeto)
2. [Como Usar](#como-usar)
3. [Requisitos Funcionais](#requisitos-funcionais)
4. [Requisitos Não Funcionais](#requisitos-não-funcionais)
5. [Execução de Testes](#execução-de-testes)
6. [Estrutura do Projeto](#estrutura-do-projeto)
7. [Licença](#licença)

---

## 📘 Descrição do Projeto

Este projeto aplica a **Cifra de Vigenère** para criptografar e descriptografar mensagens de texto. O algoritmo utiliza uma chave alfabética que é repetida para coincidir com o comprimento da mensagem original, permitindo cifragem mais segura que cifras monoalfabéticas como a de César.

O sistema é capaz de validar entradas, rejeitar caracteres inválidos e manter a robustez mesmo com variações de espaços e capitalização.

---

## ▶️ Como Usar

### Executando o programa:

```bash
python main.py
```

Você será solicitado a inserir:

* Uma **mensagem** (ex: `"bom dia"`)
* Uma **palavra-chave** (ex: `"macaco"`)

O resultado será uma mensagem cifrada impressa no console.

---

## ✅ Requisitos Funcionais

* [x] Codificar mensagens usando a Cifra de Vigenère
* [x] Decodificar mensagens cifradas
* [x] Aceitar chaves curtas ou longas, repetindo a chave conforme necessário
* [x] Rejeitar entradas com:

  * Números (devem ser escritos por extenso)
  * Caracteres especiais e pontuações
  * Strings vazias
* [x] Manter insensibilidade a maiúsculas/minúsculas
* [x] Permitir espaços em mensagens sem afetar a lógica da cifra
* [x] Levantar exceções com mensagens específicas para entradas inválidas
* [x] Suporte completo à reversibilidade (criptografia → descriptografia)

---

## ⚙️ Requisitos Não Funcionais

* **Validação robusta de entrada**:

  * Caracteres devem ser apenas letras (a-z, A-Z)
  * Erros retornam mensagens claras e específicas
* **Cobertura de testes automatizados** com `unittest`:

  * Casos comuns, limites e entradas inválidas
* **Código modular e manutenível**:

  * Separação em `main.py`, `cifra_vigenere.py`, e `test_cifra_vigenere.py`
* **Compatível com Python 3.6 ou superior**
* **Boas práticas de POO** com encapsulamento e validações privadas

---

## 🧲 Execução de Testes

Para rodar todos os testes:

```bash
python -m unittest test_cifra_vigenere.py
```

Testes abordam:

* Criptografia e descriptografia com chaves variadas
* Rejeição de caracteres especiais e números
* Comportamento com espaços e maiúsculas/minúsculas
* Casos de erro (chave ou mensagem vazia)
* Reversibilidade (end-to-end)

---

## 📁 Estrutura do Projeto

```
.
├── main.py                  # Interface principal de uso
├── cifra_vigenere.py        # Implementação da lógica da cifra
├── test_cifra_vigenere.py   # Suite de testes unitários
```

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
