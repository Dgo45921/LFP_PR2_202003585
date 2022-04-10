import os


def reporte_tokens(lista_tokens):
    reporte = open("Reporte_tokens.html", "w")
    reporte.write("<!DOCTYPE html>\n")
    reporte.write("<html>\n")
    reporte.write("<head>\n")
    reporte.write("""<meta charset="UTF-8">\n""")
    reporte.write("<title>reporte de tokens</title>\n")
    reporte.write("""<link rel="stylesheet" href="style.css">\n""")
    reporte.write("</head>\n")
    reporte.write("<body>\n")
    reporte.write("<h1>Reporte de tokens</h1>")
    # aqui ira la tabla
    reporte.write("<table>\n")
    reporte.write("<tr>\n")
    reporte.write("<th>Lexema</th>\n")
    reporte.write("<th>Linea</th>\n")
    reporte.write("<th>Columna</th>\n")
    reporte.write("<th>Tipo</th>\n")
    reporte.write("</tr>\n")
    for token in lista_tokens:
        reporte.write("<tr>\n")
        reporte.write("<td>" + token.lexema + "</td>\n")
        reporte.write("<td>" + str(token.linea) + "</td>\n")
        reporte.write("<td>" + str(token.columna) + "</td>\n")
        reporte.write("<td>" + token.tipo + "</td>\n")
        reporte.write("</tr>\n")

    reporte.write("</table>\n")
    reporte.write("</body>\n")
    reporte.write("</html>\n")
    reporte.close()
    if os.name == "nt":
        os.startfile("Reporte_tokens.html")
    else:
        os.system("xdg-open Reporte_tokens.html")


def reporte_errores(lista_errores):
    reporte = open("Reporte_errores.html", "w")
    reporte.write("<!DOCTYPE html>\n")
    reporte.write("<html>\n")
    reporte.write("<head>\n")
    reporte.write("""<meta charset="UTF-8">\n""")
    reporte.write("<title>reporte de errores</title>\n")
    reporte.write("""<link rel="stylesheet" href="style.css">\n""")
    reporte.write("</head>\n")
    reporte.write("<body>\n")
    reporte.write("<h1>Reporte de errores</h1>")
    # aqui ira la tabla
    reporte.write("<table>\n")
    reporte.write("<tr>\n")
    reporte.write("<th>Descripcion</th>\n")
    reporte.write("<th>Linea</th>\n")
    reporte.write("<th>Columna</th>\n")
    reporte.write("</tr>\n")
    for error in lista_errores:
        reporte.write("<tr>\n")
        reporte.write("<td>" + error.descripcion + "</td>\n")
        reporte.write("<td>" + str(error.linea) + "</td>\n")
        reporte.write("<td>" + str(error.columna) + "</td>\n")
        reporte.write("</tr>\n")

    reporte.write("</table>\n")
    reporte.write("</body>\n")
    reporte.write("</html>\n")
    reporte.close()
    if os.name == "nt":
        os.startfile("Reporte_errores.html")
    else:
        os.system("xdg-open Reporte_errores.html")

