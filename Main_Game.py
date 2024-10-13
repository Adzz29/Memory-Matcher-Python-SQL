# build a guessing game!
import pygame, random, sys
def GAME():
    global options_list, spaces, used, new_board, first_guess, second_guess, first_guess_num, second_guess_num, scoreone, scoretwo, matches, game_over, rows, cols, correct
    pygame.init()
 
    #game variables and constants
    screen_width = 600
    screen_height = 600
    white = (255, 255, 255)
    black = (0, 0, 0)
    orange = (255,97,3)
    turquoise = (0, 206, 209)
    green = (0, 255, 0)
    fps = 60
    timer = pygame.time.Clock()
    rows = 5
    cols = 6
    correct = [[0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0,], 
               [0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0, 0]]
    options_list = []
    spaces = []
    used = []
    new_board = True
    first_guess = False
    second_guess = False
    #Guess is assigned an index value. Checks what number is clicked
    first_guess_num = 0
    second_guess_num = 0
    scoreone = 0
    scoretwo = 0
    matches = 0
    game_over = False
    cards_left_covered = 0

    # create screen
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption('Memory Game!')
    #sets fonts
    large_font = pygame.font.Font('freesansbold.ttf', 56)
    small_font = pygame.font.Font('freesansbold.ttf', 26)
    
    def generate_board():
        global options_list, spaces, used
        for item in range(rows * cols // 2):
            options_list.append(item)
            
    # goes through list of options between 1-24. Guarantees that only 2 cards can be selected
        for item in range(rows * cols):
            card = options_list[random.randint(0, len(options_list) - 1)]
            spaces.append(card)
            if card in used:
                used.remove(card)
                options_list.remove(card)
            else:
                used.append(card)
                
    #Sets background colours and shapes
    def draw_backgrounds():
        top_menu = pygame.draw.rect(screen, orange, [0, 0, screen_width, 75])
        #adds score ontop of screen
        score_text1 = small_font.render(f'Player 1s score :  {scoreone}             Player 2s score: {scoretwo}', True, white)
        screen.blit(score_text1, (20, 20))
 
        board_space = pygame.draw.rect(screen, turquoise, [0, 100, screen_width, screen_height - 200], 0)
        
        bottom_menu = pygame.draw.rect(screen, orange, [0, screen_height - 100, screen_width, 100], 0)
        turn_text = small_font.render(f'It is player {player}s turn',True,white)
        screen.blit(turn_text,(40,530))
 
    def draw_exit_button():
    # Set the position and size of the exit button
        exit_button_x = screen_width - 120
        exit_button_y = screen_height - 70
        exit_button_width = 81
        exit_button_height = 35
 
        # Draw the exit button as a rectangle
        exit_button = pygame.draw.rect(screen, black, [exit_button_x, exit_button_y, exit_button_width, exit_button_height], 5)
 
        # Add text to the exit button
        exit_button_text = small_font.render("Exit", True, white)
        screen.blit(exit_button_text, (exit_button_x + 15, exit_button_y + 5))
 
 
    def draw_cards():
        global rows, columns, correct
        card_list = []
        for i in range(cols):
            for j in range(rows):
                
                #draws the cards and sets their size and position
                card = pygame.draw.rect(screen, orange,[i * 85 + 48, j *78 + 110, 61, 65], 0, 4)
                card_list.append(card)
                ## randomly adds numbers onto the cards. to make sure that the black numbers dont populate instantly when game is created 
                '''card_text = small_font.render(f'{spaces[i * rows + j]}', True, black)
                screen.blit(card_text, (i * 75 + 18, j * 65 + 120))'''
        for r in range(rows):
            for c in range(cols):
                if correct[r][c] == 1:
                    #creates green border around cards when match is made
                    pygame.draw.rect(screen, green, [c * 85 + 48, r * 78 + 110, 61, 65], 3, 4)
                    card_text = small_font.render(f'{spaces[c * rows + r]}', True, black)
                    screen.blit(card_text, (c * 85 + 55, r * 78 + 125))
        return card_list
 
    def check_guesses(first, second,player):
        global spaces, correct, scoreone,scoretwo, matches
        if spaces[first] == spaces[second]:
 
            #floor division
            col1 = first // rows
            col2 = second // rows
            row1 = first - (first // rows * rows)
            row2 = second - (second // rows * rows)
            #checks for match and score incremented by 1
            if correct[row1][col1] == 0 and correct[row2][col2] == 0:
                correct[row1][col1] = 1
                correct[row2][col2] = 1
                print(player)
                if player == 1:
                    scoreone += 1
                elif player == 2:
                    scoretwo += 1
                matches += 1
 
    running = True
    player = 1
    while running:
        timer.tick(fps)
        screen.fill(turquoise)
        if new_board:
            generate_board()
            new_board = False
        draw_backgrounds()
        board = draw_cards()
        draw_exit_button()
 
        if first_guess and second_guess:
            check_guesses(first_guess_num, second_guess_num,player)
            if player == 1:
                player = 2
            else:
                player = 1
 
     ##delays code for miliseconds to see second guess
            pygame.time.delay(1000)
            first_guess = False
            second_guess = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(board)):
                    button = board[i]
                    
                #can guess as long as it's not game over
                    if not game_over:
                     if button.collidepoint(event.pos) and not first_guess:
                        first_guess = True
                        first_guess_num = i
                        
            ##ensures that the same card cannot be clicked twice
                    if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                        second_guess = True
                        second_guess_num = i
                        
    #Checks for game over
        if matches == rows * cols // 2:
            game_over = True
            winner = pygame.draw.rect(screen, turquoise,[0, 0, 600, 600])
            if scoreone < scoretwo:
                winner_text = large_font.render(f'Player 2 wins!!', True, orange)
            else:
                winner_text = large_font.render(f'Player 1 wins!!', True, orange)
            screen.blit(winner_text, (70, screen_height - 350))
 
 
    #allows card to be flipped to show number
        if first_guess:
            card_text = small_font.render(f'{spaces[first_guess_num]}', True, black)
            location = (first_guess_num // rows * 85 + 55, (first_guess_num - (first_guess_num // rows * rows)) * 78 + 125)
            screen.blit(card_text, (location))
            
        if second_guess:
            card_text = small_font.render(f'{spaces[second_guess_num]}', True, black)
            location = (second_guess_num // rows * 85 + 55, (second_guess_num - (second_guess_num // rows * rows)) * 78 + 125)
            screen.blit(card_text, (location))
 
 
        pygame.display.flip()
    pygame.quit()