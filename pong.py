import turtle

window = turtle.Screen()
window.title("Pong by Dhrumil")
window.bgcolor("black")
window.setup(width= 800, height= 600)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

# Ball

#Main game loop
while True:
    window.update()