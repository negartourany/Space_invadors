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
# Bullets
bullet_pic = pygame.image.load("bullet.png")
bullet_pic = pygame.transform.scale(bullet_pic, (bullet_pic.get_width(), bullet_pic.get_height()))
bullet_position = []
# Game over sign
font = pygame.font.Font(None, 80)
text = font.render("Game Over!", True, "white", "black")
win_text = font.render("You are a badass spider killer!", True, "red", "black")
game_over = False
# Making player rect
player_rect = pygame.Rect(player_pos.x, player_pos.y, player.get_width(), player.get_height())
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Shooting
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet_position.append(
                        pygame.Rect(player_pos.x - 55, player_pos.y - 55, bullet_pic.get_width(),
                                    bullet_pic.get_height()))

    screen.blit(background, (0, 0))
    # Drawing and moving enemies
    reverse_direction = False
    x_cor = 160

    for enemy in enemy_positions:
        if not game_over:
            enemy.move_ip(2 * enemy_direction, 0)
        if enemy.right >= screen.get_width() or enemy.left < 0:
            reverse_direction = True
        if 30 <= enemy.y:
            screen.blit(enemy_1, enemy)
        # Game over
        if enemy.bottom >= screen.get_height() - 20 or enemy.colliderect(player_rect):
            screen.blit(text, (480, screen.get_height() / 2 - 50))
            game_over = True

    if reverse_direction:
        enemy_direction *= -1
        # Move all enemies down
        for enemy in enemy_positions:
            enemy.move_ip(0, 10)
    screen.blit(player, player_pos)
    keys = pygame.key.get_pressed()
    # Checking for player boundaries
    if 0 <= player_pos.x <= 1200:
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
    elif player_pos.x <= 0:
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
    elif player_pos.x >= 1200:
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
    # Moving the bullet upward
    for bullet in bullet_position[:]:
        bullet.y -= 300 * dt
        if bullet.bottom < 0:
            bullet_position.remove(bullet)
        else:
            screen.blit(bullet_pic, (bullet.x, bullet.y))
    # Collision detection
    for bull in bullet_position[:]:
        for target in enemy_positions[:]:
            hit = bull.inflate(-bull.width * 0.75, -bull.height * 0.75).colliderect(target)
            if hit:
                enemy_positions.remove(target)
                bullet_position.remove(bull)
                break
    if len(enemy_positions) == 0:
        screen.blit(win_text, (250, screen.get_height() / 2 - 50))

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
