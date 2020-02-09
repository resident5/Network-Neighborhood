


label MainMapScreen:
    call screen mapscreen

label CentralProcessor:
    #Change BG

    scene serverRoom with fade

    if hidingEvent == 0:
        $ hidingEvent = 1
        jump CPU_Intro


label ByteRoom:
