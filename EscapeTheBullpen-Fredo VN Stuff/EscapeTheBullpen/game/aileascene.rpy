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
    show heloise main at center_left with moveinleft:
        xzoom -1
    h "Whoa! Who the hell are you two?! You're not... cows... nor do you seem to be bulls..."
    show mona main at left with moveinleft:
        xzoom-1
    m "Relax, Heloise."
    m @ happy "These must be some of those non-cow, non-bull people that Ailea was telling us about."
    h "Is that true? Are you friends with Ailea?"
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
    j @ happy "Ailea? I'm Jack. I've come a long way to find you."
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
    a "I've been planning an escape of my own. Everything's in place."
    j "OK, let's hear it."
    jump a_section2


label a_section1_no_r:
show jack cow at right with moveinright
show heloise main at center_left with moveinleft:
    xzoom -1
h "Whoa! Who the hell are you?! You don't seem to be a bull... but any self-respecting cow wouldn't be caught {i}dead{/i} wearing those old rags..."
show mona main at left with moveinleft:
    xzoom-1
m "Relax, Heloise."
m @ happy "He must be some of those non-cow, non-bull people that Ailea was telling us about."
h "Is that true? Did Ailea send for you?"
j @ cowembarrassed "Uh..."
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
a "Whoa, there. Jack, right?"
j "Y-yeah?"
a "Slow down. I appreciate you coming here, but I think I have a better way out."
j "OK, let's hear it."
jump a_section2

#Section 2
label a_section2:
    a "Parachutes!"
    if r_companion == True:
        jump a_section2_withr
    else:
        jump a_section2_nor

label a_section2_withr:
    j "What?!"
    r @ exhasperated "Oh no, not this again..."
    a "Yes, this again! But this time, it'll work!"
    menu:
        "What do you mean by parachutes?":
            a "See, long ago, before they figured out anti-gravity technology, the only way to slow your fall was through air resistance."
            a "They would take these giant sheets of fabric and jump off all sorts of things, and the surface area of the-..."
            j "I know what parachutes are! What's your plan?"
            a "Oh. We jump off the roof with parachutes."
        "Um... 'not again'? 'This time'?!? What's going on...":
            r @ exhasperated "Years ago, Ailea break both her damn ankles trying to make her own parachute."
            a "Yes, and like I told you then, I just hadn't been able to requisition enough fabric."
            a @ happy "In here, between all the bed sheets and Mona's preference for voluminous sleeves, I had plenty!"
    menu:
        "But why can't we just walk out?":
            a "It'll be way harder for a big group of us to sneak out than it will be for two of you to sneak in!"
            j "A big group?"
            a "Well... is five a big group? You two, me, Heloise, Mona."
            menu:
                "What are you talking about?! We came to rescue {i}you{/i}, not a bunch of cows!":
                    $ a_points -= 1
                    r "It was going to be difficult with three of us, but five..."
                    a "It's non-negotiable. Heloise and Mona are coming with us."
                    a "And Heloise, at the very least, can take care of herself."
                "Yeah, no problem, whoever wants can come along...":
                    $ a_points += 1
                    a "Good. Now I'm not sure if my plan will work for five of us..."
                    a "But I'm sure we'll figure it out."
                    j "That's not giving me a lot of confidence."
            j "I still think we could walk out, and if someone tries to stop us..."
            a "What? You kill them?"
            j "Wouldn't be the worst thing..."
            a "No killing. Not unless there's no other way."
            menu:
                "But... your parchute plan could kill us all!":
                    a "It won't. I did the math right this time."
                    a "I think."
                    a "Probably."
                    j "..."
                "Is it better to risk our own lives?":
                    a "Yes. As long as we all willingly take on the risk, it's better."
                    menu:
                        "I see your point.":
                            $ a_points += 1
                            a "Thank you."
                        "Nah. I'm not willing to put my safety in your hands.":
                            $ a_points -= 1
                            a "But you want me to put mine and others' in yours?"
        "Hmmm... I guess parachutes will work? It'll save us from having to sneak around...":
            a @ happy "I can't believe I finally get to test this idea!"
            a "I've never been good at math, but I'm {i}sure{/i} I've done it right this time..."
            show jack scared
            r "Ailea, you're scaring him."
            j "Only a little..."
            show jack main
            a "OK, so we'll go two to a chute and Rakesh, you have your hoverboard..."
            j "You mentioned being bad at math..."
            a "No, this stuff I can do right. Two parachutes. Me, you, Mona, Heloise, Rakesh on hoverboard, right?"
            menu:
                "Oh, so we're just rescuing everybody now?":
                    a @ happy "Everybody who expressed interest in coming!"
                    a "I wish it was more, but... I've also run out of parachute materials, so I suppose things are working out for the best."
                    menu:
                        "Leave them behind. We came for you, not a bunch of cows.":
                            $ a_points -= 1
                            a @ upset "They're coming. That's non-negotiable."
                            j "Ugh! Fine!"
                            jump alarm_withr
                        "Well... as long as they're OK with maybe dying.":
                            $ a_points += 1
                            a "Aren't we all?"
                            r "No."
                            j "Yeah, not so much."
                            a "Oh. That must be so stressful."
                            jump alarm_withr
                "Yeah... if they're coming, you did the math right.":
                    a @ happy "Thank goodness. I was almost embarrassed."
                    menu:
                        "But... they're not coming, to be clear.":
                            a @ upset "What?! Of course they are. Stop being absurd. Either they come, or I'm staying."
                            menu:
                                "Well maybe Rakesh and I just knock you out and escape!":
                                    $ a_points -= 1
                                    r "What the hell, man!? Leave me out of this!"
                                    a "It's OK to be frustrated and scared, Jack. It's not OK to be an asshole."
                                    menu:
                                        "You're right, I'm sorry.":
                                            jump alarm_withr
                                        "Nobody but me gets it! Sometimes you have to do bad things for good reasons!":
                                            jump alarm_withr
                                "But I need you!":
                                    show ailea main
                                    a "So do they."
                                    menu:
                                        "I don't care!":
                                            jump alarm_withr
                                        "... Of course, you're right.":
                                            jump alarm_withr
                        "So is it just Mona and Heloise? Anyone who wants to can come...":
                            a "Ah, that's very kind, Jack. But no."
                            a "Heloise and Mona are... bolder than the others."
                            a @ sad "I hate to leave anyone behind, but I have to help who I can with what I have right now."
                            jump alarm_withr

