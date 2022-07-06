#Dramatis Presonae Addition
define t = Character("Takeshi", image="jack", who_color="#eaffc5")
default t_points = 0
default t_companion = False
default trust_response_1 = 0
default t_refusedhelp = False
default t_bull_discussion_flag = False

#Scene 2
default t_section2_flag = 0
label takeshi_garage:

scene takeshi_shop_bg with fade
show takeshi main at left with moveinleft
show jack main at right with moveinright

#Introductions
t "Well, well, well. Who is this, alighting upon my doorstep?"
menu:
    "Oh, wow... it's really you! I'm trying not to freak out.":
        $ t_points += 2
        show jack upset with dissolve
        j "Your music is EVERYTHING."
        show jack main with dissolve
        t "Oh, well, hello! Always nice to meet a fan, uh..."
        j "Jack."
        t @ happy "Always nice to meet a fan, Jack."
    "Uh... Takeshi?":
        t "The literal one and only!"
if r_companion == True:
    show rakesh main at center with moveinright:
        xzoom -1
    r "Hey, Takeshi! How you been, man?"
    t "Been better, been worse..."
    t "I heard about Ailea, brother. Can't believe they got to her."
    r "That's why we're here."
    jump t_greeting_menu
else:
    j "Rakesh sent me... He mentioned you might be able to help."
    t "Help with what?"
    j "I'm pregnant. I need an abortion."
    t "Hmmm... And Ailea's been missing for weeks. I see the problem."
    jump t_greeting_menu

#Section 1

#with Rakesh
label t_greeting_menu:
if r_companion == True:
    j "Takeshi, we need your help."
    r "We're breaking Ailea out of the breeding facility."
    t @ scared "The breeding facility... you're not asking me to go back, are you?"
    j "Uh... Go back?"
    r "Takeshi... xe escape once before..."
    menu:
        "How did you escape?!":
            t "Well... it wasn't as hard for me as it might have been for others."
            j "Huh?"
            r "Takeshi... you don't have to..."
            t "It's fine."
            t "I had my advantages when escaping. I... I used to be a bull."
            jump t_bull_discussion
        "Takeshi... the badass rockerboy... used to be a cow?":
            $ t_points -= 1
            t "I wasn't a cow. I wasn't anything they called me."
            j @ embarrassed "Yeah, I know what you mean..."
            t "And even then..."
            t "*sigh*"
            t "Even then, they didn't call me a cow..."
            show jack upset
            jump t_bull_discussion
    label t_bull_discussion:
        $ t_bull_discussion_flag = True
        j "YOU WERE A BULL?!"
        t "..."
        extend "Yeah."
        show jack upset with dissolve
        if r_companion == True:
            t "Rakesh, why would you bring me here?! This lunatic could go berserk any second!"
            r "Calm down, friend. Takeshi's OK."
            j "No way dude!"
        if r_companion == False:
            j "What the shit?! Get the fuck away from me!"
            t "Jack, it's... it's OK, I'm not a bull anymore..."
            j "Yeah right! You're trying to trick me!"
        j "Bulls are vicious, unthinking rape machines!"
        t "OK, enough of that."
        j "What, they aren't?!"
        t "No."
        extend "They're human beings."
        menu:
            "Not like me and Rakesh, they're not. Rakesh, get behind me." if r_companion == True:
                $ t_points -= 1
                r @ shrug "I... *sigh* Sorry, Takeshi. Didn't know he'd be like this."
                t "It's fine. Let me... let me just explain"
                jump t_bull_flashback
            "Not like me, they're not." if r_companion == False:
                $t_points -= 1
                t "Let me explain... maybe then you'll understand."
                jump t_bull_flashback
            "Human beings?! Do you have any idea what bulls have done to me?!":
                t "I have an idea. To you and a lot of people..."
                j "Yeah, beacuse you were one of the ones doing it!"
                t @ angry "I never..."
                show takeshi sad
                t "*sigh*"
                t "Listen..."
                jump t_bull_flashback
        label t_bull_flashback:
            show takeshi sad
            t "When they find out you're a bull, they come for you."
            t "They take you from your family."
            t "They pump you full of so many drugs and hormones that you're always horny."
            t "The older bulls can't always get access to the cows, if too many of them are pregnant or injured..."
            t "So they start fighting."
            t "And the fighting turns into fucking... and the younger bulls don't really have a say in the matter."
            show jack main with dissolve
            t "I was 16 when I got out. By then, I had lost count of how many times I'd been raped."
            t "So believe me, I have some idea of what bulls can do."
            menu:
                "That's... that's terrible. I never thought about what bulls go through...":
                    show jack main with dissolve
                    $ t_points += 1
                    t "I get it... If you're a cow, all you ever see is the ones who make it through."
                    t "To be a bull, to be the bull they want, you have to the strong and cruel..."
                    t "Most don't survive. They're gelded and turned out to the streets."
                    t "Without the drugs to keep them going, they get sick... well. Like I said, most don't survive."
                    t "But some of us... we make it out, and we do our best to pick up the pieces."
                    menu:
                        "I'm sorry, Takeshi.":
                            $ t_points += 1
                            t "It's fine. I've made my peace with it, more or less. I got my music and..."
                            t @ sad "..."
                            extend "I'll be OK."
                            jump t_bull_postd
                        "Good riddance to the ones who die.":
                            $ t_points -= 1
                            t "No matter what you think of them, their lives are being ruined. They're being hurt."
                            j "I guess so... I feel bad for the young ones at least."
                            t "..."
                            extend "Close enough, I guess."
                            jump t_bull_postd
                "That doesn't change anything. You still had an easier life than the cows.":
                    $ t_points -= 1
                    t "Easier doesn't mean easy. The breeding center hurts everyone and everything it touches."
                    if r_companion == True:
                        r @ angry "It's a poison."
                        r "Someday, it's gonna burn to the ground."
                        j "Yeah... But it sure as shit won't be the bulls doing the burning."
                    else:
                        t "It would be better for everyone, bulls included, if it burned to the ground."
                        j "Yeah, but it sure as shit own't be the bulls doing the burning."
            t "Maybe you're right, Jack..."
            jump t_bull_postd
            label t_bull_postd:
                show takeshi main
                t "Anyway, it was Ailea who got me out. She risked her life and safety for me. So if you're rescuing her from that place..."
                extend "I'll do what I can to help..."
                t "But I can't go back inside."
                if t_section2_flag == 1:
                    jump t_plan_menu
                else:
                    jump t_section2

