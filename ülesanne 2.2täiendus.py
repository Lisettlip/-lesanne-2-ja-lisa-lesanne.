import pygame
import sys
import os
import math

os.chdir(r"C:\Users\lisett.liplap\PyCharmMiscProject")

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne 2")

bg = pygame.image.load("bg_shop.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

seller = pygame.image.load("seller.png").convert_alpha()
seller_width = 265
seller_height = 314
seller = pygame.transform.scale(seller, (seller_width, seller_height))
seller_x = 104
seller_y = 139

chat = pygame.image.load("chat.png").convert_alpha()
chat_width = 231
chat_height = 183
chat = pygame.transform.scale(chat, (chat_width, chat_height))
chat_x = 263
chat_y = 68

cake = pygame.image.load("tort.png.png").convert_alpha()
cake.set_colorkey((0, 0, 0))
cake_width = 73
cake_height = 76
cake = pygame.transform.scale(cake, (cake_width, cake_height))
cake_x = 403
cake_y = 211

sword = pygame.image.load("mõõk.png").convert_alpha()
sword.set_colorkey((0, 0, 0))
sword_width = 62
sword_height = 169
sword = pygame.transform.scale(sword, (sword_width, sword_height))
sword_x = 560
sword_y = 101

logo = pygame.image.load("VIKK logo.png").convert_alpha()
logo_width = 324
logo_height = 43
logo = pygame.transform.scale(logo, (logo_width, logo_height))
logo_x = 14
logo_y = 15

font = pygame.font.SysFont("Arial", 22)
text_surface = font.render("Tere, Lisett", True, (255, 255, 255))
text_x = chat_x + (chat_width // 2) - (text_surface.get_width() // 2)
text_y = chat_y + 65

# Kaartekst "TULEVIK 2050"
# Kaartekst "TULEVIK 2050"
font2 = pygame.font.SysFont("Arial", 16, bold=True)
arc_text = "TULEVIK 2050"

arc_cx = 320
arc_cy = 32
arc_radius = 33

# parem kaare algus (keskelt)
total_angle = math.pi * 0.8
arc_start = -total_angle / 2 - 0.7

# segatud roheline (mitte liiga hele ega tume)
nice_green = (100, 200, 120)

for i, char in enumerate(arc_text):
    angle = arc_start + i * (total_angle / (len(arc_text) - 1))

    x = arc_cx + int(arc_radius * math.cos(angle))
    y = arc_cy + int(arc_radius * math.sin(angle))

    char_surf = font2.render(char, True, nice_green)

    # keerab tähed kaare järgi (ilusam)
    char_surf = pygame.transform.rotate(char_surf, -math.degrees(angle))

    rect = char_surf.get_rect(center=(x, y))
    screen.blit(char_surf, rect)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0, 0))
    screen.blit(sword, (sword_x, sword_y))
    screen.blit(cake, (cake_x, cake_y))
    screen.blit(seller, (seller_x, seller_y))
    screen.blit(chat, (chat_x, chat_y))
    screen.blit(text_surface, (text_x, text_y))
    screen.blit(logo, (logo_x, logo_y))

    for i, char in enumerate(arc_text):
        angle = arc_start + i * (math.pi / len(arc_text)) * 1.4
        x = arc_cx + int(arc_radius * math.cos(angle))
        y = arc_cy + int(arc_radius * math.sin(angle))
        char_surf = font2.render(char, True, (255, 255, 255))
        char_surf = pygame.transform.rotate(char_surf, -math.degrees(angle) - 90)
        screen.blit(char_surf, (x, y))

    pygame.display.flip()
    clock.tick(60)