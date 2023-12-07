from p5 import *

# --------- GLOBAL VARIABLES -----------
# screen width and height variables:
width = 800
height = 450
# player related variables:
player_x = 10
player_y = 200
falling = True
dead = False
finished = False
# jump related variables:
jump_distance = int(input("how far would you like to jump?"))
jumping = False
jumps_left = int(input("how many jumps do you want to do?")) -1
jump_progress = 0
# -------------------------------------


# Setup our game!
def setup():
    global bgd_colour, jump_distance, jumps_left
    
    bgd_colour = Color(255,255,255)  # set background colour
    size(width, height) # set screen size
    
    
# Draw our game!
def draw():
    global width, height, falling, jump_distance, finished
    
    if not finished:
        draw_level()
        finished = check_if_finished()
        if dead == False:
            draw_player()
    else:
        text_size(25)
        text_align(CENTER, CENTER)
        text("You WIN!", width/2, height/2)

# Draw the background to our level
def draw_level():
    global width, height, falling
    
    # Draw white background
    fill(255,255,255)
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

def draw_player():
    global player_x, player_y, bgd_colour, falling, jumping, jump_distance, dead, jumps_left, jump_progress
    
    # Draw player
    player_colour = Color(255,0,0)
    fill(player_colour)
    player_height = 20
    player_width = 10
    rect(player_x, player_y, player_width, player_height)

    # Get colour of level directly below player's feet, so we know if they are standing on anything
    contact_colour = get(player_x, player_y+player_height+1).hex   
    
    # if we are not in contact with any platform and not in the middle of a jump
    if contact_colour == bgd_colour.hex and not jumping:
        # free fall!
        player_y += 5
        print("falling!")
        falling = True
    elif contact_colour == Color(255,0,0).hex:
        # dead
        dead = True
        print("you died bro")
    else:
        # no longer falling!
        falling = False
        
    if not falling and not jumping:
        # if we are stood at a platform then we want to begin jumping!
        jumping = True
    elif jumping == True:
        if jump_progress < 10:
            jump(jump_progress)
            jump_progress += 1
        else:
            if jumps_left > 0:
                jumping = False
                jump_progress = 0
                jumps_left -= 1

    if jumps_left <= 0 and not falling:
        # if we are out of jumps and stood on a platform,
        # then we walk right
        jumping = False
        player_x += 2
    
# This is what the get function does behind the scenes...
# def get(x, y):
#     load_pixels()
#     pixel = pixels[(x,y)]
#     return pixel


run(frame_rate=15)
# runs will call setup() then will repeatedly call draw() forever!
