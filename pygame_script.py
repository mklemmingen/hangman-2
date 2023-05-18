import pygame
import pygame_gui

import game_events

# pygame
pygame.init()

pygame.display.set_caption("Hangman - the dictionaries strike back")
window_surface = pygame.display.set_mode((1000, 600))

background = pygame.Surface((1000, 600))
background.fill(pygame.Color("#000000"))

manager = pygame_gui.UIManager((1000, 600))

# size of buttons
button_layout_rect = pygame.Rect(0, 0, 65, 20)

# respected distance to corners
button_layout_rect.bottomright = (50, -50)
button_layout_rect.bottomleft = (30, -20)
button_layout_rect.topleft = (30, -20)
button_layout_rect.topright = (-30, -20)

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

textbox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(0, 0, 200, 20),
                                              manager=manager,
                                              anchors={"bottom": "bottom",
                                                       "right": "right",
                                                       "right_target": push_enter_button})

push_8_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text="8",
                                             manager=manager,
                                             anchors={"bottom": "bottom",
                                                      "right": "right",
                                                      "right_target": textbox})

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

# text_box = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((350, 275), (100, 50)),
#                                         text="1",
#                                         manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # if event.type == pygame_gui.UI_TEXt_ENTRY_FINISHED:
        #

        # if event.type == pygame_gui.UI_BUTTON_PRESSED:
        #    if event.ui_element == push_1_button:
        #    if event.ui_element == push_2_button:
        #    if event.ui_element == push_3_button:
        #    if event.ui_element == push_4_button:
        #    if event.ui_element == push_5_button:
        #    if event.ui_element == push_6_button:
        #    if event.ui_element == push_7_button:
        #    if event.ui_element == push_8_button:
        #    if event.ui_element == push_enter_button:
        #    if event.ui,element == push_quit_button:

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
