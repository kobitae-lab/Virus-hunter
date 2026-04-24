from sys import exit

import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# background images
background = pygame.image.load("human_background.png")
blood_vessel = pygame.image.load("blood_vessel.png")
# images for first antibody
antibody1 = pygame.image.load("antibody_1.png")
antibody1_right = pygame.image.load("antibody_1_right.png")
antibody1_left = pygame.image.load("antibody_1_left.png")
antibody1_down = pygame.image.load("antibody_1_down.png")
antibody1_current = antibody1
# images for second antibody
antibody2 = pygame.image.load("antibody_2.png")
antibody2_right = pygame.image.load("antibody_2_right.png")
antibody2_left = pygame.image.load("antibody_2_left.png")
antibody2_down = pygame.image.load("antibody_2_down.png")
antibody2_current = antibody2
# virus images
virus1 = pygame.image.load("virus1.png")
virus2 = pygame.image.load("virus2.png")
virus3 = pygame.image.load("virus3.png")
virus4 = pygame.image.load("virus4.png")
# on-screen text for when you lose
text_font = pygame.font.SysFont("Arial", 50)
game_over = text_font.render("you died lol", True, (0,0,0), (255, 255, 255))
# pre-game instructions on screen
instructions_font = pygame.font.SysFont("Arial", 25)
instructions1 = instructions_font.render("Control your antibodies using WASD and arrow keys", True, (0,0,0), (255, 255, 255))
instructions2 = instructions_font.render("To kill a virus have both your antibodies touching them at the same time", True, (0,0,0), (255, 255, 255))
instructions3 = instructions_font.render("The goal of the game is to kill 30 viruses before you get infected 4 times", True, (0,0,0), (255, 255, 255))
instructions4 = instructions_font.render("Press spacebar to start playing", True, (0,0,0), (255, 255, 255))
instructions5 = instructions_font.render("You get infected by a virus when it reaches the left side of the screen", True, (0,0,0), (255, 255, 255))
# count virus kills and virus infections
virus_counter = 0
virus_infected = 0
# on-screen text
victory = text_font.render("You Have Developed Immunity to this virus", True, (0,0,0), (255, 255, 255))
viruses = text_font.render("Viruses infected " + str(virus_infected), True, (0,0,0), (255, 255, 255))
counter = text_font.render("Viruses Killed " + str(virus_counter), True, (0,0,0), (255, 255, 255))

play_game = True


# bounding box

#antibody1
antibody1_rect = antibody1.get_rect()
antibody1_width = antibody1_rect.width
antibody1_height = antibody1_rect.height

antibody1_right_rect = antibody1_right.get_rect()
antibody1_right_width = antibody1_right_rect.width
antibody1_right_height = antibody1_right_rect.height

antibody1_left_rect = antibody1_left.get_rect()
antibody1_left_width = antibody1_left_rect.width
antibody1_left_height = antibody1_left_rect.height

antibody1_down_rect = antibody1_down.get_rect()
antibody1_down_width = antibody1_down_rect.width
antibody1_down_height = antibody1_down_rect.height

#antibody2
antibody2_rect = antibody2.get_rect()
antibody2_width = antibody2_rect.width
antibody2_height = antibody2_rect.height

antibody2_right_rect = antibody2_right.get_rect()
antibody2_right_width = antibody2_right_rect.width
antibody2_right_height = antibody2_right_rect.height

antibody2_left_rect = antibody2_left.get_rect()
antibody2_left_width = antibody2_left_rect.width
antibody2_left_height = antibody2_left_rect.height

antibody2_down_rect = antibody2_down.get_rect()
antibody2_down_width = antibody2_down_rect.width
antibody2_down_height = antibody2_down_rect.height

# arm
background_rect = background.get_rect()
background_width = background_rect.width
background_height = background_rect.height

#viruses
virus1_rect = virus1.get_rect()
virus1_width = virus1_rect.width
virus1_height = virus1_rect.height

virus2_rect = virus2.get_rect()
virus2_width = virus2_rect.width
virus2_height = virus2_rect.height

virus3_rect = virus3.get_rect()
virus3_width = virus3_rect.width
virus3_height = virus3_rect.height

virus4_rect = virus4.get_rect()
virus4_width = virus4_rect.width
virus4_height = virus4_rect.height


# coords
antibody1_x = 200
antibody1_y = 200
                                 
antibody1_right_x = 250
antibody1_right_y = 250

antibody1_left_x = 250
antibody1_left_y = 250

antibody1_down_x = 250
antibody1_down_y = 250

antibody2_x = 200
antibody2_y = 400
                                 
antibody2_right_x = 250
antibody2_right_y = 250

antibody2_left_x = 250
antibody2_left_y = 250

antibody2_down_x = 250
antibody2_down_y = 250

virus1_x = 800
virus1_y = 70

virus2_x = 800
virus2_y = 170

virus3_x = 800
virus3_y = 320

virus4_x = 800
virus4_y = 470

# colours
WHITE = (255,255,255)
RED = (200,0,0)

