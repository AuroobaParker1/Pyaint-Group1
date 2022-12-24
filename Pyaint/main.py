import copy
from utils import *
from utils import Sliders
from utils import Segment
import pygame
from utils import *
import math
from operator import itemgetter

#Essential Variables
four_points=[(0,0),(0,0),(0,0),(0,0)]
slider_thickness=False
WIN = pygame.display.set_mode((WIDTH+180 + RIGHT_TOOLBAR_WIDTH, HEIGHT))
pygame.display.set_caption("Pyaint")
STATE = "COLOR"
copied_shape=None
Change = False
free_draw = True
selection_points=[]
Shape_storage = []
selected_rectangle = None
drawn = False
selected = False
selected_shape = None
ShapeType = "Rectangle"
counter=1
shapename="10gon"
drawshape=False
select_resize =False
select_selection2=False
resize_left=False

#Initializes The Grid
def init_grid(rows, columns, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(columns):  # use _ when variable is not required
            grid[i].append(color)
    return grid


#Draws Th Slider
slider = Sliders.Slider((700, 600))

#Draws The Grid
def draw_grid(win, grid):

    global selected,selection_points

    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, SILVER, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS + 1):
            pygame.draw.line(win, SILVER, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

    #Checks if shape drawn
    if (drawn == True):

        for Shape in Shape_storage:
            #Draw Shapes On Grid
            Shape.Draw(win)

    #Checks if a shape is selected
    if (selected and selected_shape):
        #Sets its thickness according to slider
        selected_shape.thickness=math.ceil(slider.getValue())
        #Draws Selection rectangle around it
        selection_points=draw_dashed_rectangle(win,four_points)


#Draws Selection Rectangle Around Selected Shape
def draw_dashed_rectangle(surf,points_list):
    
    draw_dashed_line_x(surf,points_list[0],points_list[2])
    draw_dashed_line_x(surf, points_list[1], points_list[3])
    draw_dashed_line_y(surf,points_list[0],points_list[1])
    draw_dashed_line_y(surf,points_list[2],points_list[3])


    rect2 = pygame.Rect(points_list[0][0]-5, points_list[0][1]-5, 10, 10)
    rect3 = pygame.Rect(points_list[1][0]-5, points_list[1][1] - 5, 10, 10)
    rect4 = pygame.Rect(points_list[2][0] - 5, points_list[2][1] -5, 10, 10)
    rect5 = pygame.Rect(points_list[3][0] - 5, points_list[3][1]- 5, 10, 10)

    pygame.draw.rect(surf, (0, 0, 0), rect2, 2, 3)
    pygame.draw.rect(surf, (0, 0, 0), rect3, 2, 3)
    pygame.draw.rect(surf, (0, 0, 0), rect4, 2, 3)
    pygame.draw.rect(surf, (0, 0, 0), rect5, 2, 3)

    #Adds Rotate Image Around Selected Shape
    img = pygame.image.load("rotate.png").convert_alpha()
    img = pygame.transform.scale(img, (20, 20))
    surf.blit(img, (points_list[0][0] + (points_list[2][0]-points_list[0][0]) / 2 - 5, points_list[0][1] - 20))

    #Adds Flip Image Around Selected Shape
    img2 = pygame.image.load("download.png").convert_alpha()
    img2 = pygame.transform.scale(img2, (20, 20))
    surf.blit(img2, (points_list[0][0] + (points_list[2][0]-points_list[0][0]) / 2 - 5, points_list[1][1] + 5))
    return rect2,rect3,rect4,rect5


#Draw A single Vertical Dashed Line
def draw_dashed_line_y(surf, start_pos, end_pos, width=3, dash_length=10):
    origin = (start_pos)
    target = (end_pos)
    displacement = target[1] - origin[1]

    something = math.floor(displacement / dash_length)

    for index in range(0, something, 2):

        start = (origin[0],origin[1] + (    index    * dash_length))
        end   =(origin[0], origin[1] + ( (index + 1) * dash_length))

        pygame.draw.line(surf, (19, 56, 190), start, end, width)
        if (something - index) < 3:
            pygame.draw.line(surf, (19, 56, 190), end, target, width)

#Draw A single Horizontal Dashed Line
def draw_dashed_line_x(surf, start_pos, end_pos, width=3, dash_length=10):
    origin = (start_pos)
    target = (end_pos)
    displacement = target[0] - origin[0]
    something=math.floor(displacement / dash_length)

    for index in range(0, something, 2):

        start = (origin[0] + (index * dash_length),origin[1])
        end = (origin[0] + ((index + 1) * dash_length),origin[1] )


        pygame.draw.line(surf, (19, 56, 190), start, end, width)
        if (something-index)<3:
            pygame.draw.line(surf, (19, 56, 190), end, target, width)


#Gets Text Regarding Mouse Position
def draw_mouse_position_text(win):
    global Shape_storage,selected
    #Gets Mouse Position
    pos = pygame.mouse.get_pos()
    pos_font = get_font(MOUSE_POSITION_TEXT_SIZE)
    try:
        row, col = get_row_col_from_pos(pos)
        text_surface = pos_font.render(str(row) + ", " + str(col), 1, BLACK)
        win.blit(text_surface, (5, HEIGHT - TOOLBAR_HEIGHT))
    except IndexError:
        for button in buttons:
            #Checks if a button is clicked
            if not button.clicked(pos):
                continue

            #Clears the screen if clear button is pressed
            if button.text == "Clear":
                text_surface = pos_font.render("Clear Everything", 1, BLACK)

                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                Shape_storage=[]
                selected=False
                break
            #Erases On Click If Eraser Button is Pressed
            if button.text == "Erase":
                text_surface = pos_font.render("Erase", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break

            #Allows Shape and grid Colouring If Fill Bucket button is Pressed
            if button.name == "FillBucket":
                text_surface = pos_font.render("Fill Bucket", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            #Allows Free Drawing If Brush Button Is Selected
            if button.name == "Brush":
                text_surface = pos_font.render("Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            #Swaps The Toolbar Buttons if Change Button Is Pressed
            if button.name == "Change":
                text_surface = pos_font.render("Swap Toolbar", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            #Checks the Color Of Button and Renders it to screen
            r, g, b = button.color
            text_surface = pos_font.render("( " + str(r) + ", " + str(g) + ", " + str(b) + " )", 1, BLACK)

            win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))

        #Sets Different Free Draw Pen Sizes Based On The Brush Width Button Selected
        for button in brush_widths:
            if not button.hover(pos):
                continue
            if button.width == size_small:
                text_surface = pos_font.render("Small-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_medium:
                text_surface = pos_font.render("Medium-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_large:
                text_surface = pos_font.render("Large-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break

#Renders the slider On Screen
slider = Sliders.Slider((700, 600))

#Draws The Screen
def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)



    pygame.event.get()

    #Draws The Slider
    slider.render(win)
    slider.changeValue()


    # Draws The Buttons
    button: object
    for button in buttons:
        button.draw(win)

    #Draws The Brush Size Buttons
    draw_brush_widths(win)
    #Draws Mouse Position Texr
    draw_mouse_position_text(win)
    #Updates the screen
    pygame.display.update()


#Draw the different Brush Widths On Screen
def draw_brush_widths(win):
    brush_widths = [
        Button(rtb_x - size_small / 2, 480, size_small, size_small, drawing_color, None, None, "ellipse"),
        Button(rtb_x - size_medium / 2, 510, size_medium, size_medium, drawing_color, None, None, "ellipse"),
        Button(rtb_x - size_large / 2, 550, size_large, size_large, drawing_color, None, None, "ellipse")
    ]
    for button in brush_widths:
        button.draw(win)
        # Set border colour
        border_color = BLACK
        if button.color == BLACK:
            border_color = GRAY
        else:
            border_color = BLACK
        # Set border width
        border_width = 2
        if ((BRUSH_SIZE == 1 and button.width == size_small) or (BRUSH_SIZE == 2 and button.width == size_medium) or (
                BRUSH_SIZE == 3 and button.width == size_large)):
            border_width = 4
        else:
            border_width = 2
        # Draw border
        pygame.draw.ellipse(win, border_color, (button.x, button.y, button.width, button.height),
                            border_width)  # border


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    if col >= ROWS:
        raise IndexError
    return row, col


def paint_using_brush(row, col, size):
    if BRUSH_SIZE == 1:
        grid[row][col] = drawing_color
    else:  # for values greater than 1
        r = row - BRUSH_SIZE + 1
        c = col - BRUSH_SIZE + 1

        for i in range(BRUSH_SIZE * 2 - 1):
            for j in range(BRUSH_SIZE * 2 - 1):
                if r + i < 0 or c + j < 0 or r + i >= ROWS or c + j >= COLS:
                    continue
                grid[r + i][c + j] = drawing_color

            # Checks whether the coordinated are within the canvas
def inBounds(row, col):
    if row < 0 or col < 0:
        return 0
    if row >= ROWS or col >= COLS:
        return 0
    return 1


def fill_bucket(row, col, color):
    # Visiting array
    vis = [[0 for i in range(101)] for j in range(101)]

    # Creating queue for bfs
    obj = []

    # Pushing pair of {x, y}
    obj.append([row, col])

    # Marking {x, y} as visited
    vis[row][col] = 1

    # Until queue is empty
    while len(obj) > 0:

        # Extracting front pair
        coord = obj[0]
        x = coord[0]
        y = coord[1]
        preColor = grid[x][y]

        grid[x][y] = color

        # Popping front pair of queue
        obj.pop(0)

        # For Upside Pixel or Cell
        if inBounds(x + 1, y) == 1 and vis[x + 1][y] == 0 and grid[x + 1][y] == preColor:
            obj.append([x + 1, y])
            vis[x + 1][y] = 1

        # For Downside Pixel or Cell
        if inBounds(x - 1, y) == 1 and vis[x - 1][y] == 0 and grid[x - 1][y] == preColor:
            obj.append([x - 1, y])
            vis[x - 1][y] = 1

        # For Right side Pixel or Cell
        if inBounds(x, y + 1) == 1 and vis[x][y + 1] == 0 and grid[x][y + 1] == preColor:
            obj.append([x, y + 1])
            vis[x][y + 1] = 1

        # For Left side Pixel or Cell
        if inBounds(x, y - 1) == 1 and vis[x][y - 1] == 0 and grid[x][y - 1] == preColor:
            obj.append([x, y - 1])
            vis[x][y - 1] = 1


#Check if polygon Selected
def selected_polygon(shape, click_left, click_up):
    return shape.collidepoint(click_left, click_up),shape


#Check if Mouse Position is within a polygon
def select_notpolygon(shape, click_left, click_up):
    #Ray-Casting Algorithm Used
    def PointInPolygon(shape, point):
        testline_left = Segment(Point(-999999999, point.y), point)
        testline_right = Segment(point, Point(-999999999, point.y))
        count_left = 0
        count_right = 0
        for e in shape.GetEdges():
            if EdgesIntersect(testline_left, e):
                count_left += 1
            if EdgesIntersect(testline_right, e):
                count_right += 1
        if count_left % 2 == 0 and count_right % 2 == 0:
            return False
        else:
            return True

    #Checks if The Edges Are Intersecting
    def EdgesIntersect(e1, e2):

        a = e1.p1
        b = e1.p2
        c = e2.p1
        d = e2.p2

        cmp = Point(c.x - a.x, c.y - a.y)
        r = Point(b.x - a.x, b.y - a.y)
        s = Point(d.x - c.x, d.y - c.y)

        cmpxr = cmp.x * r.y - cmp.y * r.x
        cmpxs = cmp.x * s.y - cmp.y * s.x
        rxs = r.x * s.y - r.y * s.x

        if cmpxr == 0:
            return (c.x - a.x < 0) != (c.x - b.x < 0)
        if rxs == 0:
            return False

        rxsr = 1 / rxs
        t = cmpxs * rxsr
        u = cmpxr * rxsr

        return t >= 0 and t <= 1 and u >= 0 and u <= 1
    joke= PointInPolygon(shape,Point(click_left,click_up))
    return joke,shape

#Checks Selection In Resizing
def select_notpolygon2(shape, click_left, click_up):
    def counterclockwise(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    def segment_intersect(A, B, C, D):
        return counterclockwise(A, C, D) != counterclockwise(B, C, D) and counterclockwise(A, B, C) != counterclockwise(
            A, B, D)

    def ray_cast(point, polyPoints, farAwayPoint):
        intersections = 0
        for i in range(len(polyPoints) - 1):
            if segment_intersect(point, farAwayPoint, polyPoints[i], polyPoints[i + 1]):
                intersections += 1
        if intersections % 2 == 0:
            return False
        else:
            return True
    joke=ray_cast((click_left,click_up),[shape.topleft, shape.bottomleft, shape.topright, shape.bottomright],(100000,10000))
    return joke,shape

run = True

clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_width = 40
button_height = 40
button_y_top_row = HEIGHT - TOOLBAR_HEIGHT / 2 - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT / 2 + 1
button_space = 42

size_small = 25
size_medium = 35
size_large = 50

rtb_x = WIDTH + RIGHT_TOOLBAR_WIDTH / 2
brush_widths = [
    Button(rtb_x - size_small / 2, 480, size_small, size_small, drawing_color, None, "ellipse"),
    Button(rtb_x - size_medium / 2, 510, size_medium, size_medium, drawing_color, None, "ellipse"),
    Button(rtb_x - size_large / 2, 550, size_large, size_large, drawing_color, None, "ellipse")
]

button_y_top_row = HEIGHT - TOOLBAR_HEIGHT / 2 - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT / 2 + 1
button_space = 42

# Adding Buttons
buttons = []

for i in range(int(len(COLORS) / 2)):
    buttons.append(Button(100 + button_space * i, button_y_top_row, button_width, button_height, COLORS[i]))

for i in range(int(len(COLORS) / 2)):
    buttons.append(
        Button(100 + button_space * i, button_y_bot_row, button_width, button_height, COLORS[i + int(len(COLORS) / 2)]))

# Right toolbar buttonst
# need to add change toolbar button.
for i in range(10):
    if i == 0:
        buttons.append(Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                              name="Change"))  # Change toolbar buttons
    else:
        buttons.append(Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                              "B" + str(i - 1), BLACK, name="B" + str(i - 1)))  # append tools



#Adding Buttons For Drawing Different Shapes
for i in range(7):
        buttons.append(Button(670, (i * (button_height+20)) + 100, button_width+10, button_height+10, WHITE,
                              "", BLACK, name=str(i+2), image_url="assets/" + str(i+2) + ".jpeg"))  # append tools

for i in range(7):
        buttons.append(Button(730, (i * (button_height+20)) + 100, button_width+10, button_height+10, WHITE,
                              "", BLACK, name=str(i+9), image_url="assets/" + str(i+9) + ".jpeg"))  # append tools

for i in range(7):
        buttons.append(Button(790, (i * (button_height+20)) + 100, button_width+10, button_height+10, WHITE,
                              "", BLACK, name=str(i+16), image_url="assets/" + str(i+16) + ".jpeg"))  # append tools

#MENU

#Button For Unfilling Colour Of A Shape
buttons.append(Button(490, 660, button_width+10, button_height-15, WHITE,"", BLACK, name="Unfill",image_url="assets/Unfill.jpeg"))
#Headings For Shape and Edge Thickness
buttons.append(Button(685, 30, button_width+100, button_height+10,WHITE,"",BLACK,name="shapes", image_url="assets/shapes.jpeg"))
buttons.append(Button(685, 565, button_width+100, button_height-10,WHITE,"",BLACK,name="edge", image_url="assets/edge.jpeg"))


buttons.append(
    Button(WIDTH - button_space, button_y_top_row, button_width, button_height, WHITE, "Erase", BLACK))  # Erase Button
buttons.append(
    Button(WIDTH - button_space, button_y_bot_row, button_width, button_height, WHITE, "Clear", BLACK))  # Clear Button
buttons.append(
    Button(WIDTH - 3 * button_space + 5, button_y_top_row, button_width - 5, button_height - 5, name="FillBucket",
           image_url="assets/paint-bucket.png"))  # FillBucket
buttons.append(
    Button(WIDTH - 3 * button_space + 45, button_y_top_row, button_width - 5, button_height - 5, name="Brush",
           image_url="assets/paint-brush.png"))  # Brush

draw_button = Button(5, HEIGHT - TOOLBAR_HEIGHT / 2 - 30, 60, 60, drawing_color)
buttons.append(draw_button)

while run:

    clock.tick(60)  # limiting FPS to 60 or any other value

    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # if user closed the program
            run = False

        out = False
        if pygame.mouse.get_pressed()[0]:


            pos = pygame.mouse.get_pos()

            for x in pos:
                if x < 0 or x>600:
                    out=True
                    break



            try:
                row, col = get_row_col_from_pos(pos)

                if (STATE == "COLOR" and free_draw == True):
                    paint_using_brush(row, col, BRUSH_SIZE)

                #Fill Colour In A shape if shape is selected and colour bucket is selected
                elif STATE == "FILL":
                    selector=False

                    for shape in Shape_storage:
                        click_left = int(pygame.mouse.get_pos()[0])
                        click_up = int(pygame.mouse.get_pos()[1])
                        flag2, shape2 = select_notpolygon(shape, click_left, click_up)
                        if flag2:
                            selected = True
                            selector=True
                            factory = ShapeFactory()
                            if shape2.rect is not None:
                                four_points = [(shape2.rect.left, shape2.rect.top),
                                               (shape2.rect.left, shape2.rect.top + shape2.rect.height),
                                               (shape2.rect.left + shape2.rect.width, shape2.rect.top),
                                               (shape2.rect.left + shape2.rect.width, shape2.rect.top + shape2.rect.height)
                                               ]

                                selected_rectangle = Shape
                                selected_shape = shape
                                selected_shape.thickness = 0
                                selected_shape.color = drawing_color


                                break
                    if selector ==False:
                        fill_bucket(row, col, drawing_color)




            except IndexError:
                #Change States Of Grid Based On Button Pressed
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    #Clear The Screen If Clear Button Pressed
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        draw_button.color = drawing_color
                        STATE = "COLOR"
                        break

                    #Set state to Fill if FillBucket button selected
                    if button.name == "FillBucket":
                        STATE = "FILL"
                        drawshape=False
                        break

                    #Unfill the selected shape if unfill button pressed
                    if button.name=="Unfill":
                        if selected_shape:
                            selected_shape.thickness=3;
                            selected_shape.Draw(WIN)
                            selected_shape = None
                            STATE="COLOR"
                            break

                    #Draw Square if Square Button Pressed
                    if button.name == "2":
                        shapename = "Square"
                        drawshape = True
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
                        free_draw = False
                        STATE="SHAPE"

                    # Draw Triangle if Triangle Button Pressed
                    if button.name == "3":

                        shapename = "Triangle"
                        drawshape = True
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
                        free_draw = False
                        STATE="SHAPE"

                    # Draw Rectangle if Rectangle Button Pressed
                    if button.name == "4":

                        shapename = "Rectangle"
                        drawshape = True
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
                        free_draw = False
                        STATE="SHAPE"

                    # Draw N Sided  Polygon if N sided Polygon Button Pressed
                    if ((button.name == "5") or (button.name == "6") or (button.name == "7") or (
                            button.name == "8") or (
                            button.name == "9") or
                            (button.name == "10") or (button.name == "11") or (button.name == "12") or (
                                    button.name == "13") or (button.name == "14") or
                            (button.name == "15") or (button.name == "16") or (button.name == "17") or (
                                    button.name == "18") or (button.name == "19") or
                            (button.name == "20")):

                        shapename = button.name + "gon"
                        drawshape = True
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
                        free_draw = False
                        STATE="SHAPE"
                        selected_shape=None
                        selected=False


                    #Draw Star if Star Button Pressed
                    if (button.name == "21"):

                        shapename = "Star"
                        drawshape = True
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
                        free_draw = False
                        STATE="SHAPE"

                    # Draw Diamonnd if Diamond Button Pressed
                    if (button.name == "22"):

                        shapename = "Diamond"
                        drawshape = True
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
                        free_draw = False
                        STATE="SHAPE"


                    #Change Toolbar buttons if change button pressed
                    if button.name == "Change":
                        Change = not Change
                        for i in range(10):
                            if i == 0:
                                buttons.append(Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                                                      button_height, WHITE, name="Change"))
                            else:
                                if Change == False:
                                    buttons.append(
                                        Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                                               button_height, WHITE, "B" + str(i - 1), BLACK))
                                if Change == True:
                                    buttons.append(
                                        Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                                               button_height, WHITE, "C" + str(i - 1), BLACK))
                        break

                    #Turn free draw Mode On If Brush Button Selected
                    if button.name == "Brush":
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        free_draw=True;
                        drawshape=False
                        STATE = "COLOR"
                        break

                    #Set Drawing Color According To Color Pallete
                    drawing_color = button.color
                    draw_button.color = drawing_color

                    break

                #Set Different Brush Sizes Based On Button Selected
                for button in brush_widths:
                    if not button.clicked(pos):
                        continue
                    # set brush width
                    if button.width == size_small:
                        BRUSH_SIZE = 1
                    elif button.width == size_medium:
                        BRUSH_SIZE = 2
                    elif button.width == size_large:
                        BRUSH_SIZE = 3

                    STATE = "COLOR"

        #Prevent the shape from moving out of grid
        if out: break

        #Check if edge points of a shape clicked
        if event.type == pygame.MOUSEBUTTONDOWN and selected_shape:
            click_left = int(pygame.mouse.get_pos()[0])
            click_up = int(pygame.mouse.get_pos()[1])
            if event.button == 1:
                for rec in selection_points:
                    if select_notpolygon2(rec,click_left,click_up)[0]:
                        if selection_points.index(rec)==0 or selection_points.index(rec)==1:
                            resize_left=True
                        select_resize=True
                        drawshape=False

        #Check if a shape selected
        if event.type == pygame.MOUSEBUTTONDOWN and selected_shape:
            click_left = int(pygame.mouse.get_pos()[0])
            click_up = int(pygame.mouse.get_pos()[1])

            if event.button == 1:
                if select_notpolygon(selected_shape,click_left,click_up)[0]:
                        select_selection2=True


        #If Edge Points of a shape are draggged then Resize Shape
        if event.type == pygame.MOUSEMOTION and select_resize==True:


            if event.buttons[0]:
                if resize_left:
                    selected_shape.changewidth(-1*event.rel[0])
                    selected_shape.changeheight(-1*event.rel[1])

                else:
                    selected_shape.changewidth(event.rel[0])
                    selected_shape.changeheight(event.rel[1])



                four_points = [(selected_shape.rect.left, selected_shape.rect.top),
                               (selected_shape.rect.left, selected_shape.rect.top + selected_shape.rect.height),
                               (selected_shape.rect.left + selected_shape.rect.width, selected_shape.rect.top),
                               (selected_shape.rect.left + selected_shape.rect.width,
                                selected_shape.rect.top + selected_shape.rect.height)
                               ]
                selection_points = draw_dashed_rectangle(WIN, four_points)
            break

        #If a shape is selected from inside and mouse moved upon clicking then drag the shape usin mmouse
        if event.type == pygame.MOUSEMOTION and select_selection2==True:


            if event.buttons[0]:
                pos = pygame.mouse.get_pos()
                if (not(selected_shape.width==1000)and selected_shape.check==0):
                    if(min(selected_shape.pivot_X,(selected_shape.pivot_X+selected_shape.width)) + event.rel[0]>0 and max(selected_shape.pivot_X,(selected_shape.pivot_X+selected_shape.width)) + event.rel[0]<600):
                        selected_shape.change_position_x(event.rel[0])
                    if(min(selected_shape.pivot_Y,(selected_shape.pivot_Y+selected_shape.height)) + event.rel[1]>0 and max(selected_shape.pivot_Y,(selected_shape.pivot_Y+selected_shape.height))+ event.rel[1]<600):
                        selected_shape.change_position_y(event.rel[1])
                else:
                    if(selected_shape.MinimumX()+ event.rel[0]>0 and selected_shape.MaximumX()+event.rel[0]<600):
                        selected_shape.change_position_x(event.rel[0])
                    if (selected_shape.MinimumY() + event.rel[1] > 0 and selected_shape.MaximumY() + event.rel[
                        1] < 600):
                        selected_shape.change_position_y(event.rel[1])

                four_points = [(selected_shape.rect.left, selected_shape.rect.top),
                               (selected_shape.rect.left, selected_shape.rect.top + selected_shape.rect.height),
                               (selected_shape.rect.left + selected_shape.rect.width, selected_shape.rect.top),
                               (selected_shape.rect.left + selected_shape.rect.width,
                                selected_shape.rect.top + selected_shape.rect.height)
                               ]
                selection_points = draw_dashed_rectangle(WIN, four_points)


        #Draw selection Rectangle over the newly dragged or resized shape
        if event.type ==pygame.MOUSEBUTTONUP and (select_resize or select_selection2):
            if selected_shape is not None:
                four_points = [(selected_shape.rect.left, selected_shape.rect.top),
                           (selected_shape.rect.left, selected_shape.rect.top + selected_shape.rect.height),
                           (selected_shape.rect.left + selected_shape.rect.width, selected_shape.rect.top),
                           (selected_shape.rect.left + selected_shape.rect.width, selected_shape.rect.top + selected_shape.rect.height)
                           ]
            select_selection2=False
            select_resize=False
            if STATE !="FILL":


                drawshape=True






        #If shape selected and slider value changed then change thickness of shape
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1:
                click_left = int(pygame.mouse.get_pos()[0])
                click_up = int(pygame.mouse.get_pos()[1])
                selector=False

                for shape in Shape_storage:
                    flag2, shape2 =select_notpolygon(shape,click_left,click_up)
                    if flag2:
                        selected = True
                        factory = ShapeFactory()

                        four_points=[(shape2.rect.left,shape2.rect.top),
                                     (shape2.rect.left, shape2.rect.top + shape2.rect.height),
                                     (shape2.rect.left+shape2.rect.width,shape2.rect.top),
                                     (shape2.rect.left + shape2.rect.width, shape2.rect.top+ shape2.rect.height)
                                     ]
                        selected_rectangle = Shape
                        selected_shape = shape
                        slider.setValue(selected_shape.thickness)
                        slider_thickness=True

                        selector=True

                        break
                if selector:
                        continue
                drawn = True
        # if no shape seleted and shape drawing turned on then draw a new shape using mouse,drawing color and slider thickness

        if event.type == pygame.MOUSEBUTTONDOWN and drawshape==True:
            if event.button == 1:
                # If drawn with shift pressed and shape is triangle, draw a symmetric triangle
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    if(shapename=="Triangle"):
                        shapename="STriangle"

                factory = ShapeFactory()
                selected_shape=None
                slider.setValue(3)
                if drawing_color==(255,255,255):
                    drawing_color = (0, 0, 0)
                    draw_button.color = (0, 0, 0)

                Shape = factory.Create(shapename, drawing_color)
                Shape_storage.append(Shape)



                drawn = True


        elif event.type == pygame.KEYDOWN:
            # Copy the selected shape if CTRL + C is pressed
            if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    counter=1
                    copied_shape = copy.deepcopy(selected_shape)


                    print("pressed CTRL-C as an event")
            #Paste the copied shape if CTRL + V is pressed
            elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    # paste=copied_shape
                    # paste.rect=copied_shape.rect.move(100, 100)
                    if(copied_shape):
                        paste = copy.deepcopy(copied_shape)
                        paste.change_position_x(30*counter)
                        counter=counter+1
                        Shape_storage.append(paste)

        #Draw The Shape On Grid
        elif event.type == pygame.MOUSEMOTION and drawshape==True:
            for shape in Shape_storage:
                if shape.selected == True:
                    if event.buttons[0]:
                        shape.changewidth(event.rel[0])
                        shape.changeheight(event.rel[1])

       #Draw Selection Rectangle Around the shape after shape is drawn
        elif event.type == pygame.MOUSEBUTTONUP and drawshape==True:
            if(shapename=="STriangle"): shapename="Triangle"
            for shape in Shape_storage:
                if(shape.selected == True):
                    selected = True
                    factory = ShapeFactory()

                    selected_rectangle = Shape
                    selected_shape = shape
                    shape.selected=False
                    if shape.rect:
                        four_points = [(shape.rect.left, shape.rect.top),
                                   (shape.rect.left, shape.rect.top + shape.rect.height),
                                   (shape.rect.left + shape.rect.width, shape.rect.top),
                                   (shape.rect.left + shape.rect.width, shape.rect.top + shape.rect.height)
                                   ]
            for shape in Shape_storage:
                shape.selected=False

            pygame.display.flip()

    #DRaw the grid
    draw(WIN, grid, buttons)

pygame.quit()
