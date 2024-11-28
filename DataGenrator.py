import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
FRAME_WIDTH = 5.0  # Frame size in simulation units
FRAME_HEIGHT = 5.0
FRAME_DISCRETIZATION = 0.1  # Step size
SPEED = 0.2  # Weed movement speed
ROTATION_ANGLE = 10  # Rotation in degrees
SCREEN_WIDTH = 500  # Pixel width of the window
SCREEN_HEIGHT = 500  # Pixel height of the window
CELL_WIDTH = SCREEN_WIDTH // int(FRAME_WIDTH / FRAME_DISCRETIZATION)
CELL_HEIGHT = SCREEN_HEIGHT // int(FRAME_HEIGHT / FRAME_DISCRETIZATION)
FONT_SIZE = 16

# Screen and fonts
screen = pygame.display.set_mode((SCREEN_WIDTH + 100, SCREEN_HEIGHT + 50))  # Extra space for numbering
pygame.display.set_caption("Weed Simulation")
font = pygame.font.Font(None, FONT_SIZE)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Weed data structure
class Weed:
    id_counter = 1

    def __init__(self, x, y, speed, angle):
        self.id = Weed.id_counter
        Weed.id_counter += 1
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Unique color

    def update_position_approx(self):
        # Move weed according to speed and rotation
        self.x += self.speed
        self.y += self.speed * (random.choice([-1, 1]) * self.angle / 90)
    
    def update_position(self):
        self.x += self.speed
        self.y += self.speed * self.angle / 90

# Simulation data
weed_approx_list = []
weed_list = []

def generate_new_weed():
    """Generate a new weed at x=0.0 and a random y-coordinate."""
    y = round(random.uniform(0, FRAME_HEIGHT), 1)
    weed = Weed(0.0, y, SPEED, ROTATION_ANGLE)
    weed_approx = Weed(0.0, y, SPEED, ROTATION_ANGLE)
    weed_approx_list.append(weed_approx)
    weed_list.append(weed)


def update_weed_positions():
    """Update all weed positions."""
    for weed in weed_approx_list:
        weed.update_position_approx()
    
    for weed in weed_list:
        weed.update_position()

def draw_frame():
    """Draw the frame, weeds, and numbering."""
    # Clear the screen
    screen.fill(WHITE)

    # Draw border
    pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2)

    # Draw vertical and horizontal grid lines
    for i in range(int(FRAME_WIDTH / FRAME_DISCRETIZATION)):
        x = i * CELL_WIDTH
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for i in range(int(FRAME_HEIGHT / FRAME_DISCRETIZATION)):
        y = i * CELL_HEIGHT
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

    # Draw weeds
    for weed in weed_approx_list:
        # Convert weed coordinates to pixels
        pixel_x = int(weed.x / FRAME_DISCRETIZATION * CELL_WIDTH)
        pixel_y = int(weed.y / FRAME_DISCRETIZATION * CELL_HEIGHT)

        # Draw weed as a circle with its unique color
        pygame.draw.circle(screen, weed.rgb, (pixel_x, pixel_y), 5)

        # Draw weed ID
        id_text = font.render(f"{weed.id}", True, BLACK)
        screen.blit(id_text, (pixel_x + 10, pixel_y - 10))

    for weed in weed_list:
        # Convert weed coordinates to pixels
        pixel_x = int(weed.x / FRAME_DISCRETIZATION * CELL_WIDTH)
        pixel_y = int(weed.y / FRAME_DISCRETIZATION * CELL_HEIGHT)

        # Draw weed as a circle with its unique color
        pygame.draw.circle(screen, BLACK, (pixel_x, pixel_y), 5)

    # Draw y-axis numbering (right side)
    for i in range(int(FRAME_HEIGHT / FRAME_DISCRETIZATION)):
        label = f"{i * FRAME_DISCRETIZATION:.1f}"
        text = font.render(label, True, BLACK)
        screen.blit(text, (SCREEN_WIDTH + 10, i * CELL_HEIGHT - FONT_SIZE // 2))

    # Draw x-axis numbering (bottom)
    # Integer part (e.g., 00000)
    for i in range(int(FRAME_WIDTH / FRAME_DISCRETIZATION)):
        x_pos = i * CELL_WIDTH
        label = f"{int(i * FRAME_DISCRETIZATION // 1)}"
        text = font.render(label, True, BLACK)
        screen.blit(text, (x_pos + CELL_WIDTH // 4, SCREEN_HEIGHT + 5))

    # Dots row (e.g., . . . . .)
    for i in range(int(FRAME_WIDTH / FRAME_DISCRETIZATION)):
        x_pos = i * CELL_WIDTH
        dot_text = font.render(".", True, BLACK)
        screen.blit(dot_text, (x_pos + CELL_WIDTH // 4, SCREEN_HEIGHT + 20))

    # Fractional part row (e.g., 0123456789)
    for i in range(int(FRAME_WIDTH / FRAME_DISCRETIZATION)):
        x_pos = i * CELL_WIDTH
        label = f"{int(i * FRAME_DISCRETIZATION % 1 * 10)}"
        text = font.render(label, True, BLACK)
        screen.blit(text, (x_pos + CELL_WIDTH // 4, SCREEN_HEIGHT + 35))

def main():
    """Main simulation loop."""
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update simulation
        if random.choice([0, 1]) > 0.7:
            generate_new_weed()
        update_weed_positions()

        # Draw everything
        draw_frame()

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(5)  # 10 FPS

    # On exit, log final state
    print("Simulation stopped. Final weed list:")
    for weed in weed_list:
        print(f"Weed ID: {weed.id}, Position: ({weed.x:.1f}, {weed.y:.1f}), Color: {weed.rgb}")

    pygame.quit()

if __name__ == "__main__":
    main()
