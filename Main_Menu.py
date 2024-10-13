import pygame, sys, random
from Main_Game import *
from Time_Trial import *

#initialises pygame
pygame.init()

#set screen width and height
SCREEN = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Memory Game")  # Add window title

orange = (255, 97, 3)

def get_font(size):  # defines desired font and size
    return pygame.font.Font("freesansbold.ttf", size)

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # Fill the next screen turquoise when Play is clicked
        SCREEN.fill("turquoise")

        GAME()

        # When clicked play button, the next screen will display this
        # Creates the exit button in next screen
        PLAY_EXIT = Button(image=None, pos=(580, 560), 
                           text_input="EXIT", font=get_font(75), base_color="White", hovering_color="Orange")

        # Exit button changes colour when mouse hovers over button
        PLAY_EXIT.changeColor(PLAY_MOUSE_POS)

        # Updates screen when the exit button is clicked
        PLAY_EXIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_EXIT.checkForInput(PLAY_MOUSE_POS):
                    # If exit button in play screen is clicked then return back to menu
                    main_menu()

        pygame.display.update()

def time_trial():
    while True:
        TIME_MOUSE_POS = pygame.mouse.get_pos()

        # Fill the next screen turquoise when TIME TRIAL is clicked
        SCREEN.fill("turquoise")

        time_trial()

        # Creates the exit button in next screen
        TIME_EXIT = Button(image=None, pos=(580, 560),
                           text_input="EXIT", font=get_font(75), base_color="black", hovering_color="orange")

        # Exit button changes colour when mouse hovers over button
        TIME_EXIT.changeColor(TIME_MOUSE_POS)

        # Updates screen when the exit button is clicked
        TIME_EXIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TIME_EXIT.checkForInput(TIME_MOUSE_POS):
                    # If exit button in play screen is clicked then return back to menu
                    main_menu()

        pygame.display.update()

def leaderboard():
    while True:
        leaderboard_MOUSE_POS = pygame.mouse.get_pos()

        # Fill the next screen turquoise when leaderboard is clicked
        SCREEN.fill("#008000")

        # Text inside the leaderboard screen
        leaderboard_TEXT = get_font(15).render("", True, "Black")
        leaderboard_RECT = leaderboard_TEXT.get_rect(center=(310, 220))
        SCREEN.blit(leaderboard_TEXT, leaderboard_RECT)

        # Leaderboard button
        leaderboard_EXIT = Button(image=None, pos=(580, 560), 
                                  text_input="EXIT", font=get_font(75), base_color="Black", hovering_color="orange")

        # Exit button changes colour when mouse hovers over button
        leaderboard_EXIT.changeColor(leaderboard_MOUSE_POS)

        # Updates screen when the exit button is clicked
        leaderboard_EXIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if user quits the window then the game ends
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if leaderboard_EXIT.checkForInput(leaderboard_MOUSE_POS):  # if exit in leaderboard is clicked, return back to main menu
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        #sets desired colour for the main menu screen
        SCREEN.fill('#008000')

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #adds the title Main menu
        MENU_TEXT = get_font(50).render("MAIN MENU", True, orange)
        MENU_RECT = MENU_TEXT.get_rect(center=(330, 40))

        #creates the Play button in main menu screen
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(330, 145),
                             text_input="PLAY", font=get_font(60), base_color="#d7fcd4", hovering_color="orange")

        #creates time trial button in the main menu screen
        Time_Trial_BUTTON = Button(image=pygame.image.load("assets/Time Rect.png"), pos=(330, 275),
                                   text_input="Time Trial", font=get_font(60), base_color="#d7fcd4", hovering_color="orange")

        #creates the leaderboard button in main menu screen
        leaderboard_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(370, 400),
                                    text_input="leaderboard", font=get_font(50), base_color="#d7fcd4", hovering_color="orange")

        #creates the quit button in main menu screen
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(330, 530),
                             text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="orange")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, leaderboard_BUTTON, Time_Trial_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): # If the play button is clicked then display the Play screen
                    play()

                if Time_Trial_BUTTON.checkForInput(MENU_MOUSE_POS):# If the Time Trial button is clicked then display the Time Trial screen
                    Time_Trial()
                
                if leaderboard_BUTTON.checkForInput(MENU_MOUSE_POS): # If the Leaderboard button is clicked then display the Leaderboard screen
                    leaderboard()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): #If the quit button is clicked then close program
                    pygame.quit()
                    sys.exit()

    pygame.display.update()

main_menu()
                    
