import pandas as pd
import os

csv_data = None


def definir_csv(ruta):
    global csv_data
    try:
        csv_data = pd.read_csv(ruta, header=0)
        print(csv_data)
    except Exception as e:
        print(e)
        csv_data = None


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
                contador += 1
        return "LaLiga Bot: Los goles anotados por: " + equipo + " como visitante y local, en la temporada: " + str(
            anio1) + "-" + str(anio2) + " fueron: " + str(contador) + "\n" + "\n"
    elif condicion == "LOCAL":
        for i in range(len(partidos)):
            partido = partidos.iloc[i]
            anios = partido.Temporada.split("-")
            anio_inico = int(anios[0])
            anio_final = int(anios[1])
            if partido.Equipo1 == equipo and anio_inico == anio1 and anio_final == anio2:
                contador += 1
        return "LaLiga Bot: Los goles anotados por: " + equipo + " como local, en la temporada: " + str(
            anio1) + "-" + str(anio2) + " fueron: " + str(contador) + "\n" + "\n"
    elif condicion == "VISITANTE":
        for i in range(len(partidos)):
            partido = partidos.iloc[i]
            anios = partido.Temporada.split("-")
            anio_inico = int(anios[0])
            anio_final = int(anios[1])
            if partido.Equipo2 == equipo and anio_inico == anio1 and anio_final == anio2:
                contador += 1
        return "LaLiga Bot: Los goles anotados por: " + equipo + " como visitante, en la temporada: " + str(
            anio1) + "-" + str(anio2) + " fueron: " + str(contador) + "\n" + "\n"


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
