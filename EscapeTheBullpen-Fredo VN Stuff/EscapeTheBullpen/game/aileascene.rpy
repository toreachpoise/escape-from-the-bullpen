#dramatis personae vol. 4
define a = Character("Ailea", image="ailea", who_color="#e5c620")
default a_points = 0
define m = Character("Mona", image="mona", who_color="#aad7f2")
define h = Character("Heloise", image="heloise", who_color="#a90000")
default c_points = 0


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
    show jack cowmain at right with moveinright
    show heloise main at center_left with moveinleft:
        xzoom -1
    h "Whoa! Who the hell are you?! You don't seem to be a bull... but any self-respecting cow wouldn't be caught {i}dead{/i} wearing those old rags..."
    show mona main at left with moveinleft:
        xzoom-1
    m "Relax, Heloise."
    m @ happy "He must be one of those non-cow, non-bull people that Ailea was telling us about."
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
    j "Come on, it was clear on the way in! If we hurry, we can-..."
    a "Whoa, there. Jack, right?"
    j "Y-yeah?"
    a "Slow down. I appreciate you coming here, but I think I have a better way out."
    j "OK, let's hear it."
    jump a_section2

#Section 2

default a_section2_loop1_1 = False
default a_section2_loop2_1 = False
default parachute_reassurance = False
default a_section2_nor_loop_1_1 = False
default a_section2_nor_loop_1_2 = False
default a_section2_withr_loop_1_2 = False


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
            j @ upset "I know what parachutes are! What's your plan?"
            a "Oh."
            a @ happy "We jump off the roof with parachutes."
        "Um... 'not again'? 'This time'?!? What's going on...":
            r @ exhasperated "Years ago, Ailea break both her damn ankles trying to make her own parachute."
            a "Yes, and like I told you then, I just hadn't been able to requisition enough fabric."
            a @ happy "In here, between all the bed sheets and Mona's preference for voluminous sleeves, I had plenty!"
    label a_section_2_withr_loop_1:
    menu:
        "Are you sure parachutes are safe?" if a_section2_withr_loop_1_2 == False:
            $ a_section2_withr_loop_1_2 = True
            $ parachute_reassurance = True
            a "Pretty sure it's safe. Like... mostly sure."
            j "I can't tell how serious you are..."
            a @ irritated "I mean, do you want me to go into all the details? We used bedsheets, and wove torn pillowcases into ropes to make a harness..."
            a @ irritated "We uncoiled mattress springs and used it to maintain aerodynamic shapes. I've accounted for mass up to twice what we needed, which is useful, given your presence..."
            a @ irritated_notes"Do you want to check my notes? Make sure I didn't get it wrong?!"
            j "Uh..."
            a "Mmmmhm."
            jump a_section_2_withr_loop_1
        "But why can't we just walk out?":
            a "It'll be way harder for a big group of us to sneak out than it will be for two of you to sneak in!"
            j "A big group?"
            a "Well... is five a big group? You two, me, Heloise, Mona. I hope this isn't a problem..."
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
    a "Well, looks like the decision's been made. No way out now but the roof."
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
            jump cow_convo
        "OK. What's next? We gotta move!":
            show jack determined
            show jack main
            a "Do you know how to get parachutes ready?"
            menu:
                "I can try my best?":
                    a "... I'd better do it. I need you to talk to Mona and Heloise. Get them ready to go."
                    jump cow_convo
                "No! Why would I?!":
                    a "Fair enough. Go talk to Mona and Heloise. They need to be ready as soon as possible."
                    jump cow_convo

