from library_item import LibraryItem


library = {}
library["1"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4,"https://www.youtube.com/watch?v=AB4JZr9nWCY&list=PLbEif3LMBbrxFaXONS-1Uf51G0hkzQ3j4" )
library["2"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5,"https://www.youtube.com/watch?v=1ClCpfeIELw")
library["3"] = LibraryItem("Casablanca", "Michael Curtiz", 2,"https://www.youtube.com/watch?v=BrmyQNI9s_E")
library["4"] = LibraryItem("The Sound of Music", "Robert Wise", 1,"https://www.youtube.com/watch?v=edpeRzNTA8w")
library["5"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3,"https://www.youtube.com/watch?v=lrhNPS4nbmQ")


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

def get_url(key):
    try:
        item = library[key]
        return item.url
    except KeyError:
        return None