label alarm_withr:
    play sound "audio/alarm.mp3" volume .25
    j "..."
    a "..."
    r "..."
    r "I knew I missed something somewhere. My bad, everyone."
    a "Well, looks like the decision's been made. No way out now."
    r "I'll see what I can do to jam the doors."
    hide rakesh with moveoutright
    a "Also, please turn the sound off."
    r "No shit."
    play sound "audio/brokenelectronics.mp3" volume.25
    r "..."
    r "Is that better?"
    stop sound
    a "Much better, thanks, Rakesh!"
    menu:
        "We're trapped! I'm going to die in here!":
            show jack scared
            a "Hey! Snap out of it, Jack! You got this far, which means you're a badass."
            j "Y-yeah?"
            a "Yeah!"
            a "So go get Mona and Heloise, and tell them we're going. Right now!"
            j @ determined "You can count on me!"
            jump section3
        "OK. What's next? We gotta move!":
            show jack determined
            show jack main
            a "Do you know how to get parachutes ready?"
            menu:
                "I can try my best?":
                    a "Yeah, OK, dumb question. I need you to talk to Mona and Heloise. Get them ready to go."
                    jump section3
                "No! Why would I?!":
                    a "Fair enough. Go talk to Mona and Heloise. They need to be ready as soon as possible."
                    jump section3

