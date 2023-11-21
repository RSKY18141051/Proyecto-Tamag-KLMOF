import tkinter as tk
import time
import math

def update_clock():
    # Resto del código para actualizar el reloj...

    # Llamar a esta función nuevamente después de 1000 ms (1 segundo)
    root.after(1000, update_clock)

def display_reminders():
    reminders = [
        "Recordatorio 1: Reunión a las 10:00 AM",
        "Recordatorio 2: Llamada con el cliente a las 3:00 PM",
        "Recordatorio 3: Completar informe antes de las 5:00 PM"
    ]

    # Limpiar el widget de etiqueta
    reminder_label.config(text='\n'.join(reminders))
    
    # Llamar a esta función cada 60000 ms (1 minuto) para actualizar los recordatorios
    root.after(60000, display_reminders)

root = tk.Tk()
root.title("Reloj Analógico")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Dibujar el dial del reloj
canvas.create_oval(50, 50, 250, 250)
for i in range(60):
    angle = math.radians(i * 6)
    if i % 5 == 0:
        length = 10
    else:
        length = 5
    canvas.create_line(150 + 100 * math.cos(angle) * 0.9, 150 - 100 * math.sin(angle) * 0.9, 150 + 100 * math.cos(angle) * 0.95, 150 - 100 * math.sin(angle) * 0.95, width=2, fill="black")
    canvas.create_text(150 + 120 * math.cos(angle) * 0.8, 150 - 120 * math.sin(angle) * 0.8, text=str(i + 1), fill="black")

# Crear un widget de etiqueta para mostrar los recordatorios
reminder_label = tk.Label(root, text="", justify="left")
reminder_label.pack(pady=10)

# Iniciar la función para mostrar los recordatorios
display_reminders()

# Iniciar la función para actualizar el reloj
update_clock()

root.mainloop()
