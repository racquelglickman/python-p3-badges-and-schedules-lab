def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]

def printer(names):
    for entry in batch_badge_creator(names):
        print(entry)
    for entry in assign_rooms(names):
        print(entry)