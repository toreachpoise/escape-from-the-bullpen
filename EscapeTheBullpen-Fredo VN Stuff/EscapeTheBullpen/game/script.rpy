#Dramatis Personae
#Jack
define j = Character("Jack", image="jack", who_color="#ad3515", what_style="say_protagdialogue", who_style="protag_name")

#Rakesh Def(aults/initions)
define r = Character("Rakesh", image="rakesh", who_color="#46b5dc")
default r_points = 0
default r_companion = False
default rakesh_age_comment = False

#Takeshi Def(aults/initions)
define t = Character("Takeshi", image="takeshi", who_color="#eaffc5")
default t_points = 0
default t_companion = False

#Matron Def(aults/initions)
define ma = Character("Matron", image="matron", who_color="#b585be")

#Ailea Def(aults/initions)
define a = Character("Ailea", image="ailea", who_color="#e5c620")
default a_points = 0

#Mona Def(aults/initions)
define m = Character("Mona", image="mona", who_color="#aad7f2")

#Heloise Def(aults/initions)
define h = Character("Heloise", image="heloise", who_color="#a90000")

#Taurus Def(aults/initions)
define ta = Character("Taurus", image="Taurus", who_color="#cfb29d")

#Custom Positions
transform center_right:
    xalign .80 yalign 1.0
transform center_left:
    xalign .25 yalign 1.0
transform center_left_left:
    xalign .33 yalign 1.0


#Scene 1
label start:
    #jump end_cutscene
    #jump BC_gates
scene black
"You are awoken by a low buzz."
"The black screens that tile your closet of a room light up with a notification."
scene jacks room bg with fade
show jack upset at right
"Your heart drops somewhere into the sloshing mass of your middle."
"Another bull visit? But it's been less than a month. You haven't even had your period since the last one."
"Oh ... oh no ..."
show jack scared
extend "... Maybe you're pregnant."
show jack depressed
"That's what the bulls want, or rather, what the system as a whole wants. That's why the bulls visit you every month."
"Once a month they come to force themselves on you, your fate for being one of the rare humans remaining who is able to get pregnant."
show jack main
j "I mean, maybe being raped will cause me to miscarry?"
"Unlikely."
show jack depressed
extend "It's much more likely that the bull will notice and demand that you be taken back to the facility where they keep all the other cows ..."
"You'll be taken, sedated until you give birth, and kept and raped over and over again for having been unlucky enough to prove your fertility."
"You managed to escape from the facility only a couple of years ago, having almost aged out of being a cow, and being too trans and ugly to be prized by the bulls."
"These monthly visits were the doctors' compromise--you could be free, but only a little bit. They would still extract what they needed from you."
show jack scared with dissolve
j "Fuck ... what do I do? "
extend "Do I just wait here until they come? Pretend everything is normal and hope they don't notice?"
show jack determined with dissolve
j "No."
extend "I have to do something. I have to find someone who can help me."
j "I have to get out of here ..."
jump minigame
