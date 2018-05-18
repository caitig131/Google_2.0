#!/usr/bin/python3
import pygame_textinput
import pygame
import ast
pygame.init()



screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

class Quest():
    question = "ttt"
    qalist = [("Why is the sky blue?","Because"),("What is the meaning of life?","To be loved and to love others")]
    def __init__(self, screen):
        pass
        # Create TextInput-object
        #self.textinput = pygame_textinput.TextInput()
        #self.screen= screen

    def answer(self, question):
        self.question = question
        print(self.question)
       # self.screen = screen
        #events = pygame.event.get()
        # Feed it with events every frame
        #self.textinput.update(events)
        #self.question = self.textinput.get_text()
        # Blit its surface onto the screen
        #self.screen.blit(self.textinput.get_surface(), (10, 10))
question = ""
quest = Quest(screen)
textinput = pygame_textinput.TextInput()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            quest.answer(question)


    #quest.ask()

    # Feed it with events every frame
    textinput.update(events)
    question = textinput.get_text()
    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))

    pygame.display.update()
    clock.tick(30)
