import pygame
import random

pygame.init()

pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((600,600))

pygame.draw.line(screen,(255,255,255),(200,100),(200,400))
pygame.draw.line(screen,(255,255,255),(400,100),(400,400))
pygame.draw.line(screen,(255,255,255),(100,200),(500,200))
pygame.draw.line(screen,(255,255,255),(100,300),(500,300))

x_mark_img = pygame.image.load('X_mark.png')
o_mark_img = pygame.image.load('O_mark.png')

positions = [[120,120],[260,120],[420,120],[120,220],[260,220],[420,220],[120,320],[260,320],[420,320]]
x_marks = []
o_marks = []
pdict = {'[260,220]':5, '[120,120]':1, '[260,120]':2, '[420,120]':3,'[120,220]':4, '[120,320]':7, '[260,320]':8, '[420,320]':9, '[420,220]':6}

over_font = pygame.font.Font('freesansbold.ttf', 32)

def x_check_win():
	x_marks.sort()
	print(x_marks)
	if x_marks == [1,4,7] or x_marks == [2,5,8] or x_marks == [3,6,9] or x_marks == [1,2,3] or x_marks == [4,5,6] or x_marks == [7,8,9] or x_marks == [1,5,9] or x_marks == [3,5,7]:
		return True
	else:
		return False

def o_check_win():
	o_marks.sort()
	if o_marks == [1,4,7] or o_marks == [2,5,8] or o_marks == [3,6,9] or o_marks == [1,2,3] or o_marks == [4,5,6] or o_marks == [7,8,9] or o_marks == [1,5,9] or o_marks == [2,5,7]:
		return True
	else:
		return False

def mark_o():
	r = random.randint(0,len(positions)-1)
	print(r)
	x,y = positions[r]
	print(x,y)
	positions.remove([x,y])
	print(positions)
	o_marks.append(pdict[f"[{x},{y}]"])
	screen.blit(o_mark_img,(x,y))

def game_over(s):
	if s == 'x':
		over_text = over_font.render("YOU WON", True,(0,0,0),(255, 0, 0))
		screen.blit(over_text, (220, 50))
	else:
		over_text = over_font.render("YOU LOST", True,(0,0,0),(255,0,0))
		screen.blit(over_text, (220,50))

def mark_x(x,y):
	check = o_check_win()
	if check == False:
		if x<400 and x>200 and y<300 and y>200:
			screen.blit(x_mark_img,(260,220))
			positions.remove([260,220])
			x_marks.append(5)
		elif x<200 and x>100 and y>100 and y<200:
			screen.blit(x_mark_img,(120,120))
			positions.remove([120,120])
			x_marks.append(1)
		elif x<400 and x>200 and y<200 and y>100:
			screen.blit(x_mark_img,(260,120))
			positions.remove([260,120])
			x_marks.append(2)
		elif x>400 and x<500 and y<200 and y>100:
			screen.blit(x_mark_img,(420,120))
			positions.remove([420,120])
			x_marks.append(3)
		elif x<200 and x>100 and y>200 and y<300:
			screen.blit(x_mark_img,(120,220))
			positions.remove([120,220])
			x_marks.append(4)
		elif x<200 and x>100 and y<400 and y>300:
			screen.blit(x_mark_img,(120,320))
			positions.remove([120,320])
			x_marks.append(7)
		elif x<400 and x>200 and y<400 and y>300:
			screen.blit(x_mark_img,(260,320))
			positions.remove([260,320])
			x_marks.append(8)
		elif x>400 and x<500 and y<400 and y>300:
			screen.blit(x_mark_img,(420,320))
			positions.remove([420,320])
			x_marks.append(9)
		elif x>400 and x<500 and y>200 and y<300:
			screen.blit(x_mark_img,(420,220))
			positions.remove([420,220])
			x_marks.append(6)
		else:
			return None
		check = x_check_win()
		if check == False:
			mark_o()
		else:
			game_over('x')
	else:
		game_over('o')


running = True
while running:
	for event in pygame.event.get():
		try:
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				x,y = event.pos
				mark_x(x,y)
		except:
			print("Game Complete")

	pygame.display.update()