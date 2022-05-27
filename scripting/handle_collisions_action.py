import arcade


class HandleCollisions():
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when robot collides
    with an object.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        

    def LeverCollision(players, levers):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        leversHit = arcade.check_for_collision_with_list(
            players,levers
        )
        for l in leversHit:
            #If not the first lever then check the flip property of the previous lever.
            if l.properties['order'] != 0:
                if levers[int(l.properties['order']-1)].properties['flip']== True:
                    l.properties["flip"] = True
                    #Add flipped texture to list of textures then set to flipped.
                    l.append_texture(arcade.load_texture("placeholder_assets\levers\lever_"+l.properties["color"]+"_down.png"))
                    l.set_texture(1)
            else:
                l.properties["flip"] = True
                l.append_texture(arcade.load_texture("placeholder_assets\levers\lever_"+l.properties["color"]+"_down.png"))
                l.set_texture(1)
        
        

    def _handle_object_collision(self, cast):
        pass
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            pass