#Without Rakesh
if r_companion == False:
    menu:
        "Hang on, how do I know I can trust you?!" if trust_response_1 == 0:
            $t_points -= 1
            $ trust_response_1 = 1
            t "Hm. I could ask you the same question, but where would that get us?"
            j "Uh..."
            t "If Rakesh sent you, just ask yourself: do you trust Rakesh?"
            menu:
                "How am I supposed to know!? I literally met him this morning.":
                    $t_points += 1
                    t "Ah... recursion. Neat."
                    j "What do you mean?"
                    t "How do you know if you trust someone..."
                    t "...if you don't know if you can trust someone else..."
                    t "...because you don't know if you can trust someone else..."
                    j "..."
                    t "Mad respect, bro. You're asking deep questions."
                    j "Thanks? I guess?"
                    t "Totally."
                    jump t_greeting_menu
                "Yes, of course, he helped me...":
                    $ trust_response_1 = 2
                    t "Then you should trust me."
                    j "OK, that makes sense!"
                    t "Of course, that doesn't explain why Rakesh didn't help you himself..."
                    menu:
                        "He did his part, right? From here on out, it's up to me.":
                            $ t_points += 1
                            t "I suppose it is."
                            jump t_greeting_menu
                        "Hey... yeah! Why didn't Rakesh come with me?":
                            t "Who can say? Rakesh is an enigmatic being."
                            jump t_greeting_menu
                "No... he claims he's an adult, yet he looks like a child." if rakesh_age_comment == True:
                    $t_points -= 1
                    $ trust_response_1 = 3
                    t "That's... a terrible reason to not trust someone."
                    j "..."
                    t "Well, he sent you here, so you apparently trusted him enough to listen."
                    jump t_greeting_menu
                "No. I've never seen him before..." if rakesh_age_comment == False:
                    $ trust_response_1 = 3
                    t "Maybe open yourself up to new experiences. Not everybody's out to get you."
                    jump t_greeting_menu
        "But about this trust thing..." if trust_response_1 == 1 or trust_response_1 == 3:
            t "Yeah?"
            j "I still don't know where we stand!"
            t "Does it matter?"
            menu:
                "Yes.":
                    $trust_response_1 = 4
                    t "Ah. Well. Then decide for yourself..."
                    t "And then, however you end up feeling, decide what you're going to do."
                    jump t_greeting_menu
                "No.":
                    $trust_response_1 = 4
                    t "OK. Then why ask?!"
                    jump t_greeting_menu
        "Do you trust me?" if trust_response_1 == 2:
            $ trust_response_1 = 4
            t "Yes."
            j "Oh..."
            t "It can be that simple, kid."
            j "Huh..."
            jump t_greeting_menu
        "I need your help rescuing Ailea.":
            $ t_points += 1
            t "Whoa... You mean... You're gonna break into the breeding center?"
            j "That's the idea."
            j @ determined "But we'll need a plan."
            jump t_section2
        "Never mind, I don't need your help." if t_refusedhelp == False:
            $ t_points -= 1
            $ t_refusedhelp = True
            t "Are you sure? Why did Rakesh send you here?"
            menu:
                "I don't care what Rakesh says, I'll do it on my own!":
                    $ t_points -= 1
                    t "Yeah, I've heard that before."
                    t "Right before whatever lone wolf individualist got themselves KILLED."
                    menu:
                        "You can't scare me with your collectivist fear-mongering! My own strength will carry me through!":
                            $ t_points -= 1
                            t "OK, guy, just think about what you're saying."
                            t "You didn't make it this far on your own."
                            extend "You needed Rakesh."
                            t "You can't give yourself an abortion."
                            extend "You need Ailea."
                            t "You see what I'm saying?"
                            menu:
                                "You're right... none of us can do it on our own...":
                                    $t_points += 1
                                    t "Exactly, my friend. So. How can I help you?"
                                    jump t_greeting_menu
                                "Well. I'm special, so don't even worry about it.":
                                    $ t_points -= 1
                                    t "..."
                                    t "I..."
                                    extend "Ugh. OK, I guess. I'll see you later."
                                    jump t_worstending
                        "Ah... I see your point.":
                            $ t_points += 2
                            j "I didn't get this far by relying on myself... I got this far by seeking help from others, from helping in return..."
                            t "Precisely my point. And now that points is no longer mine, but ours, as all things should be."
                            j "W..."
                            extend "What?"
                            t "I... you know, we're all in this together. What's mine is yours. Ownership is an illusion."
                            j "Right..."
                            jump t_greeting_menu
                "I guess... he wanted to help me.":
                    $ t_points += 1
                    t "Seems reasonable. I am, after all, very helpful."
                    jump t_greeting_menu

