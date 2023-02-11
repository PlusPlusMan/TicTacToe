import tkinter as tk
import random
import time

# Window and canvas setup
root = tk.Tk()
root.geometry("750x500")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Circle class
class Circle:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        self.gx = random.uniform(-0.1, 0.1)
        self.gy = random.uniform(-0.1, 0.1)
        self.item = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)

# Function for detecting collisions
# Function for detecting collisions
def detect_collisions(circle1, circle2):
    # Check if the circles are overlapping
    distance = ((circle1.x - circle2.x)**2 + (circle1.y - circle2.y)**2)**0.5
    if distance <= (circle1.r + circle2.r):
        # Calculate normal and tangent unit vectors
        nx = (circle2.x - circle1.x) / distance
        ny = (circle2.y - circle1.y) / distance
        tx = -ny
        ty = nx

        # Project velocity vectors onto the normal and tangent axes
        v1n = circle1.vx * nx + circle1.vy * ny
        v1t = circle1.vx * tx + circle1.vy * ty
        v2n = circle2.vx * nx + circle2.vy * ny
        v2t = circle2.vx * tx + circle2.vy * ty

        # Calculate new velocity vectors after collision
        # Elastic collision formula
        v1n_after = v2n
        v2n_after = v1n
        v1x_after = v1n_after * nx + v1t * tx
        v1y_after = v1n_after * ny + v1t * ty
        v2x_after = v2n_after * nx + v2t * tx
        v2y_after = v2n_after * ny + v2t * ty

        # Update velocity vectors
        circle1.vx = v1x_after
        circle1.vy = v1y_after
        circle2.vx = v2x_after
        circle2.vy = v2y_after


# Function for detecting collisions with window borders
def detect_border_collisions(circle):
    # Check if the circle is hitting the left or right border
    if (circle.x - circle.r + circle.vx <= 0) or (circle.x + circle.r + circle.vx >= 750):
        # Reverse x velocity
        circle.vx = -circle.vx
    # Check if the circle is hitting the top or bottom border
    if (circle.y - circle.r + circle.vy <= 0) or (circle.y + circle.r + circle.vy >= 500):
        # Reverse y velocity
        circle.vy = -circle.vy

# Function for updating the circles on the canvas
def update_circles():
    for c1 in circles:
        # Update position of circle
        c1.x += c1.vx
        c1.y += c1.vy
        canvas.move(c1.item, c1.vx, c1.vy)

        # Check collisions with other circles
        for c2 in circles:
            if c1 != c2:
                detect_collisions(c1, c2)

        # Check collisions with window borders
        detect_border_collisions(c1)

    # Repeat after 10 milliseconds
    root.after(10, update_circles)

# Create 20 circles with random parameters
circles = []
for i in range(20):
    x = random.randint(50, 700)
    y = random.randint(50, 450)
    r = random.randint(10, 50)
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    circles.append(Circle(x, y, r, color))

update_circles()
root.mainloop()
