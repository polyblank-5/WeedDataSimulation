import random
import time
from colorama import init

# Initialize colorama for colored console output
init(autoreset=True)

# Constants
FRAME_WIDTH = 50  # Reduced frame size
FRAME_HEIGHT = 50  # Reduced frame size
UPDATE_INTERVAL = 0.1  # 100ms
SPEED = 2  # Movement speed in pixels per update
ROTATION_ANGLE = 10  # Rotation in degrees per update

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
        self.rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update_position(self):
        # Move weed according to speed and rotation
        self.x += self.speed
        self.y += int(self.speed * (random.choice([-1, 1]) * self.angle / 90))

# Simulation setup
weed_list = []

def generate_new_weed():
    """Generate a new weed at x=0 and random y."""
    y = random.randint(0, FRAME_HEIGHT - 1)
    weed = Weed(x=0, y=y, speed=SPEED, angle=ROTATION_ANGLE)
    weed_list.append(weed)

def update_weed_positions():
    """Update all weed positions in the list."""
    for weed in weed_list:
        weed.update_position()

def visualize_frame():
    """Visualize the 50x50 frame with weeds, their IDs, and a border."""
    frame = [[' ' for _ in range(FRAME_WIDTH)] for _ in range(FRAME_HEIGHT)]

    for weed in weed_list:
        if 0 <= weed.x < FRAME_WIDTH and 0 <= weed.y < FRAME_HEIGHT:
            # Create a visual representation of the weed with its ID
            r, g, b = weed.rgb
            id_display = f"\033[38;2;{r};{g};{b}m*{weed.id}\033[0m"

            # Ensure the weed fits in the frame horizontally
            max_chars = FRAME_WIDTH - weed.x  # Maximum characters that fit
            id_display = id_display[:max_chars]  # Truncate if necessary

            for i, char in enumerate(id_display):
                frame[weed.y][weed.x + i] = char

    # Add the border to the frame
    horizontal_border = "#" * (FRAME_WIDTH + 2)  # Top and bottom border
    print("\033[H\033[J", end="")  # Clear console
    print(horizontal_border)  # Top border
    for row in frame:
        print(f"#{''.join(row)}#")  # Left and right border
    print(horizontal_border)  # Bottom border


def log_weed_list():
    """Log the weed list."""
    print("\n[LOG] Final State of weed_list:")
    for weed in weed_list:
        print(f"Weed ID: {weed.id}, Position: ({weed.x}, {weed.y}), "
              f"Speed: {weed.speed}, Angle: {weed.angle}, RGB: {weed.rgb}")

def main():
    """Main simulation loop."""
    try:
        while True:
            generate_new_weed()
            update_weed_positions()
            visualize_frame()
            time.sleep(UPDATE_INTERVAL)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
        log_weed_list()  # Display the weed list on simulation stop

if __name__ == "__main__":
    main()
