import tkinter as tk
import time
import math

def update_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour

    # Calcular los ángulos de las manecillas del reloj
    sec_angle = math.radians((seconds - 15) * 6)
    min_angle = math.radians((minutes - 15) * 6 + (seconds / 10))
    hour_angle = math.radians((hours - 3) * 30 + (minutes / 2))

    # Actualizar la posición de las manecillas
    canvas.delete("hands")
    canvas.create_line(150, 150, 150 + 60 * math.cos(hour_angle), 150 - 60 * math.sin(hour_angle), width=4, fill="black", tags="hands")
    canvas.create_line(150, 150, 150 + 80 * math.cos(min_angle), 150 - 80 * math.sin(min_angle), width=3, fill="blue", tags="hands")
    canvas.create_line(150, 150, 150 + 90 * math.cos(sec_angle), 150 - 90 * math.sin(sec_angle), fill="red", tags="hands")

    # Llamar a esta función nuevamente después de 1000 ms (1 segundo)
    root.after(1000, update_clock)

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

update_clock()

root.mainloop()
