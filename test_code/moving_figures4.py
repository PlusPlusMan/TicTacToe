import random
import tkinter as tk
import math

root = tk.Tk()
root.geometry("750x500")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)


# Class for circle objects
class Circle:
    def __init__(self, x, y, r, color, vx, vy, turn_around_speed, turn_around_direction):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = vx
        self.vy = vy
        self.turn_around_speed = turn_around_speed
        self.turn_around_direction = turn_around_direction
        self.shape = canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)

    def update_position(self):
        # Update the position of the circle based on its velocity vector
        self.x += self.vx
        self.y += self.vy

        # Change the turn around direction of the circle
        self.turn_around_direction += self.turn_around_speed

        # Update the shape on the canvas
        canvas.coords(self.shape, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canvas.create_polygon(self.x, self.y, self.x + self.r * math.cos(self.turn_around_direction),
                              self.y + self.r * math.sin(self.turn_around_direction), fill=self.color)


    # Function for updating all the circles
    def update_circles():
        # Update the position and turn around direction of each circle
        for circle in circles:
            circle.update_position()

        # Detect collisions between circles and between circles and the window borders
        for i, circle1 in enumerate(circles):
            for circle2 in circles[i + 1:]:
                detect_collisions(circle1, circle2)
            detect_collisions_with_borders(circle1)

        # Call this function again after a short delay
        canvas.after(10, update_circles)


    # Function for detecting collisions
    def detect_collisions(circle1, circle2):
        # Check if the circles are overlapping
        distance = ((circle1.x - circle2.x) ** 2 + (circle1.y - circle2.y) ** 2) ** 0.5
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

            # Calculate new velocity vectors after the collision
            v1n_ = v2n
            v2n_ = v1n
            v1x_ = v1n_ * nx + v1t * tx
            v1y_ = v1n_ * ny + v1t * ty
            v2x_ = v2n_ * nx + v2t * tx
            v2y_ = v2n_ * ny + v2t * ty

            # Update velocity vectors
            circle1.vx = v1x_
            circle1.vy = v1y_
            circle2.vx = v2x_
            circle2.vy = v2y_

            # Change turn around direction and speed for each circle
            circle1.turn_around_direction = random.uniform(-math.pi, math.pi)
            circle1.turn_around_speed = random.uniform(-0.05, 0.05)
            circle2.turn_around_direction = random.uniform(-math.pi, math.pi)
            circle2.turn_around_speed = random.uniform(-0.05, 0.05)

    # Function for detecting collisions with the window borders
    def detect_collisions_with_borders(circle):
        # Check if the circle is hitting the left or right border
        if circle.x - circle.r <= 0 or circle.x + circle.r >= 750:
            # Reverse the x velocity
            circle.vx = -circle.vx
            # Change turn around direction and speed
            circle.turn_around_direction = random.uniform(-math.pi, math.pi)
            circle.turn_around_speed = random.uniform(-0.05, 0.05)

        # Check if the circle is hitting the top or bottom border
        if circle.y - circle.r <= 0 or circle.y + circle.r >= 500:
            # Reverse the y velocity
            circle.vy = -circle.vy
            # Change turn around direction and speed
            circle.turn_around_direction = random.uniform(-math.pi, math.pi)
            circle.turn_around_speed = random.uniform(-0.05, 0.05)

    # Create 20 circles with random parameters
    circles = []
    for i in range(20):
        x = random.randint(50, 700)
        y = random.randint(50, 450)
        r = random.randint(10, 50)
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        vx = random.uniform(-5, 5)
        vy = random.uniform(-5, 5)
        turn_around_speed = random.uniform(-0.05, 0.05)
        turn_around_direction = random.uniform(-math.pi, math.pi)
        circles.append(Circle(x, y, r, color, vx, vy, turn_around_speed, turn_around_direction))

    # Start animation
    update_circles()
    root.mainloop()

