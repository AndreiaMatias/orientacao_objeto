class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Criando objeto...")
        self.__numero = numero #atributo privado
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.saldo} do titular{self.titular}")

    def deposita(self, valor):
        self.__saldo +=valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite