import pickle
from dungeon_adventure import DungeonAdventure


class SaveGame:
    def save_slot_1(self):
        dungeon_adv = DungeonAdventure()
        pickle_save = open('save_slot_1.pkl', 'wb')
        pickle.dump(dungeon_adv, pickle_save)
        pickle_save.close()


# save = SaveGame()
# save.save_slot_1()
