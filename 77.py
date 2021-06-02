for event in pygame.event.get():
    if event.type == pygame.QUIT:
    	done = True
        break
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            person_dx = -5
        elif event.key == pygame.K_RIGHT:
            person_dx = 5
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            person_dx = 0
        elif event.key == pygame.K_RIGHT:
            person_dx = 0
for bomb in bombs:
    bomb['rect'].top += bomb['dy']
    if bomb['rect'].top > size[1]:
        bombs.remove(bomb)
        rect = pygame.Rect(bomb_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        bombs.append({'rect': rect, 'dy': dy})

person.left = person.left + person_dx
 
if person.left < 0:
    person.left = 0
elif person.left > size[0] - person.width:
    person.left = size[0] - person.width
 
screen.blit(person_image, person)

for bomb in bombs:
    if bomb['rect'].colliderect(person):
        done = True
    screen.blit(bomb_image, bomb['rect'])
 
pygame.display.update()
