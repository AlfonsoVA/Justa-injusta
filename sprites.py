import pygame
from ajustes import *

# Declaramos vec como vector de 2 campos
vec = pygame.math.Vector2

# Clase Player, la usamos para el jugador, o sea sus fisicas y su aspecto orrendo :)
class Player(pygame.sprite.Sprite):

	def __init__(self, game):


		# Iniciamos el jugador con su aspecto y fisicas simples
		pygame.sprite.Sprite.__init__(self)

		# Usamos una referencia a la clase main con game
		self.game = game

		# Iniciamos una imagen dando sus dimensiones
		self.image = pygame.Surface((20,30))

		# La coloreamos con ajustes.py el color blanco
		self.image.fill(yellow)

		# Iniciamos la forma de forma fisica a partir de la imagen
		self.rect = self.image.get_rect()

		# Damos el centro de la forma
		self.rect.center = ((ancho / 2) , (largo / 2))

		# Inicializamos las coordenadas de posicion
		self.pos = vec((ancho / 2) , (largo / 2))

		# Inicializamos la velocidad
		self.vel = vec(0,0) 

		# Inicializamos la aceleracion
		self.acc = vec(0,0) 


	def update(self):
		# Damos la aceleracion de 0 al actualizar en x, en y 0.5 para la gravedad
		self.acc = vec(0,gravedad)

		#Eventos para controles
		keys = pygame.key.get_pressed()

		# Izquierda
		if keys[pygame.K_LEFT]:			
			self.acc.x = -Player_acc

		# Derecha
		if keys[pygame.K_RIGHT]:			
			self.acc.x = Player_acc

		self.acc.x += self.vel.x * Player_friction
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc 

		# Casos donde nos salgamos de los bordes; aparecemos en el lado opuesto de la pantalla
		if self.pos.x > ancho:
			self.pos.x = 0

		if self.pos.x < 0:
			self.pos.x = ancho

		self.rect.midbottom = self.pos

	# Jump, para saltar en caso de golpear no avanzamos en altura sino retrocedemos
	def jump(self):
		self.rect.x += 1
		hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.x -= 1
		if hits:
			self.vel.y = -10			

# Clase Platform, la usamos para las plataformas (creativo AF)
class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, w, h):
		# Iniciamos la plataforma con su aspecto y fisicas simples
		pygame.sprite.Sprite.__init__(self)
		# Damos la posicion y medidas de la plataforma con x, y, w, h 
		self.image = pygame.Surface((w,h))
		self.image.fill(green)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Player_2(pygame.sprite.Sprite):
	def __init__(self, game):
		
		pygame.sprite.Sprite.__init__(self)

		self.game = game

		self.image = pygame.Surface((20,30))

		self.image.fill(blue)

		self.rect = self.image.get_rect()
		
		self.rect.center = ((ancho / 2), (largo / 2))
		
		self.pos = vec((ancho / 2) - 100, (largo / 2) - 100)
		
		self.vel = vec(0,0) 
		
		self.acc = vec(0,0) 


	def update(self):
		# Damos la aceleracion de 0 al actualizar en x, en y 0.5 para la gravedad
		self.acc = vec(0,gravedad)

		#Eventos para controles
		keys = pygame.key.get_pressed()

		# Izquierda
		if keys[pygame.K_a]:			
			self.acc.x = -Player_acc

		# Derecha
		if keys[pygame.K_d]:			
			self.acc.x = Player_acc

		self.acc.x += self.vel.x * Player_friction
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc 

		# Casos donde nos salgamos de los bordes; aparecemos en el lado opuesto de la pantalla
		if self.pos.x > ancho:
			self.pos.x = 0

		if self.pos.x < 0:
			self.pos.x = ancho

		self.rect.midbottom = self.pos

	def jump(self):
		self.rect.x += 1
		hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.x -= 1
		if hits:
			self.vel.y = -10	