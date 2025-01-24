import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
game = True
dt = 0
# Setting the background image
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (1280, 720))
# Setting the player
player_pos = pygame.Vector2(screen.get_width() / 2, 630)
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (70, 70))
# Setting the enemies
enemy_1 = pygame.image.load("enemy1.png")
enemy_1 = pygame.transform.scale(enemy_1, (80, 80))
enemy_2 = pygame.image.load("enemy2.png")
enemy_2 = pygame.transform.scale(enemy_2, (70, 70))
enemy_3 = pygame.image.load("enemy3.png")
enemy_3 = pygame.transform.scale(enemy_3, (85, 60))
enemy_positions = []
# Initialize enemy positions
for i in range(11):
    enemy_positions.append(pygame.Rect((160 + i * 90, 30, 80, 80)))
    enemy_positions.append(pygame.Rect((160 + i * 90, 110, 70, 70)))
    enemy_positions.append(pygame.Rect((160 + i * 90, 200, 85, 60)))
enemy_direction = 1
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.blit(background, (0, 0))
    # Drawing and moving enemies
    reverse_direction = False
    x_cor = 160
    for i in range(11):
        enemy1 = screen.blit(enemy_1,(x_cor,30))
        x_cor += 90
    # for enemy in enemy_positions:
    #     # enemy.move_ip(0,1)
    #     enemy.move_ip(2 * enemy_direction,0)
    #     if enemy.right >= screen.get_width() or enemy.left < 0:
    #         reverse_direction = True
    #     # if enemy.y == 30:
    #     #     screen.blit(enemy_1, enemy)
    #     elif enemy.y == 110:
    #         screen.blit(enemy_2, enemy)
    #     elif enemy.y == 200:
    #         screen.blit(enemy_3, enemy)

    if reverse_direction:
        enemy_direction *= -1
        # Move all enemies down
        for enemy in enemy_positions:
            enemy.move(0,10)
    screen.blit(player, player_pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
