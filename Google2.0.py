#When  making your question, the beginning of the sentence must be a capital letter with a question mark on the end
import pygame
background_color = (255, 255, 255)
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Google 2.0')
screen.fill(background_color)
pygame.display.flip()
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