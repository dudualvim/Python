import time
import pygame
import sys

pygame.init()

# Configurações da janela
width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo de Corrida")

clock = pygame.time.Clock()

def draw_track():
    # Carregue a imagem da pista de corrida aqui
    track_image = pygame.image.load('assets/pista.jpg')
    win.blit(track_image, (0, 0))

def draw_car(x, y, car_image):
    car = pygame.image.load(car_image)
    win.blit(car, (x, y))

def main():
    # Caminhos para as imagens dos carros
    ferrari_image = 'assets/ferrari2.jpg'
    lamborghini_image = 'assets/ferrari.jpg'
    
    distancia = width - 200  # Distância da pista em pixels
    
    velocidade_ferrari = 5  # Valor de exemplo
    velocidade_lamborghini = 4  # Valor de exemplo
    
    pos_ferrari = 0
    pos_lamborghini = 0
    
    while pos_ferrari < distancia and pos_lamborghini < distancia:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pos_ferrari += velocidade_ferrari
        pos_lamborghini += velocidade_lamborghini
        
        win.fill((255, 255, 255))
        
        draw_track()
        
        draw_car(pos_ferrari, height - 100, ferrari_image)
        draw_car(pos_lamborghini, height - 50, lamborghini_image)
        
        pygame.display.update()
        clock.tick(30)
    
    print("\nCorrida finalizada!")
    
    if pos_ferrari > pos_lamborghini:
        print("A Ferrari venceu!")
    elif pos_lamborghini > pos_ferrari:
        print("A Lamborghini venceu!")
    else:
        print("Foi um empate!")
    
    pygame.quit()

if __name__ == "__main__":
    main()
