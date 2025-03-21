import tkinter as tk
from tkinter import messagebox
from acta_trimestral import abrir_ventana_acta_trimestral  # Importar la función del archivo secundario

# Funciones asociadas a los botones
def acta_por_competencia():
    messagebox.showinfo("Acta por Competencia", "Generando acta por competencia...")

def seguimiento_por_aprendiz():
    messagebox.showinfo("Seguimiento por Aprendiz", "Generando seguimiento por aprendiz...")

def seguimiento_a_la_formacion():
    messagebox.showinfo("Seguimiento a la Formación", "Generando seguimiento a la formación...")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Seguimiento de Formación")
ventana.geometry("400x300")  # Tamaño de la ventana

# Crear botones y asociar funciones
boton_acta_trimestral = tk.Button(ventana, text="Acta Trimestral", command=abrir_ventana_acta_trimestral, width=20, height=2)
boton_acta_trimestral.pack(pady=10)

boton_acta_competencia = tk.Button(ventana, text="Acta por Competencia", command=acta_por_competencia, width=20, height=2)
boton_acta_competencia.pack(pady=10)

boton_seguimiento_aprendiz = tk.Button(ventana, text="Seguimiento por Aprendiz", command=seguimiento_por_aprendiz, width=20, height=2)
boton_seguimiento_aprendiz.pack(pady=10)

boton_seguimiento_formacion = tk.Button(ventana, text="Seguimiento a la Formación", command=seguimiento_a_la_formacion, width=20, height=2)
boton_seguimiento_formacion.pack(pady=10)


# Iniciar el bucle principal de la ventana
ventana.mainloop()