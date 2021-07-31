def on_button_pressed_a():
    hero.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    hero.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

rock: game.LedSprite = None
position = 0
hero: game.LedSprite = None
basic.show_leds("""
    . # # # .
        . . . # .
        . # # # .
        . . . # .
        . # # # .
""")
basic.pause(200)
basic.show_leds("""
    . # # . .
        . . . # .
        . . # . .
        . # . . .
        . # # # .
""")
basic.pause(200)
basic.show_leds("""
    . . # . .
        . # # . .
        . . # . .
        . . # . .
        . # # # .
""")
basic.pause(100)
basic.clear_screen()
hero = game.create_sprite(2, 4)

def on_forever():
    global position, rock
    position = randint(0, 4)

    basic.pause(1000)
    rock = game.create_sprite(position, 0)
    for index2 in range(4):
        rock.change(LedSpriteProperty.Y, 1)
        basic.pause(300)

    if rock.is_touching_edge():
        rock.delete()

basic.forever(on_forever)

def on_forever2():
    if rock:
        if rock.is_touching(hero):
            game.game_over()
basic.forever(on_forever2)
