#  script-para-trocar-senha-python

Um sistema simples de autenticação e redefinição de credenciais via terminal feito em Python.

## 🤷‍♂️ Sobre o Projeto

Este repositório nasceu do mais puro suco do ócio estudantil. Eu estava sem absolutamente nada para fazer durante a aula no SENAI, olhei para o VS Code e decidi criar uma estrutura de login com troca de senha dinâmica para testar o comportamento de variáveis globais dentro de loops estruturados (`while`).

O script simula um painel onde a senha atualizada na memória passa a ser exigida imediatamente nas tentativas de login seguintes, substituindo a chave padrão de forma dinâmica.

##  Funcionalidades

*   **Menu interativo:** Escolha de opções direto pelo terminal usando Strings (`"1"`, `"2"`, `"3"`).
*   **Tela de Login:** Autenticação simples validando o usuário (`admin`) e a senha atual da variável.
*   **Troca de Senha:** Substitui o valor de `senhaFixa` na memória do programa em tempo real, descartando a chave inicial (`1234`) caso o usuário confirme com `"S"`.

## Como testar (Se você também estiver sem nada para fazer na aula)

Você só precisa ter o Python instalado na máquina. Abra o terminal na pasta do arquivo e execute:

```bash
python tarefa.py
```
