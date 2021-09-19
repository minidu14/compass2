def on_pin_pressed_p0():
    basic.show_arrow(ArrowNames.SOUTH)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    basic.show_arrow(ArrowNames.WEST)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    basic.show_arrow(ArrowNames.SOUTH_EAST)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_arrow(ArrowNames.NORTH_EAST)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_logo_pressed():
    basic.show_arrow(ArrowNames.EAST)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    pass
basic.forever(on_forever)
