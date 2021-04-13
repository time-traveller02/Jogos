import pygame

# Inicializando o pygame e criando a janela
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Palavras Cruzadas")

drawGroup = pygame.sprite.Group()

guy = pygame.sprite.Sprite(drawGroup)
guy.image = pygame.image.load("Data/pixil-frame-0.png")
guy.image = pygame.transform.scale(guy.image, [100, 100])
guy.rect = pygame.Rect(50, 50, 50, 50)


# Desenhando
def draw():
    display.fill([19, 173, 235])

    player = pygame.Rect(50, 50, 100, 100)
    # player.center = [50, 50]
    pygame.draw.rect(display, [255, 255, 255, 255], player)
    drawGroup.draw(display)


GameLoop = True
if __name__ == "__main__":
    while GameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameLoop = False
            # Analizando as teclas que foram pressionadas
            """elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("Apertou w")"""
            # Analizando as teclas que foram soltadas
            """elif event.type == pygame.KEYUP:
                print("Soltou w")"""
        # Analizando as teclas que estam sendo pressionadas
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_d]:
            guy.rect.x += 1
            # print("Segurando w")
        if Keys[pygame.K_a]:
            guy.rect.x -= 1
        if Keys[pygame.K_s]:
            guy.rect.y += 1
        if Keys[pygame.K_w]:
            guy.rect.y -= 1

        draw()
        pygame.display.update()
