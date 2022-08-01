from eye_of_sauron import EyeOfSauron
from bad_guy import BadGuy


def test_sauron_eye():
    hobbit_count = 1
    dwarf_count = 1
    elf_count = 2
    human_count = 0

    eye = EyeOfSauron()
    saruman = BadGuy(eye, "Saruman")
    witch_king = BadGuy(eye, "Witch King")

    eye.set_enemies(hobbit_count, dwarf_count, elf_count, human_count)
    # message should be displayed from Saruman and Witch King
    # that they know about 1 hobbit, 1 elf, 2 dwarves

    saruman.defeated()  # Saruman is no longer registered with the Eye

    hobbit_count = 4
    dwarf_count = 1
    elf_count = 1
    human_count = 100  # here come the Riders of Rohan! lol

    eye.set_enemies(hobbit_count, dwarf_count, elf_count, human_count)


test_sauron_eye()
