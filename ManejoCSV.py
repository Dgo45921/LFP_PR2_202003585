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
    num_filas = len(csv_data)
    for i in range(num_filas):
        partido = csv_data.iloc[i]
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

    num_filas = len(csv_data)
    for i in range(num_filas):
        partido = csv_data.iloc[i]
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
