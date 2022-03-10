from game.scripting.action import Action

class MoveActorsAction(Action):
    def __init__(self) -> None:
        pass

    def execute(self, cast, script) -> None:
        for actor in cast.get_all_actors():
            actor.move_next()