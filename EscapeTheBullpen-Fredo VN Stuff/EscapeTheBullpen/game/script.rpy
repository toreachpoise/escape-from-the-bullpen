#Dramatis Personae

define j = Character("Jack", image="jack", who_color="#ad3515")

define r = Character("Rakesh", image="rakesh", who_color="#46b5dc")
default r_points = 0

#Scene 1
label start:
jump apothecary

label apothecary:
scene apothecary with fade
show jack main with moveinright

j "Hello?"
"..."
j "Anyone?"
"..."
show jack main at right with moveoutright
show rakesh main at left with moveinleft

#Section 1
r "What you want?"
menu:
    "You're not Ailea...":
        r "She's not here man."
        j "But I need help!"
        r @ shrug "..."
        jump rakesh_continue_1
    "I need birth medicine.":
        $ r_points += 1
        r @ happy "Aaaah, you look for juice in your caboose."
        r @ shrug "Everybody shoot blank these days, man. The birth police come here two days ago and take all our fertility medicine for the bulls."
        j "No... I already have a baby. I need to get rid of it."
        r "Oh. Sorry, man. They take the lady who can help with that too."
        j @ worried "Where is she?"
        jump rakesh_continue_1
    "Oh, great, it's just some kid.":
        $ r_points -= 1
        show rakesh upset with dissolve
        r "Man, I'm twice your age."
        show jack embarassed with dissolve
        j "..."
        menu:
            "Sorry, I didn't mean to assume...":
                jump rakesh_apology
            "Yeah, if I was like 3. Or younger.":
                $ r_points -= 1
                r "What the hell?! Did you just come here to be a dick?!"
                menu:
                    "I guess I did, you little creep!":
                        jump worst_ending
                    "No! I'm sorry! I'm just... I'm sorry...":
                        jump rakesh_apology

                label rakesh_apology:
                    $ r_points += 1
                    show jack main at right with dissolve
                    r "Hmph. Apology accepted..."
                    pause
                    show jack main with dissolve
                    j "I'm looking for Ailea. I heard she could help me with a baby?"
                    jump rakesh_continue_1

#Section 2
label rakesh_continue_1:
if r_points < 0:
    "(Rakesh seems a bit annoyed with you.)"
if r_points > 0:
    "(Rakesh seems to trust you.)"
if r_points == 0:
    "(Rakesh is tolerating your presence, for now.)"

r "They take her to the breeding center. They say she need to help with one of the cows, but then she never come back."
menu:
    "She's gone? Oh God, this can't be happening...":
        r "Hey, it's OK. I been looking for help anyway."
        j "Help with what?"
        r "What do you think, man? We gotta rescue her!"
        jump rakesh_continue_2
    "What, you couldn't stop them?":
        show rakesh angry with dissolve
        r "..."
        menu:
            "Sorry, I'm just scared...":
                if r_points <= -2:
                    jump worst_ending
                if r_points > -2:
                        $ r_points += 1
                        r "It's OK to be scared, man. Scary times."
                        j "Yeah..."
                        r "Just don't be rude, we gotta help each other."
                        j "Yeah!"
                        jump rakesh_continue_2
            "Y'know, with your hoverboard or whatever?":
                $ r_points -= 1
                if r_points <= -2:
                    jump worst_ending
                if r_points > -2:
                        show rakesh angry with dissolve
                        r "What is this, man? Did someone send you just to mess with me?"
                        j "No! I really do need help!"
                        r @ happy "I love to help!"
                        r "So stop being an ass!"
                        jump rakesh_continue_2
    "Then we'll just have to go get her.":
            r "It won't be easy..."
            menu:
                "I didn't expect it to be.":
                    $ r_points += 1
                    jump rakesh_continue_2
                "Maybe... someone else could help?":
                    $ r_points -=1
                    r "Just hear me out, man!"
                    jump rakesh_continue_2

#Section 3
label rakesh_continue_2:

if r_points < 0:
    "(Rakesh seems a bit annoyed with you.)"
    jump rakesh_section3_annoyed
if r_points > 0:
    "(Rakesh seems to trust you.)"
    jump rakesh_section3_friendly
if r_points == 0:
    "(Rakesh is tolerating your presence, for now.)"
    jump rakesh_section3_friendly

    label rakesh_section3_annoyed:
        $ inside = 1
        $ distractions = 1
        $ bull_disguise = 1
        $ matron_disguise = 1
        r "You'll need two things: A way inside and a distraction."
        label rakesh_section3_annoyed_options:
        menu:
            "How am I supposed to get inside?" if inside == 1:
                r "You'll have to find a disguise, I think."
                label disguise_menu:
                menu:
                    "Maybe a Bull?" if bull_disguise == 1:
                        $ bull_disguise = 0
                        r "Hmmm... muscles too small, eyes too kind."
                        jump disguise_menu
                    "Maybe a Matron?" if matron_disguise == 1:
                        $ matron_disguise = 0
                        r "Nah... Wrong smell. Smile not fake."
                        jump disguise_menu
                    "... Not as a cow..." if bull_disguise == 0 and matron_disguise == 0:
                        r "Afraid so, man."
                        $ cow_disguise = 1
                        $ inside = 0
                        jump rakesh_section3_annoyed_options

            "A distraction?" if distractions == 1:
                r "Nobody better at distracting than my friend Takeshi."
                menu:
                    "The useless washed up rockerboy?!":
                        $ r_points -= 1
                        $ distractions = 0
                        r "Ugh. If you ask hir for help, try to be more polite. Xe isn't as patient as me."
                        jump rakesh_section3_annoyed_options
                    "Takeshi! I love hir music!":
                        $ r_points += 1
                        $ distractions = 0
                        r "Tell that to Takeshi. Xe'll help for sure then."
                        jump rakesh_section3_annoyed_options


    label rakesh_section3_friendly:
    r "I've been practicing my lockpicking, so all we need is a distraction..."





#Endings
label worst_ending:
show rakesh main with dissolve
r "Whatever. Not helping the likes of you. Come back when you're in a better mood."
pause
scene neighborhood with fade
show jack depressed
"You wander off, alone, unhelped. Because you were a dick for no reason."
jump end

label rakesh_good_ending:

label rakesh_bad_ending:



#Return to Menu
label end:
pause
return
