class Tv:
    def __init__(self, tamanho, marca, ligada, volume, canal):
        self.tamanho = tamanho
        self.marca = marca
        self.ligada = ligada
        self.volume = volume
        self.canal = canal

    def mudar_canal(self, novo_canal):
        if self.ligada and 1 <= novo_canal <= 100:
            self.mudar_canal = novo_canal
    
    def ligar_desligar(self):
        self.ligada = not self.ligada

    def aumentar_volume(self):
        if self.ligada and self.volume < 100:
            self.volume += 1

    def diminuir_volume(self):
        if self.ligada and self.volume > 0:
            self.volume -=1

    def __str__(self):
        estado = "ligada" if self.ligada else "desligada"
        return f"TV {self.marca} de {self.tamanho} polegadas, {estado}, volume {self.volume}, canal {self.canal}"

minha_tv = Tv(32, "Philips", volume=3, ligada=True, canal=4 )
print (minha_tv)
