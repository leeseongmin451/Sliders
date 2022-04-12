import pygame
import random
# import time

# START GAME AND INITIAL SETTING #

pygame.init()

# DEFINING COLORS#

BLACK = (0, 0, 0)
WHITE1 = (255, 255, 255)
WHITE2 = (127, 127, 127)
WHITE3 = (63, 63, 63)
RED1 = (255, 63, 63)
RED2 = (127, 31, 31)
RED3 = (63, 15, 15)
GREEN1 = (0, 255, 0)
GREEN2 = (0, 127, 0)
GREEN3 = (0, 63, 0)
BLUE1 = (63, 191, 255)
BLUE2 = (31, 95, 127)
BLUE3 = (15, 47, 63)
CYAN1 = (0, 255, 255)
CYAN2 = (0, 127, 127)
CYAN3 = (0, 63, 63)
MAGENTA1 = (255, 0, 255)
MAGENTA2 = (127, 0, 127)
MAGENTA3 = (63, 0, 63)
YELLOW1 = (255, 255, 0)
YELLOW2 = (127, 127, 0)
YELLOW3 = (63, 63, 0)
ORANGE1 = (255, 102, 0)
ORANGE2 = (127, 51, 0)
ORANGE3 = (63, 25, 0)
PURPLE1 = (191, 95, 255)
PURPLE2 = (95, 47, 127)
PURPLE3 = (47, 23, 63)

gamefield_size = 1000

screen_width = gamefield_size + 300
screen_height = gamefield_size
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Slider")


def draw_text(surf, text, size, color, pos, x, y):
    """
    draw text at a specified position
    :param surf: surface on which text will be drawn(screen)
    :param text: text to be drawn
    :param size: font size
    :param color: text color
    :param pos: a fixed point of text defined by [x, y]
    :param x: x position
    :param y: y position
    :return: None
    """
    font = pygame.font.Font(text_font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if pos == "topleft":
        text_rect.x = x
        text_rect.y = y
    elif pos == "midtop":
        text_rect.midtop = (x, y)
    elif pos == "topright":
        text_rect.topright = (x, y)
    elif pos == "center":
        text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)


done = False
click = False
clock = pygame.time.Clock()
fps = 60

num_font = pygame.font.SysFont("verdana", 20)
text_font = pygame.font.match_font("verdana")

curspos = (0, 0)

# grid
grid_size = 10

cell_wall_ratio = 5
cell_size = cell_wall_ratio * gamefield_size / ((cell_wall_ratio + 1) * grid_size + 1)

cells = []

wall_color = WHITE1
wall_thickness = gamefield_size / ((cell_wall_ratio + 1) * grid_size + 1)

walls_horizontal = []
walls_vertical = []
wall_density = 10       # at percentage

block_size = cell_size + wall_thickness

player_number = 0


