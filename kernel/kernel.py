from brain.cortex import think
from world.model import load as load_world
from world.model import save as save_world


class PartnerKernel:

    def __init__(self):

        self.world = load_world()

    def run(self, message):

        self.world["last_message"] = message

        save_world(self.world)

        reply = think(message)

        return reply


kernel = PartnerKernel()
