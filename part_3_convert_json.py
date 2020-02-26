import cc_dat_utils
import cc_classes

import json
#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

output_dat_file = "data/pjsheeha_cc1.dat"

print("DD")

class level:
    def __init__(self, level_number, time, num_chips, upper_layer, optional_fields):
        self.level_number = level_number
        self.time = time
        self.num_chips = num_chips
        self.upper_layer = upper_layer
        self.optional_fields = []

def make_levelPack_from_json(json_data):
    CCLevels = cc_classes.CCLevelPack()
    for l in json_data:
        print("KK")
        myL = cc_classes.CCLevel()
        myL.level_number = l["level_number"]
        myL.time= l["time"]
        myL.num_chips=l["num_chips"]
        myL.upper_layer = l["upper_layer"]
        myL.optional_fields = []
        opt = l["optional_fields"]
        for o in opt:
            if (o["field_type"] == "title"):
                print(o["title"])
                hu = cc_classes.CCMapTitleField(o["title"]);
                print(hu)
                myL.add_field(hu)
            if (o["field_type"] == "passcode"):
                print("OO")
                myL.add_field(cc_classes.CCEncodedPasswordField(o["passcode"]))
            if (o["field_type"] == "hint"):
                myL.add_field(cc_classes.CCMapHintField(o["hint"]))
            if (o["field_type"] == "monsters"):
                cL = []
                for c in o["coordinates"]:
                    
                    cL.append(cc_classes.CCCoordinate(c["x"], c["y"]))
                myL.add_field(cc_classes.CCMonsterMovementField(cL))
        CCLevels.add_level(myL)
    
    cc_dat_utils.write_cc_level_pack_to_dat(CCLevels, output_dat_file)
    mycc = cc_dat_utils.make_cc_level_pack_from_dat("data/pjsheeha_cc1.dat")
    print(mycc)



input_json_file = "data/pjsheeha_cc1.json"

with open (input_json_file, 'r') as json_file:
    json_data = json.load(json_file)
    print("LL")
make_levelPack_from_json(json_data) 