read_instructions = True

while read_instructions == True:
    pygame.draw.rect(screen, WHITE, (0,0, 800, 800), 0)
    screen.blit(background, (-170,-500))

    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    
    screen.blit(instructions1, (120, 100))
    screen.blit(instructions2, (120, 150))
    screen.blit(instructions3, (120, 200))
    screen.blit(instructions4, (250, 350))
    screen.blit(instructions5, (120, 250))
    # start game if spacebar is pressed
    if keys[pygame.K_SPACE]:
        read_instructions = False

    pygame.display.update()
        
        
    


# game loop
while play_game == True:
    # images drawn on screen
    pygame.draw.rect(screen, RED, (0,0, 800, 800), 0)
    screen.blit(background, (-170,-500))
    screen.blit(blood_vessel, (105, 310))
    screen.blit(blood_vessel, (105, 125))
    screen.blit(blood_vessel, (105, -65))
    screen.blit(blood_vessel, (105, 500))
    screen.blit(viruses, (105, 0))
    screen.blit(virus1, (virus1_x, virus1_y))
    screen.blit(counter, (500, 0))
    screen.blit(virus2, (virus2_x, virus2_y))
    screen.blit(virus3, (virus3_x, virus3_y))
    screen.blit(virus4, (virus4_x, virus4_y))
    
    screen.blit(antibody1_current, (antibody1_x, antibody1_y))
    screen.blit(antibody2_current, (antibody2_x, antibody2_y))
    
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    # bounding box check
    antibody1_box = pygame.Rect(antibody1_x, antibody1_y, antibody1_width, antibody1_height)
    antibody1_left_box = pygame.Rect(antibody1_left_x, antibody1_left_y, antibody1_left_width, antibody1_left_height)
    antibody1_right_box = pygame.Rect(antibody1_right_x, antibody1_right_y, antibody1_right_width, antibody1_right_height)
    antibody1_down_box = pygame.Rect(antibody1_down_x, antibody1_down_y, antibody1_down_width, antibody1_down_height)

    antibody2_box = pygame.Rect(antibody2_x, antibody2_y, antibody2_width, antibody2_height)
    antibody2_left_box = pygame.Rect(antibody2_left_x, antibody2_left_y, antibody2_left_width, antibody2_left_height)
    antibody2_right_box = pygame.Rect(antibody2_right_x, antibody2_right_y, antibody2_right_width, antibody2_right_height)
    antibody2_down_box = pygame.Rect(antibody2_down_x, antibody2_down_y, antibody2_down_width, antibody2_down_height)

    virus1_box = pygame.Rect(virus1_x, virus1_y, virus1_width, virus1_height)
    virus2_box = pygame.Rect(virus2_x, virus2_y, virus2_width, virus2_height)
    virus3_box = pygame.Rect(virus3_x, virus3_y, virus3_width, virus3_height)
    virus4_box = pygame.Rect(virus4_x, virus4_y, virus4_width, virus4_height)

    background_box = pygame.Rect(-170, -500, background_width, background_height)
 
    # check if collides, if collides move virus back and ad + 1 to virus counter
    if antibody1_box.colliderect(virus1_box):
        if antibody2_box.colliderect(virus1_box):
            virus1_x = 900
            virus1_y = 220
            virus_counter = virus_counter + 1
            counter = text_font.render("Viruses Killed " + str(virus_counter), True, (0,0,0), (255, 255, 255))
            screen.blit(counter, (500, 0))
            pygame.display.update()


    elif antibody2_box.colliderect(virus1_box):
        virus1_x = virus1_x - 0
        
    else:
        if virus1_x > 80:
            if virus_counter >= 5:
                virus1_x = virus1_x - 1.5
            if virus_counter >= 10:
                virus1_x = virus1_x - 2
            if virus_counter >= 15:
                virus1_x = virus1_x - 2.5
            if virus_counter >= 20:
                virus1_x = virus1_x - 3
            if virus_counter >= 25:
                virus1_x = virus1_x - 4
            else:
                virus1_x = virus1_x - 1


    if antibody1_box.colliderect(virus2_box):
        if antibody2_box.colliderect(virus2_box):
            virus2_x = 900
            virus2_y = 70
            virus_counter = virus_counter + 1
            counter = text_font.render("Viruses Killed " + str(virus_counter), True, (0,0,0), (255, 255, 255))
            screen.blit(counter, (500, 0))
            pygame.display.update()
    elif antibody2_box.colliderect(virus2_box):
        virus2_x = virus2_x - 0

    else:
        if virus2_x > 80:
            if virus_counter >= 5:
                virus2_x = virus2_x - 1.5
            if virus_counter >= 10:
                virus2_x = virus2_x - 2
            if virus_counter >= 15:
                virus2_x = virus2_x - 2.5
            if virus_counter == 20:
                virus2_x = virus2_x - 3
            if virus_counter >= 25:
                virus2_x = virus2_x - 4
            else:
                virus2_x = virus2_x - 1
            

    if antibody1_box.colliderect(virus3_box):
        if antibody2_box.colliderect(virus3_box):
            virus3_x = 900
            virus3_y = 470
            virus_counter = virus_counter + 1
            counter = text_font.render("Viruses Killed " + str(virus_counter), True, (0,0,0), (255, 255, 255))
            screen.blit(counter, (500, 0))
            pygame.display.update()
    elif antibody2_box.colliderect(virus3_box):
        virus3_x = virus3_x - 0

    else:
        if virus3_x > 80:
            if virus_counter >= 5:
                virus3_x = virus3_x - 1.5
            if virus_counter >= 10:
                virus3_x = virus3_x - 2
            if virus_counter >= 15:
                virus3_x = virus3_x - 2.5
            if virus_counter >= 20:
                virus3_x = virus3_x - 3
            if virus_counter >= 25:
                virus3_x = virus3_x - 4
            else:
                virus3_x = virus3_x - 1


    if antibody1_box.colliderect(virus4_box):
        if antibody2_box.colliderect(virus4_box):
            virus4_x = 900
            virus4_y = 370
            virus_counter = virus_counter + 1
            counter = text_font.render("Viruses Killed " + str(virus_counter), True, (0,0,0), (255, 255, 255))
            screen.blit(counter, (500, 0))
            pygame.display.update()
    elif antibody2_box.colliderect(virus4_box):
        virus4_x = virus4_x - 0
    
    else:
        if virus4_x > 80:
            if virus_counter >= 5:
                virus4_x = virus4_x - 1.5
            if virus_counter >= 10:
                virus4_x = virus4_x - 2
            if virus_counter >= 15:
                virus4_x = virus4_x - 2.5
            if virus_counter >= 20:
                virus4_x = virus4_x - 3
            if virus_counter >= 25:
                virus4_x = virus4_x - 4
            else:
                virus4_x = virus4_x - 1





    # check if virus collides with arm, if collides move viruses back and + 1 to virus infected
    if virus1_box.colliderect(background_box):
        virus1_x = 1000
        virus1_y = 220
        virus_infected = virus_infected + 1
        viruses = text_font.render("Viruses Infected " + str(virus_infected), True, (0,0,0), (255, 255, 255))
        screen.blit(viruses, (105, 0))
        pygame.display.update()
        
    if virus2_box.colliderect(background_box):
        virus2_x = 1000
        virus2_y = 70
        virus_infected = virus_infected + 1
        viruses = text_font.render("Viruses Infected " + str(virus_infected), True, (0,0,0), (255, 255, 255))
        screen.blit(viruses, (105, 0))
        pygame.display.update()
    if virus3_box.colliderect(background_box):
        virus3_x = 1000
        virus3_y = 470
        virus_infected = virus_infected + 1
        viruses = text_font.render("Viruses Infected " + str(virus_infected), True, (0,0,0), (255, 255, 255))
        screen.blit(viruses, (105, 0))
        pygame.display.update()
    if virus4_box.colliderect(background_box):
        virus4_x = 1000
        virus4_y = 370
        virus_infected = virus_infected + 1
        viruses = text_font.render("Viruses Infected " + str(virus_infected), True, (0,0,0), (255, 255, 255))
        screen.blit(viruses, (105, 0))
        pygame.display.update()

    if virus_infected >= 4:
        screen.blit(game_over, (300, 200))
        pygame.display.update()
        pygame.time.delay(3000)
        play_game = False

    if virus_counter >= 30:
        screen.blit(victory, (0, 200))
        pygame.display.update()
        pygame.time.delay(5000)
        play_game = False



    # WASD movement keys
    if keys[pygame.K_a]:
        if antibody1_x > 0:
            antibody1_x = antibody1_x - 15
            antibody1_current = antibody1_left

    if keys[pygame.K_d]:
        if antibody1_x < 760:
            antibody1_x = antibody1_x + 15
            antibody1_current = antibody1_right

    if keys[pygame.K_w]:
        if antibody1_y > 0:
            antibody1_y = antibody1_y - 15
            antibody1_current = antibody1

    if keys[pygame.K_s]:
        if antibody1_y < 560:
            antibody1_y = antibody1_y + 15
            antibody1_current = antibody1_down


    # ARROW KEYS
    if keys[pygame.K_LEFT]:
        if antibody2_x > 0:
            antibody2_x = antibody2_x - 15
            antibody2_current = antibody2_left

    if keys[pygame.K_RIGHT]:
        if antibody2_x < 760:
            antibody2_x = antibody2_x + 15
            antibody2_current = antibody2_right

    if keys[pygame.K_UP]:
        if antibody2_y > 0:
            antibody2_y = antibody2_y - 15
            antibody2_current = antibody2

    if keys[pygame.K_DOWN]:
        if antibody2_y < 560:
            antibody2_y = antibody2_y + 15
            antibody2_current = antibody2_down

    # close program when escape is pressed
    if keys[pygame.K_ESCAPE]:
        play_game = False

        
 


    pygame.time.delay(25)



    pygame.display.update()




pygame.quit()
exit()                                 
