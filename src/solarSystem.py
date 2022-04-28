import random
import turtle
import math
from tkinter import TclError

class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0)
        self.ssscreen.tracer(50)
        self.ssscreen.bgcolor("black")

    def add(self, aplanet):
        self.planets.append(aplanet)

    def addSun(self, asun):
        self.thesun = asun

    def run(self):
        self.ssscreen.mainloop()

    def createStars(self):
        self.starTurtle = turtle.Turtle() 
        for i in range(250):
            self.starTurtle.penup()
            self.starTurtle.goto(random.uniform(-2,2), random.uniform(-2,2))
            self.starTurtle.pendown()
            color = "blue" if i % 2 == 0 else "white"
            color = "red" if i % 3 == 0 else color
            self.starTurtle.dot(5, color)
    
    def asteroid(self, radius):
        self.aTurtle = turtle.Turtle()
        self.aTurtle.hideturtle()
        # self.aTurtle.pensize(5)
        self.aTurtle.color("burlywood4")
        self.rad = radius
        for i in range(1, 361):
            y = math.sin(i)
            x = math.cos(i)
            self.aTurtle.penup()
            self.aTurtle.goto((x * self.rad), (y * self.rad))
            self.aTurtle.pendown()

            self.aTurtle.dot(5)
    

    def movePlanets(self):
        # Fg = G * 6.673e-11 * m1*m2 / (radiusOfSun + distance between planets)^2 
        G = .1
        dt = .001

        for p in self.planets:  
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()

            if type(p) == '__main__.Comet':
                r = -math.sqrt(rx**2 + ry**2)
            else:
                r = math.sqrt(rx**2 + ry**2)

            gravityx = G * self.thesun.getMass()*rx/r**3 
            gravityy = G * self.thesun.getMass()*ry/r**3

            p.setXVel(p.getXVel() + dt * gravityx)

            p.setYVel(p.getYVel() + dt * gravityy)
class Sun:
    def __init__(self, sname, srad, smass):
        self.name = sname
        self.radius = srad
        self.mass = smass
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getYPos(self):
        return self.y

    def getXPos(self):
        return self.x

class Planet:                 # 186 million / 1 = 5000 / x
   def __init__(self, pname, pradius, pmass, pdist, vx, vy, pcolor):
       self.name = pname
       self.radius = pradius
       self.mass = pmass
       self.distance = pdist
       self.x = pdist
       self.y = 0
       self.velx = vx
       self.vely = vy
       self.color = pcolor

       self.pturtle = turtle.Turtle()
       self.pturtle.penup()
       self.pturtle.color(self.color)
       self.pturtle.shape("circle")
       self.pturtle.goto(self.x,self.y)
       self.pturtle.pendown()

   def getName(self):
       return self.name

   def getRadius(self):
       return self.radius

   def getMass(self):
       return self.mass

   def getDistance(self):
       return self.distance

   def moveTo(self, newx, newy):
       self.x = newx
       self.y = newy
       self.pturtle.goto(newx, newy)

   def getXPos(self):
       return self.x

   def getYPos(self):
       return self.y

   def getXVel(self):
       return self.velx

   def getYVel(self):
       return self.vely

   def setXVel(self, newvx):
       self.velx = newvx

   def setYVel(self, newvy):
       self.vely = newvy

class Comet:
    def __init__(self, pradius, pmass, pdist, vx, vy, pcolor):
        self.radius = pradius
        self.mass = pmass
        self.distance = pdist
        self.x = pdist
        self.y = 1
        self.velx = vx
        self.vely = vy
        self.color = pcolor

        self.cTurtle = turtle.Turtle()
        self.cTurtle.up()
        self.cTurtle.color(self.color)
        self.cTurtle.shape("circle")
        self.cTurtle.goto(self.x,self.y)
        self.cTurtle.down()

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.cTurtle.goto(newx, newy)

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velx

    def getYVel(self):
        return self.vely

    def setXVel(self, newvx):
        self.velx = newvx

    def setYVel(self, newvy):
        self.vely = newvy

class Rocket:
    def  __init__(self, xVel, yVel, color, xEarth):
        self.xVelocity = xVel 
        self.rcolor = color 
        self.yVelocity = yVel 
        self.x = xEarth 
        self.y = 0 

        self.rTurtle = turtle.Turtle() 
        self.rTurtle.penup() 
        self.rTurtle.goto(self.x, self.y) 
        self.rTurtle.pendown() 
        self.rTurtle.color(self.rcolor) 
        self.rTurtle.tilt(43) 
        self.rTurtle._tracer(50) 

    # def launch(self, xEarth):
    #     self.rTurtle.penup()
    #     self.rTurtle.goto(xEarth, 0)
    #     self.rTurtle.pendown()
    def getXPos(self): 
        return self.x

    def getYPos(self):
        return self.y
    
    def getYVel(self):
        return self.yVelocity

    def getXVel(self):
        return self.xVelocity

    def setXVel(self, newvx):
        self.velx = newvx

    def setYVel(self, newvy):
        self.vely = newvy

    def moveTo(self, newx, newy):
        self.rTurtle.pendown()
        self.x = newx
        self.y = newy
        self.rTurtle.goto(newx, newy)


def createSSandAnimate():
    ss = SolarSystem(2,2)    
    ss.createStars()
    ss.asteroid(.75)
    ss.asteroid(1.55)

    sun = Sun("SUN", 5000, 10)
    ss.addSun(sun)


    # .1 = 30,866,333
    mercury = Planet("Mercury", 19.5, 1000, .2, 0, 2, "grey") # 2
    venus = Planet("Venus", 30, 1500, 0.28, 0, -2.0, "gold")  # -2
    earth = Planet("Earth", 47.5, 5000, 0.4, 0, 1.65, "green") # 1.65
    mars = Planet("Mars", 50, 9000, 0.65, 0, 1.2, "red") # 1.2
    jupiter = Planet("Jupiter", 100, 49000, .85, 0, 1.1, "orange") # 1.1
    saturn = Planet("Saturn", 90, 35000, 1.13, 0, .94, "brown") # .94
    uranus = Planet("Uranus", 60, 20000, 1.35, 0, .85, "skyblue") # 1.35 
    neptune = Planet("Neptune", 47.5, 50000, 1.5, 0, .8, "blue") # .8
    pluto = Planet("Pluto", 20, 500, 1.8, 0, .75, "pink") # .75
    # self, pradius, pmass, pdist, vx, vy, pcolor, childOf
    voyager1 = Rocket(.5, .5, "red", earth.x)
    halieys_comet = Comet(40, 10, 2.5, -0.65, -0.6, "darkblue") # -.6

    ss.add(voyager1)
    ss.add(earth)
    ss.add(mercury)
    ss.add(venus)
    ss.add(mars)
    ss.add(jupiter)
    ss.add(saturn)
    ss.add(neptune)
    ss.add(uranus)
    ss.add(pluto)
    ss.add(halieys_comet)

    numTimePeriods = 200000
    for amove in range(numTimePeriods):
        print(amove)
        if amove % 5000 == 0:
            amove = 1 
            earth.pturtle.clear()
            mercury.pturtle.clear()
            venus.pturtle.clear()
            mars.pturtle.clear()
            jupiter.pturtle.clear()
            saturn.pturtle.clear()
            neptune.pturtle.clear()
            uranus.pturtle.clear()
            pluto.pturtle.clear()
            halieys_comet.cTurtle.clear()
            voyager1.rTurtle.clear()
            ss.movePlanets()
        ss.movePlanets()
    ss.run()
createSSandAnimate()
