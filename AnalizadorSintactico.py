import ManejoCSV
lista_banderas = ["", "", "", ""]


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

    def ver_token2(self):
        try:
            return self.lista_tokens[1]
        except:
            return None

    def S(self):
        respuesta = self.INICIO()
        return respuesta

    def INICIO(self):
        global lista_banderas
        lista_banderas[0] = ""
        lista_banderas[1] = ""
        lista_banderas[2] = ""
        lista_banderas[3] = ""
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
            respuesta = self.PARTIDOS()
            return respuesta
        elif actual.tipo == "reservada_TOP":
            respuesta = self.TOP()
            return respuesta
        elif actual.tipo == "reservada_ADIOS":
            respuesta = self.ADIOS()
            return respuesta
        else:
            self.agregar_error("RESULTADO | JORNADA | GOLES | TABLA | PARTIDOS | TOP | ADIOS", actual.tipo)
            return self.mensaje_error()

    def BANDERA1(self):
        actual = self.sacar_token()
        if actual is None:
            print("se crea archivo default")  # exito
            return None
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
                    lista_banderas[0] = actual.lexema
                    return "exito"
                else:
                    self.agregar_error("name_archivo", actual.tipo)
                    return self.mensaje_error()
            else:
                self.agregar_error("bandera_f", actual.tipo)
                return self.mensaje_error()
        else:
            self.agregar_error("EOF", actual.tipo)
            return self.mensaje_error()

    def BANDERA2(self):
        actual = self.sacar_token()
        if actual is None:
            print("incluir partidos desde la jornada inicial")  # exito
        elif actual.tipo == "guion":
            actual = self.sacar_token()
            if actual is None:
                self.agregar_error("bandera_ji", "EOF")
                return self.mensaje_error()
            elif actual.tipo == "bandera_ji":
                actual = self.sacar_token()
                if actual is None:
                    self.agregar_error("numero", "EOF")
                    return self.mensaje_error()
                elif actual.tipo == "numero":
                    lista_banderas[1] = actual.lexema
                    return "exito"
                else:
                    self.agregar_error("numero", actual.tipo)
                    return self.mensaje_error()
            else:
                self.agregar_error("bandera_ji", actual.tipo)
                return self.mensaje_error()
        else:
            self.agregar_error("EOF", actual.tipo)
            return self.mensaje_error()

    def BANDERA3(self):
        actual = self.sacar_token()
        if actual is None:
            print("incluir todos los partidos hasta la jornada final")  # exito
        elif actual.tipo == "guion":
            actual = self.sacar_token()
            if actual is None:
                self.agregar_error("bandera_jf", "EOF")
                return self.mensaje_error()
            elif actual.tipo == "bandera_jf":
                actual = self.sacar_token()
                if actual is None:
                    self.agregar_error("numero", "EOF")
                    return self.mensaje_error()
                elif actual.tipo == "numero":
                    lista_banderas[2] = actual.lexema
                    return "exito"
                else:
                    self.agregar_error("numero", actual.tipo)
                    return self.mensaje_error()
            else:
                self.agregar_error("bandera_jf", actual.tipo)
                return self.mensaje_error()
        else:
            self.agregar_error("EOF", actual.tipo)
            return self.mensaje_error()

    def BANDERA4(self):
        actual = self.sacar_token()
        if actual is None:
            print("incluir todos los partidos hasta la jornada final")  # exito
        elif actual.tipo == "guion":
            actual = self.sacar_token()
            if actual is None:
                self.agregar_error("bandera_n", "EOF")
                return self.mensaje_error()
            elif actual.tipo == "bandera_n":
                actual = self.sacar_token()
                if actual is None:
                    self.agregar_error("numero", "EOF")
                    return self.mensaje_error()
                elif actual.tipo == "numero":
                    lista_banderas[3] = actual.lexema
                    return "exito"
                else:
                    self.agregar_error("numero", actual.tipo)
                    return self.mensaje_error()
            else:
                self.agregar_error("bandera_n", actual.tipo)
                return self.mensaje_error()
        else:
            self.agregar_error("EOF", actual.tipo)
            return self.mensaje_error()

    def LISTA_BANDERAS(self):
        respuesta_bot = "LaLiga Bot: creando archivo... Si una bandera no fue escrita se usarán valores por defecto \n"
        actual = self.ver_token()
        actual2 = self.ver_token2()
        if actual is None:
            return ""
        elif actual.tipo == "guion":
            if actual2.tipo == "bandera_f":
                respuesta = self.BANDERA1()
                if respuesta is None:
                    lista_banderas[0] = ""
                    respuesta_bot += "con nombre por defecto" + "\n"
                elif respuesta == "exito":
                    respuesta_bot += " con nombre: " + lista_banderas[0] + "\n"
                else:
                    return self.mensaje_error()
            elif actual2.tipo == "bandera_ji":
                respuesta = self.BANDERA2()
                if respuesta is None:
                    lista_banderas[1] = ""
                    respuesta_bot += "con jornada inicial primera" + "\n"
                elif respuesta == "exito":
                    respuesta_bot += " temporada inicial: " + lista_banderas[1] + "\n"
                else:
                    return self.mensaje_error()
            elif actual2.tipo == "bandera_jf":
                respuesta = self.BANDERA3()
                if respuesta is None:
                    lista_banderas[2] = ""
                    respuesta_bot += "con jornada final última" + "\n"
                elif respuesta == "exito":
                    respuesta_bot += " temporada final: " + lista_banderas[2] + "\n"
                else:
                    return self.mensaje_error()
            else:
                self.agregar_error("bandera_f | bandera_ji | bandera_jf", actual2.tipo)
                return self.mensaje_error()

            respuesta2 = self.LISTA_BANDERAS_()
            return respuesta_bot + respuesta2 + "\n"
        else:
            self.agregar_error("bandera_f | bandera_ji | bandera_jf", actual.tipo)
            return self.mensaje_error()

    def LISTA_BANDERAS_(self):
        respuesta_bot = ""
        global lista_banderas
        actual = self.ver_token()
        actual2 = self.ver_token2()
        if actual is None:
            return ""
        elif actual.tipo == "guion":
            if actual2.tipo == "bandera_f":
                respuesta = self.BANDERA1()
                if respuesta is None:
                    lista_banderas[0] = ""
                    respuesta_bot += "con nombre por defecto" + "\n"
                elif respuesta == "exito":
                    respuesta_bot += " con nombre: " + lista_banderas[0] + "\n"
                else:
                    return self.mensaje_error()
            elif actual2.tipo == "bandera_ji":
                respuesta = self.BANDERA2()
                if respuesta is None:
                    lista_banderas[1] = ""
                    respuesta_bot += "con jornada inicial primera" + "\n"
                elif respuesta == "exito":
                    respuesta_bot += " temporada inicial: " + lista_banderas[1] + "\n"
                else:
                    return self.mensaje_error()
            elif actual2.tipo == "bandera_jf":
                respuesta = self.BANDERA3()
                if respuesta is None:
                    lista_banderas[2] = ""
                    respuesta_bot += "con jornada final última" + "\n"
                elif respuesta == "exito":
                    respuesta_bot += " temporada final: " + lista_banderas[2] + "\n"
                else:
                    return self.mensaje_error()
            else:
                self.agregar_error("bandera_f | bandera_ji | bandera_jf", actual2.tipo)
                return self.mensaje_error()

            respuesta2 = self.LISTA_BANDERAS_()
            return respuesta_bot + respuesta2
        else:
            self.agregar_error("bandera_f | bandera_ji | bandera_jf", actual.tipo)
            return self.mensaje_error()

    def RESULTADO(self):
        equipo1 = ""
        equipo2 = ""
        anio1 = 0
        anio2 = 0

        actual = self.sacar_token()
        if actual.tipo == "reservada_RESULTADO":
            actual = self.sacar_token()
            if actual is None:
                self.agregar_error("cadena", "EOF")
                return self.mensaje_error()
            elif actual.tipo == "cadena":
                equipo1 = actual.lexema.replace('"', "")
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
                        equipo2 = actual.lexema.replace('"', "")
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
                                    anio1 = int(actual.lexema)
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
                                            anio2 = int(actual.lexema)
                                            actual = self.sacar_token()
                                            if actual is None:
                                                self.agregar_error("mayorQUE", "EOF")
                                                return self.mensaje_error()
                                            elif actual.tipo == "mayorQUE":
                                                return ManejoCSV.resultado(equipo1, equipo2, anio1, anio2)
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
        num_jornada = 0
        anio1 = 0
        anio2 = 0
        actual = self.sacar_token()
        if actual.tipo == "reservada_JORNADA":
            actual = self.sacar_token()
            if actual is None:
                self.agregar_error("numero", "EOF")
                return self.mensaje_error()
            elif actual.tipo == "numero":
                num_jornada = actual.lexema
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
                            anio1 = actual.lexema
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
                                    anio2 = actual.lexema
                                    actual = self.sacar_token()
                                    if actual is None:
                                        self.agregar_error("mayorQUE", "EOF")
                                        return self.mensaje_error()
                                    elif actual.tipo == "mayorQUE":
                                        respuesta = self.BANDERA1()
                                        if respuesta is None:
                                            print("nombre default")
                                            ManejoCSV.jornada(int(num_jornada), int(anio1), int(anio2), "jornada.html")
                                            return "LaLiga Bot: Generando archivo de resultados jornada" + num_jornada + " temporada " + anio1 + " - " + anio2 + "\n" + "\n"
                                        elif respuesta == "exito":
                                            ManejoCSV.jornada(int(num_jornada), int(anio1), int(anio2), lista_banderas[0] + ".html")
                                            return "LaLiga Bot: Generando archivo de resultados: " + lista_banderas[
                                                0] + ".html jornada" + num_jornada + " temporada " + anio1 + " - " + anio2 + "\n" + "\n "
                                        else:
                                            return respuesta
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
        condicion = ""
        equipo = ""
        anio1 = 0
        anio2 = 0
        actual = self.sacar_token()
        if actual.tipo == "reservada_GOLES":
            respuesta = self.CONDICION_GOLES()
            if respuesta == "reservada_LOCAL" or respuesta == "reservada_VISITANTE" or respuesta == "reservada_TOTAL":
                condicion = respuesta.replace("reservada_", "")
                actual = self.sacar_token()
                if actual is None:
                    self.agregar_error("cadena", "EOF")
                    return self.mensaje_error()
                elif actual.tipo == "cadena":
                    equipo = actual.lexema.replace('"', "")
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
                                anio1 = int(actual.lexema)
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
                                        anio2 = int(actual.lexema)
                                        actual = self.sacar_token()
                                        if actual is None:
                                            self.agregar_error("mayorQUE", "EOF")
                                            return self.mensaje_error()
                                        elif actual.tipo == "mayorQUE":
                                            return ManejoCSV.goles(condicion, equipo, anio1, anio2)
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
        anio1 = 0
        anio2 = 0
        name_archivo = ""
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
                        anio1 = int(actual.lexema)
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
                                anio2 = int(actual.lexema)
                                actual = self.sacar_token()
                                if actual is None:
                                    self.agregar_error("mayorQUE", "EOF")
                                    return self.mensaje_error()
                                elif actual.tipo == "mayorQUE":
                                    respuesta = self.BANDERA1()
                                    if respuesta is None:
                                        ManejoCSV.tabla(anio1, anio2, "temporada.html")
                                        return "LaLiga Bot: Generando archivo de clasificación de temporada" + str(anio1) + "-" + str(anio2) + "\n" + "\n"
                                    elif respuesta == "exito":
                                        ManejoCSV.tabla(anio1, anio2, lista_banderas[0] + ".html")
                                        return "LaLiga Bot: Generando archivo de clasificación de temporada: " + lista_banderas[0] + str(anio1) + "-" + str(anio2) + "\n" + "\n"
                                    else:
                                        return respuesta
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

    def PARTIDOS(self):
        jornada_inicial = 0
        jornada_final = 0
        anio1 = 0
        anio2 = 0
        name_equipo = ""
        actual = self.sacar_token()
        if actual.tipo == "reservada_PARTIDOS":
            actual = self.sacar_token()
            if actual is None:
                self.agregar_error("cadena", "EOF")
                return self.mensaje_error()
            elif actual.tipo == "cadena":
                name_equipo = actual.lexema.replace('"', "")
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
                            anio1 = int(actual.lexema)
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
                                    anio2 = int(actual.lexema)
                                    actual = self.sacar_token()
                                    if actual is None:
                                        self.agregar_error("mayorQUE", "EOF")
                                        return self.mensaje_error()
                                    elif actual.tipo == "mayorQUE":
                                        name_archivo = ""
                                        print(lista_banderas)
                                        print(lista_banderas[0])
                                        if lista_banderas[0] == "":
                                            name_archivo = "partidos.html"
                                        else:
                                            name_archivo = lista_banderas[0] + ".html"

                                        if lista_banderas[1] == "":
                                            jornada_inicial = 1
                                        else:
                                            jornada_inicial = int(lista_banderas[1])

                                        if lista_banderas[2] == "":
                                            jornada_final = 0
                                        else:
                                            jornada_final = int(lista_banderas[2])

                                        ManejoCSV.temporada(name_equipo, anio1, anio2, name_archivo, jornada_inicial, jornada_final)

                                        return "Generando archivo de resultados de temporada: " + str(anio1) + "-" + str(anio2) + " del " + name_equipo
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
            self.agregar_error("reservada_PARTIDOS", actual.tipo)
            return self.mensaje_error()

    def CONDICION_TOP(self):
        actual = self.sacar_token()
        if actual is None:
            self.agregar_error("reservada_SUPERIOR|reservada_INFERIOR", "EOF")
            return self.mensaje_error()
        elif actual.tipo == "reservada_SUPERIOR" or actual.tipo == "reservada_INFERIOR":
            return actual.tipo
        else:
            self.agregar_error("reservada_SUPERIOR|reservada_INFERIOR", actual.tipo)
            return self.mensaje_error()

    def TOP(self):
        condicion = ""
        anio1 = 0
        anio2 = 0
        actual = self.sacar_token()
        if actual.tipo == "reservada_TOP":
            respuesta = self.CONDICION_TOP()
            if "Error" not in respuesta:
                condicion = respuesta.replace("reservada_", "")
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
                            anio1 = int(actual.lexema)
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
                                    anio2 = int(actual.lexema)
                                    actual = self.sacar_token()
                                    if actual is None:
                                        self.agregar_error("mayorQUE", "EOF")
                                        return self.mensaje_error()
                                    elif actual.tipo == "mayorQUE":
                                        respuesta = self.BANDERA4()
                                        if respuesta is None:
                                            respuesta = ManejoCSV.top(anio1, anio2, 5, condicion)
                                            return respuesta + "\n" + "\n"
                                        elif respuesta == "exito":
                                            respuesta = ManejoCSV.top(anio1, anio2, int(lista_banderas[3]), condicion)
                                            return respuesta + "\n" + "\n"
                                        else:
                                            return respuesta
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
                return respuesta
        else:
            self.agregar_error("reservada_TOP", actual.tipo)
            return self.mensaje_error()

    def ADIOS(self):
        return "Laliga Bot: ADIOS"


    def mensaje_error(self):
        return "LaLiga bot: " + self.lista_errores[len(self.lista_errores) - 1] + "\n" + "\n"
