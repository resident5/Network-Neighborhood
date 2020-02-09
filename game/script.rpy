# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    $ kiloByte = Character("KiloByte", color="#c8ffc8")
    $ byte = Character("Byte")

    image black = "#000000"
    image serverRoom = "ServerRoom.jpg"
    image openEyes = "openeyes.jpg"
    image update = "Char.jpg"

screen mapscreen:
    add "map/house_idle.png"

    imagebutton auto "map/house1_%s.png" focus_mask True action Jump("CentralProcessor")

    hbox:
        yalign 0.0
        xalign 1.0
        imagebutton auto "map/globe_icon_%s.jpg" action Return()


# The game starts here.

label start:

    jump prologue

label houseTest:

    "I cant believe we got a house man"
