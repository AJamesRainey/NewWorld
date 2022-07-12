"""
Platformer Game
"""
from pickle import NONE
from xmlrpc.client import boolean
import arcade
import scripting.handle_collisions_action as collisions
import scripting.puzzle as puzzle
import constants as CONSTANT


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(CONSTANT.SCREEN_WIDTH, CONSTANT.SCREEN_HEIGHT, CONSTANT.SCREEN_TITLE)

        self.point_x = 128
        self.point_y = 1744

        # This is the stage that your on.
        self.stage_num = 2

        self.num_list = []

        self.block = True
        self.bridge = False

        # Our TileMap Object

        self.tile_map = None


        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Keep track of the score
        self.score = 0

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        self.wallsList = None

        arcade.set_background_color(arcade.csscolor.GRAY)

    # def main():
    # """ Main function """

    #     window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    #     start_view = InstructionView()
    #     window.show_view(start_view)
    #     arcade.run()

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)


        # Name of map file to loads


        # Layer specific options are defined based on Layer names in a dictionary

        # Doing this will make the SpriteList for the platforms layer

        # use spatial hashing for detection.

        layer_options = {

            "Platforms": {

                "use_spatial_hash": True,

            },
            'Blocking': {
                'use_spatial_hash': True,
            },
            'Bridge': {
                'use_spatial_hash': True,
            }

        }



        # Read in the tiled map
        # map_name = f":resources:tiled_maps/map2_level_{self.level}.json"
        if self.stage_num == 0:
            self.tile_map = arcade.load_tilemap(f"maps/start_screen2.tmx", CONSTANT.TILE_SCALING, layer_options)
        elif self.stage_num == 1:
            self.tile_map = arcade.load_tilemap(f"Stage_{self.stage_num}.tmx", CONSTANT.TILE_SCALING, layer_options)
        elif self.stage_num == 2:
            self.tile_map = arcade.load_tilemap(f"Stage_1.tmx", CONSTANT.TILE_SCALING, layer_options)
        elif self.stage_num == 3:
            self.tile_map = arcade.load_tilemap(f"Stage_2.tmx", CONSTANT.TILE_SCALING, layer_options)
        elif self.stage_num == 4:
            self.tile_map = arcade.load_tilemap(f"Stage_3.tmx", CONSTANT.TILE_SCALING, layer_options)
        elif self.stage_num == 5:
            self.tile_map = arcade.load_tilemap(f"Stage_4.tmx", CONSTANT.TILE_SCALING, layer_options)
        elif self.stage_num == 6:
            self.tile_map = arcade.load_tilemap(f"Stage_.tmx", CONSTANT.TILE_SCALING, layer_options)
        elif self.stage_num == 10:
            self.tile_map = arcade.load_tilemap(f"you_died.tmx", CONSTANT.TILE_SCALING, layer_options)



        # Initialize Scene with our TileMap, this will automatically add all layers

        # from the map as SpriteLists in the scene in the proper order.

        self.scene = arcade.Scene.from_tilemap(self.tile_map)


        # Keep track of the score
        self.score = 0

        # Set up the player, specifically placing it at these coordinates.
        image_source = "Ozie/ozie_nomove.png"
        self.player_sprite = arcade.Sprite(image_source, CONSTANT.CHARACTER_SCALING)
        self.player_sprite.center_x = self.point_x
        self.player_sprite.center_y = self.point_y
        self.scene.add_sprite("Player", self.player_sprite)


        # --- Other stuff

        # Set the background color

        if self.tile_map.background_color:

            arcade.set_background_color(self.tile_map.background_color)



        # Create the 'physics engine'
        self.wallsList = [self.scene["Platforms"],self.scene['Blocking']]

        self.physics_engine = arcade.PhysicsEnginePlatformer(

            self.player_sprite, gravity_constant=CONSTANT.GRAVITY, walls=(self.wallsList)

        )


    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()


        # Draw our Scene

        self.scene.draw()


        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.WHITE,
            18,
        )

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = CONSTANT.PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -CONSTANT.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = CONSTANT.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.E:
            col_num = collisions.HandleCollisions.LeverCollision(self.player_sprite,self.scene['Levers'])
            if col_num == None:
                pass
            else:
                self.num_list.append(col_num)
            for n in self.num_list:
                if n == None:
                    del self.num_list[n]
            # if self.block == True:
            #     self.block = collisions.HandleCollisions.LeverCollision(self.player_sprite,self.scene['Levers'], self.block)
            # else: 
            #     self.bridge = collisions.HandleCollisions.LeverCollision(self.player_sprite,self.scene['Levers'], self.block)
            print(self.num_list)
            if self.block == True:
                for n in self.scene['Problem_Screen']:
                    if n.properties["number"] == len(self.num_list):
                        n.append_texture(arcade.load_texture(f"placeholder_assets/math/{int(self.num_list[len(self.num_list)-1])}.png"))
                        n.set_texture(1)
            else: 
                for n in self.scene['Problem_Screen']:
                    if n.properties["number"] == len(self.num_list)+ 4:
                        n.append_texture(arcade.load_texture(f"placeholder_assets/math/{int(self.num_list[len(self.num_list)-1])}.png"))
                        n.set_texture(1)
            if len(self.num_list) == 4:
                # if self.stage_num == 2:
                # stage 1
                if self.num_list[0] == 1 and self.num_list[1] == 9 and self.num_list[2] == 2 and self.num_list[3] == 7 and self.stage_num == 2:
                    self.block = False
                    self.num_list.clear()     
                elif self.num_list[0] == 7 and self.num_list[1] == 4 and self.num_list[2] == 3 and self.num_list[3] == 2 and self.stage_num == 2:   
                    self.bridge = True
                    self.num_list.clear()
                # Stage 2
                elif self.num_list[0] == 2 and self.num_list[1] == 9 and self.num_list[2] == 6 and self.num_list[3] == 1 and self.stage_num == 3:  
                    self.block = False
                    self.num_list.clear()
                elif self.num_list[0] == 2 and self.num_list[1] == 3 and self.num_list[2] == 5 and self.num_list[3] == 9 and self.stage_num == 3:
                    self.bridge = True
                    self.num_list.clear()
                # Stage 3
                elif ((self.num_list[0] == 1 and self.num_list[1] == 3) or (self.num_list[0] == 3 and self.num_list[1] == 1)) and self.num_list[2] == 2 and self.num_list[3] == 4 and self.stage_num == 4:  
                    self.block = False
                    self.num_list.clear()
                elif ((self.num_list[0] == 6 and self.num_list[1] == 8) or (self.num_list[0] == 8 and self.num_list[1] == 6)) and ((self.num_list[2] == 4 and self.num_list[3] == 3) or (self.num_list[2] == 3 and self.num_list[3] == 4)) and self.stage_num == 4:
                    self.bridge = True
                    self.num_list.clear()
                # Stage 4
                elif self.num_list[0] == 4 and self.num_list[1] == 3 and self.num_list[2] == 3 and self.num_list[3] == 2 and self.stage_num == 5:  
                    self.block = False
                    self.num_list.clear()
                elif self.num_list[0] == 5 and self.num_list[1] == 5 and self.num_list[2] == 3 and self.num_list[3] == 9 and self.stage_num == 5:
                    self.bridge = True
                    self.num_list.clear()
                else:
                    self.num_list.clear()
                    print("working")
                    for l in self.scene['Levers']:
                        l.properties["flip"] = False
                        l.append_texture(arcade.load_texture("placeholder_assets/levers/lever_"+l.properties["color"]+"_up.png"))
                        l.set_texture(0)
                        print(l)
                    if self.block == True:
                        for n in self.scene['Problem_Screen']:
                                n.append_texture(arcade.load_texture(f"placeholder_assets/math/blank.png"))
                                n.set_texture(0)
                    else: 
                        for n in self.scene['Problem_Screen']:
                            if n.properties["number"] > 4:
                                n.append_texture(arcade.load_texture(f"placeholder_assets/math/blank.png"))
                                n.set_texture(0)
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # See if we hit any levers
       
        death = collisions.HandleCollisions.DangerCollision(self.player_sprite, self.scene['Danger'])
        if death:
            self.num_list.clear() 
            self.setup()
        portal = collisions.HandleCollisions.PortalCollision(self.player_sprite, self.scene['Portal'])
        if portal:
            self.stage_num +=1
            self.point_x = 128
            self.point_y = 1744
            self.block = True
            self.bridge = False
            self.setup()
        checkpoint = collisions.HandleCollisions.CheckpointCollision(self.player_sprite, self.scene['Checkpoint'])
        if checkpoint:
            self.point_x = self.player_sprite.center_x
            self.point_y = self.player_sprite.center_y
        
        if self.stage_num >= 1:
            puzzle.HandlePuzzle.leversDoor(self.scene['Levers'],self.scene['Blocking'])
            
            puzzle.HandlePuzzle.leversBridge(self.scene['Levers'],self.scene['Bridge'],self.physics_engine)


        # Position the camera
        self.center_camera_to_player()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()