import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)


def animate_line(start, end, line):
    ax, ay = start
    cx, cy = end

    if cx < 5:
        cx += 0.1
        cy += 0.1
        canvas.coords(line, ax * 100 + 65, ay * 100 + 145, cx * 100 + 65, cy * 100 + 145)
        canvas.update()
        root.after(100, animate_line, (ax, ay), (cx, cy), line)
    else:
        canvas.delete(line)


def start_animation(start, end):
    line = canvas.create_line(start[0] * 100 + 65, start[1] * 100 + 145, end[0] * 100 + 65, end[1] * 100 + 145,
                              fill="red", width=2)
    animate_line(start, end, line)


start_animation((0, 0), (0, 1))

root.mainloop()
