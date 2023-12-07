from p5 import *

# --------- GLOBAL VARIABLES -----------
# screen width and height variables:
width = 800
hieght = 450
# player related variables:


finished = False
# jump related variables:

# -------------------------------------


# Setup our game!
def setup():
    bgd_colour = (255,255,255)
    size(width, height)
    
    # Take inputs from the user here
    

# Draw our game!
def draw():
    
    draw_level()
    # draw player here!


# Draw the background to our level
def draw_level():
    global width, height, falling, bgd_colour
    
    # Draw white background
    fill(bgd_colour)
    rect(0,0,width, height)
    
    fill(0,0,0) # set colour (black)
    platform_thickness = 50 # set thickness of platform
    platform_height = 200 # set height of platforms

    # Draw platforms
    for i in range(8):
        distance_between_platforms = 100
        platform_x_position = i * distance_between_platforms
        rect((0 + platform_x_position), (height - 200), platform_thickness, platform_height)

    # Draw end zone and finish flag
    rect(750, height-200, 50, 200)
    fill(0, 255, 0)
    rect(770, height-220, 2, 20)
    triangle(770, height-220, 770, height-210, 780, height-215) # (x1,y2) (x2,y2) (x3,y3)

    # Draw lava pit
    fill(255, 0, 0)
    rect(0, height-20, width, 20)

# Check if we cross the green flag
def check_if_finished():
    global player_x, player_y
    
    # get the colour of the level at the player's head height
    current_pos_colour = get(player_x, player_y+15)
    
    # if the colour is green then we have reached the end of the level
    if current_pos_colour.hex == Color(0, 128, 0).hex:
        print("finish line reached")
        return True
    else:
        return False

# Jump in stages so there is a nice animation in our game
def jump(jump_progress):
    global player_x, player_y, jumping, jump_distance
    jump_interval_distance = jump_distance / 10
    if jump_progress < 5:
        player_x += jump_interval_distance
        player_y -= 4
    else:
        player_x += jump_interval_distance
        player_y += 4

# define function to draw player here

    
# This is what the get function does behind the scenes...
# def get(x, y):
#     load_pixels()
#     pixel = pixels[(x,y)]
#     return pixel


# add run function call here
run(frame_rate=15)

# runs will call setup() then will repeatedly call draw() forever!

