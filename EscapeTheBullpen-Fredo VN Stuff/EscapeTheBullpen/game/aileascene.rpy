#dramatis personae vol. 4
define a = Character("Ailea", image="ailea", who_color="#e5c620")
define m = Character("Mona", image="mona", who_color="#aad7f2")
define h = Character("Heloise", image="Heloise", who_color="#a90000")

transform center_right:
    xalign .75 yalign 1.0
transform center_left:
    xalign .25 yalign 1.0
transform center_left_left:
    xalign .33 yalign 1.0

label hospitalharem:
    scene harem bg with fade
    show jack main at right with moveinright
    show rakesh main at center_right with moveinright:
        xzoom -1
    show heloise main at center_left_left with moveinleft:
        xzoom -1
    h "Who the hell are you two...?! You aren't bulls, you aren't cows... what in the world..."
    show mona main at left with moveinleft:
        xzoom -1
    m "Oooh, they're probably those weird different non-bull, non-cows that Ailea was talking about..."
    j "Uh..."
    show ailea main at center with moveinleft
    a "Yo we gotta get the eff out broh!"
    r @ happy "Hell yeah! let's go!"

#Section 1

# rakesh or no?
#if r_companion == True:
#Ailea is trusting of Jack, but worried about getting out

#if not, Ailea feels protective of Jack and is worried about getting out

#either way, the player party is all "we're here to rescue you, if we move fast we can make it out the same way we came in..."

#alarm sounds

#Section 2
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
