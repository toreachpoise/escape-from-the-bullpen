label minigame:
if handler.first_try == True:
    label controls_explanation:
    j "I don't know why I feel compelled to say this but ..."
    j "... to move me, use the arrow keys. To jump, press SPACEBAR. To knife bad guys, hit ENTER"
    j "or if you're on a controller, use the D pad or joystick to move, A or X to jump, and B to attack. Or something, you'll figure it out."
menu:
    "Do you need to hear about the controls again?"
    "yes":
        jump controls_explanation
    "no":
        pass
j "alright, let's do this"
python:
    player.reset()
    handler.game_over = False
    handler.reset()
    player.died = False
    player.fallcount = 0
call screen minigame("level 1")
menu:
    "do you want to try again?"
    "yep":
        jump minigame
    "no thanks, let's skip this level":
        $ handler.next_stage()
        pass
label leveldone:
$ handler.stage_complete = False
if handler.level == "level 2":
    jump apothecary
elif handler.level == "level 3a":
    jump takeshi_garage
elif handler.level == "level 3bn":
    jump BC_gates
elif handler.level == "level 3br":
    jump BC_gates_withr
elif handler.level == "level 4":
    jump hospitalharem
else:
    jump end_cutscene ## animatic label goes here
