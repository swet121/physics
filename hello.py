import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Simulation")

black = (0, 0, 0)
white = (255, 255, 255)


background_img = pygame.transform.scale(pygame.image.load("space.jpg"), (WIDTH, HEIGHT))
planet_img = pygame.transform.scale(pygame.image.load("earth.png"), (300, 150)) 
rocket_img = pygame.transform.scale(pygame.image.load("rocket.png"), (80, 80))  


font_path = "Rubik.ttf"  
font_size = 36
font = pygame.font.Font(font_path, font_size)

def draw_background():
    win.blit(background_img, (0, 0))

def draw_planet(x, y):
    win.blit(planet_img, (x, y))

def draw_rocket(x, y):
    win.blit(rocket_img, (x - rocket_img.get_width() // 2, y - rocket_img.get_height() // 2))

def display_message(message):
    text = font.render(message, True, white)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    win.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(10000)  

def calculate_escape_velocity(mass, celestial_body_radius):
    gravitational_constant = 6.674 * (10 ** -11)
    escape_velocity = math.sqrt((2 * gravitational_constant * mass) / celestial_body_radius)
    return escape_velocity

def calculate_rocket_position(initial_velocity, launch_angle, time):
    g = 9.8
    launch_angle_rad = math.radians(launch_angle)
    x = initial_velocity * math.cos(launch_angle_rad) * time
    y = (initial_velocity * math.sin(launch_angle_rad) * time) - (0.5 * g * (time ** 2))
    return x, HEIGHT - y

def main():
    clock = pygame.time.Clock()

    planet_x = 0
    planet_y = HEIGHT - planet_img.get_height()  

    
    draw_background()
    draw_planet(planet_x, planet_y)


    escape_velocity = calculate_escape_velocity(5.972 * (10 ** 24), 6371 * 10**3)  
    print(f"Escape Velocity of the earth is : {escape_velocity} m/s")


    initial_velocity = float(input("Enter the initial velocity of the rocket (in m/s): "))

    if initial_velocity < escape_velocity:
        print("Check The Simulation")
        message = "Rocket Couldn't Escape"
        display_message(message)
        pygame.quit()
        sys.exit()


    launch_angle = float(input("Enter launch angle (degrees): "))
    print("Rocket launched")
    rocket_x = WIDTH // 2
    rocket_y = HEIGHT - 10  

    time = 0
    time_step = 0.0005
    fps = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_background()
        draw_planet(planet_x, planet_y)

        rocket_x, rocket_y = calculate_rocket_position(initial_velocity, launch_angle, time)

        draw_rocket(rocket_x, rocket_y)

        pygame.display.flip()

        time += time_step

        clock.tick(fps)


        if rocket_y < 0:
            message = "You escaped!"
            display_message(message)
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
