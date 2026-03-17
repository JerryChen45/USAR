''''
button 0 = A
button 1 = B
button 2 = X
button 3 = Y
button 4 = view
button 5 = xbox
button 6 = menu
button 7 = left stick click
button 8 = right stick click
button 9 = LB
button 10 = RB
button 11 = up
button 12 = down
button 13 = left
button 14 = right

AXIS_LX = 0   # left stick left -1 /right 1
AXIS_LY = 1   # left stick up -1 /down 1
AXIS_RX = 2   # right stick  left -1 /right 1
AXIS_RY = 3   # right stick up -1 /down 1
AXIS_LT = 4   # left trigger, rest=-1.0, pressed=1.0
AXIS_RT = 5   # right trigger, rest=-1.0, pressed=1.0
'''

import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected.")
    raise SystemExit

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Connected controller:", joystick.get_name())
print("Axes:", joystick.get_numaxes())
print("Buttons:", joystick.get_numbuttons())
print("Hats:", joystick.get_numhats())
print("Move controls now...\n")

prev_axes = None
prev_buttons = None
prev_hats = None

while True:
    pygame.event.pump()

    axes = tuple(round(joystick.get_axis(i), 3) for i in range(joystick.get_numaxes()))
    buttons = tuple(joystick.get_button(i) for i in range(joystick.get_numbuttons()))
    hats = tuple(joystick.get_hat(i) for i in range(joystick.get_numhats()))

    if axes != prev_axes or buttons != prev_buttons or hats != prev_hats:
        print("Axes   :", axes)
        print("Buttons:", buttons)
        print("Hats   :", hats)
        print("-" * 50)

        prev_axes = axes
        prev_buttons = buttons
        prev_hats = hats