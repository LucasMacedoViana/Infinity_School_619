'''Crie uma classe para armazenar as informações de um computador. O computador deve ter os seguintes atributos:-Modelo
-Fabricante
-Processador
-Memória RAM
-Tamanho do HD
-Espaço ocupado do HD
-Está ligado?Sua classe também deve ter os seguintes métodos:-liga() -> altera o status de "Está ligado" para True
-desliga() -> altera o status de "Está ligado" para False
-limparHD() -> recebe por parâmetro o tamanho do espaço que deseja liberar do HD
-ocuparHD() -> recebe por parâmetro o tamanho do espaço que deseja ocupar do HD
Lembre-se de manter as boas práticas na hora de criar os atributos, e certifique-se de que o valor passado nos métodos "limparHD" e "ocuparHD" sejam válidos!'''



class Computador:
    def __init__(self, modelo, fabricante, processador, ram, tamanhoHd, ocupacaoHd):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador = processador
        self.ram = ram
        self.tamanhoHd = tamanhoHd
        self.ocupacaoHd = ocupacaoHd
        self.ligado = bool()

    def ligar(self):
        self.ligado = True
        print('Está ligado')

    def desligar(self):
        self.ligado = False
        print('Está Desligado')

    def limparHD(self,limpar):
        if self.ocupacaoHd > 0 :
            self.ocupacaoHd -= limpar
            livre = self.tamanhoHd - self.ocupacaoHd

            if limpar > self.tamanhoHd:
                print('Não foi permitido liberar esse espaço ,póis ele é maior que o tamanho do HD')

            else:
                print(f'Você liberou {limpar} Gb, seu espaço atual é de {livre}Gb e estão ocupados {self.ocupacaoHd}Gb')

        else:
            print('Seu HD está totalmente Limpo')

    def ocuparHD(self, ocupar):
        if ocupar > self.tamanhoHd:
            print('Não foi permitido ocupar esse espaço ,póis ele é maior que o tamanho do HD')

        elif (ocupar + self.ocupacaoHd) > self.tamanhoHd:
            print('Espaço insuficiente')

        else:
            self.ocupacaoHd += ocupar
            livre = self.tamanhoHd - self.ocupacaoHd
            print(f'Você ocupou {ocupar} Gb, seu espaço atual é de {livre}Gb e estão ocupados {self.ocupacaoHd}Gb')

            if self.ocupacaoHd == self.tamanhoHd:
                print("Você acabou de lotar o seu HD!")

pc = Computador('nootbook', 'Intel','i5', '16gb', 100, 50)

print(f'Modelo: {pc.modelo} Fabrincate: {pc.fabricante} Processador: {pc.processador} Memoria ran: {pc.ram} Tamanho do Hd {pc.tamanhoHd}Gb Espaço Ocupado no HD: {pc.ocupacaoHd}Gb')



