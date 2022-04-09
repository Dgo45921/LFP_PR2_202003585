class Token:
    def __init__(self, lexema, linea, columna, tipo):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.tipo = tipo