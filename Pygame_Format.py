#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 01:58:41 2018

@author: radhakrishnamallik
"""

import os, sys, math, pygame.mixer
from pygame import *
vec = pygame.math.Vector2
# Defining some basic colors
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
Aqua = (0, 255, 255)
Black = (0, 0, 0)
Blue = (0, 0,255)
Fuchsia = (255,0, 255)
Gray = (128,128,128)
Green = (0, 128, 0)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
NavyBlue = (0, 0,128)
Olive = (128,128, 0)
Purple = (128,0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)
Yellow = (255,255, 0)
# Defining the screen size
# Set the width and height of the screen [width, height]

WIDTH = 1500
DEPTH = 950
size = (WIDTH, DEPTH) 


# Defining Constant
FPS = 120
DSF = 2E9
DIASF = 5E6
G = 6.67E-11
M = 1.989E30
DaySec = 24*60*60 # Sec
DayNo = 150 # Day Time Scale factor 1 sec = n day

DT = DayNo*DaySec/FPS
TimeStepCount = 1000
DDT = DT/TimeStepCount
sunPos = vec(WIDTH*0.5, DEPTH*0.5)
# Planet Images Loading
b = 5 
h = 5
s = 5
m = 2
v = 2
e = 3
ma = 2
j = 20
sa = 20
sunImage = pygame.image.load("images/sun.jpg")
sunImageM = pygame.transform.scale(sunImage, (b*s,h*s))

mercImage = pygame.image.load("images/merc.jpg")
mercImageM = pygame.transform.scale(mercImage, (b*m,h*m))


venusImage = pygame.image.load("images/venus.jpg")
venusImageM = pygame.transform.scale(venusImage, (b*v,h*v))

earthImage = pygame.image.load("images/earth.jpg")
earthImageM = pygame.transform.scale(earthImage, (b*e,h*e))

marsImage = pygame.image.load("images/mars.jpg")
marsImageM = pygame.transform.scale(marsImage, (b*ma,h*ma))

jupiterImage = pygame.image.load("images/jupiter.jpg")
jupiterImageM = pygame.transform.scale(jupiterImage, (b*j,h*j))
 
saturnImage = pygame.image.load("images/saturn.jpg")
saturnImageM = pygame.transform.scale(saturnImage, (b*sa,h*sa))


class Planet:       
    def __init__(self,dia,distanceFromSun,mass,velocity,tilt,color,image):
        self.dia = dia
        self.distanceFromSun = distanceFromSun
        self.mass = mass
        self.velocity = velocity
        self.tilt = tilt
        self.color = color
        self.image = image
        self.vel = vec(0,self.velocity)   
        self.posWrtSun = vec(-self.distanceFromSun,0)
#        self.pos = (self.posWrtSun/DSF + sunPos)        

    def InstantV(self,IposWrtSun,Ivel):
        self.IposWrtSun = IposWrtSun
        self.Ivel = Ivel
        for i in range(TimeStepCount):            
            self.acc = -G*M*(self.IposWrtSun)/((vec.length(self.IposWrtSun))**3)            
            self.IposWrtSun += self.Ivel*DDT+0.5*self.acc*DDT**2
            self.Ivel += self.acc*DDT            
            self.pos = (self.IposWrtSun/DSF + sunPos)
        return self.pos,self.IposWrtSun,self.Ivel
        
    def display(self):

        rect = self.image.get_rect()
        rect.center = ((int(self.pos.x),int(self.pos.y)))
        screen.blit(self.image, rect)
 

# initializing pygame window
# Setting the display and getting the Surface object
pygame.init()
screen = pygame.display.set_mode(size)
bg = pygame.image.load("NightSky2.jpg")    
    

# Getting the Clock object
clock = pygame.time.Clock()

#Setting the title to the window  
pygame.display.set_caption("Planet around the Sun")




# Creating planet object from Planet Class
sun = Planet(1.392E9, 0, 1.989E30, 0, 0, Yellow,sunImageM)  #MKS units, tilt is in degree
venus = Planet(12.104E6, 108.2E9, 4.9E24, 35000, 177, Maroon, venusImageM)
merc = Planet(5.0E6, 57.9E9, 3.3E23, 47400, 0.01, Maroon, mercImageM)
earth = Planet(12.756E6, 149.6E9, 6.0E24, 29800, 23.5, GREEN, earthImageM)
mars = Planet(6.779E6, 227.9E9, 6.0E24, 24100, 25, RED, marsImageM)
jupiter = Planet(143E6, 778.6E9, 2.0E27, 13100, 3, Yellow, jupiterImageM)
saturn = Planet(120.5E6, 1427E9, 5.7E26, 9700, 27, Silver, saturnImageM)
 
# Initial velocity  of the planet

venus_vel = -venus.vel
merc_vel = merc.vel
earth_vel = earth.vel
mars_vel = mars.vel
jupiter_vel = jupiter.vel
saturn_vel = saturn.vel

# Initial  position of the planet
venus_wrtSun = venus.posWrtSun
merc_wrtSun = merc.posWrtSun
earth_wrtSun = earth.posWrtSun
mars_wrtSun= mars.posWrtSun
jupiter_wrtSun = jupiter.posWrtSun
saturn_wrtSun = saturn.posWrtSun

# For debugging
#venus.InstantV(venus_wrtSun,venus_vel)
#venus_wrtSun = venus.IposWrtSun
#venus_vel =venus.Ivel
#print(venus_wrtSun)
#print(venus.pos)
#print(venus_vel) 

# Defining the variables for FPS and continued running
FPS = 60
run_me = True
while run_me:
    # Limit the framerate
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_me = False
            
    # Clear the screen
    screen.blit(bg,(0,0))

#    sun.display()
    screen.blit(sunImageM,(int(WIDTH*0.5-0.5*b*s),int(DEPTH*0.5-0.5*b*s))),
    venus.InstantV(venus_wrtSun,venus_vel)
    venus_wrtSun = venus.IposWrtSun
    venus_vel =venus.Ivel
    
    merc.InstantV(merc_wrtSun,merc_vel)
    merc_wrtSun = merc.IposWrtSun
    merc_vel =merc.Ivel 
    
    earth.InstantV(earth_wrtSun,earth_vel)
    earth_wrtSun = earth.IposWrtSun
    earth_vel = earth.Ivel 
    
    mars.InstantV(mars_wrtSun,mars_vel)
    mars_wrtSun = mars.IposWrtSun
    mars_vel = mars.Ivel    
    
    jupiter.InstantV(jupiter_wrtSun,jupiter_vel)
    jupiter_wrtSun = jupiter.IposWrtSun
    jupiter_vel = jupiter.Ivel 
    
    saturn.InstantV(saturn_wrtSun,saturn_vel)
    saturn_wrtSun = saturn.IposWrtSun
    saturn_vel = saturn.Ivel 
#    all_sprites = pygame.sprite.Group()
    venus.display()
    merc.display()
    earth.display()
    mars.display()
    jupiter.display()
    saturn.display()

    # Display everything in the screen
    pygame.display.flip()
    
# Quit the game
pygame.quit()
sys.exit()
    