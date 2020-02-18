import test_data
import json

class Platform:
    def __init__(self,launchyear, name):
        self.launch_year = launchyear
        self.name = name

class Game:

    def __init__(self,title, platform, year):
        self.title= title
        self.platform = platform
        self.year= year
    



#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    for g in json_data:
        prep = g['platform']
        p = Platform(prep['launch_year'], prep['name'])
        game_library.add_game(Game(g['title'],p,g['year']))
    
    ### Begin Add Code Here ###
    #Loop through the json_data
        
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

with open (input_json_file, 'r') as json_file:
    json_data = json.load(json_file)
gamelib = make_game_library_from_json(json_data) 
print(gamelib)

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