label a_section2_nor:
    j "Parachutes?"
    a @ happy "Specifically, parachuting off the top of the building, floating over the walls, and into the loving embrace of the city on the other side."
    label a_section2_nor_loop_1:
    menu:
        "Parachutes? Is that safe?!" if a_section2_nor_loop_1_1 == False:
            $ a_section2_nor_loop_1_1 = True
            $ parachute_reassurance = True
            a "Pretty sure it's safe. Like... yeah. Pretty sure."
            j "I can't tell how serious you are..."
            a @ irritated "I mean, do you want me to go into all the details? We used bedsheets, and wove torn pillowcases into ropes to make a harness..."
            a @ irritated "We uncoiled mattress springs and used it to maintain aerodynamic shapes. I've accounted for mass up to twice what we needed, which is useful, given your presence..."
            a @ irritated_notes"Do you want to check my notes? Make sure I didn't get it wrong?!"
            j "Uh..."
            a "Mmmmhm."
            jump a_section2_nor_loop_1
        "Well... I don't really have a deathwish, so why don't we just walk out the way I came in?" if a_section2_nor_loop_1_2 == False:
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
                                    j @ cowhappy "Yeah, I guess it is."
                                    jump alarm_nor
                                "OK, I'll speak with conviction: I don't care about grander problems. I've helped you by coming here, so now you should help me.":
                                    $ a_points -= 1
                                    a "That's a legitimately absurd point of view."
                                    j "Oh well? I'm sorry, but the only way any of us can get through life is if we look out for ourselves."
                                    a "OK, Jack. I don't live by that principle, so if you want, you can still join in on our escape plan."
                                    j "The parachutes?"
                                    a "Yeah. There's enough room for you, so no worries there. But if you want to just look out for yourself, that's fine too."
                                    j "Hmmm..."
                                    jump alarm_nor
                "Fine, if it's important to you, it's important to me.":
                    a "It is, Jack. Will you help me get them out?"
                    menu:
                        "I will.":
                            $ a_points += 1
                            a "I see why Rakesh sent you."
                            j "Yeah, So that's all good, but... can we talk about the parachutes?"
                            a "What about them?"
                            menu:
                                "I need you to be real with me. Are they actually going to work?":
                                    a "Hmmm..."
                                    j "I'm begging you, just... please tell me the truth."
                                    a "OK."
                                    a "Then in all likelihood, we'll all be dead or captured before we even get to the roof."
                                    j @ cowhorror "..."
                                    j @ cowhorror "Wh-..."
                                    show ailea happy
                                    pause 1.5
                                    show ailea main
                                    a "Just kidding, I have no idea."
                                    jump alarm_nor
                                "It's an insane idea that'll never work.":
                                    a "You are such a negative person."
                                    j "I'm just being realistic here."
                                    a "Well here's my realism: the doors and gates are locked, the walls are high, yet we must be free."
                                    a "So excuse me if I've found myself looking for ways to fly."
                                    jump alarm_nor
                        "They can tag along, but don't expect me to take on a bull for them.":
                            $ a_points -= 1
                            a @ upset "Ah. Well. I see Rakesh has found quite a mercenary this time."
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
                                    jump alarm_nor

