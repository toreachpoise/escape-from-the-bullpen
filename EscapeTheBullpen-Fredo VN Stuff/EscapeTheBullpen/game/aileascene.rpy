#dramatis personae vol. 4
define a = Character("Ailea", image="ailea", who_color="#e5c620")
default a_points = 0
define m = Character("Mona", image="mona", who_color="#aad7f2")
default m_points = 0
define h = Character("Heloise", image="heloise", who_color="#a90000")
default h_points = 0


transform center_right:
    xalign .80 yalign 1.0
transform center_left:
    xalign .25 yalign 1.0
transform center_left_left:
    xalign .33 yalign 1.0

label hospitalharem:
    scene harem bg with fade
    if r_companion == True:
        jump a_section1_with_r
    else:
        jump a_section1_no_r

#Section 1
label a_section1_with_r:
    show jack main at right with moveinright
    show rakesh main at center_right with moveinright:
        xzoom -1
    show heloise main at left with moveinleft:
        xzoom -1
    h "Whoa! Who the hell are you two?! You're not... cows... nor do you seem to be bulls..."
    show mona main at center_left_left with moveinleft:
        xzoom-1
    m "Relax, Heloise."
    m @ happy "These must be some of those non-cow, non-bull people that Ailea was telling us about."
    h "Is that true? Did Ailea send for you?"
    j @ embarrassed "Uh..."
    show rakesh shrug
    r "..."
    show rakesh main
    show ailea main at center with moveinleft
    a "Heloise, Mona, could I get a moment alone with the newcomers?"
    hide heloise with moveoutleft
    hide mona with moveoutleft
    show ailea main at left with moveinright
    r @ happy "Hello, Ailea! Long time no see."
    a @ upset "Are you crazy?! What do you think you're doing here?! "
    a @ happy "And uh... who's your friend?"
    j "Ailea? I'm Jack. I've come a long way to find you."
    r "Jack's cool as a cucumber, Ailea. We're here to rescue you!"
    a "..."
    a "I guess you had no way of knowing..."
    r "What do you mean?"
    a "Well... Good work, you two! You got all the way inside the breeding center."
    j "Yeah, and if we hurry we can get all the way back out before they even notice we were here."
    a "Whoa! Slow down. Listen to me."
    a "I appreciate what you're doing here, I really do..."
    a "But all you've done is complicate things."
    j "Huh?!"
    r "Uh oh..."
    a "I've been planning an escape of my own. Everything's in place, but I can't leave without Mona and Heloise..."
    menu:
        "What are you talking about?! We came to rescue {i}you{/i}, not a bunch of cows!":
            $ a_points -= 1
            r "It was going to be difficult with three of us, but five..."
            a "It's non-negotiable."
            a "And Heloise, at the very least, can take care of herself."
            j "OK... So let's go!"
            jump a_section2
        "Yeah, no problem, whoever wants can come along...":
            $ a_points += 1
            a "Good. Now I'm not sure if my plan will work for five of us..."
            a "But I'm sure we'll figure it out."
            j "So what's your plan? Because I really liked my plan."
            a "What was it again?"
            j @ embarrassed "Y'know, we just... walk out the same way we came in?"
            a "Ah... well, hear me out, and then we'll decide."
            jump a_section2

label a_section1_no_r:
show jack cow at right with moveinright
show heloise main at left with moveinleft:
    xzoom -1
h "Whoa! Who the hell are you?! You don't seem to be a bull... but any self-respecting cow wouldn't be caught {i}dead{/i} wearing those old rags..."
show mona main at center_left_left with moveinleft:
    xzoom-1
m "Relax, Heloise."
m @ happy "He must be some of those non-cow, non-bull people that Ailea was telling us about."
h "Is that true? Did Ailea send for you?"
j @ embarrassed "Uh..."
show ailea main at center with moveinleft
a "Mona, Heloise, give us a second here..."
hide heloise with moveoutleft
hide mona with moveoutleft
show ailea main at left with moveinright
a "And who might you be?"
j "I'm Jack. Rakesh sent me."
if t_companion == True:
    extend "Takeshi too, or at least we're working with hir."
j "I'm here to rescue you!"
a "Oh... that's very kind, but..."
j "Come on, the way was clear on the way in, we can get out the same way."
###MISSING DIALOGUE###




# rakesh or no?
#if r_companion == True:
#Ailea is trusting of Jack, but worried about getting out

#if not, Ailea feels protective of Jack and is worried about getting out

#either way, the player party is all "we're here to rescue you, if we move fast we can make it out the same way we came in..."

#alarm sounds

#Section 2
label a_section2:
    "Parachutes!"
#ailea has her parachute plan, but won't leave before talking to Mona and Heloise, the two cows who most expressed a desire to escape

    #convo with Heloise: Convince Heloise that she'll be free to live her own life

    #Convo with Mona: Convince Mona that she'll be safe in the scary outside world

        #If both agree to go, everything's good

            #if only Mona agrees to go, Ailea will try to convince Heloise to come, assisted by Jack

                #if Heloise is convinced (by Jack's militant connections) to come, good to go

                #if Heloise stays, the party moves on without her, leaving behind a means of communication in case she wants out

            #if only Heloise agrees to go, Ailea will try to convince Mona to come, assisted by Jack

                #if Mona is convinced (by Jack's experiences with mutual aid stuff) to come, good to go

                #if Mona stays, the party moves on without her, leaving behind a means of communication in case she wants out

#Section 3

#Endings, arrangements of parachute partners, etc.

#if t_companion == false:
    #Boss fight!
#else:
    #takeshi's musical happening begins
    #Takeshi blows up the gate
