Assignment 3: Read Me
Pranav Ramakrishnan

Time Spent on Assignment:
I spent around 20 hours on this assignment, not including spending 1 hour on a video call with my classmate Darence Thong regarding the assignment.

Assignment Problem Areas:
For the most part, I had not trouble with the program code. I had a couple of bugs bad_guy.py that I was only able to fix with help from my classmate Darence.

Shortcomings in Solution:
I was unable to get the output to read "Sauraman/Witch King has been notified that the number of.....".
I had trouble connecting the right variables together.
Instead, I found a workaround. My program prints a message whenever the BadGuy class is notified:

    def notify_observer(self, army_list):
        print(self.name, "is in Troop Command")
        print(self.name, "has been notified of the army count.\n")

Then, my set_enemies function in EyeOfSauron class prints the following:

	print("Troop Command has confirmed reports that the advancing enemy force contains", {hobbit_count}, "hobbits,", {dwarf_count}, "dwarfs,", {elf_count}, "elfs, and", {human_count}, "humans.\n")

This is how I made a workaround. The output can be viewed in 'observer_output.txt'.

Extra Credit:
I made the Observer class in observer.py an abstract class.
I added set_changed, has_changed, and clear_changed methods too the Observable class in observable.py. However, I am not sure if what I did was enough. I just wanted to point out my attempt.
