from funcoes import mensagem
from dados import Ruas
from time import sleep


class RedAlert:

    def __init__(self):
        mensagem()

    def cadastro_nome(self):
        self.nome = input("Nome: ").upper().strip()
        self.Endereco = input("Sua Rua: ").upper().strip()

    def verificar(self):
            for nome_rua in Ruas[0]['Endereço'].items():
                if nome_rua[0] == self.Endereco:
                    print()
                    print(f"\033[32mOlá Sr(a) {self.nome}")
                    print("Localizamos o Endereço, verificando o horario\033[m")
                    sleep(2)
                    print()
                    print(f"Rua: {nome_rua[0]} - Horario: {nome_rua[1]}")
                    exit(0)
            if nome_rua[0] not in self.Endereco:
                print("\033[31mNÂO foi lozalizado o Endereço.\033[m")
            self.cadastro_nome()
            self.verificar()