label alarm_nor:
    play sound "audio/alarm.mp3" volume .25
    "..."
    a @ surprised "Uh-oh... looks like somebody realized you aren't actually supposed to be here."
    j @ scared "Oh god, is this bad?!"
    show ailea determined
    a "Nah, just give me a second..."
    hide ailea with moveoutleft
    a "Hmmm... maybe if I..."
    play sound "audio/brokenelectronics.mp3" volume.25
    a "There we go!"
    show ailea determined at left with moveinleft
    a "There, that's better. I jammed the doors and bought us some time."
    a "Think quick, Jack. What's your plan? You coming with us, or waiting here to get caught?"
    menu:
        "OK, Ailea. I trust your engineering skills. I'm coming with you." if parachute_reassurance == True:
            $ a_points += 1
            a "Then I need you to go get Mona and Heloise while I get the parachutes ready."
            j "You got it, boss!"
            jump cow_convo
        "Parachutes are better than bulls! Let's go!" if parachute_reassurance == False:
            $ a_points += 1
            a "On that we can agree. You get Mona and Heloise, I'll get the parachutes."
            j "On it!"
            jump cow_convo
        "Forget it! I'm not risking my life on your goofball parachute plan!":
            $ a_points -= 1
            j "We're doing my plan. You and the cows get whatever weapons you can find, we'll fight our way out."
            a "What's this all about, Jack? Why won't you just come with me?"
            j "Because if we had just stuck to my plan, we'd be out by now!"
            a "No we wouldn't be. We'd be trapped halfway down the building, all exits cut off."
            j "All exits are cut off now."
            a "Except for the roof."
            menu:
                "And you think your crazy cartoon plan is going to work?!":
                    a "First of all, it's based in science."
                    a "Second of all, what other choice do you have?"
                    a "Heloise claims she's handy in a fight, but I've never seen it. I'm sure you can handle yourself if you've made it this far..."
                    a "But Mona and I aren't really fighters."
                    a "I trust myself to see us through this without unnecessary violence."
                    menu:
                        "But... I'm so tired of running.":
                            show jack cowsad
                            a "I know, kid."
                            a "I know."
                            a "Maybe there was a time when standing and fighting was the right idea..."
                            a "Or maybe that day will come."
                            a "Or... maybe that time is all the time, and it just takes the right people in the right place at the right time..."
                            a "But, at least for me, I know it's time to run and hide and keep living in spite of everything."
                            menu:
                                "What if it's my time to stand and fight?":
                                    a "How do you know when it's your time?"
                                    a "What good would you be doing?"
                                    a "What could we build from there?"
                                    j "I don't know... but maybe it's just good to fight every once in a while."
                                    a "It's also good to protect each other, when the chance presents itself."
                                    a "If you're so willing to be violent... come with us. Protect us."
                                    menu:
                                        "Hmmm... that feels right, actually. You can count on me.":
                                            j ""
                                            a "OK, you get Heloise and Mona while I get the parachutes ready. Thanks, Jack."
                                            jump cow_convo
                                        "No. My place is here.":
                                            a "OK, then. Stay here and just... see what you can do. I have to go get everything ready."
                                            a "Good luck, Jack."
                                            hide ailea with moveoutleft
                                            jump cow_convo_denied
                                "That seems like a selfish approach.":
                                    a "How so?"
                                    j "You're just living life as if your principles are the only ones that matter."
                                    a "Principles? You're still talking about principles?"
                                    j "What else is there?"
                                    a "What about helping people, Jack? Or do you only help people when your principles call for it?"
                                    a "Forget principles!"
                                    a "I know I'm useless in a fight, but every day I also know that people are alive because of my skills and knowledge as a healer."
                                    a "I can do more good alive out there than dead in here."
                                    menu:
                                        "But what if your plan fails and you end up out there and dead?":
                                            a "Then at least my abilities won't be stolen by this fertility center."
                                            a "When I help people in here, they're just fed back into the machine..."
                                            a "So it's time for me to go. To either get back to the city, or die trying, and either way:"
                                            a "Net positive."
                                            j "Huh..."
                                            a "So what'll it be, Jack?"
                                            jump alarm_nor_menu_1
                                        "So it's pragmatic...":
                                            a "Pragmatic with the end goal of a kinder and healthier world, but sure."
                                            j "Huh..."
                                            a "So what'll it be, Jack?"
                                            jump alarm_nor_menu_1
                        "Killing matrons and bulls is necessary violence.":
                            a "What?!"
                            j "They're the ones responsible for all of this! If we want it to stop, we have to deal with them."
                            a "They're people! Every time a bull or matron dies, that's a human life snuffed out."
                            j "So it doesn't matter that they harm the world? That they've destroyed lives?!"
                            a "Of course that matters, and they're responsible for the evils they've committed..."
                            a "But why does that give you the right to do violence against them?"
                            j "To stop them from doing violence against others."
                            a "But they're people, Jack. People aren't just tools of violence."
                            menu:
                                "Some people become tools: cows, bulls, matrons...":
                                    a "If people are used as tools, then they've been victimized."
                                    a "Cows, bulls, matrons..."
                                    a "We've all been tortured into our roles in one way or another."
                                    j "The only difference is, so me roles get to turn around and start torturing everyone else."
                                    a "Do you think that's a reward? Do you think being a torturer is good for you? For your soul and mind?"
                                    a "Hold them accountable, Jack, but don't lose your compassion."
                                    j "Compassion for torturers?"
                                    a "Yes."
                                    a "Now, time's wasting. What's it going to be?"
                                    jump alarm_nor_menu_1
                                "So... we take away their tools?":
                                    a "Seems like the right idea to me. But that's just me."
                                    j "But what would that even mean?"
                                    a "Blow up their weapons factories. Destroy their registries and scanners and drones. Disrupt their networks."
                                    a "Their greatest tool is that the best established physical and psychic infrastructures belong to them."
                                    a "So while we're blowing up and destroying and disrupting, start building tools for ourselves."
                                    j "And how are we supposed to do any of that?!"
                                    a "Not sure."
                                    a "But I'm pretty sure it won't be by standing here and debating things while there were wolves at the door."
                                    j "I thought you said they were people..."
                                    a "Yes, but right now they are hungry and have teeth, so... shall we?"
                                    jump alarm_nor_menu_1
                "I don't consider that an exit.":
                    a "Then maybe the issue is a failure of imagination."
                    a "Quick thought experiment: what if the roof was an exit?"
                    menu:
                        "I suppose... I would use it.":
                            label alarm_nor_loop1:
                            a "Brilliant!"
                            j "But..."
                            a "Jack, quiet. The roof is an exit."
                            j "The roof is an exit?"
                            a "The roof is an exit."
                            a "Because of my ingenious parachute design."
                            j "And you're pretty sure they'll work."
                            a "Pretty sure. You coming or staying?"
                            jump alarm_nor_menu_1
                        "But it's not...":
                            a "No, but just imagine."
                            menu:
                                "It's. Not. Going. To. Happen. How am I supposed to imagine it?!":
                                    a "Ugh, you won't even try?"
                                    menu:
                                        "We'll never make it off the roof!":
                                            a "..."
                                            a "OK."
                                            a "Would you at least be willing to trust in {i}my{/i} imagination of the roof as an exit?"
                                            menu:
                                                "Ugh, fine...":
                                                    jump alarm_nor_loop1
                                                "Sorry, Ailea. I have to stay here. In reality.":
                                                    a "Then I guess this is where we part ways. Do what thou wilt, my friend. Good luck."
                                                    jump cow_convo_denied
                                        "Oh, fine! I'll do this thought experiment, just for you!":
                                            j "I guess if the roof was an exit... and I had to leave... and there were no other options..."
                                            a "Yeah?"
                                            j "I guess I would use it?"
                                            jump alarm_nor_loop1
                                "OK, OK, I'll do my best...":
                                    j "Hmmm. I guess I would... use it?"
                                    jump alarm_nor_loop1