class Button:
    def __init__(self, fixpoint, btn_pos_size, btn_color, text, text_size, btnbck_color=(0, 0, 0), active=True):
        self.btn_color = btn_color
        self.btnbck_color_orig = btnbck_color
        self.btnbck_color = btnbck_color
        self.mouse_on_color = []
        self.clicked_color = []
        self.rect = btn_pos_size
        if fixpoint == "topleft":
            pass
        if fixpoint == "midtop":
            self.rect[0] -= self.rect[2] // 2
        if fixpoint == "topright":
            self.rect[0] -= self.rect[2]
        if fixpoint == "left":
            self.rect[1] -= self.rect[3] // 2
        if fixpoint == "center":
            self.rect[0] -= self.rect[2] // 2
            self.rect[1] -= self.rect[3] // 2
        if fixpoint == "right":
            self.rect[0] -= self.rect[2]
            self.rect[1] -= self.rect[3] // 2
        if fixpoint == "bottomleft":
            self.rect[1] -= self.rect[3]
        if fixpoint == "midbottom":
            self.rect[0] -= self.rect[2] // 2
            self.rect[1] -= self.rect[3]
        if fixpoint == "bottomright":
            self.rect[0] -= self.rect[2]
            self.rect[1] -= self.rect[3]
        self.text = text
        self.text_size = text_size
        self.active = active
        self.pressed = False
        self.released = False
        self.operate = False
        for ind in range(3):
            self.mouse_on_color.append((self.btn_color[ind] + self.btnbck_color[ind]) // 2)
            self.clicked_color.append((self.mouse_on_color[ind] + self.btnbck_color[ind]) // 2)
        pygame.draw.rect(screen, self.btnbck_color, self.rect, 0)
        pygame.draw.rect(screen, self.btn_color, self.rect, 2)
        draw_text(screen, self.text, self.text_size, self.btn_color, "center", self.rect[0] + self.rect[2] // 2, self.rect[1] + self.rect[3] // 2)

    def update(self):
        if self.active:
            if pygame.Rect(self.rect).collidepoint(curspos[0], curspos[1]):
                self.btnbck_color = self.mouse_on_color
                if click:
                    self.pressed = True
                if self.pressed:
                    self.btnbck_color = self.clicked_color
                    if not click:
                        self.released = True
                        self.pressed = False
                        self.btnbck_color = self.mouse_on_color
                elif self.released:
                    self.operate = True
                    self.released = False
            else:
                self.btnbck_color = self.btnbck_color_orig
                self.pressed = False
                self.released = False
                self.operate = False
            pygame.draw.rect(screen, self.btnbck_color, self.rect, 0)
            pygame.draw.rect(screen, self.btn_color, self.rect, 2)
            draw_text(screen, self.text, self.text_size, self.btn_color, "center", self.rect[0] + self.rect[2] // 2, self.rect[1] + self.rect[3] // 2)
        else:
            pygame.draw.rect(screen, self.btnbck_color, self.rect, 0)
            pygame.draw.rect(screen, self.clicked_color, self.rect, 2)
            draw_text(screen, self.text, self.text_size, self.clicked_color, "center", self.rect[0] + self.rect[2] // 2, self.rect[1] + self.rect[3] // 2)
            self.btnbck_color = self.btnbck_color_orig
            self.pressed = False
            self.released = False
            self.operate = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False


class Player:
    def __init__(self, start_pos, color_set, move_keys):
        global player_number
        player_number += 1
        self.number = player_number
        self.xpos = start_pos[0]
        self.ypos = start_pos[1]
        self.score = 1
        self.color1, self.color2 = color_set
        self.up = move_keys[0]
        self.down = move_keys[1]
        self.left = move_keys[2]
        self.right = move_keys[3]
        cells[self.xpos][self.ypos] = self.number

        self.moveable = True
        self.move_ready = False
        self.moving = False
        self.move_direction = None
        self.key_pressed = False

        all_players[self.number] = self
        all_player_colors[self.number] = self.color1
        all_cell_colors[self.number] = self.color2

    def update(self):
        if self.moveable:
            keystate = pygame.key.get_pressed()
            if keystate[self.up] and not any(
                    [keystate[self.down], keystate[self.left], keystate[self.right]]):
                self.key_pressed = True
                self.move_direction = "up"
            if keystate[self.down] and not any(
                    [keystate[self.up], keystate[self.left], keystate[self.right]]):
                self.key_pressed = True
                self.move_direction = "down"
            if keystate[self.left] and not any(
                    [keystate[self.up], keystate[self.down], keystate[self.right]]):
                self.key_pressed = True
                self.move_direction = "left"
            if keystate[self.right] and not any(
                    [keystate[self.up], keystate[self.down], keystate[self.left]]):
                self.key_pressed = True
                self.move_direction = "right"

            if self.key_pressed:
                self.move_ready = True
            if self.move_ready:
                if not any([keystate[self.up], keystate[self.down], keystate[self.left], keystate[self.right]]):
                    self.key_pressed = False
                    self.moving = True
                    self.moveable = False
                    self.move_ready = False

        if self.moving:
            if self.move_direction == "up":
                if self.ypos != 0 and not walls_horizontal[self.xpos][self.ypos - 1] and not any([self.xpos == other.xpos and self.ypos == other.ypos + 1 for other in all_players.values()]):
                    self.ypos -= 1
                    current_cell_value = cells[self.xpos][self.ypos]
                    if current_cell_value != self.number:
                        if current_cell_value != 0:
                            all_players[current_cell_value].score -= 1
                        self.score += 1
                    cells[self.xpos][self.ypos] = self.number
                else:
                    self.moving = False
                    self.moveable = True
            if self.move_direction == "down":
                if self.ypos != grid_size - 1 and not walls_horizontal[self.xpos][self.ypos] and not any([self.xpos == other.xpos and self.ypos == other.ypos - 1 for other in all_players.values()]):
                    self.ypos += 1
                    current_cell_value = cells[self.xpos][self.ypos]
                    if current_cell_value != self.number:
                        if current_cell_value != 0:
                            all_players[current_cell_value].score -= 1
                        self.score += 1
                    cells[self.xpos][self.ypos] = self.number
                else:
                    self.moving = False
                    self.moveable = True
            if self.move_direction == "left":
                if self.xpos != 0 and not walls_vertical[self.xpos - 1][self.ypos] and not any([self.ypos == other.ypos and self.xpos == other.xpos + 1 for other in all_players.values()]):
                    self.xpos -= 1
                    current_cell_value = cells[self.xpos][self.ypos]
                    if current_cell_value != self.number:
                        if current_cell_value != 0:
                            all_players[current_cell_value].score -= 1
                        self.score += 1
                    cells[self.xpos][self.ypos] = self.number
                else:
                    self.moving = False
                    self.moveable = True
            if self.move_direction == "right":
                if self.xpos != grid_size - 1 and not walls_vertical[self.xpos][self.ypos] and not any([self.ypos == other.ypos and self.xpos == other.xpos - 1 for other in all_players.values()]):
                    self.xpos += 1
                    current_cell_value = cells[self.xpos][self.ypos]
                    if current_cell_value != self.number:
                        if current_cell_value != 0:
                            all_players[current_cell_value].score -= 1
                        self.score += 1
                    cells[self.xpos][self.ypos] = self.number
                else:
                    self.moving = False
                    self.moveable = True

    def draw_self(self):
        pygame.draw.rect(screen, self.color1,
                         [round(wall_thickness + self.xpos * block_size), wall_thickness + self.ypos * block_size,
                          cell_size, cell_size])

    def display_score(self):
        draw_text(screen, "PLAYER {} SCORE : {}".format(self.number, self.score), 20, self.color1, "topleft", 1050, 50 * self.number)


def rearrange():
    global walls_horizontal, walls_vertical
    walls_horizontal = []
    for n in range(grid_size):
        walls_horizontal += [[False] * (grid_size - 1)]

    walls_vertical = []
    for n in range(grid_size - 1):
        walls_vertical += [[False] * grid_size]

    for n in range(grid_size):
        for m in range(grid_size - 1):
            if random.random() < wall_density / 100:
                walls_horizontal[n][m] = True
    for n in range(grid_size - 1):
        for m in range(grid_size):
            if random.random() < wall_density / 100:
                walls_vertical[n][m] = True


mainmenu_show = True
start_button = Button("midbottom", [screen_width // 2, screen_height - 350, 400, 100], WHITE1, "START", 60)
settings_button = Button("midbottom", [screen_width // 2, screen_height - 200, 400, 100], WHITE1, "SETTINGS", 60)
number_of_players = 2
settings_show = False
number_of_players_inc_button = Button("topright", [screen_width - 350, 175, 100, 50], WHITE1, "+ 1", 30, (0, 0, 0), False)
number_of_players_dec_button = Button("topright", [screen_width - 350, 225, 100, 50], WHITE1, "- 1", 30, (0, 0, 0), False)
grid_size_inc_button = Button("topright", [screen_width - 350, 325, 100, 50], WHITE1, "+ 1", 30, (0, 0, 0), False)
grid_size_dec_button = Button("topright", [screen_width - 350, 375, 100, 50], WHITE1, "- 1", 30, (0, 0, 0), False)
wall_density_inc_button = Button("topright", [screen_width - 350, 475, 100, 50], WHITE1, "+ 1", 30, (0, 0, 0), False)
wall_density_dec_button = Button("topright", [screen_width - 350, 525, 100, 50], WHITE1, "- 1", 30, (0, 0, 0), False)
back_button = Button("midbottom", [screen_width // 2, screen_height - 100, 300, 75], WHITE1, "MAINMENU", 45)
play = False
rearrange_button = Button("bottomright", [screen_width - 50, screen_height - 150, 200, 70], WHITE1, "REARRANGE", 25)
quit_button = Button("bottomright", [screen_width - 50, screen_height - 50, 200, 70], WHITE1, "QUIT GAME", 25)


all_players = {}
all_player_colors = {}
all_cell_colors = {}


# MAIN GAME LOOP #

while not done:
    #clock.tick_busy_loop(fps)
    clock.tick(fps)

    # EVENT CHECK#

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            click = False
        elif event.type == pygame.QUIT:
            done = True

    # get mouse position on screen
    curspos = pygame.mouse.get_pos()

    screen.fill(BLACK)

    if mainmenu_show:
        draw_text(screen, "SLIDERS", 70, WHITE1, "midtop", screen_width // 2, 50)
        start_button.update()
        settings_button.update()

        if start_button.operate:
            cells = []
            for i in range(grid_size):
                cell_size = cell_wall_ratio * gamefield_size / ((cell_wall_ratio + 1) * grid_size + 1)
                cells += [[0] * grid_size]
            wall_thickness = gamefield_size / ((cell_wall_ratio + 1) * grid_size + 1)
            block_size = cell_size + wall_thickness

            rearrange()

            player1 = Player([0, 0], [BLUE1, BLUE2], [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
            player2 = Player([grid_size - 1, grid_size - 1], [RED1, RED2],
                             [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
            if number_of_players >= 3:
                player3 = Player([grid_size - 1, 0], [GREEN1, GREEN2],
                                 [pygame.K_KP8, pygame.K_KP5, pygame.K_KP4, pygame.K_KP6])
            if number_of_players >= 4:
                player4 = Player([0, grid_size - 1], [YELLOW1, YELLOW2],
                                 [pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l])

            mainmenu_show = False
            play = True
            start_button.operate = False

        if settings_button.operate:
            mainmenu_show = False
            settings_show = True
            settings_button.operate = False

    elif settings_show:
        draw_text(screen, "SETTINGS", 50, WHITE1, "midtop", screen_width // 2, 60)
        draw_text(screen, "NUMBER OF PLAYERS : {}".format(number_of_players), 30, WHITE1, "topleft", 350, 200)
        draw_text(screen, "GRID SIZE : {} x {}".format(grid_size, grid_size), 30, WHITE1, "topleft", 350, 350)
        draw_text(screen, "WALL DENSITY : {}%".format(wall_density), 30, WHITE1, "topleft", 350, 500)
        draw_text(screen, "BLUE : WSAD", 30, BLUE1, "topleft", 350, 580)
        draw_text(screen, "RED : Arrow keys", 30, RED1, "topleft", 350, 620)
        draw_text(screen, "GREEN : Numpad 8546", 30, GREEN1, "topleft", 350, 660)
        draw_text(screen, "YELLOW : IKJL", 30, YELLOW1, "topleft", 350, 700)
        if number_of_players <= 2:
            number_of_players_dec_button.deactivate()
        else:
            number_of_players_dec_button.activate()
        if number_of_players >= 4:
            number_of_players_inc_button.deactivate()
        else:
            number_of_players_inc_button.activate()

        if grid_size <= 5:
            grid_size_dec_button.deactivate()
        else:
            grid_size_dec_button.activate()
        if grid_size >= 40:
            grid_size_inc_button.deactivate()
        else:
            grid_size_inc_button.activate()

        if wall_density <= 5:
            wall_density_dec_button.deactivate()
        else:
            wall_density_dec_button.activate()
        if wall_density >= 15:
            wall_density_inc_button.deactivate()
        else:
            wall_density_inc_button.activate()

        number_of_players_inc_button.update()
        number_of_players_dec_button.update()
        grid_size_inc_button.update()
        grid_size_dec_button.update()
        wall_density_inc_button.update()
        wall_density_dec_button.update()
        back_button.update()

        if number_of_players_inc_button.operate:
            number_of_players += 1
            number_of_players_inc_button.operate = False

        if number_of_players_dec_button.operate:
            number_of_players -= 1
            number_of_players_dec_button.operate = False

        if grid_size_inc_button.operate:
            grid_size += 1
            grid_size_inc_button.operate = False

        if grid_size_dec_button.operate:
            grid_size -= 1
            grid_size_dec_button.operate = False

        if wall_density_inc_button.operate:
            wall_density += 1
            wall_density_inc_button.operate = False

        if wall_density_dec_button.operate:
            wall_density -= 1
            wall_density_dec_button.operate = False

        if back_button.operate:
            settings_show = False
            mainmenu_show = True
            back_button.operate = False

    elif play:
        for player in all_players.values():
            player.update()

        curspos = pygame.mouse.get_pos()

        ##########################################3

        # draw grid lines
        for i in range(grid_size - 1):
            pygame.draw.line(screen, WHITE3, [wall_thickness / 2 + block_size * (i + 1), 0], [wall_thickness / 2 + block_size * (i + 1), gamefield_size])
        for i in range(grid_size - 1):
            pygame.draw.line(screen, WHITE3, [0, wall_thickness / 2 + block_size * (i + 1)], [gamefield_size, wall_thickness / 2 + block_size * (i + 1)])

        # draw cells
        for i in range(grid_size):
            for j in range(grid_size):
                if cells[i][j]:
                    pygame.draw.rect(screen, all_cell_colors[cells[i][j]], [round(2 * wall_thickness + i * block_size), 2 * wall_thickness + j * block_size, cell_size - 2 * wall_thickness, cell_size - 2 * wall_thickness])

        # draw players
        for player in all_players.values():
            player.draw_self()

        # draw horizontal walls
        for i in range(grid_size):
            for j in range(grid_size - 1):
                if walls_horizontal[i][j]:
                    pygame.draw.rect(screen, wall_color, [round(i * block_size), (j + 1) * block_size, block_size + wall_thickness, wall_thickness])

        # draw_vertical_walls
        for i in range(grid_size - 1):
            for j in range(grid_size):
                if walls_vertical[i][j]:
                    pygame.draw.rect(screen, wall_color, [round((i + 1) * block_size), j * block_size, wall_thickness, block_size + wall_thickness])

        # draw edge wall
        pygame.draw.rect(screen, wall_color, [0, 0, gamefield_size, gamefield_size], round(wall_thickness))

        # draw score text
        for player in all_players.values():
            player.display_score()

        # rearrange button
        rearrange_button.update()
        if rearrange_button.operate:
            rearrange()
            rearrange_button.operate = False

        # quit button
        quit_button.update()
        if quit_button.operate:
            player_number = 0
            all_players = {}
            all_player_colors = {}
            all_cell_colors = {}
            play = False
            mainmenu_show = True
            quit_button.operate = False

    pygame.display.flip()

pygame.quit()
exit()
