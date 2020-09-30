import time
import random

class WorldManager:
    size=50

    def __init__(self,f_path="world_maps/",world_name="test_world"):
        self.file_location=f_path+world_name
        self.game_over=False
        self.game_update()

    def game_update(self):
        while not self.game_over:
            new_map={}
            time.sleep(300)
            #load file from file_location
            for row in range(self.size+1):
                new_map[row]=self.update_row(old_map,row_num)
            # future work - handle population migrations
            # future work - handle invasions
            self.write_json(new_map)

    def check_player_location(self):
        # read json file for player location
        return (loc["x"],loc["y"])

    def update_row(self,old_map,row_num):
        new_row=[]
        player_loc=self.check_player()
        for col in range(self.size+1):
            new_row[col]={}
            if row_num==player_loc[0] and col_num==player_loc[1]:
                new_row[col]=old_map[row_num][col]
            else:
                new_row[col]=self.change_chance(old_map[row_num][col])
        return new_row

    def change_chance(self,map_spot):
        rand_int=random.randint(10)
        new_spot=map_spot
        if rand_int > 5:
            if rand_int < 9:
                new_spot["population"]=map_spot["population"]+2*(rand_int-5)
            else:
                new_spot["population"]=map_spot["population"]-1
        return new_spot
