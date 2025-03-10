import tkinter as tk
from tkinter import messagebox

# Función para agregar tarea a la lista
def agregar_tarea():
    tarea = entry_tarea.get()  # Obtener el texto del campo de entrada
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)  # Agregar la tarea a la lista
        entry_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

# Función para eliminar la tarea seleccionada
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()  # Obtener la tarea seleccionada
        lista_tareas.delete(tarea_seleccionada)  # Eliminar la tarea de la lista
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Función para marcar tarea como completada
def marcar_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()  # Obtener la tarea seleccionada
        tarea = lista_tareas.get(tarea_seleccionada)
        lista_tareas.delete(tarea_seleccionada)  # Eliminarla de la lista
        lista_tareas.insert(tk.END, tarea + " (Completada)")  # Volver a agregarla con la etiqueta "(Completada)"
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Crear los widgets
entry_tarea = tk.Entry(ventana, width=40)
boton_agregar = tk.Button(ventana, text="Agregar Tarea", width=20, command=agregar_tarea)
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", width=20, command=eliminar_tarea)
boton_completada = tk.Button(ventana, text="Marcar como Completada", width=20, command=marcar_completada)
lista_tareas = tk.Listbox(ventana, width=40, height=10)

# Ubicar los widgets en la ventana usando grid
entry_tarea.grid(row=0, column=0, padx=10, pady=10)
boton_agregar.grid(row=0, column=1, padx=10, pady=10)
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
boton_eliminar.grid(row=2, column=0, padx=10, pady=10)
boton_completada.grid(row=2, column=1, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
