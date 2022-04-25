from Token import Token
from Error import Error
from prettytable import PrettyTable


class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.lista_tokens_actuales = []
        self.lista_errores_actuales = []
        self.linea = 1
        self.columna = 1
        self.buffer = ""
        self.estado = 0
        self.i = 0

    def imprimir_tokens_acumulados(self):
        x = PrettyTable()
        x.field_names = ["lexema", "linea", "columna", "tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna, token.tipo])
        print(x)

    def imprimir_errores_acumulados(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "linea", "columna"]
        for error in self.listaErrores:
            x.add_row([error.descripcion, error.linea, error.columna])
        print(x)

    def imprimir_tokens(self):
        x = PrettyTable()
        x.field_names = ["lexema", "linea", "columna", "tipo"]
        for token in self.lista_tokens_actuales:
            x.add_row([token.lexema, token.linea, token.columna, token.tipo])
        print(x)

    def imprimir_errores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "linea", "columna"]
        for error in self.lista_errores_actuales:
            x.add_row([error.descripcion, error.linea, error.columna])
        print(x)

    def agrega_token(self, lexema, linea, columna, tipo):
        self.listaTokens.append(Token(lexema, linea, columna, tipo))
        self.lista_tokens_actuales.append(Token(lexema, linea, columna, tipo))
        self.buffer = ""

    def agrega_error(self, caracter, linea, columna):
        self.listaErrores.append(Error("Caracter: " + caracter + " desconocido", linea, columna))
        self.lista_errores_actuales.append(Error("Caracter: " + caracter + " desconocido", linea, columna))

    def s0(self, caracter):
        if caracter == '"':
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        elif caracter == "<" or caracter == ">" or caracter == "-":
            self.estado = 4
            self.buffer += caracter
            self.columna += 1
        elif caracter.isalpha():
            self.estado = 5
            self.buffer += caracter
            self.columna += 1
        elif caracter == " ":
            self.columna += 1
        elif caracter == "\n":
            self.linea += 1
            self.columna = 1
        elif caracter == "\t":
            self.columna += 8
        elif caracter == "#":
            print("fin del análisis")
        else:
            self.agrega_error(caracter, self.linea, self.columna)
            self.columna += 1

    def s1(self, caracter):
        if caracter != '"':
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 2
            self.buffer += caracter
            self.columna += 1

    def s2(self):
        self.agrega_token(self.buffer, self.linea, self.columna-len(self.buffer), "cadena")
        self.estado = 0

    def s3(self, caracter):
        if caracter.isdigit():
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        else:
            self.agrega_token(self.buffer, self.linea, self.columna-len(self.buffer), "numero")
            self.estado = 0
            self.i -= 1

    def s4(self):
        if self.buffer == ">":
            self.agrega_token(self.buffer, self.linea, self.columna-len(self.buffer), "mayorQUE")
            self.estado = 0
            self.i -= 1
        elif self.buffer == "<":
            self.agrega_token(self.buffer, self.linea, self.columna-len(self.buffer), "menorQUE")
            self.estado = 0
            self.i -= 1
        elif self.buffer == "-":
            self.agrega_token(self.buffer, self.linea, self.columna-len(self.buffer), "guion")
            self.estado = 0
            self.i -= 1

    def s5(self, caracter):
        if caracter.isdigit() or caracter.isalpha() or caracter == "_":
            self.estado = 5
            self.buffer += caracter
            self.columna += 1
        else:
            if self.buffer in ["RESULTADO", "VS", "TEMPORADA", "JORNADA", "GOLES", "LOCAL", "VISITANTE", "TOTAL", "TABLA", "PARTIDOS", "TOP", "SUPERIOR", "INFERIOR", "ADIOS"]:
                self.agrega_token(self.buffer, self.linea, self.columna-len(self.buffer), "reservada_" + self.buffer)
                self.estado = 0
                self.i -= 1
            elif self.buffer in ["f", "ji", "jf", "n"]:
                self.agrega_token(self.buffer, self.linea, self.columna-len(self.buffer), "bandera_" + self.buffer)
                self.estado = 0
                self.i -= 1
            else:
                self.agrega_token(self.buffer, self.linea, self.columna-len(self.buffer), "name_archivo")
                self.estado = 0
                self.i -= 1

    def analizar(self, cadena):
        self.lista_tokens_actuales = []
        self.lista_errores_actuales = []
        self.linea = 1
        self.columna = 1
        self.i = 0
        cadena += "#"
        while self.i < len(cadena):
            if self.estado == 0:
                self.s0(cadena[self.i])

            elif self.estado == 1:
                self.s1(cadena[self.i])

            elif self.estado == 2:
                self.s2()

            elif self.estado == 3:
                self.s3(cadena[self.i])

            elif self.estado == 4:
                self.s4()

            elif self.estado == 5:
                self.s5(cadena[self.i])

            self.i += 1
