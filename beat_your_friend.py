import pygame
from pygame.locals import *
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import random
import math
import time

color=(0,0,0)

class user_input:
    def __init__(self):
        self.root=Tk()

    def open(self):
        global image_location
        self.root.filename=filedialog.askopenfilename(initialdir="/snake_game/resources",title="Select a file",filetypes=(("png files","*.png"),("all files","*.*")))
        image_location = self.root.filename

    def run(self):
        positionRight = int( self.root.winfo_screenwidth()/2 - 600/2 )
        self.root.geometry("{}x{}+{}+{}".format(650,600,positionRight, 150))
        self.root.configure(bg='black')
        #initializing 

        my_btn = Button(self.root,text="open file",command=self.open,bg='black',fg='white',width=20,height=2)
        label1=Label(self.root,text="press confirm button after selection",bg='black',font=("SHOWCARD GOTHIC",20),fg='white')
        btn=Button(self.root,text="confirm",command=self.root.destroy,bg='black',fg='white',width=20,height=2)
        label2=Label(self.root,text="Welcome to the game\nBeat your friend",bg='black',font=("SHOWCARD GOTHIC",20),fg='white')
        label3=Label(self.root,text="In this game your friend's photo along with mario's\nphoto will render in 9 holes randomly \n\nyou have to beat your friend's photo from that\n and you will get a score of 10 on every beat\n\nyou will lose if you beat empty holes or mario instead\n\nuse number keys to acess holes \n\n select your friend's photo from bellow button",bg='black',font=("Arial",15),fg='white')

        #placing

        label2.place(x=170,y=0)
        label3.place(x=100,y=100)
        my_btn.place(x=260,y=380)
        label1.place(x=50,y=430)
        btn.place(x=260,y=490)

        self.root.mainloop()

class holes:
    def __init__(self,parent_screen):
        self.screen=parent_screen
        self.image1=pygame.image.load("resources/hole.png")
        

    def draw(self):
        self.screen.blit(self.image1,(0,0))
        self.screen.blit(self.image1,(258,0))
        self.screen.blit(self.image1,(520,0))
        self.screen.blit(self.image1,(0,258))
        self.screen.blit(self.image1,(258,258))
        self.screen.blit(self.image1,(520,258))
        self.screen.blit(self.image1,(0,520))
        self.screen.blit(self.image1,(258,520))
        self.screen.blit(self.image1,(520,520))
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()

        pygame.mixer.init()
        self.play_backgroundmusic()
        self.surface=pygame.display.set_mode((1100,750))
        self.holes=holes(self.surface)
        self.score=0
        self.image2=pygame.image.load("resources/mario.png")
        self.userimage=pygame.image.load(image_location)

    def display_score(self):
        pygame.display.flip()
        font = pygame.font.SysFont('SHOWCARD GOTHIC',30)
        leaderboard=font.render(f"Leaderboard",True,(200,200,200))
        self.surface.blit(leaderboard,(830,300))
        font = pygame.font.SysFont('Arial',30)
        totalscore=font.render(f"score : {self.score}",True,(200,200,200))
        self.surface.blit(totalscore,(840,350))

    def render(self):
        global random_value
        random_value=math.ceil(9*(random.random()))
        if random_value==1:
            self.surface.blit(self.image2,(53,78))

        if random_value==2:
            self.surface.blit(self.image2,(311,78))
        
        if random_value==3:
            self.surface.blit(self.image2,(573,78))

        if random_value==4:
            self.surface.blit(self.image2,(53,336))

        if random_value==5:
            self.surface.blit(self.image2,(311,336))

        if random_value==6:
            self.surface.blit(self.image2,(573,336))

        if random_value==7:
            self.surface.blit(self.image2,(53,598))

        if random_value==8:
            self.surface.blit(self.image2,(311,598))

        if random_value==9:
            self.surface.blit(self.image2,(573,598))
       
    def play_backgroundmusic(self):
        pygame.mixer.music.load('resources/background_music.mp3')
        pygame.mixer.music.play(-1,0)

    def render_background(self):
        bg=pygame.image.load("resources/background_image.jpeg")
        self.surface.blit(bg,(0,0))

    def play(self):
        self.surface.fill(color)
        self.render_background()
        self.holes.draw()
        self.display_score()
        self.render()
        pygame.display.flip()

    def run_game(self):
        running =True
        while(running):
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                    if event.key==K_1:
                        if random_value==1:
                            self.score=self.score+10

                    if event.key==K_2:
                        if random_value==2:
                            self.score=self.score+10
                    
                    if event.key==K_3:
                        if random_value==3:
                            self.score=self.score+10

                    if event.key==K_4:
                        if random_value==4:
                            self.score=self.score+10

                    if event.key==K_5:
                        if random_value==5:
                            self.score=self.score+10

                    if event.key==K_6:
                        if random_value==6:
                            self.score=self.score+10

                    if event.key==K_7:
                        if random_value==7:
                            self.score=self.score+10

                    if event.key==K_8:
                        if random_value==8:
                            self.score=self.score+10

                    if event.key==K_9:
                        if random_value==9:
                            self.score=self.score+10

                elif event.type == QUIT:
                    running = False
            
            self.play()
            time.sleep(1)



if __name__=='__main__':
    open_image=user_input()
    open_image.run()

