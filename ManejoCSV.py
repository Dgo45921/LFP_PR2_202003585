import pandas as pd
import os
from prettytable import PrettyTable

csv_data = None


def definir_csv(ruta):
    global csv_data
    try:
        csv_data = pd.read_csv(ruta, header=0)
    except Exception as e:
        print(e)
        csv_data = None


# indica el resultado final de un partido

def resultado(equipo1, equipo2, anio1, anio2):
    partidos = csv_data[csv_data["Temporada"].str.contains(str(anio1) + "-" + str(anio2))]
    for i in range(len(partidos)):
        partido = partidos.iloc[i]
        anios = partido.Temporada.split("-")
        anio_inico = int(anios[0])
        anio_final = int(anios[1])
        if partido.Equipo1 == equipo1 and partido.Equipo2 == equipo2 and anio_inico == anio1 and anio_final == anio2:
            return "LaLiga Bot: El resultado de este partido fue: " + equipo1 + ": " + str(
                partido.Goles1) + " " + equipo2 + ": " + str(partido.Goles2) + "\n" + "\n"
    return "LaLiga Bot: No encontré un partido con la información que me has dado..."


# genera una tabla con todos los partidos de una jornada especifica en cierta temporada


def jornada(num_jornada, anio1, anio2, name_archivo):
    reporte = open(name_archivo, "w")
    reporte.write("<!DOCTYPE html>\n")
    reporte.write("<html>\n")
    reporte.write("<head>\n")
    reporte.write("""<meta charset="UTF-8">\n""")
    reporte.write("<title>Resultados jornada</title>\n")
    reporte.write("""<link rel="stylesheet" href="style.css">\n""")
    reporte.write("</head>\n")
    reporte.write("<body>\n")
    reporte.write("<h1>RESULTADOS</h1>")
    reporte.write("<h3>Jornada:" + str(num_jornada) + "</h3>")
    reporte.write("<h3>Temporada:  " + str(anio1) + "-" + str(anio2) + "</h3>")
    # aqui ira la tabla
    reporte.write("<table>\n")
    reporte.write("<tr>\n")
    reporte.write("<th>Local</th>\n")
    reporte.write("<th>Goles local</th>\n")
    reporte.write("<th>Visitante</th>\n")
    reporte.write("<th>Goles visitante</th>\n")
    reporte.write("</tr>\n")

    partidos = csv_data[csv_data["Temporada"].str.contains(str(anio1) + "-" + str(anio2))]
    for i in range(len(partidos)):
        partido = partidos.iloc[i]
        anios = partido.Temporada.split("-")
        anio_inico = int(anios[0])
        anio_final = int(anios[1])
        if partido.Jornada == num_jornada and anio_inico == anio1 and anio_final == anio2:
            reporte.write("<tr>\n")
            reporte.write("<td>" + partido.Equipo1 + "</td>\n")
            reporte.write("<td>" + str(partido.Goles1) + "</td>\n")
            reporte.write("<td>" + partido.Equipo2 + "</td>\n")
            reporte.write("<td>" + str(partido.Goles2) + "</td>\n")
            reporte.write("</tr>\n")

    reporte.write("</table>\n")
    reporte.write("</body>\n")
    reporte.write("</html>\n")
    reporte.close()
    if os.name == "nt":
        os.startfile(name_archivo)
    else:
        os.system("xdg-open " + name_archivo)


# se encarga de mostrar los goles hechos por un equipo en cierta temporada y cierta condicion