label alarm_nor_menu_1:
    menu:
        "OK, I'm coming. What do I need to do?":
            a "Go get Heloise and Mona ready to go. I'll get the parachutes."
            j "OK!"
            jump cow_convo
        "I'm staying. I want to take out as many bulls as I can today.":
            a "OK... that's your decision, I guess?"
            a "But I think there's more to you than that..."
            a "More that you could do."
            a "I'm wasting time now. I hope I see you again, Jack."
            jump cow_convo_denied


#Section 3

default cow_convo_loop_1_1 = False
default cow_convo_loop_1_2 = False
default cow_convo_loop_1_3 = False
default cow_convo_loop_1_4 = False

label cow_convo:
    scene harem bg with fade
     heloise main at center_left with moveinleft:
        xzoom -1
    show mona main at left with moveinleft:
        xzoom -1
    if a_points > 0:
        $ c_points += 1
    if a_points < 0:
        $ c_points -= 1
    if r_companion == True:
        show jack main at right with moveinright
    if r_companion == False:
        show jack cowmain at right with moveinright
    h "Was that alarm your fault?"
    m "Stop it, Heloise! I'm sure it was nothing to do with him. Probably just some bulls getting into a fight or..."
    if r_companion == False:
        j "No, it was me."
        h @ upset "OK. Thanks for that, then. Can't wait to get cavity searched."
    if r_companion == True:
        menu:
            "Y-yeah, that was my fault. Sorry.":
                h @ upset "OK. Thanks for that, then. Can't wait to get cavity searched."
            "It was Rakesh, actually.":
                h @ upset "OK, great. Now I know who to blame when we all get cavity searched."
    j "Not this time."
    h "..."
    h "What does that mean?!"
    j "Ailea says it's time to go."
    show heloise happy
    "We're escaping?"
    show mona scared
    m "We're... escaping?"
    label cow_convo_loop_1:
    if cow_convo_loop_1_2 and cow_convo_loop_1_1 == True:
        jump cow_convo_continue
    menu:
        "You know about the plan?" if cow_convo_loop_1_1 == False:
            $ cow_convo_loop_1_1 = True
            m "Y-yeah... we know."
            show heloise main
            h "Some of us are less excited about it than others."
            m "I'm just saying... if she wants us to jump off the roof..."
            m @ upset "Why not find a way to build a portable micro-gravity field generator?!"
            h "What, with bedsheets?"
            menu:
                "Don't worry... I understand the science. Ailea knows what she's doing.":
                    $ c_points += 1
                    m "Are you sure???"
                    j @ happy "Oh, yeah, no worries."
                    if parachute_reassurance == True:
                        j "She did all the calculations, what with mass and... aerodynamics... and stuff."
                        m "Did she show you her notes?"
                        j "..."
                        j "Yeah?"
                        m "OK!!! As long as it's peer reviewed, I trust the science."
                        h @ suspicious "Yes. So glad our new friend here {i}understands the science{/i}."
                        jump cow_convo_loop_1
                    if parachute_reassurance == False:
                        j "I've heard about these things, these parachute things, they... I know they work, y'know. I've seen videos and stuff."
                        m "..."
                        h "And I'm sure those videos were..."
                        j "Not faked at all!"
                        m @ scared "Ok. As long as they're not fake videos, I think..."
                        extend " I..."
                        extend " believe..."
                        extend " you..."
                        extend " ???"
                        j "Good, because I'm telling the truth."
                        m @ happy "Yeah! OK!"
                        jump cow_convo_loop_1
                "I know what you mean, but what other choice do we have?!":
                    $ c_points -= 1
                    m "Oh God, you're right!"
                    h "Calm down, Mona..."
                    m "It's come down to this! I have to choose between a life of misery or death itself!!!"
                    h "Thanks a lot, Jack."
                    jump cow_convo_loop_1
        "Are y'all ready to go?"if cow_convo_loop_1_2 == False:
            $ cow_convo_loop_1_2 = True
            h @ happy "Yes! Can't wait to get out there, back into the world."
            m "I just..."
            show heloise main
            h "Mona isn't sure she wants to come..."
            m "That's not true! I know I want to go with you and Ailea..."
            m "I {i}need{/i} to, or I'll die."
            m "But... I know what it's like out there. It's scary and people try to hurt each other, and at least here..."
            m @ desperate "At least here I know who's going to hurt me!"
            h "Mona, it'll be OK."
            h "Ailea will be there, and I'll be there..."
            if r_companion == False:
                h "And hey, if this kid came from out there, it can't be all bad!"
            if r_companion == True:
                h "And hey, at least two of the people out there came in here to save us, so it can't be that bad!"
            if t_companion == True:
                if r_companion == True:
                    show jack cowhappy
                if r_companion == False:
                    show jack happy
                j "And also this person Takeshi is waiting out there for us! The world is {i}full{/i} of helpful people!"
                if r_companion == True:
                    show jack cowmain
                if r_companion == False:
                    show jack main
            m "Yeah... I guess you're right."
            m "And like I said, if I stay here... I won't survive. It's time to go."
            h @ upset"Yeah, Jack! Time to go!"
            m @ upset "What the hell are we doing standing around talking?!"
            j "All right, jeez..."
            jump cow_convo_loop_1
    label cow_convo_continue:
        if r_companion == True:
            jump a_section4_withr
        if r_companion == False:
            jump a_section4_nor

