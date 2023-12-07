    
""" A short activity to put a santa hat onto an avatar.
    Will need to install Pillow package and have Python installed to use this!
    Use "pip install Pillow"
"""
from PIL import Image

try:
    # Change "default_avatar.png" this to the name of your avatar image:
    avatar_image = Image.open("default-avatar.png").copy().convert('RGB') # if it's a png it needs to be converted to RGB
    hat_img = Image.open("santa_hat.png").copy()
    
    width, height = hat_img.size
    
    # Edit these variables to get the hat to fit!
    width = int(width / 2)
    height = int(height / 2)
    x_position = 50
    y_position = 50
    # Uncomment this line to flip your hat.
    # hat_img = hat_img.transpose(Image.FLIP_LEFT_RIGHT)
    
    hat_img = hat_img.resize((width, height))
    avatar_image.paste(hat_img, (x_position, y_position), hat_img)
    
    avatar_image.save("hatted_avatar.png")
    
    print("DONE")
except IOError:
    pass
