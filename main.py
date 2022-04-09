from tkinter import *
import tkinter.font as font
from tkinter import scrolledtext
from tkinter import messagebox
from AnalizadorLexico import AnalizadorLexico

analizador_lexico = AnalizadorLexico()


def mandar_mensaje():
    if len(area_texto.get(1.0, END)) > 1:
        mensaje = "Tú: " + area_texto.get(1.0, END) + "\n"
        print(mensaje)
        area_chat.config(state="normal")
        area_chat.insert(END, mensaje)
        area_chat.config(state="disabled")
        area_texto.delete(1.0, END)
    else:
        messagebox.showinfo(title="Error", message="No puedes enviar un mensaje vacío")


# Info sobre la ventana
Ventana_principal = Tk()
Ventana_principal.title("LaLiga Bot")
Ventana_principal.configure(width=1100, height=800)
Ventana_principal.resizable(False, False)
Ventana_principal.eval('tk::PlaceWindow . center')
# Creando botones
mi_fuente = font.Font(family='Helvetica', size=15)

# boton para enviar comando
boton_analizar = Button(Ventana_principal, text="Enviar")
boton_analizar.configure(width=6, height=2, bg="#213dec", fg="white", borderwidth=5, command=mandar_mensaje)
boton_analizar['font'] = mi_fuente
boton_analizar.place(x=700, y=660)

# boton de generar reporte tokens
boton_tokens = Button(Ventana_principal, text="Reporte de tokens")
boton_tokens.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5)
boton_tokens['font'] = mi_fuente
boton_tokens.place(x=850, y=130)

# boton de generar reporte de errores
boton_errores = Button(Ventana_principal, text="Reporte de errores")
boton_errores.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5)
boton_errores['font'] = mi_fuente
boton_errores.place(x=850, y=200)

# boton de para limpiar tokens
boton_delete_tokens = Button(Ventana_principal, text="Limpiar log tokens")
boton_delete_tokens.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5)
boton_delete_tokens['font'] = mi_fuente
boton_delete_tokens.place(x=850, y=270)

# boton de para limpiar errores
boton_delete_errors = Button(Ventana_principal, text="Limpiar log errores")
boton_delete_errors.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5)
boton_delete_errors['font'] = mi_fuente
boton_delete_errors.place(x=850, y=340)

# boton manual de usuario
boton_manual_users = Button(Ventana_principal, text="Manual de usuario")
boton_manual_users.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5)
boton_manual_users['font'] = mi_fuente
boton_manual_users.place(x=850, y=410)

# boton manual tecnico
boton_manual_tecnico = Button(Ventana_principal, text="Manual técnico")
boton_manual_tecnico.configure(width=15, height=2, bg="#213dec", fg="white", borderwidth=5)
boton_manual_tecnico['font'] = mi_fuente
boton_manual_tecnico.place(x=850, y=480)
# creando area de chat
area_chat = scrolledtext.ScrolledText(Ventana_principal, height=27, width=90)
area_chat.place(x=60, y=130)
area_chat.config(state="normal")
area_chat.insert(END, """LaLiga bot: ¡Hola! preguntame lo que quieras sobre 'LaLiga'""" + "\n" + "\n")
area_chat.config(state="disabled")
area_chat.configure(font=("Times New Roman", 12))

# creando area para enviar comando
area_texto = Text(Ventana_principal, height=3, width=75)
area_texto.place(x=60, y=660)

Ventana_principal.mainloop()
