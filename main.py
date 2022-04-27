from tkinter import *
import tkinter.font as font
from tkinter import scrolledtext, filedialog
from tkinter import messagebox
from tkinter.messagebox import askyesno
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
import FileWriter
import ManejoCSV

analizador_lexico = AnalizadorLexico()
analizador_sintactico = AnalizadorSintactico([])


def cargar_archivo():
    ruta = filedialog.askopenfilename(title="Selecciona un archivo", initialdir="/",
                                      filetypes=(("csv files", "*.csv"), ("", "")))
    if type(ruta) != tuple:
        ManejoCSV.definir_csv(ruta)


def mandar_mensaje():
    if ManejoCSV.csv_data is not None:
        contenido_mensaje = area_texto.get(1.0, END)
        if len(contenido_mensaje) > 1:
            mensaje = "Tú: " + contenido_mensaje + "\n"
            print(mensaje)
            area_chat.config(state="normal")
            area_chat.insert(END, mensaje)
            area_chat.config(state="disabled")
            area_texto.delete(1.0, END)
            analizador_lexico.analizar(contenido_mensaje)
            print("estos son los datos acumulados")
            analizador_lexico.imprimir_tokens_acumulados()
            analizador_lexico.imprimir_errores_acumulados()
            print("estos son los datos actuales")
            analizador_lexico.imprimir_tokens()
            analizador_lexico.imprimir_errores()
            analizador_sintactico.lista_tokens = analizador_lexico.lista_tokens_actuales
            respuesta = analizador_sintactico.S()
            if respuesta is not None:
                area_chat.config(state="normal")
                area_chat.insert(END, respuesta)
                area_chat.config(state="disabled")
                if respuesta == "Laliga Bot: ADIOS":
                    answer = askyesno(title='confirmación',
                                      message='¿Seguro que deseas salir?')
                    if answer:
                        exit()
        else:
            messagebox.showinfo(title="Error", message="No puedes enviar un mensaje vacío")
    else:
        messagebox.showinfo(title="Error", message="Cargue un archivo csv, por favor")


def reporte_tokens():
    if len(analizador_lexico.listaTokens) != 0:
        FileWriter.reporte_tokens(analizador_lexico.listaTokens)
    else:
        messagebox.showinfo(title="error", message="No hay tokens para generar este reporte")


def reporte_errores():
    if len(analizador_lexico.listaErrores) != 0 or len(analizador_sintactico.lista_errores) != 0:
        FileWriter.reporte_errores(analizador_lexico.listaErrores, analizador_sintactico.lista_errores)
    else:
        messagebox.showinfo(title="error", message="No hay errores para generar este reporte")


def limpia_tokens():
    analizador_lexico.listaTokens.clear()
    messagebox.showinfo(title="aviso", message="Los tokens fueron limpiados")


def limpia_errores():
    analizador_lexico.listaErrores.clear()
    analizador_sintactico.lista_errores.clear()
    messagebox.showinfo(title="aviso", message="Los errores fueron limpiados")


# Info sobre la ventana
Ventana_principal = Tk()
Ventana_principal.title("LaLiga Bot")
Ventana_principal.configure(width=1200, height=800)
Ventana_principal.resizable(False, False)
Ventana_principal.eval('tk::PlaceWindow . center')
# Creando botones
mi_fuente = font.Font(family='Helvetica', size=15)

# boton para enviar comando
boton_analizar = Button(Ventana_principal, text="Enviar")
boton_analizar.configure(width=6, height=2, bg="#213dec", fg="white", borderwidth=5, command=mandar_mensaje)
boton_analizar['font'] = mi_fuente
boton_analizar.place(x=790, y=640)

# boton de generar reporte tokens
boton_tokens = Button(Ventana_principal, text="Reporte de tokens")
boton_tokens.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5, command=reporte_tokens)
boton_tokens['font'] = mi_fuente
boton_tokens.place(x=950, y=130)

# boton de generar reporte de errores
boton_errores = Button(Ventana_principal, text="Reporte de errores")
boton_errores.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5, command=reporte_errores)
boton_errores['font'] = mi_fuente
boton_errores.place(x=950, y=200)

# boton de para limpiar tokens
boton_delete_tokens = Button(Ventana_principal, text="Limpiar log tokens")
boton_delete_tokens.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5, command=limpia_tokens)
boton_delete_tokens['font'] = mi_fuente
boton_delete_tokens.place(x=950, y=270)

# boton de para limpiar errores
boton_delete_errors = Button(Ventana_principal, text="Limpiar log errores")
boton_delete_errors.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5, command=limpia_errores)
boton_delete_errors['font'] = mi_fuente
boton_delete_errors.place(x=950, y=340)

# boton manual de usuario
boton_manual_users = Button(Ventana_principal, text="Manual de usuario")
boton_manual_users.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5)
boton_manual_users['font'] = mi_fuente
boton_manual_users.place(x=950, y=410)

# boton manual tecnico
boton_manual_tecnico = Button(Ventana_principal, text="Manual técnico")
boton_manual_tecnico.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5)
boton_manual_tecnico['font'] = mi_fuente
boton_manual_tecnico.place(x=950, y=480)

# boton cargar archivo
boton_manual_tecnico = Button(Ventana_principal, text="Cargar .csv", command=cargar_archivo)
boton_manual_tecnico.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5)
boton_manual_tecnico['font'] = mi_fuente
boton_manual_tecnico.place(x=60, y=30)

# creando area de chat
area_chat = scrolledtext.ScrolledText(Ventana_principal, height=27, width=90)
area_chat.place(x=60, y=130)
area_chat.config(state="normal")
area_chat.insert(END, """LaLiga bot: ¡Hola! preguntame lo que quieras sobre 'LaLiga'""" + "\n" + "\n")
area_chat.config(state="disabled")
area_chat.configure(font=('Consolas', 11))

# creando area para enviar comando
area_texto = Text(Ventana_principal, height=4, width=85)
area_texto.place(x=60, y=630)

Ventana_principal.mainloop()
