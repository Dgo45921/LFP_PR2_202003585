from Token import Token
from Error import Error
from prettytable import PrettyTable


class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ""
        self.estado = 0
        self.i = 0

    def imprimir_tokens(self):
        x = PrettyTable()
        x.field_names = ["lexema", "linea", "columna", "tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna, token.tipo])
        print(x)

    def imprimir_errores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "linea", "columna"]
        for error in self.listaErrores:
            x.add_row([error.descripcion, error.linea, error.columna])
        print(x)

    def agrega_token(self, lexema, linea, columna, tipo):
        self.listaTokens.append(Token(lexema, linea, columna, tipo))
        self.buffer = ""

    def agrega_error(self, caracter, linea, columna):
        self.listaErrores.append(Error("Caracter: " + caracter + " desconocido", linea, columna))

    def analizar(self, cadena):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.i = 0
        cadena += "#"
