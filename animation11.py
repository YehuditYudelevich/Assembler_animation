import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1200, 800
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'light_gray': (220, 220, 220)
}
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('animation11')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Define words and corresponding binary codes
words = [
    'Main: add r3, LIST',
    'jsr fn1',
    'LOOP: prn #48',
    'lea STR, r6',
    'inc r6',
    'mov *r6, L3',
    'sub r1, r4',
    'cmp r3, #-6',
    'bne END',
    'add r7, *r6'
]

binary_codes = [
    ["001010000010100", "000000011000100", "000010001001010"],
    ["110100000010100", "000000000000001"],
    ["110000000001100", "000000110000100"],
    ["010000101000100", "000010000100010", "000000000110100"],
    ["011100001000100", "000000000110100"],
    ["000001000010100", "000000110000100", "000000000000001"],
    ["001110001000100", "000000001100100"],
    ["000110000001100", "000000011000100", "111111111010100"],
    ["101000000010100", "000010000011010"],
    ["001010000100100", "000000111110100"],
]

def draw_rounded_rect(surface, color, rect, radius=20):
    """Draw a rounded rectangle"""
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def encode_word(word, x, y):
    draw_rounded_rect(screen, colors['black'], (x, y, 280, 40), 10)
    text = font.render(word, True, colors['white'])
    screen.blit(text, (x + 10, y + 10))

def encode_number(binary_code, x, y):
    draw_rounded_rect(screen, colors['black'], (x, y, 280, 40), 10)
    text = font.render(binary_code, True, colors['white'])
    screen.blit(text, (x + 10, y + 10))

def draw_the_box(color, x, y, width, height):
    draw_rounded_rect(screen, color, (x, y, width, height), 20)
    font = pygame.font.Font(None, 50)
    text = font.render('Assembler', True, colors['black'])
    text_rect = text.get_rect(center=(x + width // 2, y + 40))
    screen.blit(text, text_rect)

def display_explanation(text, y):
    font = pygame.font.Font(None, 40)
    explanation_text = font.render(text, True, colors['black'])
    text_rect = explanation_text.get_rect(center=(width // 2, y))
    screen.blit(explanation_text, text_rect)

def display_assembler_description():
    descriptions = [
        "The assembler translates assembly code into machine language.",
        "It converts instructions into binary code.",
        "Each assembly instruction is translated into several machine words.",
        "This process enables direct communication with the hardware."
    ]
    for i, desc in enumerate(descriptions):
        font = pygame.font.Font(None, 30)
        text = font.render(desc, True, colors['black'])
        screen.blit(text, (20, height - 200 + i * 30))

def process_word(word, binary_code):
    assembler_x, assembler_y = 450, height // 2 - 150
    assembler_width, assembler_height = 300, 300
    x, y = -300, height // 2 - 20

    # Word moving into the assembler
    while x < assembler_x + assembler_width:
        screen.fill(colors['light_gray'])
        display_assembler_description()
        
        # Draw the word only if it's not fully inside the box
        if x < assembler_x + assembler_width - 300:
            encode_word(word, x, y)
        
        # Draw the assembler box on top of the word
        draw_the_box(colors['red'], assembler_x, assembler_y, assembler_width, assembler_height)
        display_explanation(f"Processing word: {word}", 100)
        display_explanation(f"Number of binary words: {len(binary_code)}", 150)
        
        pygame.display.flip()
        x += 5
        clock.tick(80)

    # Word is inside the assembler
    screen.fill(colors['light_gray'])
    display_assembler_description()
    draw_the_box(colors['green'], assembler_x, assembler_y, assembler_width, assembler_height)
    display_explanation(f"Processing word: {word}", 100)
    display_explanation(f"Number of binary words: {len(binary_code)}", 150)
    pygame.display.flip()
    pygame.time.wait(5)

    # Binary codes coming out
    bx, by = assembler_x + assembler_width, height // 2 - 20
    for i, code in enumerate(binary_code):
        while bx < width + 300:
            screen.fill(colors['light_gray'])
            display_assembler_description()
            draw_the_box(colors['green'], assembler_x, assembler_y, assembler_width, assembler_height)
            display_explanation(f"Binary output: {code}", 100)
            display_explanation(f"Binary word {i+1} of {len(binary_code)}", 150)
            encode_number(code, bx, by)
            pygame.display.flip()
            bx += 5
            clock.tick(60)
        bx = assembler_x + assembler_width
        pygame.time.wait(5)

def main_process():
    for word, binary_code in zip(words, binary_codes):
        screen.fill(colors['light_gray'])
        display_assembler_description()
        
        assembler_x, assembler_y = 450, height // 2 - 150
        assembler_width, assembler_height = 300, 300
        draw_the_box(colors['red'], assembler_x, assembler_y, assembler_width, assembler_height)
        display_explanation(f"Processing: {word}", 700)
        display_explanation(f"Number of binary words: {len(binary_code)}", 750)
        pygame.display.flip()
        process_word(word, binary_code)
        pygame.time.wait(5)

# Main loop
main_process()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)