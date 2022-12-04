

# ---------------------------------------------
# This code haven't been finished yet
# ---------------------------------------------



# https://medium.com/@pelicanlabs/a-very-simple-python-simulation-of-earths-orbit-29589a39af22
import math
from vpython import *
from time import sleep

sun = sphere(pos=vector(0,0,0), radius=0.1, color=color.yellow, mass=200, velocity=vector(0,0,0), make_trail=True)

# Semieje mayor
semiMA = sphere(pos=vector(-0.76,0,0), radius=0.01, color=color.black, mass=200, velocity=vector(0,0,0), make_trail=True)

Earth = sphere(pos=vector(1,0,0), radius=0.08, color=color.blue, mass = 0.001, velocity = vector(0,2*math.pi,0), make_trail=True)

# rocket object
rocket = sphere(pos=vector(1,0,0), radius=0.03, color=color.white, velocity = vector(0,2*math.pi,0), make_trail=True)

mars = sphere(pos=vector(1.52,0,0), radius=0.04, color=color.red, mass = 0.001, velocity=vector(0,(2*math.pi*1.52)/1.52,0), make_trail=True)

dt = 0.001

def acceleration(p1,p2):
    G=4*math.pi**2
    
    r_vec = p1.pos - p2.pos
    r_mag = mag(r_vec)
    r_hat = r_vec/r_mag
    
    acceleration_magnitude = G/r_mag
	
    print(acceleration_magnitude)
    acceleration_vector = -acceleration_magnitude*r_hat
	
    return acceleration_vector

# Tenia pensado realizar otro calculo para la orbita eliptica del objeto pero ocupo mas fisica xd
# def accelerationRocket(p1,p2):
#     G=4*math.pi**2
# 	
#     r_vec = p1.pos - p2.pos # Distance between orbiting bodies
#     r_mag = mag(r_vec) 
#     r_hat = r_vec/r_mag
#     
#     acceleration_magnitude = sqrt((G/r_mag)*((2/1.26))) # Magnitude in km/s
# 	
#     acceleration_vector = -acceleration_magnitude*r_hat
# 	
#     return acceleration_vector


def planetPos(obj):
    obj.acceleration = acceleration(obj,sun)
    obj.velocity = obj.velocity + obj.acceleration*dt
    obj.pos = obj.pos + obj.velocity*dt

s = 0
while(True):
    rate(100); # Velocidad de ejecución
    # Comenzar a ejecutar todos los objetos hasta que marte se situe a 44 grados del centro aprox
    if(s <= 186): 
        planetPos(mars)
    else:
        Earth.acceleration = acceleration(Earth,sun)
        mars.acceleration = acceleration(mars,sun)
        rocket.acceleration = acceleration(rocket, semiMA)
        
        Earth.velocity = Earth.velocity + Earth.acceleration*dt
        mars.velocity = mars.velocity + mars.acceleration*dt
        rocket.velocity = rocket.velocity + rocket.acceleration*dt

        Earth.pos = Earth.pos + Earth.velocity*dt  
        mars.pos = mars.pos + mars.velocity*dt
        rocket.pos = rocket.pos + rocket.velocity*dt
    s += 1
    
    print(s)
