class Console:
    def __init__(self, modelo, marca, desempenho, custo):
        self.modelo = modelo
        self.marca = marca
        self.desempenho = desempenho
        self.custo = custo
    def __str__(self):
        return 'Modelo: '+ self.modelo + '\nMarca: '+ self.marca + '\nDesempenho: '+ self.desempenho + '\nCusto: '+ self.custo
        
        
console1 = Console('Playstation 4', 'Sony', 'Alta taxa de quadros', 'R$1500 - R$2000')
print(console1)

