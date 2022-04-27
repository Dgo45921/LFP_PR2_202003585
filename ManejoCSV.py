import pandas as pd

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
    pass