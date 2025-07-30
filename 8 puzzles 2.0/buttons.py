import pygame
from pygame.locals import *

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
        self.font = pygame.font.SysFont('Arial', font_size)

    def draw(self, surface):
        # Draw button background (changes color on hover)
        button_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, button_color, self.rect, border_radius=8)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2, border_radius=8)  # Border

        # Draw button text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def update_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            return self.rect.collidepoint(event.pos)
        return False