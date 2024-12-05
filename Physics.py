import pygame

import math
import random

import sys
scaleFactor = 75
additiveOptics = False
if len(sys.argv) > 2:
    if sys.argv[1].lower() == "true":
        additiveOptics = True
    scaleFactor = int(sys.argv[2])


width, height = 1920,1080

root = pygame.display.set_mode((width, height))

def calculateIntensity(position, slitSize, wavelength, viewScreenDistance):
    if position == 0:
        position = 0.00000000000000001
    slitModulation = (math.pi * slitSize * position) / (wavelength * viewScreenDistance)


    return (math.sin(slitModulation) / slitModulation)**2

surfaces = []
surface_colors = []

resolution = width

resolutionWidth = width / resolution
for i in range(resolution):
    tempSurface = pygame.Surface((resolutionWidth, height))
    surfaces.append(tempSurface)
    surface_colors.append((0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    

    root.fill((0,0,0))

    for i in range(resolution):
        position = (i-round(resolution/2)) / scaleFactor
        intensity = calculateIntensity(position, 0.000150, 0.000000500, 2.5) * 1000000

        if additiveOptics:
            surface_colors[i] = (surface_colors[i][0] + intensity,0,0)
        else:
            surface_colors[i] = (intensity,0,0)
        if surface_colors[i][0] > 255:
            surface_colors[i] = (255, surface_colors[i][1], surface_colors[i][2])
        
        # print(surface_colors[i])
        surfaces[i].fill(surface_colors[i])
        root.blit(surfaces[i], (i * resolutionWidth, 0))



    pygame.display.flip()