label cow_convo_denied:
    scene harem bg with fade
    show jack cowmain at right with moveinright
    show mona main at center_left with moveinleft:
        xzoom -1
    m "Hey, I overheard some stuff..."
    menu:
        "Don't worry about it.":
            m "I'm not worrying."
            show heloise main at left with moveinleft:
                xzoom -1
            h "Mona, come on! Ailea says it's time to go!"
            m "Just a second, Heloise."
            m "Jack, I think you're making a mistake."
            menu:
                "How would you know?":
                    m @ desperate "Because it's a mistake I would like to make."
                    j "Huh?"
                    m "Everything in my body is screaming at me to just stay here."
                    m "I want to do nothing and stay here with a bed I know, in a room I'm familiar with, a routine that I hate, but at least I know what to expect..."
                    m "All of that would be easier than trusting Ailea and trusting you, even trusting Heloise..."
                    m "But it would still be a mistake."
                    m "Don't make easy mistakes, Jack. Please come with us."
                    menu:
                        "OK. You're right. I'll come.":
                            m "Yay!"
                            j "Thanks, Mona."
                        "It's... it's just too late for me. I'll hold them off as long as they can":
                            h "Oh my {i}God{/i}, this dude."
                            m @ sad "Y-you're sure?"
                            menu:
                                "Yeah, just go. I'm done.":
                                    hide heloise with moveoutleft
                                    m "Please don't stay here, Jack."
                                    hide mona with moveoutleft
                                    menu:
                                        "(Follow them)":
                                            jump a_jack_reluctant_ending
                                        "(Sit down and wait)":
                                            jump a_worst_ending
                                "...":
                                    show jack cowdepressed
                                    h "I mean, listen... you came this far, right?"
                                    j "..."
                                    h "So... is that all gonna be a waste?"
                                    j "..."
                                    m "Ugh!!!"
                                    m "At least try to make it to the end!!!"
                                    m "EVEN IF THAT END IS DYING BECAUSE SOME CRAZY LADY THINKS PARACHUTES ARE REAL!!!"
                                    j "..."
                                    j "Parachutes are real..."
                                    m "OK, then come on, you little optimist."
                                    hide heloise with moveoutleft
                                    hide mona with moveoutleft
                                    menu:
                                        "(Follow them)":
                                            jump a_jack_reluctant_ending
                                        "(Sit down and wait)":
                                            jump a_worst_ending
                "I think my whole {i}life{/i} is just a series mistakes.":
                    m "Well... mine too, but I'm ready to start changinging that."
                    menu:
                        "Good for you.":
                            m "And... good for you too, right?"
                            m "When I said that thing about changing things..."
                            j "..."
                            m "Do you understand how that also applies to you?"
                            menu:
                                "Yeah. I do!":
                                    m "Oh, good! I didn't want to have to explain it, I would have gotten really condescending about it."
                                    m "So..."
                                    j "I'll come, Mona. Thank you."
                                    m "For what?"
                                    j "For... talking to me."
                                    m @ happy "Oh, no big deal, I love talking."
                                    hide heloise with moveoutleft
                                    hide mona with moveoutleft
                                    menu:
                                        "(Follow them)":
                                            jump a_jack_reluctant_ending
                                        "(Sit down and wait)":
                                            jump a_worst_ending
                                "Just shut up.":
                                    m @ upset "!!!"
                                    h @ upset "Hey! Lay off, buddy."
                                    j "Of course I understand how it might apply to me, but that doesn't mean I think it's possible."
                                    h "OK, well. Whatever, dude. Like mona said, you have a choice to make."
                                    hide heloise with moveoutleft

                        "Well it's too late for me.":
                            h "Boohoo, too late for me, boohoo."
                            h "What a baby. Come on, Mona, let's go."
                            m "I know that it feels like that, Jack, but every mistake begins as a choice..."
                            m "And it's OK to make mistakes over and over again, because there's always new choices, and always new contexts in which we're choosing..."
                            m "But every once in a while, it's obvious."
                            m "So please don't stay here..."
                            h "Let's go!"
                            hide heloise with moveoutleft
                            m "Please, Jack."
                            hide mona with moveoutleft
                            menu:
                                "(Follow them)":
                                    jump a_jack_reluctant_ending
                                "(Sit down and wait)":
                                    jump a_worst_ending
                        "I hadn't thought of it that way...":
                            m "Well now that you {i}are{/i} thinking about it that way..."
                            m "Um..."
                            m "What are your thoughts on this matter?"
                            menu:
                                "I guess I could... stop making mistakes with you?":
                                    m "So you'll come after all?"
                                    j "Yeah. I'm coming."
                                    m @ happy "Wow! I'm getting goosebumps!"
                                    h "OK, then. Both of you, come on!"
                                    jump a_jack_reluctant_ending
                                "I don't think you're one to be handing out life advice.":
                                    h @ upset "Hey!"
                                    h "OK, Mona, let's get out of here."
                                    hide heloise with moveoutleft
                                    m "So rude..."
                                    m "But please come, Jack. This isn't where you want to die."
                                    hide mona with moveoutleft
                                    menu:
                                        "(Follow them)":
                                            jump a_jack_reluctant_ending
                                        "(Sit down and wait)":
                                            jump a_worst_ending
        "Get the hell away from me!":
            m "Oh! Sorry..."
            show heloise main at left with moveinleft:
                xzoom -1
            h "Hey, what are you yelling at {i}her{/i} for, you freak?"
            m "Ugh, calm down, Heloise. I was just trying to talk to him."
            h "You're wasting your time."
            show mona determined at center_left:
                xzoom 1
            m "Hey!!!"
            m "Ailea taught us to do what's necessary for our survival, right?"
            m "So maybe for me, for my heart..."
            m "It's necessary to try to help people..."
            m @ determined "Even if it's a waste of time!!!"
            h "OK, fair enough."
            j "Are you two done?"
            show mona determined at center_left:
                xzoom -1
            m "No. Jack, I think you're making a mistake. I know heights are scary, but it'll be OK!"
            menu:
                "Scary for you, maybe.":
                            m "Um, OK, fair, wow."
                            m "But I'm still going."
                            m "Whatever it is that's keeping you here..."
                            m @ upset "GET OVER IT!!!"
                            m "This isn't where you want to die."
                            menu:
                                "No... I guess not.":
                                    m "So you'll come?"
                                    j "Yeah..."
                                    menu:
                                        "Let's go!":
                                            jump a_jack_reluctant_ending
                                        "I'm sorry for snapping earlier...":
                                            m "Oh, yeah..."
                                            m @ happy "Thanks for saying that."
                                            h "Hmph."
                                            h "I'm still watching you, kid."
                                            jump a_jack_reluctant_ending
                                "You have no idea where I want to die.":
                                    m "Oh... I just assumed you didn't want to die at all."
                                    m "My bad."
                                    h "Well... seems like things are working out just fine, then."
                                    show heloise at left:
                                        xzoom 1
                                    hide heloise with moveoutleft
                                    show mona at left with moveoutleft
                                    m "Well... if you change your mind..."
                                    m "Please come with us."
                                    show mona at left:
                                        xzoom 1
                                    hide mona with moveoutleft
                                    menu:
                                        "(Follow them)":
                                            jump a_jack_reluctant_ending
                                        "(Sit down and wait)":
                                            jump a_worst_ending

                "OK? You're all going to die!":
                            m "Maybe?"
                            h "Who cares?"
                            m "I'd rather do everything I can to look for a better life, even if that means dying."
                            h "Life in here isn't worth living, Jack."
                            h "Now we gotta go, so maybe think about that for a second. You won't have much longer than that."
                            hide heloise with moveoutleft
                            m "Whatever you decide..."
                            m @ sad "..."
                            m "Just... please come with us."
                            hide mona with moveoutleft
                            menu:
                                    "(Follow them)":
                                        jump a_jack_reluctant_ending
                                    "(Sit down and wait)":
                                        jump a_worst_ending




