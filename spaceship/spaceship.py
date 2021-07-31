def on_button_pressed_a():
    item.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global bullet
    bullet = game.create_sprite(0, item.get(LedSpriteProperty.Y))
    for index in range(4):
        bullet.change(LedSpriteProperty.X, 1)
        basic.pause(100)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    item.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.B, on_button_pressed_b)

enemy_bullet: game.LedSprite = None
position = 0
bullet: game.LedSprite = None
item: game.LedSprite = None
basic.show_string("Starting in")
basic.pause(100)
basic.show_leds("""
    . # # # .
        . . . # .
        . # # # .
        . . . # .
        . # # # .
""")
basic.pause(500)
basic.show_leds("""
    . # # . .
        . . . # .
        . . # . .
        . # . . .
        . # # # .
""")
basic.pause(500)
basic.show_leds("""
    . . # . .
        . # # . .
        . . # . .
        . . # . .
        . # # # .
""")
basic.pause(500)
basic.clear_screen()
basic.show_string("Go!")
game.set_score(0)
item = game.create_sprite(0, 2)
enemy = game.create_sprite(4, 2)

def on_forever():
    global position, enemy_bullet
    position = randint(0, 4)
    enemy.set(LedSpriteProperty.Y, position)
    basic.pause(1000)
    if bullet:
        if bullet.is_touching(enemy):
            game.add_score(1)
            enemy_bullet.delete()
    enemy_bullet = game.create_sprite(4, enemy.get(LedSpriteProperty.Y))
    for index2 in range(4):
        enemy_bullet.change(LedSpriteProperty.X, -1)
        basic.pause(100)
    if bullet:
        if bullet.is_touching_edge():
            bullet.delete()
    if enemy_bullet.is_touching_edge():
        enemy_bullet.delete()
    if game.score() == 5:
        game.game_over()
basic.forever(on_forever)

def on_forever2():
    if enemy_bullet:
        if enemy_bullet.is_touching(item):
            game.game_over()
basic.forever(on_forever2)
