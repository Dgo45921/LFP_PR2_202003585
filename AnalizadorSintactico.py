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
            respuesta = self.JORNADA()
            return respuesta
        elif actual.tipo == "reservada_GOLES":
            respuesta = self.GOLES()
            return respuesta
        elif actual.tipo == "reservada_TABLA":
            respuesta = self.TABLA()
            return respuesta
        elif actual.tipo == "reservada_PARTIDOS":
            pass
        elif actual.tipo == "reservada_TOP":
            pass
        elif actual.tipo == "reservada_ADIOS":
            pass
        else:
            self.agregar_error("RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS", actual.tipo)
            return self.mensaje_error()

    def BANDERA1(self, tipo):
        actual = self.sacar_token()
        if actual is None:
            print("se crea archivo default")  # exito
        elif actual.tipo == "guion":
            actual = self.sacar_token()
            if actual is None:
                self.agregar_error("bandera_f", "EOF")
                return self.mensaje_error()
            elif actual.tipo == "bandera_f":
                actual = self.sacar_token()
                if actual is None:
                    self.agregar_error("name_archivo", "EOF")
                    return self.mensaje_error()
                elif actual.tipo == "name_archivo":
                    print("siuuuuuu")  # exito
                else:
                    self.agregar_error("name_archivo", actual.tipo)
                    return self.mensaje_error()
            else:
                self.agregar_error("bandera_f", actual.tipo)
                return self.mensaje_error()
        else:
            self.agregar_error("EOF", actual.tipo)
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
                                                print("siuuuuuuuu")  # exito
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

    def JORNADA(self):
        actual = self.sacar_token()
        if actual.tipo == "reservada_JORNADA":
            actual = self.sacar_token()
            if actual is None:
                self.agregar_error("numero", "EOF")
                return self.mensaje_error()
            elif actual.tipo == "numero":
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
                                        return self.BANDERA1("jornada")
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
                self.agregar_error("numero", actual.tipo)
                return self.mensaje_error()
        else:
            self.agregar_error("reservada_JORNADA", actual.tipo)
            return self.mensaje_error()

    def CONDICION_GOLES(self):
        actual = self.sacar_token()
        if actual is None:
            self.agregar_error("reservada_LOCAL | reservada_VISITANTE | reservada_TOTAL", "EOF")
            return None
        elif actual.tipo == "reservada_LOCAL" or actual.tipo == "reservada_VISITANTE" or actual.tipo == "reservada_TOTAL":
            return actual.tipo
        else:
            self.agregar_error("reservada_LOCAL | reservada_VISITANTE | reservada_TOTAL", actual.tipo)
            return actual.tipo

    def GOLES(self):
        actual = self.sacar_token()
        if actual.tipo == "reservada_GOLES":
            respuesta = self.CONDICION_GOLES()
            if respuesta == "reservada_LOCAL" or respuesta == "reservada_VISITANTE" or respuesta == "reservada_TOTAL":
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
                                            print("siuuuuuuu")  # exito
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

            elif respuesta is None:
                return self.mensaje_error()
            else:
                return self.mensaje_error()

        else:
            self.agregar_error("reservada_GOLES", actual.tipo)
            return self.mensaje_error()

    def TABLA(self):
        actual = self.sacar_token()
        if actual.tipo == "reservada_TABLA":
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
                                    return self.BANDERA1("tabla")
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
            self.agregar_error("TABLA", actual.tipo)
            return self.mensaje_error()

    def mensaje_error(self):
        return "LaLiga bot: " + self.lista_errores[len(self.lista_errores) - 1] + "\n" + "\n"