def goles(condicion, equipo, anio1, anio2):
    contador = 0
    partidos = csv_data[csv_data["Temporada"].str.contains(str(anio1) + "-" + str(anio2))]

    if condicion == "TOTAL":
        for i in range(len(partidos)):
            partido = partidos.iloc[i]
            anios = partido.Temporada.split("-")
            anio_inico = int(anios[0])
            anio_final = int(anios[1])
            if (partido.Equipo1 == equipo or partido.Equipo2 == equipo) and anio_inico == anio1 and anio_final == anio2:
                if partido.Equipo1 == equipo:
                    contador += partido.Goles1
                else:
                    contador += partido.Goles2

        return "LaLiga Bot: Los goles anotados por: " + equipo + " como visitante y local, en la temporada: " + str(
            anio1) + "-" + str(anio2) + " fueron: " + str(contador) + "\n" + "\n"
    elif condicion == "LOCAL":
        for i in range(len(partidos)):
            partido = partidos.iloc[i]
            anios = partido.Temporada.split("-")
            anio_inico = int(anios[0])
            anio_final = int(anios[1])
            if partido.Equipo1 == equipo and anio_inico == anio1 and anio_final == anio2:
                contador += partido.Goles1
        return "LaLiga Bot: Los goles anotados por: " + equipo + " como local, en la temporada: " + str(
            anio1) + "-" + str(anio2) + " fueron: " + str(contador) + "\n" + "\n"
    elif condicion == "VISITANTE":
        for i in range(len(partidos)):
            partido = partidos.iloc[i]
            anios = partido.Temporada.split("-")
            anio_inico = int(anios[0])
            anio_final = int(anios[1])
            if partido.Equipo2 == equipo and anio_inico == anio1 and anio_final == anio2:
                contador += partido.Goles2
        return "LaLiga Bot: Los goles anotados por: " + equipo + " como visitante, en la temporada: " + str(
            anio1) + "-" + str(anio2) + " fueron: " + str(contador) + "\n" + "\n"


# genera tabla de puntuaciones de cada equipo


def tabla(anio1, anio2, name_archivo):
    equipos_leidos = []
    puntos_equipo = []
    partidos = csv_data[csv_data["Temporada"].str.contains(str(anio1) + "-" + str(anio2))]

    reporte = open(name_archivo, "w")
    reporte.write("<!DOCTYPE html>\n")
    reporte.write("<html>\n")
    reporte.write("<head>\n")
    reporte.write("""<meta charset="UTF-8">\n""")
    reporte.write("<title>Tabla resultados</title>\n")
    reporte.write("""<link rel="stylesheet" href="style.css">\n""")
    reporte.write("</head>\n")
    reporte.write("<body>\n")
    reporte.write("<h1>RESULTADOS</h1>")
    reporte.write("<h3>Temporada:  " + str(anio1) + "-" + str(anio2) + "</h3>")
    # aqui ira la tabla
    reporte.write("<table>\n")
    reporte.write("<tr>\n")
    reporte.write("<th>Equipo</th>\n")
    reporte.write("<th>Puntos</th>\n")
    reporte.write("</tr>\n")

    for i in range(len(partidos)):
        partido = partidos.iloc[i]
        name_equipo = partido.Equipo1
        if name_equipo not in equipos_leidos:
            puntos = calcular_puntos(name_equipo, partidos)
            equipos_leidos.append(name_equipo)
            puntos_equipo.append(puntos)
    lista_arrays = bubbleSort(puntos_equipo, equipos_leidos)
    puntos_equipo = lista_arrays[0]
    equipos_leidos = lista_arrays[1]

    for i in range(len(puntos_equipo)):
        reporte.write("<tr>\n")
        reporte.write("<td>" + equipos_leidos[i] + "</td>\n")
        reporte.write("<td>" + str(puntos_equipo[i]) + "</td>\n")
        reporte.write("</tr>\n")

    reporte.write("</table>\n")
    reporte.write("</body>\n")
    reporte.write("</html>\n")
    reporte.close()
    if os.name == "nt":
        os.startfile(name_archivo)
    else:
        os.system("xdg-open " + name_archivo)


# genera un reporte de todos los resultados de un equipo en cierta temporada

