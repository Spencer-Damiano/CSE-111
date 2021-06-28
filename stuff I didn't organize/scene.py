import tkinter as tk
from tkinter.constants import X
import random


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    # draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_ground(canvas, scene_right, scene_bottom)
    draw_sky(canvas, scene_left, scene_top)
    draw_moon(canvas, 650, 50)
    draw_cloud_1(canvas, 100, 100)
    draw_cloud_2(canvas, 200, 100)
    draw_ufo(canvas, 275, 275, 340, 240)
    draw_grid(canvas, scene_left, scene_right, scene_top, scene_bottom)

    


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_cloud_1(canvas, x, y):
    for i in range(0, 3):
        canvas.create_oval(x, y, x + 100, y +25, fill="darkgray", width=False)
        x += 33
        y += 5

def draw_cloud_2(canvas, x, y):
    for i in range(0, 3):
        canvas.create_oval(x, y, x + 100, y +25, fill="darkgray", width=False)
        x += 33
        y += 5

def draw_sky(canvas, scene_left, scene_top):
    horizion_x = 799
    horizion_y = 300

    canvas.create_rectangle(scene_left, scene_top, horizion_x, horizion_y, fill="#2d22a3", width=False)

def draw_ground(canvas, scene_right, scene_bottom):
    sky_ground_x = 0
    sky_ground_y = 300
    canvas.create_rectangle(sky_ground_x, sky_ground_y, scene_right, scene_bottom, fill="green", width=False)

def draw_grid(canvas, left, right, top, bottom):

    grid_spacing = 100
    horz_margin = 20
    vert_margin = 10

    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + horz_margin, i + vert_margin, text=(f'{i}'))
    
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + vert_margin, text=(f'{i}'))

def draw_ufo(canvas, x, y, x2, y2):
    canvas.create_oval(x2, y2, x2 + 75, y2 +75, fill="yellow")
    canvas.create_oval(x, y, x + 200, y + 50, fill="gray")

def draw_moon(canvas, x, y):
    
    canvas.create_oval(x, y, x +100, y + 100, fill="#c7c7c7")

    big_dent_x = x + 50
    big_dent_y = y + 10
    big_post_x = big_dent_x + 32
    big_post_y = big_dent_y + 28
    color = 999999

    canvas.create_oval(big_dent_x, big_dent_y, big_post_x, big_post_y, fill=f"#{color}")

    
    shade_x = big_dent_x + 2
    shade_y = big_dent_y + 2
    shade_x_post = big_post_x - 2
    shade_y_post = big_post_y - 2
    shade_run = 1
    pixal_shade = 1.6

    while shade_run != 9:
        canvas.create_oval(shade_x, shade_y, shade_x_post, shade_y_post, fill=f"#{color}", outline=f"#{color}")
        if shade_run != 20:
            if color != 111111 and color != 000000:
                color -= 111111
            shade_x += pixal_shade
            shade_y += pixal_shade
            shade_x_post -= pixal_shade
            shade_y_post -= pixal_shade
            shade_run += 1
    
    # moon dent 2
    big_dent_x = x + 7
    big_dent_y = y + 45
    big_post_x = big_dent_x +26
    big_post_y = big_dent_y +23
    color = 999999

    canvas.create_oval(big_dent_x, big_dent_y, big_post_x, big_post_y, fill=f"#{color}")

    shade_size = 1
    shade_x = big_dent_x + shade_size
    shade_y = big_dent_y + shade_size
    shade_x_post = big_post_x - shade_size
    shade_y_post = big_post_y - shade_size
    shade_run = 1
    pixal_shade = 1.4

    while shade_run != 9:
        canvas.create_oval(shade_x, shade_y, shade_x_post, shade_y_post, fill=f"#{color}", outline=f"#{color}")
        if shade_run != 20:
            if color != 111111 and color != 000000:
                color -= 111111
            shade_x += pixal_shade
            shade_y += pixal_shade
            shade_x_post -= pixal_shade
            shade_y_post -= pixal_shade
            shade_run += 1
    #moon dent 3
    big_dent_x = x + 60
    big_dent_y = y + 60
    big_post_x = big_dent_x +24
    big_post_y = big_dent_y +27

    canvas.create_oval(big_dent_x, big_dent_y, big_post_x, big_post_y, fill=f"#{color}")

    color = 999999
    shade_size = 1
    shade_x = big_dent_x + shade_size
    shade_y = big_dent_y + shade_size
    shade_x_post = big_post_x - shade_size
    shade_y_post = big_post_y - shade_size
    shade_run = 1
    pixal_shade = 1

    while shade_run != 8:
        canvas.create_oval(shade_x, shade_y, shade_x_post, shade_y_post, fill=f"#{color}", outline=f"#{color}")
        if shade_run != 20:
            if color != 111111 and color != 000000:
                color -= 111111
            shade_x += pixal_shade
            shade_y += pixal_shade
            shade_x_post -= pixal_shade
            shade_y_post -= pixal_shade
            shade_run += 1
    # moon dent top right
    big_dent_x = x + 25
    big_dent_y = y + 9.5
    big_post_x = big_dent_x +16
    big_post_y = big_dent_y +14
    color = 999999

    canvas.create_oval(big_dent_x, big_dent_y, big_post_x, big_post_y, fill=f"#{color}")

    shade_size = 1
    shade_x = big_dent_x + shade_size
    shade_y = big_dent_y + shade_size
    shade_x_post = big_post_x - shade_size
    shade_y_post = big_post_y - shade_size
    shade_run = 1
    pixal_shade = .75

    while shade_run != 8:
        canvas.create_oval(shade_x, shade_y, shade_x_post, shade_y_post, fill=f"#{color}", outline=f"#{color}")
        if shade_run != 20:
            if color != 111111 and color != 000000:
                color -= 111111
            shade_x += pixal_shade
            shade_y += pixal_shade
            shade_x_post -= pixal_shade
            shade_y_post -= pixal_shade
            shade_run += 1


def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()