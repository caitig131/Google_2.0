import pygame as pg


def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False


    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)

textinput = pygame_textinput.TextInput()
running = True
while running:
    for event in pygame.event.get():
        question = input("what is your question?")
        if question == "Why is the sky blue?":
            print("Because")
        elif question == "What is the meaning of life?":
            print("To be loved and to love others")
        elif question == "What is the funniest joke?":
            print("Your face")
        elif question == "What is the best movie?":
            print("The Bee Movie")
        elif question == "Who put us on this Earth?":
            print("The great beings of the planet Gab-Odon. They were bored one day and decided on creating life. We are a game that they made.")
        elif question == "What is the best food?":
            print("French fries hands down")
        elif question == "Who are you?":
            print("I am me. I am you. I am everyone who has ever lived; past, present, and future.")
        elif question == "Why am I alive?":
            print("Everyone on Earth has a purpose towards the greater power.")
        elif question == "Who is the best President?":
            print("There is none.")
        elif question == "Who is the King of France?":
            print("Taneil Knowles")
        elif question == "Where is Tupac?":
            print("Havana,Cuba.")
        elif question == "What does water taste like?":
            print("it tastes like water")
        elif question == "How far away are we from the sun?":
            print("very very far")
        elif question == "Where do we go when we die?":
            print("I guess you just have to die to figure it out")
        elif question == "Where is the nearest McDonalds?":
            print("make a left then another left then another left then another left and you'll find it")
        elif question == "What is the best song?":
            print("All Star, by Smash Mouth")
        elif question == "What do Aussies ride to school?":
            print("kangoroos")
        elif question == "What is the worst way to die?":
            print("alone with no one there to love you and to care that you are gone")
        else:
            print("I do not have the answer. You have broken me. I am defeated.")

        if event.type == pygame.QUIT:
            running = False

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()