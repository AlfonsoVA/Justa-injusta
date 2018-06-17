import pygame
from ajustes import *
from sprites import *

class Main:

	def __init__(self):

		# Inicializa los modulos
		pygame.init()

		# Inicializa el audio
		pygame.mixer.init()

		# Crea la pantalla con las medidas de ajustes.py
		self.screen = pygame.display.set_mode((ancho, largo))
		#Creamos una superficie para el background, asociando la medida de la pantalla
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()

		# Cremos imagenes para agregar al background dependiendo el nivel o pantalla en general luego las agrandamos al tamaño de la ventana
		self.background_start = pygame.image.load('title.png')
		self.background_start = pygame.transform.scale(self.background_start, (ancho, largo))
		self.background_help = pygame.image.load('help.png')
		self.background_help = pygame.transform.scale(self.background_help, (ancho, largo))
		self.background_f_level = pygame.image.load('starlight.jpg')
		self.background_f_level = pygame.transform.scale(self.background_f_level, (ancho, largo))
		self.background_s_level = pygame.image.load('lab.png')
		self.background_s_level = pygame.transform.scale(self.background_s_level, (ancho, largo))
		self.background_t_level = pygame.image.load('finale.png')		
		self.background_t_level = pygame.transform.scale(self.background_t_level, (ancho, largo))
		self.background_player_1_w = pygame.image.load('jugador_2_l.png')
		self.background_player_1_w = pygame.transform.scale(self.background_player_1_w, (ancho, largo))
		self.background_player_2_w = pygame.image.load('jugador_1_l.png')
		self.background_player_2_w = pygame.transform.scale(self.background_player_2_w, (ancho, largo))
		
		# Nombre de la ventana 
		pygame.display.set_caption(titulo)

		# Inicializamos un reloj
		self.clock = pygame.time.Clock()
		
		# Booleano para el loop para correr el geim
		self.running = True

		# Al iniciar esatremos en nivel 1
		self.on_level_1 = True
		self.on_level_2 = False
		self.on_level_3 = False

		# Booleano para ir a la pantalla de inicio
		self.opening = True

		# Booleano para ver si terminamos con los niveles
		self.done = False		

		# Dupla para contar las victorias de cada jugador
		self.victories = vec(0,0)

		# Booleano para permanecer en la pantalla de ayuda
		self.helping = True

	def new(self):		
		
		# Pantalla de titulo, en caso de juego nuevo.
		if self.opening:
			self.background.blit(self.background_start, (0,0))
			self.show_title()
		
		else:			
			# Agrupamos los sprites con Group()
			self.all_sprites = pygame.sprite.Group()

			# Creamos al jugador
			self.player = Player(self)

			# Agregamos al player		
			self.all_sprites.add(self.player)

			# Para agregar las plataformas a un grupo primero creamos el grupo ._.
			self.platforms = pygame.sprite.Group()			

			# Agregamos al segundo jugador
			self.player_2 = Player_2(self)

			self.all_sprites.add(self.player_2)

			if self.on_level_1:
				self.background.blit(self.background_f_level, (0,0))	
				self.show_f_level(self.all_sprites, self.platforms)
			elif self.on_level_2:				
				self.background.blit(self.background_s_level, (0,0))
				self.show_s_level(self.all_sprites, self.platforms)
			elif self.on_level_3:
				self.background.blit(self.background_t_level, (0,0))
				self.show_t_level(self.all_sprites, self.platforms)

			# Corremos el geim.
			self.run()

	def show_f_level(self, all_sprites, platforms):

		# Asignamos als posiciones de los jugadores
		self.player.pos = vec(450, 100)
		
		self.player_2.pos = vec(50, 100)

		p1 = Platform(0, 495, 500, 5)		
							
		# Agregamos al grupo de plataformas
		platforms.add(p1)		

		# Agregamos las plataformas a todos los sprites para dibujarlas
		all_sprites.add(p1)	

	def show_s_level(self, all_sprites, platforms):
		
		# Asignamos als posiciones de los jugadores
		self.player.pos = vec(460, 470)
		
		self.player_2.pos = vec(40, 470)

		p1 = Platform(0, 490, 500, 10)

		p2 = Platform(0, 420, 70, 10)

		p3 = Platform(430, 420, 70, 10)

		p4 = Platform(130, 360, 230, 10)

		p5 = Platform(130, 190, 230, 10)

		p6 = Platform(0, 270, 70, 10)

		p7 = Platform(430, 270, 70, 10)
		
		# Agregamos al grupo de plataformas
		platforms.add(p1)		
		platforms.add(p2)		
		platforms.add(p3)		
		platforms.add(p4)
		platforms.add(p5)
		platforms.add(p6)
		platforms.add(p7)

		# Agregamos las plataformas a todos los sprites para dibujarlas
		all_sprites.add(p1)
		all_sprites.add(p2)
		all_sprites.add(p3)
		all_sprites.add(p4)
		all_sprites.add(p5)
		all_sprites.add(p6)
		all_sprites.add(p7)

	def show_t_level(self, all_sprites, platforms):

		# Asignamos als posiciones de los jugadores
		self.player.pos = vec(460, 270)
		
		self.player_2.pos = vec(40, 270)

		p1 = Platform(100, 400, 300, 5)

		p2 = Platform(0, 200, 50, 20)
				
		p3 = Platform(450, 200, 50, 20)
		
		p4 = Platform(0, 300, 150, 20)
				
		p5 = Platform(350, 300, 150, 20)
		
		p6 = Platform(0, 100, 225, 20)
				
		p7 = Platform(275, 100, 250, 20)
		
		p8 = Platform(0, 480, 100, 20)
		
		p9 = Platform(400, 480, 100, 20)
					
		# Agregamos al grupo de plataformas
		platforms.add(p1)		
		platforms.add(p2)		
		platforms.add(p3)
		platforms.add(p4)
		platforms.add(p5)
		platforms.add(p6)
		platforms.add(p7)
		platforms.add(p8)
		platforms.add(p9)

		# Agregamos las plataformas a todos los sprites para dibujarlas
		all_sprites.add(p1)
		all_sprites.add(p2)
		all_sprites.add(p3)
		all_sprites.add(p4)
		all_sprites.add(p5)
		all_sprites.add(p6)
		all_sprites.add(p7)
		all_sprites.add(p8)
		all_sprites.add(p9)

	def next_level(self):

		if self.on_level_1:
			self.on_level_1 = False
			self.on_level_2 = True
			self.new()

		elif self.on_level_2:
			self.on_level_2 = False
			self.on_level_3 = True	
			self.new()

		else:
			self.done = True

	def run(self):

		# Loop para correr el gueim
		while self.running:
			
			# Hacemos el reloj correr conforme a fps de ajustes.py
			self.clock.tick(fps)
			
			if self.done:

				if self.victories.x == max(self.victories):					
					self.background.blit(self.background_player_1_w, (0,0))
					self.screen.blit(self.background_player_1_w, (ancho,largo))
					self.show_end()
										
				else:
					self.background.blit(self.background_player_2_w, (0,0))
					self.screen.blit(self.background_player_2_w, (ancho,largo))
					self.show_end()
					
			else:
				
				if self.on_level_1:
					self.screen.blit(self.background_f_level, (ancho,largo))

				elif self.on_level_2:
					self.screen.blit(self.background_s_level, (ancho,largo))

				elif self.on_level_3:
					self.screen.blit(self.background_t_level, (ancho,largo))

				# Llamamos events() para seguir con los eventos hasta encontrar el tipo QUIT
				self.events()

				# Llamamos update() para actualizar los sprites
				self.update()

				# Llamamos draw() para dibujar los sprites de acuerdo a como se actualicen
				self.draw()		

	def events(self):

		# Checamos el caso de caida, el que cae pierde
		if abs(self.player.pos.y) > largo:
			self.victories.y += 1
			self.next_level()
		elif abs(self.player_2.pos.y) > largo:
			self.victories.x += 1
			self.next_level()

		# A partir de los eventos que obtengamos
		for event in pygame.event.get():

			# Checamos el caso de salir en la ventana
			if event.type == pygame.QUIT:
				self.running = False

			# Checamos el caso de salto y golpe, solo se acepta si estan relativamente cerca 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.player.jump()
				elif event.key == pygame.K_w:
					self.player_2.jump()
				elif (event.key == pygame.K_s) and ((abs(self.player.pos.x - self.player_2.pos.x) < 10) and (abs(self.player.pos.y - self.player_2.pos.y) < 10)):
					self.victories.y += 1
					self.next_level()
				elif (event.key == pygame.K_DOWN) and ((abs(self.player.pos.x - self.player_2.pos.x) < 10) and (abs(self.player.pos.y - self.player_2.pos.y) < 10)):
					self.next_level()
					self.victories.x += 1

	def update(self):		
		
		# Actualizamos los sprites a partir del grupo y los ponemos en la pantalla o.o
		self.all_sprites.update()

		# Usamos hits como una lista de sprites que colisionan, el booleano asegura que si es True los que colisionen se eliminan
		hits = pygame.sprite.spritecollide(self.player, self.platforms, False)

		# Si la lista no esta vacia, manten la caida en 0 y asegura que esté arriba el colisionador del que recibe ( ͡° ͜ʖ ͡°)
		if hits:
			self.player.pos.y = hits[0].rect.top + 1
			self.player.vel.y = 0						

		hits = pygame.sprite.spritecollide(self.player_2, self.platforms, False)	
		
		if hits:
			self.player_2.pos.y = hits[0].rect.top + 1
			self.player_2.vel.y = 0
		
	def draw(self):

		# Agregamos el background a la pantalla
		self.screen.blit(self.background, (0,0))

		# Dibujamos los sprites en pantalla
		self.all_sprites.draw(self.screen)

		# Actualizamos por ultima vez toda la pantalla
		pygame.display.flip()

	def show_end(self):
		
		# Agregamos el background a la pantalla
		self.screen.blit(self.background, (0,0))

		# Actualizamos por ultima vez toda la pantalla
		pygame.display.flip()

		for event in pygame.event.get():

			# Checamos el caso de salir en la ventana
			if event.type == pygame.QUIT:
				self.running = False

			else:				
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.done = False					
						self.on_level_1 = True
						self.on_level_3 = False
						self.victories = vec(0,0)
						self.new()

	def show_title(self):
		
		# Agregamos el background a la pantalla
		self.screen.blit(self.background, (0,0))

		# Actualizamos por ultima vez toda la pantalla	
		pygame.display.flip()
			
		for event in pygame.event.get():

			# Checamos el caso de salir en la ventana
			if event.type == pygame.QUIT:
				pygame.quit()

			else:
				# Eventos para iniciar o ir a la pantalla de ayuda
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.opening = False
						self.new()
					if event.key == pygame.K_h:
						self.helping = True
						while self.helping:
							self.background.blit(self.background_help, (0,0))							
							self.show_help()


	def show_help(self):
		# Agregamos el background a la pantalla
		self.screen.blit(self.background, (0,0))
		
		# Actualizamos por ultima vez toda la pantalla	
		pygame.display.flip()

		# Actualizamos por ultima vez toda la pantalla		
		for event in pygame.event.get():

			# Checamos el caso de salir en la ventana
			if event.type == pygame.QUIT:
				pygame.quit()

			else:
				# En caso de salir				
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.helping = False									

m = Main()
print("*Código basado apartir del siguiente tutorial: https://www.youtube.com/watch?v=8LRI0RLKyt0")
print("Versión 1.0, limitantes:")
print("* Instrucciones no muy precisas; para golpear es con abajo o s, con 3 niveles / rounds se decide el ganador")
print("* Falta detalle en sprites y backgrounds")
print("* Falta de efectos de sonido / animación")
while m.running:	
	m.new()
