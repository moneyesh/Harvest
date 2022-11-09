############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon_type = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon_type.add_pairing('mint')
    casaba_type = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casaba_type.add_pairing("strawberries")
    casaba_type.add_pairing("mint")
    crenshaw_type = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw_type.add_pairing('prosciutto')
    yellow_watermelon_type = MelonType(
        "yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon_type.add_pairing("icecream")

    all_melon_types = [muskmelon_type, casaba_type,
                       crenshaw_type, yellow_watermelon_type]
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print(f"{melon_type.name} pairs with: ")
        for pairing in melon_type.pairings:
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    lookup = {}

    for melon in melon_types:
        lookup[melon[0]] = melon


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
