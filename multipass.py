import random
import pygame

N_ITEMS_PER_PAGE = 2
WAITING_TIME = 1000

WIDTH = 1200
HEIGHT = 800
RECT_WIDTH = 60
RECT_HEIGHT = 35
CONTOUR_WIDTH = 90
CONTOUR_HEIGHT = 60
FONT_SIZE = 30

BLACK = 0, 0, 0
LIGHT_BLUE = 51, 153, 255
GREEN = 0, 255, 0
ORANGE = 255, 153, 51
GREY = 160, 160, 160
colors = [(255, 153, 153), (153, 153, 255), (255, 255, 153), (255, 153, 255), (153, 255, 255),
          (153, 204, 255), (255, 204, 153), (204, 153, 255), (153, 255, 204), (255, 153, 204)]


def display_titles(title_inp, title_buffer, title_out):
    font = pygame.font.Font(None, 50)

    text_surface = font.render(title_inp, True, (255, 255, 255))
    input_x = 60
    input_y = 60
    win.blit(text_surface, (input_x, input_y))

    text_surface = font.render(title_buffer, True, (255, 255, 255))
    buffer_x = WIDTH // 2 - text_surface.get_size()[0] // 2
    buffer_y = 60
    win.blit(text_surface, (buffer_x, buffer_y))

    text_surface = font.render(title_out, True, (255, 255, 255))
    output_x = (WIDTH // 2) + (CONTOUR_WIDTH // 2) + 100
    output_y = 60
    win.blit(text_surface, (output_x, output_y))


def display_run(run, pos, color, coord_x, coord_y):
    if len(run) == 0:
        return
    for i in range(len(run)):
        if i >= pos:
            col = color
        else:
            col = GREY
        rect_x = coord_x
        rect_y = coord_y + (RECT_HEIGHT + 3) * i
        if rect_y >= HEIGHT - RECT_HEIGHT:
            coord_x = coord_x + RECT_WIDTH + 10
            coord_y = - (RECT_HEIGHT + 3) * i + 100
            rect_x = coord_x
            rect_y = coord_y + (RECT_HEIGHT + 3) * i
        pygame.draw.rect(win, col, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
        text = ",".join(str(x) for x in run[i])
        font = pygame.font.Font(None, FONT_SIZE)
        text_surface = font.render(text, True, BLACK)
        text_width, text_height = text_surface.get_size()
        win.blit(text_surface, (rect_x + (RECT_WIDTH - text_width) // 2, rect_y + (RECT_HEIGHT - text_height) // 2))
    return rect_x, rect_y


def display_input(runs, positions):
    coord_x = 60
    coord_y = 150
    for k in range(len(runs)):
        coord_x, rect_y = display_run(runs[k], positions[k], colors[k], coord_x, coord_y)
        #if len(runs) <= CONTOUR_WIDTH - 60
        if rect_y + RECT_HEIGHT + 3 >= HEIGHT - RECT_HEIGHT:
            coord_y = 150
        else:
            coord_y = rect_y + RECT_HEIGHT + 50


def display_output(runs):
    if len(runs) == 0:
        return
    coord_x = (WIDTH // 2) + (CONTOUR_WIDTH // 2) + 100
    coord_y = 150
    for k in range(len(runs)):
        coord_x, rect_y = display_run(runs[k], 0, GREEN, coord_x, coord_y)
        if rect_y + RECT_HEIGHT + 3 >= HEIGHT - RECT_HEIGHT:
            coord_y = 150
        else:
            coord_y = rect_y + RECT_HEIGHT + 50


def display_buffer(contents, colors):
    coord_x = (WIDTH // 2) - (CONTOUR_WIDTH // 2)
    coord_y = 150
    for i in range(BUFFER_FRAMES):
        rect_x = coord_x
        rect_y = coord_y + (CONTOUR_HEIGHT + 40) * i
        pygame.draw.rect(win, LIGHT_BLUE, (rect_x, rect_y, CONTOUR_WIDTH, CONTOUR_HEIGHT), 5)
    j = 0
    for cont, col in zip(contents, colors):
        rect_x = coord_x + (CONTOUR_WIDTH - RECT_WIDTH) // 2
        rect_y = coord_y + (CONTOUR_HEIGHT + 40) * j + (CONTOUR_HEIGHT - RECT_HEIGHT) // 2
        pygame.draw.rect(win, col, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
        text = ",".join(str(x) for x in cont)
        font = pygame.font.Font(None, FONT_SIZE)
        text_surface = font.render(text, True, BLACK)
        text_width, text_height = text_surface.get_size()
        win.blit(text_surface, (rect_x + (RECT_WIDTH - text_width) // 2, rect_y + (RECT_HEIGHT - text_height) // 2))
        j += 1
    if j != BUFFER_FRAMES - 1:
        for k in range(j, BUFFER_FRAMES):
            rect_x = coord_x + (CONTOUR_WIDTH - RECT_WIDTH) // 2
            rect_y = coord_y + (CONTOUR_HEIGHT + 40) * k + (CONTOUR_HEIGHT - RECT_HEIGHT) // 2
            pygame.draw.rect(win, BLACK, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))


#transorms a list into a list of pages
def list_2_pages(list):
    return [list[j:j+N_ITEMS_PER_PAGE] for j in range(0, len(list), N_ITEMS_PER_PAGE)]


#returns all the subruns in output of the sort pass
def pass0(input):
    output = []
    for i in range(0, N_PAGES // N_ITEMS_PER_PAGE, BUFFER_FRAMES):
        run = [x for page in input[i:min(i+BUFFER_FRAMES, len(input))] for x in page]
        run.sort()
        output.append(list_2_pages(run))
    return output


#def set_finished_runs(inp, n, p, ):


#ask the user for the size of the relation and the number of buffer frames
print("Hi! This is an application for the visualization of the external multipass sorting algorithm.")
print("I'm going to ask you for further details regarding the sizes. Note that in one page there is space for two items.")
N_PAGES = int(input("Please tell me how many values the input file contains: "))
BUFFER_FRAMES = int(input("Please tell me how many frames the buffer has: "))
F = BUFFER_FRAMES - 1

#initialize the visualization with pygame
pygame.init()
# setting window size
win = pygame.display.set_mode((WIDTH, HEIGHT))
# setting title to the window
pygame.display.set_caption("Multipass external sorting")
pygame.time.delay(10)
win.fill(BLACK)

#generate random numbers
inp = [random.randint(0, 50) for _ in range(N_PAGES)]
inp = list_2_pages(inp)

#chech dimensions


run = True
pazz = 0
while run:
    execute = False
    # time delay
    pygame.time.delay(10)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        #stop the application
        if event.type == pygame.QUIT:
            run = False

    #start execution
    if keys[pygame.K_SPACE]:
        execute = True

    if execute == False:
        # fill the window with black color
        win.fill((0, 0, 0))

        display_titles("INPUT", "BUFFER", f"OUTPUT - pass {pazz}")
        if pazz == 0:
            display_input([inp], [0])
        else:
            display_input(inp, [0]*len(inp))
        display_buffer([], [])

        pygame.display.update()
    else:
        # SORT PASS
        if pazz == 0:
            sorted_runs = pass0(inp)
            l = len(sorted_runs)
            out = []
            for i in range(l):
                #copy in the buffer
                display_titles("INPUT", "BUFFER", f"OUTPUT - pass {pazz}")
                display_input([inp], [(i+1) * BUFFER_FRAMES])
                display_buffer(inp[i*BUFFER_FRAMES : min((i+1)*BUFFER_FRAMES, len(inp))], [colors[0]]*BUFFER_FRAMES)
                pygame.display.update()
                pygame.time.delay(WAITING_TIME)
                #write sorted run
                out.append(sorted_runs[i])
                display_titles("INPUT", "BUFFER", f"OUTPUT - pass {pazz}")
                display_input([inp], [(i+1) * BUFFER_FRAMES])
                display_buffer([], [])
                display_output(out)
                pygame.display.update()
                pygame.time.delay(WAITING_TIME)
            inp = sorted_runs
        #MERGE PASS
        else:
            inp_copy = inp.copy()
            out = []
            p = [0] * len(inp)
            for i in range(0, len(inp), F):
                e = min(len(inp), i + F)
                run = []    #construct the actual run
                act = [x[0] for x in inp[i:e]]  #what is inside the buffer
                n = [N_ITEMS_PER_PAGE] * (e - i)   #how many values there are in each of the buffer frames
                out_frame = []
                for k in range(e-i):
                    p[i+k] = 1
                cols = colors[i:e] + [GREEN]
                z = 0
                while True:
                    #if the frame is full, send it to the output
                    if len(out_frame) == N_ITEMS_PER_PAGE:
                        if z == 0:
                            run.append([out_frame])
                            z += 1
                        else:
                            run[0].append(out_frame)
                        out_frame = []

                    display_titles("INPUT", "BUFFER", f"OUTPUT - pass {pazz}")
                    display_input(inp_copy, p)
                    display_buffer(act + [out_frame], cols)
                    display_output(out + run)
                    pygame.display.update()
                    pygame.time.delay(WAITING_TIME)

                    #check how many subruns have finished
                    finished = []
                    for j in range(i, e):
                        if p[j] == len(inp[j]) + 1:
                            finished.append(j - i)
                            act[j - i] = [10000]
                            n[j - i] = 1
                            cols[j-i] = BLACK
                    #if everyone has finished, break the while
                    if len(finished) == e - i:
                        break
                    #see if there are runs that need to load a new page
                    try:
                        renew = n.index(0)
                        #if the actual page is the last of the run, this subrun has finished
                        if p[i + renew] == len(inp[i + renew]):
                            finished.append(renew)
                            p[i+renew] += 1
                            act[renew] = [10000]
                            n[renew] = 1
                            cols[renew] = BLACK
                            if len(finished) == e - i:
                                break
                        #otherwise load next page
                        else:
                            act[renew] = inp[i + renew][p[i + renew]]
                            p[i + renew] += 1
                            n[renew] = len(act[renew])
                        #display loading of new page
                        display_titles("INPUT", "BUFFER", f"OUTPUT - pass {pazz}")
                        display_input(inp_copy, p)
                        display_buffer(act + [out_frame], cols)
                        display_output(out + run)
                        pygame.display.update()
                        pygame.time.delay(WAITING_TIME)
                    except ValueError:
                        pass
                    #find minimum value
                    listt = [x[0] for x in act]
                    minn = min(listt)
                    index_min = listt.index(minn)
                    act[index_min].remove(minn)
                    out_frame.append(minn)
                    n[index_min] -= 1

                    #display step
                    display_titles("INPUT", "BUFFER", f"OUTPUT - pass {pazz}")
                    display_input(inp_copy, p)
                    display_buffer(act + [out_frame], cols)
                    display_output(out + run)
                    pygame.display.update()
                    pygame.time.delay(WAITING_TIME)

                out += run
            inp = out
        if len(inp) == 1:
            text = f"SORTED! It took {pazz + 1} passes"
            font = pygame.font.Font(None, 60)
            text_surface = font.render(text, True, (255,0,0))
            text_width, text_height = text_surface.get_size()
            win.blit(text_surface, ((WIDTH - text_width) // 2, (HEIGHT - text_height) // 2))
            pygame.display.update()
            pygame.time.delay(8000)
            run = False
        pygame.event.clear()
        pazz += 1


    # exiting the main window
pygame.quit()
