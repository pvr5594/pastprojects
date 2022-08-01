import pickle
from save_game import SaveGame


class LoadGame:
    def load_save_slot_1(self):
        pickle_load = open('save_slot_1.pkl', 'rb')
        pickle_load = pickle.load(pickle_load)
        pickle_load.close()
