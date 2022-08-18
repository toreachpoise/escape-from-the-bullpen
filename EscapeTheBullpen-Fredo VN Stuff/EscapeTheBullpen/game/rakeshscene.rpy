#Rakesh Scene
label apothecary:
play music "audio/song3.wav"
scene ailea_shop_bg with fade
show jack main with moveinright

j "Hello?"
"..."
j "Anyone?"
"..."
show jack main at right with moveoutright
show rakesh main at left with moveinleft

#Section 1
$ r_not_a = 1
j "Hi, I'm Jack..."
r "Rakesh. What you want?"
label r_greeting_menu:
menu:
    "You're not Ailea..." if r_not_a == 1:
        $ r_not_a = 0
        r "She's not here man."
        j "But I need help!"
        r @ shrug "..."
        jump r_greeting_menu
    "I need birth medicine.":
        $ r_points += 1
        r @ happy "Aaaah, you look for juice in your caboose."
        r @ shrug "Everybody shoot blank these days, man. The birth police come here two days ago and take all our fertility medicine for the bulls."
        j "I... I already have a baby."
        j @ upset "INSIDE me..."
        j "I need to get rid of it."
        if r_not_a == 1:
            r "Oh. Sorry, man. They take the lady who can help with that too."
        if r_not_a == 0:
            r "Oh. Sorry, man. Ailea's the only one who could help with that."
        j "Where is she?"
        jump rakesh_continue_1
    "Ugh, great, it's just some kid.":
        $ r_points -= 1
        $ rakesh_age_comment = True
        r @ angry "Man, I'm twice your age."
        show jack upset
        show jack embarrassed
        j "..."
        menu:
            "Sorry, I didn't mean to assume...":
                jump rakesh_apology
            "Yeah, if I was like 3. Or younger.":
                show jack happy
                $ r_points -= 1
                r @ angry "What the hell?! Did you just come here to be a dick?!"
                show jack main
                menu:
                    "I guess I did, you little creep!":
                        jump r_worst_ending
                    "No! I'm sorry! I'm just... I'm sorry...":
                        jump rakesh_apology

                label rakesh_apology:
                    $ r_points += 1
                    show jack main
                    r "Hmph. Apology accepted..."
                    show jack main
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

show rakesh main
r "They take her to the breeding center. They say she need to help with one of the cows, but then she never come back."
menu:
    "She's gone? Oh God, this can't be happening...":
        r "Hey, it's OK. I been looking for help anyway."
        j "Help with what?"
        r "What do you think, man? We gotta rescue her!"
        jump rakesh_continue_2
    "What, you couldn't stop them?":
        show rakesh angry
        r "..."
        menu:
            "Sorry, I'm just scared...":
                if r_points <= -2:
                    jump r_worst_ending
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
                    jump r_worst_ending
                if r_points > -2:
                        show rakesh angry
                        r "What is this, man? Did someone send you just to mess with me?"
                        j "No! I really do need help!"
                        r @ happy "I love to help!"
                        r "So stop being an ass!"
                        jump rakesh_continue_2
    "Then we'll just have to go get her.":
            $ r_points += 2
            show rakesh happy
            r "It won't be easy..."
            menu:
                "I didn't expect it to be.":
                    show jack determined
                    $ r_points += 1
                    jump rakesh_continue_2
                "Oh... in that case...":
                    $ r_points -=1
                    show rakesh main
                    r "Just hear me out, man!"
                    jump rakesh_continue_2

#Section 3
label rakesh_continue_2:
show rakesh main
show jack main
if r_points < 0:
    "(Rakesh seems a bit annoyed with you.)"
    jump rakesh_section3_annoyed
if r_points > 0:
    "(Rakesh seems to trust you.)"
    jump rakesh_section3_friendly
if r_points == 0:
    "(Rakesh is tolerating your presence, for now.)"
    jump rakesh_section3_annoyed

    label rakesh_section3_annoyed:
    r "You'll need a distraction, and there's nobody more distracting than Takeshi."
    jump takeshi_opinion

    label rakesh_section3_friendly:
    r "We'll need a distraction to cover our escape."
    j "Any ideas?"
    r "Nobody better for that than my friend Takeshi."
    jump takeshi_opinion

    label takeshi_opinion:
    menu:
        "The useless washed up rockerboy?!":
            $ r_points -= 1
            $ t_fan = False
            r "Ugh. If you ask hir for help, try to be more polite. Xe isn't as patient as me."
            jump r_endings
        "Takeshi! I love hir music!":
            $ r_points += 1
            $ t_fan = True
            r "Tell that to Takeshi. Xe'll help for sure then."
            jump r_endings

#Endings
label r_endings:
r "We'll also need a way inside..."
if r_points > 0:
    $ r_companion = True
    show rakesh happy
    r "Fortunately, my lockpicking skills are second-to-none!"
    show jack determined
    j "Great! I guess our next stop is Takeshi's."
    r "Let's go!"
    jump end
if r_points <= 0:
    $ r_companion = False
    $ inside = 1
    $ bull_disguise = 1
    $ matron_disguise = 1
    j "How am I supposed to do that?"
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
                show jack upset
    j "Ugh. Great."
    r "It's OK, man. Just a disguise. Keep an eye out for something that might work."
    show jack main
    j "Ok... Guess I'm headed for Takeshi's."
    jump end

label r_worst_ending:
    show rakesh main
    r "Whatever. Not helping the likes of you. Come back when you're in a better mood."
    pause
    scene neighborhood with fade
    show jack depressed with moveinright
    "You wander off, alone, unhelped. Because you were a dick for no reason."
    return

label end:
    if r_companion == True:
        "(Rakesh has joined your party!)"
    if r_companion == False:
        "(Rakesh didn't trust you enough to join your party)"
    #currently jumps to Takeshi's scene, but in game it will jump to level 2
    jump minigame
    return
