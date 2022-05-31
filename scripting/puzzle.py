import arcade

class HandlePuzzle():

    def __init__(self) -> None:
        pass

    def leversDoor( levers, doors):
        # Check if all levers are flipped for door
        if levers[2].properties['flip'] == True:
            for block in doors:
                block.remove_from_sprite_lists()

    def leversBridge(levers,bridge,physicsEngine):
        #check if all levers are flipped for bridge
        if levers[6].properties['flip'] == True:
            bridge.visible = True
            #self.wallsList.append(self.scene['Bridge'])
            physicsEngine.walls.append(bridge)