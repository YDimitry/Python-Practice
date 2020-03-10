# process player input
def get_keyboard_input():
    return input()


player_inputs = {'w': "up", 'a': "left",
                 's': 'down', 'd': 'right',
                 ' ': 'bomb'
                 }


def process_player_input(player_input):
    x, y = game_objects[('player',)]['position']
    if player_input == 'up':
        x = x - 1
    elif player_input == 'down':
        x = x + 1
    elif player_input == 'right':
        y = y + 1
    elif player_input == 'left':
        y = y - 1
    elif player_input == 'bomb':
        new_objects.append(create_object('bomb', (x, y)))
    movements.append((("player",), (x, y)))


# GLOBALS
game_state = "in_progress"
game_objects = {}
new_objects = []
movements = []
interactions = []
old_objects = []


# GAME OBJECTS LOGIC
def idle_logic(_):
    pass


def bomb_logic(bomb_object):
    global old_objects, new_objects, game_objects
    if game_objects[bomb_object]['life_time']:
        game_objects[bomb_object]['life_time'] -= 1
    else:
        x,y = game_objects[bomb_object]['position']
        old_objects += [bomb_object]
        # remove_objects()
        dx, dy = 1, 0
        new_objects += [create_object('heatwave', (x, y))]
        for _ in range(4):
            if not (x-dx)<0 and not (y-dy)<0:
                new_objects += [create_object('heatwave',(x-dx,y-dy))]
            dx, dy = -dy, dx
        # add_new_objects()


def heatwave_logic(heatwave):
    global old_objects
    old_objects += [heatwave]
    # remove_objects()


object_logics = {
    'bomb': bomb_logic,
    'heatwave': heatwave_logic
}


def process_objects_logic():
    for game_object in game_objects:
        object_logics.get(game_object[0], idle_logic)(game_object)


# UTILITIES
def get_objects_by_coords(position):
    return [obj for obj, prop in game_objects.items() if prop.get('position',()) == position]


objects_ids_counter = 0


def get_next_counter_value():
    global objects_ids_counter
    result = objects_ids_counter
    objects_ids_counter += 1
    return result


# OBJECT CREATION
def add_new_objects():
    """В списке new_objects хранятся тройки: тип объекта,
    словарь со всеми его аттрибутами и координаты.
    Функция add_new_objects. добавляет эти объекты в список game_objects,
    если это возможно. Нельзя поставить объект, если место занято объектом
    c аттрибутом interactable == False."""
    for obj_name, prop, coord in new_objects:
        prop.setdefault('position', coord)
        objects = get_objects_by_coords(coord)
        new_obj = obj_name == 'player' and ('player',) or (obj_name,get_next_counter_value())
        if objects:
            for obj in objects:
                if game_objects[obj]['interactable']:
                    game_objects[new_obj] = prop
                    interactions.append((new_obj, obj))
        else:
            game_objects[new_obj] = prop
    new_objects.clear()


obj_types_to_char = {
    "player": "@", "wall": '#', 'soft_wall': '%', 'heatwave': '+', "bomb": '*', "coin": '$'
}


def create_object(type, position, **kwargs):
    desc = {'position': position,
            'passable': type not in ['wall', 'soft_wall'],
            'interactable': type not in ['wall'],
            'char': obj_types_to_char[type]
            }
    if type == 'player':
        desc['coins'] = 0
    if type == 'bomb':
        desc['power'] = 3
        desc['life_time'] = 3
    desc.update(kwargs)
    return type, desc, position


# OBJECT MOVEMENT
def move_objects():
    """Переместить объект в заданные координаты можно только если там нет ни одного объекта,
    у которого в описании аттрибут passable равен False. Если объект перемещается в занятую
    клетку, то он взаимодействует с теми объектами, которые там уже находятся.
    Добавьте соотвествующую пару в список interactions."""
    for obj, coord in movements:
        objects = get_objects_by_coords(coord)
        if objects:
            for obj2 in objects:
                if game_objects[obj2]['passable']:
                    if game_objects[obj2]['interactable']:
                        interactions.append((obj, obj2))
                    game_objects[obj]['position'] = coord
        else: # нет объектов в новых координатах
            game_objects[obj]['position'] = coord
    movements.clear()


# OBJECT REMOVAL
def remove_objects():
    for obj in old_objects:
        if obj in game_objects:
            del game_objects[obj]
    old_objects.clear()


# OBJECT INTERACTIONS
def idle_interaction(o1, o2):
    pass


def player_interaction(player, obj):
    """Когда игрок взаимодействует с монеткой, то монетка исчезает"""
    if 'coin' in obj:
        old_objects.append(obj)


def wave_interaction(wave, obj):
    """Когда ударная волна взаимодействует с мягкой стеной 'soft_wall'
    или игроком, то стена или игрок исчезают."""
    if obj[0] in ['soft_wall','player']:
        old_objects.append(obj)


interaction_funs = {
    'player': player_interaction,
    'heatwave': wave_interaction,
}


def process_interactions():
    for obj1, obj2 in interactions:
        interaction_funs.get(obj1[0], idle_interaction)(obj1, obj2)
        interaction_funs.get(obj2[0], idle_interaction)(obj2, obj1)
    interactions.clear()


def check_game_state():
    global game_objects
    coins = player = False
    for obj in game_objects:
        coins |= 'coin' in obj
        player |= 'player' in obj
    return ('lose', 'win', 'in_progress')[(coins and player)<<1|(not coins and player)]


# GRAPHIC
def draw_screen(screen):
    for line in screen:
        print(''.join(line))


def render_screen():
    screen = [["." for _ in range(10)] for __ in range(10)]
    for obj, desc in game_objects.items():
        x, y = desc['position']
        screen[x][y] = desc['char']
    return screen


# GAME LOAD

level_example = """
##########
#@  %    #
#   %    #
#  %%%   #
# %%$%%  #
#  %%%   #
#   %    #
#   %    #
#   %    #
##########
"""


def load_level(level):
    global new_objects, game_objects
    game_objects.clear()
    level_lines = level.strip().splitlines()
    for y,line in enumerate(level_lines):
        for x, el in enumerate(line):
            type = next((type for type, symb in obj_types_to_char.items() if el == symb), None)
            if type:
                new_objects += [create_object(type,(x,y))]
    add_new_objects()


# GAME

load_level(level_example)
screen = render_screen()
draw_screen(screen)

while game_state == 'in_progress':

    kb_inp = get_keyboard_input()
    if kb_inp == "ESC":
        game_state = "finished"
        break

    if kb_inp in player_inputs:
        process_player_input(player_inputs[kb_inp])

    process_objects_logic()
    add_new_objects()
    move_objects()
    process_interactions()
    remove_objects()

    screen = render_screen()
    draw_screen(screen)

    game_state = check_game_state()

if game_state == 'win':
    print("You win")
elif game_state == 'lose':
    print("You lost")
else:
    print("Bye Bye!")