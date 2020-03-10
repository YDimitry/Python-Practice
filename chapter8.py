# import base64
# print(base64.b64encode(b'user123:pass321'))

# ========================= Программирование Python =======================
# tree = {}
#
# for _ in range(int(input()) - 1):
#     child, parent = input().split()
#     tree.setdefault(parent, [])
#     tree.setdefault(child, []).append(parent)
#
#
# def count_parents(parents):
#     if parents:
#         c = len(parents)
#         for par in parents:
#             c += count_parents(tree[par])
#         return c
#     return 0
# e = {}
#
# for k,v in tree.items():
#     e[k] = count_parents(v)
#
# for i in sorted(e):
#     print(i,e[i])

# goods = {}
#
# for _ in range(int(input())):
#     buyer, item, quant = input().split()
#     d = goods.setdefault(buyer, dict())
#     d.setdefault(item, 0)
#     goods[buyer][item] += int(quant)
#
# for buyer in sorted(goods):
#     print(f'{buyer}:')
#     for item in sorted(goods[buyer]):
#         print(item,goods[buyer][item])

# d = {}
# for _ in range(int(input())):
#     tmp = input().split()
#     d[tmp[0]] = tmp[1:]
# for _ in range(int(input())):
#     city = input()
#     [print(k) for k, v in d.items() if city in v]

# ============================ Введение в Python. Практикум =============================
game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'},
    ('coin', 2): {'position': (1, 2), 'passable': True, 'interactable': True, 'char': '$'}
}
old_objects = []
def get_objects_by_coords(position):
    return [obj for obj, prop in game_objects.items() if prop.get('position',()) == position]

def remove_objects():
    for obj in old_objects:
        if obj in game_objects:
            del game_objects[obj]
    old_objects.clear()

interactions = []

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

objects_ids_counter = 0

def get_next_counter_value():
    global objects_ids_counter
    result = objects_ids_counter
    objects_ids_counter += 1
    return result

def add_new_objects():
    """В списке new_objects хранятся тройки: тип объекта,
    словарь со всеми его аттрибутами и координаты.
    Функция add_new_objects. добавляет эти объекты в список game_objects,
    если это возможно. Нельзя поставить объект, если место занято объектом
    c аттрибутом interactable == False."""
    for obj_name, prop, coord in new_objects:
        prop.setdefault('position', coord)
        objects = get_objects_by_coords(coord)
        if objects:
            if all([game_objects[obj]['interactable'] for obj in objects]):
                game_objects[(obj_name,get_next_counter_value())] = prop
        else:
            game_objects[(obj_name,get_next_counter_value())] = prop
    new_objects.clear()

game_objects = {('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
                ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
                ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
                ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'}}

new_objects = [('bomb', {'passable': True, 'interactable': True, 'lifetime': 5}, (1, 1))]

add_new_objects()

print(get_objects_by_coords((1, 1)))




















