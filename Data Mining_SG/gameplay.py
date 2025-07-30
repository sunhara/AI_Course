import pygame
from constrain import*
from buttons import*
from ai import*
from aprior import*
import sys
import time
import random


# Initialize pygame
pygame.init()

# Font for text
tinyfont = pygame.font.Font(None, 16)
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 36)
time_font = pygame.font.Font(None, 28)


# Set up the display
screen = pygame.display.set_mode((screenWidth, screnHeight))
screen.fill(WHITE)
pygame.display.set_caption("Casher")


# Create buttons
item_button1 = Button(x=20,y=20,width=120,height=40,text="Apple",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

item_button2 = Button(x=20,y=70,width=120,height=40,text="Bagle",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

item_button3 = Button(x=20,y=120,width=120,height=40,text="Cake",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

item_button4 = Button(x=20,y=170,width=120,height=40,text="Danish",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

item_button5 = Button(x=20,y=220,width=120,height=40,text="Lays",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

item_button6 = Button(x=250,y=20,width=120,height=40,text="Frito",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

item_button7 = Button(x=250,y=70,width=120,height=40,text="Poptarts",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

item_button8 = Button(x=250,y=120,width=120,height=40,text="Pringles",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

item_button9 = Button(x=250,y=170,width=120,height=40,text="OREO",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

item_button10 = Button(x=250,y=220,width=120,height=40,text="m&m",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

trans_button = Button(x=20,y=400,width=200,height=60,text="TRANSACTION",
color=GREEN,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)

reset_button = Button(x=250,y=400,width=150,height=60,text="RESET NUM",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK) 

clear_button = Button(x=630,y=400,width=160,height=60,text="CLEAR DATA",
color=RED,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK)    

kmeans_button = Button(x=630,y=40,width=160,height=60,text="Clustering",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK) 

associ_button = Button(x=630,y=120,width=160,height=60,text="Association",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK) 

rand_trans_button = Button(x=630,y=200,width=160,height=60,text="Generate trans",
color=LIGHT_GRAY,hover_color=BUTTON_HOVER_COLOR,text_color=BLACK) 





class Casher:
    def __init__(self):
        
        self.game_over = False
        self.item1 = 0
        self.item2 = 0
        self.item3 = 0
        self.item4 = 0
        self.item5 = 0
        self.item6 = 0
        self.item7 = 0
        self.item8 = 0
        self.item9 = 0
        self.item10 = 0

    def transaction(self):
        
        file = open("data.txt", "a")
        item_tuple = (self.item1,self.item2,self.item3,self.item4,self.item5,
        self.item6,self.item7,self.item8,self.item9,self.item10)
        
        item_name_tuple = (item_button1,item_button2,item_button3,item_button4,item_button5,
        item_button6,item_button7,item_button8,item_button9,item_button10)
        
        for i,j in zip(item_tuple,item_name_tuple):
            
            if i != 0:
                file_text = f"{j.text}:{i},"
                file.write(file_text)
        file.write('\n')
        
        file.close()
        self.reset()
                


        return 
        

    
    def kmeans(self):
        
        kmean_clustering()
        
    def generateTrans(self):
        for i in range(5):
            
            my_list = [self.item1,self.item2,self.item3,self.item4,self.item5,
            self.item6,self.item7,self.item8,self.item9,self.item10]
            #random select items
            num_elements_to_pick = random.randrange(1,8)
            # Generate random items with random quantities
            for i in range(num_elements_to_pick):
                
                # Pick a random item index (0-9)
                item_index = random.randrange(10)
                
                # Generate a random quantity (1-10)
                quantity = random.randrange(1, 9)
                
                # Set the quantity for the selected item
                if item_index == 0:
                    self.item1 = quantity
                elif item_index == 1:
                    self.item2 = quantity
                elif item_index == 2:
                    self.item3 = quantity
                elif item_index == 3:
                    self.item4 = quantity
                elif item_index == 4:
                    self.item5 = quantity
                elif item_index == 5:
                    self.item6 = quantity
                elif item_index == 6:
                    self.item7 = quantity
                elif item_index == 7:
                    self.item8 = quantity
                elif item_index == 8:
                    self.item9 = quantity
                elif item_index == 9:
                    self.item10 = quantity
                    
            self.transaction()
            
        
    def clear(self):
        file = open("data.txt", "w") 
        file.write("")
        file.close()
        

        
    def reset(self):
        self.item1 = 0
        self.item2 = 0
        self.item3 = 0
        self.item4 = 0
        self.item5 = 0
        self.item6 = 0
        self.item7 = 0
        self.item8 = 0
        self.item9 = 0
        self.item10 = 0
        
###################################################
    def draw_ui(self):
        # Draw all UI 
        screen.fill((WHITE))
        
        # Draw buttons
        item_button1.draw(screen)
        item_button2.draw(screen)
        item_button3.draw(screen)
        item_button4.draw(screen)
        item_button5.draw(screen)
        item_button6.draw(screen)
        item_button7.draw(screen)
        item_button8.draw(screen)
        item_button9.draw(screen)
        item_button10.draw(screen)
        
        trans_button.draw(screen)
        reset_button.draw(screen)
        clear_button.draw(screen)
        
        kmeans_button.draw(screen)
        associ_button.draw(screen)
        rand_trans_button.draw(screen)
        
        
        text_surface_note = font.render("Left click increase, Right click decrease", True, BLACK)
        screen.blit(text_surface_note,(20,300))
        
        #Number count
        item1_num = f"{self.item1}"
        text_surface1 = font.render(item1_num, True, BLACK)
        screen.blit(text_surface1,(160,30))
        
        item2_num = f"{self.item2}"
        text_surface2 = font.render(item2_num, True, BLACK)
        screen.blit(text_surface2,(160,80))
        
        item3_num = f"{self.item3}"
        text_surface3 = font.render(item3_num, True, BLACK)
        screen.blit(text_surface3,(160,130))
        
        item4_num = f"{self.item4}"
        text_surface4 = font.render(item4_num, True, BLACK)
        screen.blit(text_surface4,(160,180))
        
        item5_num = f"{self.item5}"
        text_surface5 = font.render(item5_num, True, BLACK)
        screen.blit(text_surface5,(160,230))
        
        item6_num = f"{self.item6}"
        text_surface6 = font.render(item6_num, True, BLACK)
        screen.blit(text_surface6,(390,30))
        
        item7_num = f"{self.item7}"
        text_surface7 = font.render(item7_num, True, BLACK)
        screen.blit(text_surface7,(390,80))
        
        item8_num = f"{self.item8}"
        text_surface8 = font.render(item8_num, True, BLACK)
        screen.blit(text_surface8,(390,130))
        
        item9_num = f"{self.item9}"
        text_surface9 = font.render(item9_num, True, BLACK)
        screen.blit(text_surface9,(390,180))
        
        item10_num = f"{self.item10}"
        text_surface10 = font.render(item10_num, True, BLACK)
        screen.blit(text_surface10,(390,230))