default a_section2_loop1_1 = False
default a_section2_loop2_1 = False
label a_section2_nor:
    j "Parachutes?"
    a @ happy "Specifically, parachuting off the top of the building, floating over the walls, and into the loving embrace of the city on the other side."
    j "..."
    j "Well... I don't really have a deathwish, so why don't we just walk out the way I came in?"
    a "You came in as one person dressed as a cow... I'm guessing by that swell in your tummy that you're on their fertility roster..."
    j "Yeah, so?"
    a "So of course they were going to let you in!"
    a "But what do you think will happen if you and I try leaving with two of their blue-ribbon cows?"
    j "Wait... hold on. Who said anything about two cows?!"
    a "Heloise and Mona are coming with us, obviously."
    j "I came here to rescue {i}you{/i}! I'm not about to risk it all for a couple of cows!"
    a "It's non-negotiable. They're either coming with us, or you'll be leaving alone."
    menu:
        "Goddammit!":
            $ a_points -= 1
            a "Whoa there, settle down! Why did you come this far in the first place?"
            j "To rescue you! I need an abortion..."
            a "And you thought... what, you think my only responsibility is to help you specifically?"
            label a_section2_loop1:
            menu:
                "I'm helping {i}you{/i} specifically, so yeah. You kinda owe me one." if a_section2_loop1_1 == False:
                    $ a_section2_loop1_1 = True
                    show ailea upset
                    $ a_points -= 1
                    a "I don't owe you anything, except what I owe to anyone else alive."
                    j "But-..."
                    a "'But' BULLSHIT. Fuck your 'but' and your 'owing' and everything else."
                    a "If you can't accept that your individual problems are part of a larger whole..."
                    a "And if you can't accept that its everyone's responsibility to help who they can with what they have right now..."
                    a "Then I have nothing else to say to you."
                    show ailea main
                    a "You can come with us when we escape, or you can stay behind."
                    j "But I came all this way!"
                    a "Isn't that a good thing? You came a long way and did crazy shit to help me, a stranger."
                    a "All only because I could help you?"
                    jump a_section2_loop1
                "I guess not...":
                    a "Why not?"
                    j "Isn't that what you... wanted me to say?"
                    a "I wanted you to speak honestly. With conviction."
                    label a_section2_loop2:
                    menu:
                        "I'm not sure what my convictions are..." if a_section2_loop2_1 == False:
                            $ a_section2_loop2_1 = True
                            a "That's OK. Maybe take some time to think on it."
                            j "I mean... This morning, I made a decision."
                            j "I couldn't have this baby. I didn't want this baby. I had to get an abortion."
                            a "Yes."
                            j "And so I set out looking for you, and now, after everything... I ended up here."
                            j "I didn't set out because I believed in anything except my own desires."
                            j "How is that any kind of conviction at all?"
                            a "Whatever I might think of your motivation, it got you this far. There's some kind of power in that, don't you think?"
                            j "I guess so. Yeah."
                            a "And it drove you to a place where, everything else aside, you've put yourself in danger to help me."
                            j "Yeah..."
                            a "But now that you're here, what do you find? I'm not the one who needs help."
                            a @ happy "I have parachutes and a plan."
                            a "So now that you are {i}here{/i}, and need as much help as Heloise and Mona, what will drive you? And where will it take you?"
                            a "You've helped in your way. That's in the past."
                            a "Now that I'm helping in my way, what would you like me to do? Is it my responsibility to help only you? Or is my responsibility to help..."
                            show ailea akimbo with dissolve
                            a "... as many people as I can."
                            show ailea main with dissolve
                            jump a_section2_loop2
                        "Then... you're right. It's not your responsibility to help me specifically.":
                            $ a_points += 1
                            a "No?"
                            j "No... no. If I've learned anything today, it's that we're all helping each other."
                            j "Or at least..."
                            j "When we all help each other, more things get done."
                            j "Even if I'm kind of anti-social, even if I can sometimes be mean and rude and selfish..."
                            j "When I looked for help, I found it."
                            a "Ah."
                            a "And isn't that a beautiful thing?"
                            j "Yeah..."
                            j @ happy "Yeah, I guess it is."
                            jump alarm_nor
                        "I don't care. I've helped you by coming here, so now you should help me.":
                            a "Wow, no, bad take alert! Weeeeh-oooooh! Weeeeeh-ooooh! Bad take alarm going off! Weee-oooh!"
                            ##MORE DIALOGUE##
        "Fine, if it's important to you, it's important to me.":
            a "It is, Jack. Will you help me get them out?"
            menu:
                "I will.":
                    $ a_points += 1
                    a "Whoa, sick!"
                    ##MORE DIALOGUE##
                "They can tag along, but don't expect me to take on a bull for them.":
                    $ a_points -= 1
                    show ailea upset
                    a "Ah. Well. I see Rakesh has found quite a mercenary this time."
                    a "Nothing I can do about it now."
                    a "But maybe consider that there's three of us and one of you..."
                    a "And maybe consider that it's {i}my{/i} plan we'll be using..."
                    a "So maybe it's more like {i}you're{/i} tagging along with us?"
                    menu:
                        "I see your point. What do I have to do?":
                            a "Well, first things first, why don't we-..."
                            jump alarm_nor
                        "Y'know, I never actually agreed to your plan in the first place.":
                            a "You're unbelievable-..."
                            jump alarm_nor_noplan

label alarm_nor:

label alarm_nor_noplan:

label alarm_nor_section2:


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
label section3:
#Heloise + Mona Conversation


#Section 4
#Endings, arrangements of parachute partners, etc.

#if t_companion == false:
    #Boss fight!
#else:
    #takeshi's musical happening begins
    #Takeshi blows up the gate
