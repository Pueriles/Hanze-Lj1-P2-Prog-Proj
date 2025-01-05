import random

class Program:
    def __init__(self, data=None):
        """
        Initialiseer het Program-object met een optionele lijst.
        """

        self.data = data or []  # Gebruik een lege lijst als er geen data is

    def __repr__(self):
        """Geef een duidelijke tekstweergave van het object."""
        return f"Program(data={self.data})" 

    def randomize(self):
        """
        Schud de data door elkaar.
        """

        if self.data: # Als er data is
            random.shuffle(self.data) # Schud de data door elkaar
        else:
            print("De lijst is leeg. Voeg eerst data toe.")

# Shuffle
if __name__ == "__main__": # Voert uit als deze script wordt geactiveerd
    prog = Program([10, 20, 30])  # Maak een object met data
    print("Voor randomize:", prog)  # Toon originele volgorde
    prog.randomize()  # Schud de data door elkaar
    print("Na randomize:", prog)  # Toon de nieuwe volgorde