#Section 4
label a_worst_ending:
    "You stay behind."
    "They take you alive."
    "You never learn what happened to the others."
    return

label a_jack_reluctant_ending:
    #"Jack rejoins the party, and the escape proceeds as normal."
    scene harem bg with fade
    show jack cowmain at right
    show mona main at center_left:
        xzoom -1
    show heloise main at left:
        xzoom -1
    show ailea main at center
    m @ happy "Jack! You're coming after all!"
    j "Yeah. What's the point of staying behind to either die or live a life of torture."
    h @ happy "Suddenly reasonable. All's well that ends well."
    j "Just... hang on a second..."
    hide jack with moveoutright
    show jack main at right with moveinright
    m "Ooooh!"
    m "If you don't want it anymore..."
    m "Can I have your outfit?"
    a "OK, enough! We gotta move."
    a "Heloise, you can take care of Mona, right?"
    h "You betcha."
    show mona happy
    a "Jack, with me."
    a "Follow close, everyone! We're getting out of here!"
    m @ happy "Yay!"
    h @ happy "Finally."
    j @ happy"Let's go!"
    #jump to level 4 - no rakesh, check for takeshi companion: y/n, plan: concert/dance
    return

label a_section4_withr:
    #"Jack and Rakesh discuss final dealings with Ailea + Co"
    scene harem bg with fade
    show rakesh main at center_right:
        xzoom -1
    show jack main at right
    show mona main at center_left:
        xzoom -1
    show heloise main at left:
        xzoom -1
    show ailea main at center
    a "OK, everyone ready?"
    m @ happy "Yeah!"
    h @ happy "Been ready for a while now."
    j @ happy "Good to go!"
    r @ happy "What are we waiting for?!"
    a "Heloise, you can take care of Mona, right?"
    h "Of course."
    show mona happy
    a "Jack, you're with me."
    a "Rakesh..."
    r @ happy "Hoverboard juiced up and ready to fly."
    a "Then let's fucking go!"
    #jump to level 4 - with rakesh, check for takeshi companion: y/n, plan: concert/dance
    return

label a_section4_nor:
    #"Jack discusses final dealings with Ailea + Co"
    scene harem bg with fade
    show jack main at right
    show ailea main at center
    show mona main at center_left:
        xzoom -1
    show heloise main at left:
        xzoom -1
    a "OK, everyone ready?"
    m @ happy "Yeah!"
    h @ happy "Been ready for a while now."
    j @ happy "Now that I'm back in my normal clothes, yeah!"
    m "Aww, I thought it was nice."
    a "Heloise, you can take care of Mona, right?"
    h "Of course."
    show mona happy
    a "Jack, you're with me."
    a "Let's fucking go!"
    #jump to level 4 - no rakesh, check for takeshi companion: y/n, plan: concert/dance
    return
