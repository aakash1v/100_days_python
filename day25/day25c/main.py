import turtle
from PIL import Image
    

screen = turtle.Screen()
screen.title('India State Game')

image_path ='india_img.gif'
image = Image.open(image_path)

# Resize the image to fit within the Turtle window if needed
#max_size = (800, 600)  # Maximum width and height to fit in Turtle window
#image.thumbnail(max_size)

# Save the resized image if needed
resized_image_path = 'resized_image.gif'
#image.save(resized_image_path, 'GIF')

# Set the window size to match the resized image size
#screen.setup(width=max_size[0], height=max_size[1])


# Register the image as a shape in Turtle
screen.addshape(resized_image_path)


turtle.shape(resized_image_path)
def get_mouse_click_coor(x,y):
   print([x,y])
turtle.onscreenclick(get_mouse_click_coor)


screen.mainloop()
