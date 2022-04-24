from tkinter import *


class AnalizadorSintactico:
    def __init__(self, lista_tokens: list):
        self.lista_tokens = lista_tokens
        self.lista_errores = []

    def agregar_error(self, esperado, obtenido):
        self.lista_errores.append(" Error: se esperaba: " + esperado + "\npero se obtuvo: " + obtenido)

    def sacar_token(self):
        try:
            return self.lista_tokens.pop(0)
        except:
            return None

    def ver_token(self):
        try:
            return self.lista_tokens[0]
        except:
            return None

    def S(self):
        respuesta = self.INICIO()
        return respuesta

    def INICIO(self):
        actual = self.ver_token()
        if actual is None:
            self.agregar_error("RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS", "EOF")
            return self.mensaje_error()
        elif actual.tipo == "reservada_RESULTADO":
            respuesta = self.RESULTADO()
            return respuesta
        elif actual.tipo == "reservada_JORNADA":
            pass
        elif actual.tipo == "reservada_GOLES":
            pass
        elif actual.tipo == "reservada_TABLA":
            pass
        elif actual.tipo == "reservada_PARTIDOS":
            pass
        elif actual.tipo == "reservada_TOP":
            pass
        elif actual.tipo == "reservada_ADIOS":
            pass
        else:
            self.agregar_error("RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS", actual.tipo)
            return self.mensaje_error()

    def RESULTADO(self):
        actual = self.sacar_token()
        if actual.tipo == "reservada_RESULTADO":
            actual = self.sacar_token()
            if actual is None:
                self.agregar_error("cadena", "EOF")
                return self.mensaje_error()
            elif actual.tipo == "cadena":
                actual = self.sacar_token()
                if actual is None:
                    self.agregar_error("reservada_VS", "EOF")
                    return self.mensaje_error()
                elif actual.tipo == "reservada_VS":
                    actual = self.sacar_token()
                    if actual is None:
                        self.agregar_error("cadena", "EOF")
                        return self.mensaje_error()
                    elif actual.tipo == "cadena":
                        actual = self.sacar_token()
                        if actual is None:
                            self.agregar_error("reservada_TEMPORADA", "EOF")
                            return self.mensaje_error()
                        elif actual.tipo == "reservada_TEMPORADA":
                            actual = self.sacar_token()
                            if actual is None:
                                self.agregar_error("menorQUE", "EOF")
                                return self.mensaje_error()
                            elif actual.tipo == "menorQUE":
                                actual = self.sacar_token()
                                if actual is None:
                                    self.agregar_error("numero", "EOF")
                                    return self.mensaje_error()
                                elif actual.tipo == "numero":
                                    actual = self.sacar_token()
                                    if actual is None:
                                        self.agregar_error("guion", "EOF")
                                        return self.mensaje_error()
                                    elif actual.tipo == "guion":
                                        actual = self.sacar_token()
                                        if actual is None:
                                            self.agregar_error("numero", "EOF")
                                            return self.mensaje_error()
                                        elif actual.tipo == "numero":
                                            actual = self.sacar_token()
                                            if actual is None:
                                                self.agregar_error("mayorQUE", "EOF")
                                                return self.mensaje_error()
                                            elif actual.tipo == "mayorQUE":
                                                print("siuuuuuuuu")
                                            else:
                                                self.agregar_error("mayorQUE", actual.tipo)
                                                return self.mensaje_error()
                                        else:
                                            self.agregar_error("numero", actual.tipo)
                                            return self.mensaje_error()
                                    else:
                                        self.agregar_error("guion", actual.tipo)
                                        return self.mensaje_error()
                                else:
                                    self.agregar_error("numero", actual.tipo)
                                    return self.mensaje_error()
                            else:
                                self.agregar_error("menorQUE", actual.tipo)
                                return self.mensaje_error()
                        else:
                            self.agregar_error("reservada_TEMPORADA", actual.tipo)
                            return self.mensaje_error()
                    else:
                        self.agregar_error("cadena", actual.tipo)
                        return self.mensaje_error()
                else:
                    self.agregar_error("reservada_VS", actual.tipo)
                    return self.mensaje_error()
            else:
                self.agregar_error("cadena", actual.tipo)
                return self.mensaje_error()


        else:
            self.agregar_error("reservada_RESULTADO", actual.tipo)
            return self.mensaje_error()

    def mensaje_error(self):
        return "LaLiga bot: " + self.lista_errores[len(self.lista_errores) - 1] + "\n" + "\n"
