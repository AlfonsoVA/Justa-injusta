import pygame
from ajustes import *
from sprites import *

class Level_1():
	def __init__(self, group_all, group_plat):
		p1 = Platform(150, 330, 200, 10)

		p2 = Platform(0, 400, 50, 10)

		p3 = Platform(450, 400, 50, 10)

		p4 = Platform(150, 230, 200, 10)

		p5 = Platform(150, 130, 200, 10)
		
		# Agregamos al grupo de plataformas
		self.group_plat.add(p1)		
		self.group_plat.add(p2)		
		self.group_plat.add(p3)		
		self.group_plat.add(p4)
		self.group_plat.add(p5)

		# Agregamos las plataformas a todos los sprites para dibujarlas
		self.group_all.add(p1)
		self.group_all.add(p2)
		self.group_all.add(p3)
		self.group_all.add(p4)
		self.group_all.add(p5)



