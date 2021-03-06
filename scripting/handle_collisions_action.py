from operator import truediv
import arcade

num_list = []
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
        

    def LeverCollision(players, levers): #, num_screens, num_list, block
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
            # if l.properties['order'] != 0:
            #     if levers[int(l.properties['order']-1)].properties['flip']== True:
            #         l.properties["flip"] = True
            #         #Add flipped texture to list of textures then set to flipped.
            #         l.append_texture(arcade.load_texture("placeholder_assets/levers/lever_"+l.properties["color"]+"_down.png"))
            #         l.set_texture(1)
            # else:
            # if block == True:
                if l.properties["flip"] != True:
                    l.properties["flip"] = True
                    l.append_texture(arcade.load_texture("placeholder_assets/levers/lever_"+l.properties["color"]+"_down.png"))
                    l.set_texture(1)
                    # if block == False:
                    #     for n in num_screens:
                    #         if n.properties["order"] == num_list:

                    return l.properties["order"]
                    # num_list.append(l.properties["order"])
                    # if len(num_list) == 4:
                    #     if block == True:
                    #         if num_list[0] == 1 and num_list[1] == 9 and num_list[2] == 2 and num_list[3] == 7:
                    #             num_list.clear()
                    #             return False     
                    #         elif num_list[0] == 2 and num_list[1] == 9 and num_list[2] == 6 and num_list[3] == 1:  
                    #             num_list.clear()
                    #             return False
                    #         else:
                    #             num_list.clear()
                    #             for n in levers:
                    #                 n.properties["flip"] = False
                    #                 n.append_texture(arcade.load_texture("placeholder_assets/levers/lever_"+n.properties["color"]+"_up.png"))
                    #                 n.set_texture(1)
                    #                 return True
                    #     else:
                    #         if num_list[0] == 7 and num_list[1] == 4 and num_list[2] == 3 and num_list[3] == 2:   
                    #             num_list.clear()
                    #             return True
                    #         elif num_list[0] == 2 and num_list[1] == 3 and num_list[2] == 5 and num_list[3] == 9:
                    #             num_list.clear()
                    #             return True
                    #         else:
                    #             num_list.clear()
                    #             for n in levers:
                    #                 n.properties["flip"] = False
                    #                 n.append_texture(arcade.load_texture("placeholder_assets/levers/lever_"+n.properties["color"]+"_up.png"))
                    #                 n.set_texture(1)
                    #                 return False

                    
        
        

    def DangerCollision(players, danger):
        dangersHit = arcade.check_for_collision_with_list(
            players,danger
        )
        for l in dangersHit:
            return True
        return False
    
    def PortalCollision(players, portal):
        portalHit = arcade.check_for_collision_with_list(
            players,portal
        )
        for l in portalHit:
            return True
        return False

    def CheckpointCollision(players, checkpoint):
        checkpointHit = arcade.check_for_collision_with_list(
            players,checkpoint
        )
        for l in checkpointHit:
            return True
        return False

            
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            pass