import pygame
from pygame.locals import *
from tkinter import *
from tkinter import filedialog
import random
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
        label3=Label(self.root,text="In this game your friend's photo along with mario's\nphoto will render in 9 holes randomly \n\nyou have to beat your friend's photo from that\n and you will get a score of 10 on every beat\n\nyou will lose if you beat empty holes or mario instead\n\nuse number keys to acess holes \n\n select your friend's photo from below button",bg='black',font=("Arial",15),fg='white')

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
        self.image3=pygame.image.load(image_location)
        self.image3= pygame.transform.scale(self.image3, (150, 150))
        self.file1=open("resources/ewai.txt","r")
        self.data=self.file1.read()
        print(self.data)
        self.file1.close()

    def display_score(self):
        pygame.display.flip()
        font = pygame.font.SysFont('SHOWCARD GOTHIC',30)
        leaderboard=font.render(f"Leaderboard",True,(200,200,200))
        self.surface.blit(leaderboard,(830,300))
        font = pygame.font.SysFont('Arial',30)
        totalscore=font.render(f"score : {self.score}",True,(200,200,200))
        self.surface.blit(totalscore,(840,350))
        font = pygame.font.SysFont('Arial',30)
        highscore=font.render(f"score : {int(self.data)}",True,(200,200,200))
        self.surface.blit(highscore,(840,380))

    def render(self):
        global random_value
        global random_value2

        #this is for user 

        random_value=random.randint(1,9)

        if random_value==1:
            self.surface.blit(self.image3,(53,78))

        if random_value==2:
            self.surface.blit(self.image3,(311,78))
        
        if random_value==3:
            self.surface.blit(self.image3,(573,78))

        if random_value==4:
            self.surface.blit(self.image3,(53,336))

        if random_value==5:
            self.surface.blit(self.image3,(311,336))

        if random_value==6:
            self.surface.blit(self.image3,(573,336))

        if random_value==7:
            self.surface.blit(self.image3,(53,598))

        if random_value==8:
            self.surface.blit(self.image3,(311,598))

        if random_value==9:
            self.surface.blit(self.image3,(573,598))

        #this is for mario

        random_value2=random.randint(1,9)

        if random_value2==1:
            self.surface.blit(self.image2,(53,78))

        if random_value2==2:
            self.surface.blit(self.image2,(311,78))
        
        if random_value2==3:
            self.surface.blit(self.image2,(573,78))

        if random_value2==4:
            self.surface.blit(self.image2,(53,336))

        if random_value2==5:
            self.surface.blit(self.image2,(311,336))

        if random_value2==6:
            self.surface.blit(self.image2,(573,336))

        if random_value2==7:
            self.surface.blit(self.image2,(53,598))

        if random_value2==8:
            self.surface.blit(self.image2,(311,598))

        if random_value2==9:
            self.surface.blit(self.image2,(573,598))

       
    def play_backgroundmusic(self):
        pygame.mixer.music.load('resources/background_music.mp3')
        pygame.mixer.music.play(-1,0)

    def render_background(self):
        bg=pygame.image.load("resources/background_image.jpeg")
        self.surface.blit(bg,(0,0))

    def play_sound(self,name):
        if name=="game_over":
            sound=pygame.mixer.Sound("resources/gameover.wav")
        if name=="collision":
            sound=pygame.mixer.Sound("resources/jump.mp3")
        pygame.mixer.Sound.play(sound)

    def show_gameover(self):
        self.surface.fill(color)
        if int(self.data)<self.score:
            f=open('resources/ewai.txt','w')
            f.write('{}'.format(self.score))
            f.close()
        pygame.mixer.music.pause()
        font = pygame.font.SysFont('SHOWCARD GOTHIC',60)
        gameover=font.render(f"Game Over",True,(200,200,200))
        self.surface.blit(gameover,(400,200))
        font = pygame.font.SysFont('SHOWCARD GOTHIC',30)
        score=font.render(f"You scored : {self.score}",True,(200,200,200))
        self.surface.blit(score,(450,280))
        font = pygame.font.SysFont('SHOWCARD GOTHIC',30)
        score=font.render(f"Press Enter to restart the game",True,(200,200,200))
        self.surface.blit(score,(390,450))
        font = pygame.font.SysFont('SHOWCARD GOTHIC',30)
        score=font.render(f"Press esc to Exit the game",True,(200,200,200))
        self.surface.blit(score,(400,360))
        pygame.display.flip()

    def play(self):
        self.surface.fill(color)
        self.render_background()
        self.holes.draw()
        self.display_score()
        self.render()
        pygame.display.flip()

    def run_game(self):
        running =True
        pause=False
        time1=1
        while(running):
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                    if event.key==K_RETURN:
                        pause=False
                        self.score=0
                        pygame.mixer.music.unpause()
                    if event.key==K_1:
                        if random_value==1:
                            self.score=self.score+10
                            self.play_sound("collision")
                            time1=time1-0.01
                        else:
                            self.play_sound("game_over")
                            pause=True

                    if event.key==K_2:
                        if random_value==2:
                            self.score=self.score+10
                            self.play_sound("collision")
                            time1=time1-0.01
                        else:
                            self.play_sound("game_over")
                            pause=True
                    
                    if event.key==K_3:
                        if random_value==3:
                            self.score=self.score+10
                            self.play_sound("collision")
                            time1=time1-0.01
                        else:
                            self.play_sound("game_over")
                            pause=True

                    if event.key==K_4:
                        if random_value==4:
                            self.score=self.score+10
                            self.play_sound("collision")
                            time1=time1-0.01
                        else:
                            self.play_sound("game_over")
                            pause=True

                    if event.key==K_5:
                        if random_value==5:
                            self.score=self.score+10
                            self.play_sound("collision")
                            time1=time1-0.01
                        else:
                            self.play_sound("game_over")
                            pause=True

                    if event.key==K_6:
                        if random_value==6:
                            self.score=self.score+10
                            self.play_sound("collision")
                            time1=time1-0.01
                        else:
                            self.play_sound("game_over")
                            pause=True

                    if event.key==K_7:
                        if random_value==7:
                            self.score=self.score+10
                            self.play_sound("collision")
                            time1=time1-0.01
                        else:
                            self.play_sound("game_over")
                            pause=True

                    if event.key==K_8:
                        if random_value==8:
                            self.score=self.score+10
                            self.play_sound("collision")
                            time1=time1-0.01
                        else:
                            self.play_sound("game_over")
                            pause=True

                    if event.key==K_9:
                        if random_value==9:
                            self.score=self.score+10
                            self.play_sound("collision")
                            time1=time1-0.01
                        else:
                            self.play_sound("game_over")
                            pause=True

                elif event.type == QUIT:
                    running = False
            
            if pause==False:
                self.play()
            else:
                self.show_gameover()
            time.sleep(time1)

if __name__=='__main__':
    open_image=user_input()
    open_image.run()
    games=Game()
    games.run_game()

