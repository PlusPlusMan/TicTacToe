import tkinter as tk

# Create the window
root = tk.Tk()
root.title("Line Animation")
root.geometry("300x300")

# Create the canvas
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Function to animate the line
def animate_line(start_x, start_y, end_x, end_y, step_size=5):
    # Calculate the change in x and y
    delta_x = end_x - start_x
    delta_y = end_y - start_y

    # Calculate the number of steps to animate the line
    steps = max(abs(delta_x), abs(delta_y)) // step_size + 1

    # Calculate the step size for x and y
    x_step = delta_x / steps
    y_step = delta_y / steps

    # Animate the line step by step
    for i in range(steps + 1):
        x = start_x + x_step * i
        y = start_y + y_step * i
        canvas.create_line(start_x, start_y, x, y)
        root.update()
        root.after(10)  # 10 milliseconds delay between each step

    # Update the starting points for the next animation
    start_x = end_x
    start_y = end_y

# Get user input for the coordinates of the line
a0 = 0*100+65
y0 = 2*100+145
a1 = 2*100+65
y1 = 0*100+145

# Call the animate_line function
animate_line(a0, y0, a1, y1)

# Start the main event loop
root.mainloop()