def temporada(name_equipo, anio1, anio2, name_archivo, jornada_inicio, jornada_fin):
    reporte = open(name_archivo, "w")
    reporte.write("<!DOCTYPE html>\n")
    reporte.write("<html>\n")
    reporte.write("<head>\n")
    reporte.write("""<meta charset="UTF-8">\n""")
    reporte.write("<title>Resultados temporada</title>\n")
    reporte.write("""<link rel="stylesheet" href="style.css">\n""")
    reporte.write("</head>\n")
    reporte.write("<body>\n")
    reporte.write("<h1>RESULTADOS " + name_equipo + "</h1>")
    reporte.write("<h3>Temporada:  " + str(anio1) + "-" + str(anio2) + "</h3>")
    # aqui ira la tabla
    reporte.write("<table>\n")
    reporte.write("<tr>\n")
    reporte.write("<th>Jornada</th>\n")
    reporte.write("<th>Local</th>\n")
    reporte.write("<th>Goles local</th>\n")
    reporte.write("<th>Visitante</th>\n")
    reporte.write("<th>Goles visitante</th>\n")
    reporte.write("</tr>\n")
    contador = jornada_inicio

    partidos = csv_data[csv_data["Temporada"].str.contains(str(anio1) + "-" + str(anio2))]
    if jornada_fin == 0:
        jornada_fin = partidos.iloc[-1].Jornada
    for i in range(len(partidos)):
        partido = partidos.iloc[i]
        anios = partido.Temporada.split("-")
        anio_inico = int(anios[0])
        anio_final = int(anios[1])
        if contador <= jornada_fin and anio_inico == anio1 and anio_final == anio2 and (
                partido.Equipo1 == name_equipo or partido.Equipo2 == name_equipo) and contador == partido.Jornada:
            reporte.write("<tr>\n")
            reporte.write("<td>" + str(partido.Jornada) + "</td>\n")
            reporte.write("<td>" + partido.Equipo1 + "</td>\n")
            reporte.write("<td>" + str(partido.Goles1) + "</td>\n")
            reporte.write("<td>" + partido.Equipo2 + "</td>\n")
            reporte.write("<td>" + str(partido.Goles2) + "</td>\n")
            reporte.write("</tr>\n")
            contador += 1
        else:
            pass

    reporte.write("</table>\n")
    reporte.write("</body>\n")
    reporte.write("</html>\n")
    reporte.close()
    if os.name == "nt":
        os.startfile(name_archivo)
    else:
        os.system("xdg-open " + name_archivo)


# genera reporte de top

def top(anio1, anio2, bandera_n, condicion):
    cadena = """LaLiga Bot: \n"""
    equipos_leidos = []
    puntos_equipo = []
    partidos = csv_data[csv_data["Temporada"].str.contains(str(anio1) + "-" + str(anio2))]

    for i in range(len(partidos)):
        partido = partidos.iloc[i]
        name_equipo = partido.Equipo1
        if name_equipo not in equipos_leidos:
            puntos = calcular_puntos(name_equipo, partidos)
            equipos_leidos.append(name_equipo)
            puntos_equipo.append(puntos)
    lista_arrays = bubbleSort(puntos_equipo, equipos_leidos)
    puntos_equipo = lista_arrays[0]
    equipos_leidos = lista_arrays[1]

    if bandera_n > len(puntos_equipo) or bandera_n > len(equipos_leidos):
        return "La bandera n es demasiado grande para realizar esta operación"

    if condicion == "INFERIOR":
        puntos_equipo.reverse()
        equipos_leidos.reverse()

        puntos_equipo = puntos_equipo[0:bandera_n]
        equipos_leidos = equipos_leidos[0:bandera_n]

        puntos_equipo.reverse()
        equipos_leidos.reverse()

        x = PrettyTable()
        x.field_names = ["No.", "Equipo", "Punteo"]
        for i in range(len(equipos_leidos)):
            x.add_row([str(i+1), equipos_leidos[i], str(puntos_equipo[i])])
        return cadena + x.get_string()
    else:
        x = PrettyTable()
        x.field_names = ["No.", "Equipo", "Punteo"]
        for i in range(bandera_n):
            x.add_row([str(i + 1), equipos_leidos[i], str(puntos_equipo[i])])
        return cadena + x.get_string()


def calcular_puntos(name_equipo, partidos):
    puntos = 0
    for i in range(len(partidos)):
        partido = partidos.iloc[i]
        if name_equipo == partido.Equipo1:
            if partido.Goles1 > partido.Goles2:
                puntos += 3
            elif partido.Goles1 == partido.Goles2:
                puntos += 1
        elif name_equipo == partido.Equipo2:
            if partido.Goles2 > partido.Goles1:
                puntos += 3
            elif partido.Goles1 == partido.Goles2:
                puntos += 1
    return puntos


def bubbleSort(alist, blist):
    lista_arrays = []
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] < alist[i + 1]:
                temp = alist[i]
                temp2 = blist[i]
                alist[i] = alist[i + 1]
                blist[i] = blist[i + 1]
                alist[i + 1] = temp
                blist[i + 1] = temp2

    lista_arrays.append(alist)
    lista_arrays.append(blist)
    return lista_arrays
