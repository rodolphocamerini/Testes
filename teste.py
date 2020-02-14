class Bola:
    def __init__(self, cor,circunf,material):
        self.cor = cor
        self.circunf = circunf
        self.material = material
    @property
    def troca_cor(self):
        return self.cor
    
    @troca_cor.setter
    def troca_cor(self,novacor):
        self.cor = novacor
        return self.cor
    def __str__(self):
        return f' {self.cor},{self.circunf},{self.material}'
    
    
       
bola = Bola('azul',10,'couro')
bola.troca_cor =  'preto'
print(bola) 