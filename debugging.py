''' Peckages & Debugging
    (1) Python packages and Core package
    (2) Package Manager & External package
    (3) Debugging
'''

#  Peckages - (module) 3 xil
print("=====  Python packages and Core package =====")
''' Python Packages/Modules: Core, File and External'''
# Core Packages > https://docs.python.org/3/library

# Core

# import turtle

# def draw_circle(t, color, radius, x, y):
   
#     t.penup()
#     t.fillcolor(color)
#     t.goto(x, y - radius) # 중심을 맞추기 위해 반지름만큼 이동
#     t.pendown()
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()

# def make_pizza():
   
#     screen = turtle.Screen()
#     screen.title("Python Turtle Pizza")
#     screen.bgcolor("#f0f0f0")
    
#     t = turtle.Turtle()
#     t.speed(3) 
    
   
#     draw_circle(t, "#D2B48C", 150, 0, 0)
    
   
#     draw_circle(t, "#FFD700", 135, 0, 0)
    
    
#     pepperoni_positions = [(-60, 40), (60, 40), (0, -20), (-40, -80), (40, -80), (0, 90)]
#     for x, y in pepperoni_positions:
#         draw_circle(t, "#B22222", 20, x, y)
    
   
#     t.penup()
#     t.goto(0, 0)
#     t.color("#8B4513")
#     t.pensize(3)
#     for _ in range(8):
#         t.pendown()
#         t.forward(150)
#         t.backward(150)
#         t.right(45)
    
#     t.hideturtle()
#     print("피자가 완성되었습니다!")
#     screen.mainloop()

# if __name__ == "__main__":
#     make_pizza()


# print("======")
# my_file = open("material/message.txt", "r")
# try:
#     content = my_file.read()
#     print("content:", content)
# finally:
#     my_file.close()


# with - context manager
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("done")


print("=== Package Manager & External package ===")


from PIL import Image
with Image.open("material/logoo.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")
    

print("==== Debugging ====")

def get_summary(*args): #define
    total_amount = 0
    for a in args:
        total_amount += a
    return total_amount


result = get_summary(1, 2, 3, 4, 5) # call
print("result:", result)