from vpython import *

# Setting up my canvas
scene = canvas(title="Gun Simulation Mechanism", width=800, height=800, background=color.white)

# Gun attributes
gun_length = 6
gun_radius = 0.5
chamber_length = 4

# Create the gun barrel
gun_body = cylinder(pos=vector(-gun_length/2, 0, 0), axis=vector(gun_length, 0, 0), radius=gun_radius, color=color.gray(0.6))
# Create an inner chamber for bullets
chamber = cylinder(pos=vector(-chamber_length/2, 0, 0), axis=vector(chamber_length, 0, 0), radius=gun_radius * 0.7, color=color.blue)

# Bullet properties
bullet_radius = 0.2
bullet_speed = 5
bullet = sphere(pos=vector(-chamber_length/2 + bullet_radius, 0, 0), radius=bullet_radius, color=color.red, make_trail=True, trail_color=color.orange)