#Section 2
label t_section2:
$ t_section2_flag = 1
$ plan_getin = 0
$ plan_inside = 0
$ plan_getout = 0
if t_points > 0:
    "(Takeshi seems to like you.)"
if t_points == 0:
    "(Takeshi regards you with an inscrutably neutral expression.)"
if t_points < 0:
    "(You have angered Takeshi.)"
label t_plan_menu:
    if plan_getout == 1 and plan_inside == 1 and plan_getin == 1:
        t "So what's my part in all this?"
        jump t_section3
    menu:
        "Let's talk about getting into the breeding center." if plan_getin == 0:
            $ plan_getin = 1
            t "OK. What are you thinking?"
            if r_companion == True:
                j "Rakesh?"
                r "I take care of any locks. No problem at all."
                t "Wow. Loving the confidence."
                jump t_plan_menu
            if r_companion == False:
                j "I found a disguise that I think will work... I'll be able to get in if I look like *ugh* a cow."
                t "Hmmm... Are you gonna shave?"
                j @ upset "Ugh, I hadn't thought about it..."
                t "No worries, we'll find you a veil or something."
                menu:
                    "This is the worst!":
                        j "I spent my whole life refusing to be a cow for them, and now..."
                        t "Oof, that's rough buddy."
                        t "Think about it this way: This isn't you. This is just something you're doing to help people in need."
                        menu:
                            "That's one way to look at it...":
                                $ t_points += 1
                                j @ happy "I'll focus on who I'm helping. That does make it easier. Thanks, Takeshi."
                                jump t_plan_menu
                            "I don't care. This is sick!":
                                $ t_points -= 1
                                t "You don't care about helping people?!"
                                j "Not this much."
                                t "Well, can you think of another way in?"
                                j "Maybe if I had more time..."
                                t "Time we don't have, my friend."
                                jump t_plan_menu
                    "Yeah, that could work...":
                        t "And also, with a veil, you can keep what's sure to be an expression of purest revulsion hidden!"
                        j "Hey! Multiple uses."
                        jump t_plan_menu
        "Let's talk about what's inside." if plan_inside == 0:
            $ plan_inside = 1
            jump t_plan_menu
        "Let's talk about how to escape." if plan_getout == 0:
            $ plan_getout = 1
            jump t_plan_menu

label t_section3:
    jump endings



label endings:
if t_points > 0:
    "(Takeshi will aid you in your quest!)"
if t_points <= 0:
    if t_fan == True:
        "(You may be a fan of Takeshi, but xe's no fan of yours! You travel on without hir.)"
    if t_fan == False:
        "(Takeshi didn't think your plan was going to help anyone. Xe's staying home on this one, pal.)"
    return

label t_worstending:
"(You proceed without Takeshi's assistance)."
#jumps to level 3 without takeshi
return


return
