import pygame
import pygame_gui

# import game_events as ge
import text_assets as assets

# pygame
pygame.init()

# RGB values of certain colours for quick matching.
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

# assigning values to X and Y variable for quick screen sizing
X = 1000
Y = 600

pygame.display.set_caption("Hangman - the dictionaries strike back")
window_surface = pygame.display.set_mode((X, Y))

manager = pygame_gui.UIManager((X, Y))

background = pygame.Surface((X, Y))
background.fill(pygame.Color("#1E2633"))

# font = pygame.font.Font('monospace', 15)

#  textbox
# text_box = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((350, 275), (100, 50)),
#                                         text="1",
#                                         manager=manager)

text_box_size = (900, 400)  # Set the size of the text box
text_box_position = (50, 50)  # Set the position of the text box

text_box = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(text_box_position, text_box_size),
                                         html_text="story",
                                         manager=manager,
                                         anchors={'left': 'left',
                                                  'top': 'top'})
text_content = assets.hangman_art
# first content of screen

text_box.set_text(text_content)
# command used to write on text_box

# text line input window

textline = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(200, 475, 600, 50),
                                               manager=manager,
                                               placeholder_text="<Enter your word or your guess letter here>")
# size of buttons
button_layout_rect = pygame.Rect(10, 10, 100, 50)

# respected distance to corners
button_layout_rect.bottomright = (0, 0)
# button_layout_rect.bottomleft = (50, -20)
# button_layout_rect.topleft = (30, -20)
# button_layout_rect.topright = (-30, -20)

push_quit_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                text='QUIT', manager=manager,
                                                anchors={"bottom": "bottom",
                                                         "right": "right"})

push_enter_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                 text="ENTER",
                                                 manager=manager,
                                                 anchors={"bottom": "bottom",
                                                          "right": "right",
                                                          "right_target": push_quit_button})

push_8_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text="8",
                                             manager=manager,
                                             anchors={"bottom": "bottom",
                                                      "right": "right",
                                                      "right_target": push_enter_button})

push_7_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text="7",
                                             manager=manager,
                                             anchors={"bottom": "bottom",
                                                      "right": "right",
                                                      "right_target": push_8_button})

push_6_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text="6",
                                             manager=manager,
                                             anchors={"bottom": "bottom",
                                                      "right": "right",
                                                      "right_target": push_7_button})

push_5_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text="5",
                                             manager=manager,
                                             anchors={"bottom": "bottom",
                                                      "right": "right",
                                                      "right_target": push_6_button})

push_4_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text="4",
                                             manager=manager,
                                             anchors={"bottom": "bottom",
                                                      "right": "right",
                                                      "right_target": push_5_button})

push_3_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text="3",
                                             manager=manager,
                                             anchors={"bottom": "bottom",
                                                      "right": "right",
                                                      "right_target": push_4_button})

push_2_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text="2",
                                             manager=manager,
                                             anchors={"bottom": "bottom",
                                                      "right": "right",
                                                      "right_target": push_3_button})

push_1_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text="1",
                                             manager=manager,
                                             anchors={"bottom": "bottom",
                                                      "right": "right",
                                                      "right_target": push_2_button})

clock = pygame.time.Clock()

# Game-loop
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # if event.type == pygame_gui.UI_TEXt_ENTRY_FINISHED:
        #    event.ui_object_id == "#textline":

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            #    if event.ui_element == push_1_button:
            #    if event.ui_element == push_2_button:
            #    if event.ui_element == push_3_button:
            #    if event.ui_element == push_4_button:
            #    if event.ui_element == push_5_button:
            #    if event.ui_element == push_6_button:
            #    if event.ui_element == push_7_button:
            #    if event.ui_element == push_8_button:
            #    if event.ui_element == push_enter_button:
            if event.ui_element == push_quit_button:
                event = pygame.QUIT

        pygame.display.update()

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.fill(black)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

# pygame.quit()
