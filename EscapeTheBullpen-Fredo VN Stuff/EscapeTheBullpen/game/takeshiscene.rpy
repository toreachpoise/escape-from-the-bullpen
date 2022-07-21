#Dramatis Presonae Addition
define t = Character("Takeshi", image="takeshi", who_color="#eaffc5")
default t_points = 0
default t_companion = False

#Scene 2
label takeshi_garage:

scene takeshi_shop_bg with fade
show takeshi main at left with moveinleft
show jack main at right with moveinright

#Introductions
t "Well, well, well. Who is this, alighting upon my doorstep?"
menu:
    "Oh, wow... it's really you! I'm trying not to freak out.":
        $ t_points += 1
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
    t @ happy "Been better, been worse... Just vibing as a fun times music guy..."
    t @ sad "I heard about Ailea, brother. Can't believe they got to her."
    r "That's why we're here."
    jump t_greeting_menu
else:
    j "I heard you might be able to help me..."
    t "Help with what?"
    j "I need an abortion and-..."
    show takeshi nervous
    t "That's not my business. I'm just a fun times music guy."
    t "Who told you to come here?"
    jump t_greeting_menu

#Section 1
#with Rakesh
label t_greeting_menu:
if r_companion == True:
    j "Takeshi, we need your help."
    r "We're breaking Ailea out of the breeding facility."
    t @ nervous "The breeding facility... you're not asking me to go back, are you?"
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
                j "Yeah, because you were one of the ones doing it!"
                t @ angry "I never..."
                show takeshi sad
                t "*sigh*"
                t "Listen..."
                jump t_bull_flashback
        label t_bull_flashback:
            show takeshi sad
            t "When they find out you're a bull, they come for you."
            t "They take you from your family."
            t "They pump you full of drugs and hormones to keep you pissed off and horny."
            t "There are never enough cows to go around, especially if too many of them get pregnant or injured..."
            t "So the bulls start fighting."
            t "And the fighting turns into fucking... and the younger bulls don't really have a say in the matter."
            show jack main with dissolve
            t "I was 16 when I got out. By then, I had lost count of how many times I'd been raped."
            t "I don't know if it's worse for the cows... it probably is..."
            t "But believe me. I know what bulls can do."
            menu:
                "That's... that's terrible. I never thought about what bulls go through...":
                    show jack main with dissolve
                    $ t_points += 1
                    t "I get it... If you're a cow, all you ever see is the ones who make it through."
                    t "To be a bull, to be the kind of prize bull they want, you have to be strong and cruel..."
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
                        j "Yeah, but it sure as shit won't be the bulls doing the burning."
            t "Maybe you're right, Jack..."
            jump t_bull_postd
            label t_bull_postd:
                show takeshi main
                t "Anyway, it was Ailea who got me out. She risked her life and safety for me. So if you're rescuing her from that place..."
                t "I'll do what I can to help..."
                t "But I can't go back inside."
                if t_section2_flag == 1:
                    jump t_plan_menu
                else:
                    jump t_section2

#Without Rakesh
default t_no_r_response1 = False
default t_no_r_response2 = False
default t_no_r_response3 = False
default t_no_r_menu_rakeshflag = False
default t_no_r_refusal = 0
default t_recursion = False
default t_paranoidresponse1 = False
default t_no_r_menu2_insert1_1 = False
default t_no_r_menu2_insert1_2 = False
default t_no_r_menu2_insert2_1 = False
default t_no_r_menu2_insert2_2 = False
default t_no_r_menu2_insert2_3 = False
if r_companion == False:
    label t_no_r_menu:
    menu:
        "Rakesh told me you might be able to help." if t_no_r_response1 == False and t_no_r_menu_rakeshflag == False and t_no_r_response3 == False:
            $ t_no_r_response1 = True
            $ t_points += 1
            t "Rakesh, eh? The scooter guy?"
            menu:
                "Uh… do you mean hoverboard?":
                    $ t_points += 1
                    t "Hmmm. Fine. What did he say?"
                    j "He said you’d be able to help me."
                    t "Yeah? I mean, I would help him..."
                    j "Well, what about me? We're buddies."
                    jump t_no_r_menu2
                "Yeah, that’s the one.":
                    $ t_points -= 1
                    t "Uh-huh, OK. What did he tell you about me?"
                    j "He said you’d be able to help me."
                    t "Hmmm..."
                    jump t_no_r_menu2
        "I... I'm not sure I should say. You could be one of {i}them{/i}!" if t_no_r_response2 == False:
            $ t_no_r_response2 = True
            t "Says the stranger walking into my place with vague requests and dodgy answers."
            menu:
                "Says the shop owner with trust issues!":
                    $ t_points -= 1
                    $ t_recursion = True
                    t "I’m not about to get stuck in your rhetorical spirals, buddy. What do you want?"
                    j "I want your help! I wasn’t lying!"
                    t "You have a funny way of going about it. Now who sent you?"
                    jump t_no_r_menu
                "OK, OK... You promise you're chill?":
                    $ t_no_r_menu_rakeshflag = True
                    t "..."
                    extend "Yeah."
                    j "Here goes, deep breath..."
                    t "Uh-huh..."
                    jump t_no_r_menu
        "That's none of your damn business. Can you help me or not?" if t_no_r_response3 == False:
            $ t_no_r_response3 = True
            $ t_points -= 1
            t @ angry "Whoa, that’s a lot of bad vibes. Probably not, my dude, unless you get real chill all of a sudden."
            jump t_no_r_menu
        "OK, Fine. I'll tell you. Rakesh sent me." if t_no_r_menu_rakeshflag == True or t_no_r_response3 == True:
            show takeshi main
            t "Why didn’t you just say that?"
            menu:
                "I thought, y’know, for safety and stuff?":
                    $ t_points += 1
                    t "OK, I guess I can’t fault you for that..."
                    jump t_no_r_menu2
                "It’s my philosophy in life. Trust no one. Not even yourself.":
                    $ t_points -= 1
                    t "That's your... like your worldview?"
                    j "Always has been."
                    t "How’s it working out for you?"
                    j "..."
                    jump t_no_r_menu2
        "I can't tell you." if t_no_r_menu_rakeshflag == True or t_no_r_response3 == True:
            $ t_no_r_refusal += 1
            if t_no_r_refusal > 1:
                jump t_worstending
            else:
                t "You're going to have to, or we're done."
                jump t_no_r_menu


    label t_no_r_menu2:
        if t_points > 0:
            "(Takeshi seems to like you.)"
        if t_points == 0:
            "(Takeshi regards you with an inscrutably neutral expression.)"
        if t_points < 0:
            "(You have angered Takeshi.)"
        t "OK. Talk to me. What did Rakesh say, exactly?"
        j "Well, we have a plan, and it involves you causing a distraction."
        t "And whom, pray tell, would need to be distracted to get you an abortion?"
        label t_no_r_menu2insert:
        menu:
            "OK, don't freak out when I tell you...":
                $ t_points += 1
                t "I'm not going to freak out."
                j "OK, good."
                j "Because we're breaking into the breeding center to rescue Ailea."
                t "..."
                show takeshi nervous
                extend "Fair enough, I'm freaking out a little."
                j "Don't worry, Rakesh and I figured the whole thing out..."
                jump t_no_r_menu2_cont
            "We're rescuing Ailea from the breeding center.":
                t "The... the breeding center?"
                j "That's where Rakesh thinks they're holding her."
                t "And you think you can just... go in and get her?"
                j "There's a plan..."
                jump t_no_r_menu2_cont
            "Ever heard of compartmentalization?! Nobody can know the whole plan." if t_paranoidresponse1 == False:
                $ t_points -= 1
                $ t_paranoidresponse1 = True
                if t_recursion == True:
                    t "Nah. Not going through this again. Stop spiraling and tell me."
                else:
                    t "Nah. Not gonna do this paranoid shit. Just tell me."
                jump t_no_r_menu2insert
        label t_no_r_menu2_cont:
            show takeshi angry
            t "Well, whatever it is, leave me the fuck out!"
            t "No chance in hell am I going back to the breeding center!"
            j "Whoa... wait..."
            t "Sorry about whatever you and Rakesh have going on, but..."
            extend "I'M NOT FUCKING GOING BACK THERE!"
            extend "EVER!"
            j "..."
            t "..."
            show takeshi sad with dissolve
            t "Sorry. I just... it took everything I had to get out of there..."
            t "I'm sorry if this ruins y'all's plan."
            j "No, don't worry about that... I get it."
            j "I escaped too, sort of..."
            j "Mostly."
            t "I know what you mean. There's some things you can't escape. Even if we aren't behind those bars..."
            j "As long as the breeding center exists..."
            t "Yeah. None of us are free."
            t "I probably had it easier than you... they used me as a bull..."
            j @ upset "YOU WERE A BULL?!??!"
            t "..."
            show takeshi nervous
            extend "No."
            extend " Just like you were never a cow."
            t "We aren't what they make of us, or the function of our bodies."
            label t_no_r_menu2_insert2:
            show takeshi main
            menu:
                "But it's different for 'assigned' bulls." if t_no_r_menu2_insert2_1 == False:
                    $ t_points -= 1
                    $ t_no_r_menu2_insert2_1 = True
                    t "Why? Like the bodies of bulls aren't just as instrumentalized as the cows?"
                    j "Are they?"
                    t "Yes. It takes less of a toll on their bodies, but the ideology is the same."
                    j "And you don't think the toll on their bodies matters?!"
                    t "Of course it does, Jack. I literally said, 'I probably had it easier'."
                    j "Hmm. But even if we can make ourselves whatever we want..."
                    j "Don't you think it matters that what {i}they {/i} make of us is based on our bodies?"
                    t "It does matter. It affects everything; specifically, what kind of abuse they think is appropriate to subject us to."
                    t "So if all they do is instrumentalize and abuse, why should we listen to a single fucking word they say?"
                    j "Hmmmm."
                    t "So what if they try to define us by a function our bodies can perform?"
                    t "Their definitions are imposed by force, and therefore meaningless."
                    jump t_no_r_menu2_insert2
                "It's hard to remember that when you're fucking pregnant." if t_no_r_menu2_insert2_2 == False:
                    $ t_no_r_menu2_insert2_2 = True
                    t "Hmph. I guess that would make it harder."
                    j "Every day, I have to remember that what they want to use my body for and what I want my body to be are different..."
                    j "And what they wanted won out, because they control everything. It's easy to say that we're more than our function."
                    j "But what if they force that function onto us?!"
                    t "Yeah..."
                    j "Or... I guess that's exactly what they do to the bulls, isn't it..."
                    t "Yeah."
                    j @ depressed "Ugh..."
                    jump t_no_r_menu2_insert2
                "You're right... those labels are pointless. We should be free of all of it." if t_no_r_menu2_insert2_1 == True or t_no_r_menu2_insert2_2 == True:
                    $ t_points += 1
                    t "Hell yeah, bro!"
                    j "So help us free Ailea. She has knowledge that can help liberate people from the labels they impose on us."
                    t "..."
                    show takeshi happy with dissolve
                    extend "OK. Tell me your plan."
                    jump t_section2
                "You're wrong... those labels reflect a material truth that affects us in material ways." if t_no_r_menu2_insert2_1 == True or t_no_r_menu2_insert2_2 == True:
                    $ t_points -= 1
                    t "No. Listen. Those labels are assigned to material factors, but that does not make them a reflection of truth."
                    j "Does that make them any less real? They still affect us! It doesn't matter if they're valid labels or not."
                    t "It does matter, because if we demonstrate that they aren't valid, if we can show they aren't true..."
                    t "People will stop believing in fake categories that don't make any sense."
                    menu:
                        "People don't care about that. They just care about what they've always known.":
                            $ t_points -= 1
                            t "So cynical."
                            j "What else am I supposed to be?"
                            t "Fair enough..."
                            t "As long as you're not so cynical that you don't want to save Ailea..."
                            menu:
                                "I'm saving her for my own reasons. I need her to help me.":
                                    $ t_points -= 1
                                    t "Great. Well. As long as she gets saved. What's the plan?"
                                    jump t_section2
                                "Never that cynical, no. The world sucks, but I don't have to.":
                                    $ t_points += 1
                                    t "OK. Differences aside for now. What's the plan?"
                                    jump t_section2
                            jump t_section2
                        "You're too optimistic. Things will never change.":
                            $ t_points -= 1
                            t "You're too pessimistic. Change demands that we divest ourselves of despair."
                            j "Huh?"
                            t "Never mind. What matters is we're saving Ailea. Let's go over the plan."
                            jump t_section2
                        "I hope you're right...":
                            $ t_points += 1
                            t "Me too. Now let's go over this plan of yours, and I'll see what I can do to help."
                            jump t_section2



#Section 2
default t_section2_flag = 0
default t_plan_menu_insert1_fight = False
default t_rejection1 = False
label t_section2:
show takeshi main
show jack main
$ t_section2_flag = 1
$ plan_getin = 0
$ plan_inside = 0
$ plan_getout = 0
if t_points > 0:
    "(You've charmed Takeshi, for now.)"
if t_points == 0:
    "(Takeshi regards you with an inscrutably neutral expression.)"
if t_points < 0:
    "(Takeshi seems real miffed.)"
label t_plan_menu:
    if plan_getout == 1 and plan_inside == 1 and plan_getin == 1:
        jump endings
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
                        $ t_points += 1
                        t @ happy "And also, with a veil, you can keep what's sure to be an expression of purest revulsion hidden!"
                        j @ happy "Hey! Multiple uses."
                        jump t_plan_menu
        "Let's talk about what's inside." if plan_inside == 0:
            $ plan_inside = 1
            t "So you make it past the Matron at the gate. Then what?"
            label t_plan_menu_insert1:
            menu:
                "We'll fight our way through!" if t_plan_menu_insert1_fight == False:
                    $ t_plan_menu_insert1_fight = True
                    t "That seems like a really bad idea..."
                    t "As soon as you start taking people out, they'll send the bulls after you, roided up and angry."
                    j "Hmmm..."
                    menu:
                        "I can handle it.":
                            $ breakin_combat = True
                            $ t_points += 1
                            t "OK, buddy. Great self-confidence."
                            jump t_plan_menu
                        "OK, let me rethink this...":
                            jump t_plan_menu_insert1
                "We play it cool until we find Ailea.":
                    $ t_points += 1
                    t "Yeah, that sounds about right. Ailea will probably be somewhere on the upper floors, with the cows."
                    j "Ugh... I never thought I'd be walking in there on purpose."
                    t "Don't worry, my friend. This time, you'll be armed and dangerous."
                    jump t_plan_menu
        "Let's talk about how to escape." if plan_getout == 0:
            $ plan_getout = 1
            if t_points > 0:
                t "That might be tricky... once you're in and trying to get out with precious cargo, everyone will be on high alert..."
                j "That's where Rakesh said you'd be able to help."
                t "Yeah?"
                menu:
                    "Like you said, you're a fun times music guy, right?":
                        $ t_points += 1
                        t "Yeah! Looks like it's time for the next unnanounced underground Takeshi Musical Happening."
                        t @ excited "With FIREWORKS."
                        t "..."
                        t @ nervous "By which I mean homebrew explosives."
                        j @ happy "Nice."
                        jump t_plan_menu
                    "Go up to the gate and do a little dance, maybe?":
                        $ t_points -= 1
                        t "Ummm... yeah. Sure. My dignity is worth Ailea's freedom. I guess."
                        j "You're a hero, Takeshi."
                        jump t_plan_menu
            if t_points <= 0:
                $ t_rejection1 = True
                t "That might be tricky... All I can recommend is to get ready to fight."
                j "Rakesh mentioned you'd be able to help cover our escape..."
                if r_companion == True:
                    r "I thought you'd be good for it, Takeshi... But no pressure, no demands here."
                    t "I'm sorry, my friends. This just... isn't something I want to get involved in."
                    menu:
                        "Goddammit, Takeshi!":
                            $ t_points -= 1
                            t "Sorry. I just don't think I'm equipped to help you."
                            jump t_plan_menu
                        "It's OK. I wouldn't want to get involved either.":
                            $ t_points += 1
                            t "Yeah..."
                            jump t_plan_menu
                        "Aren't you already involved?":
                            if r_companion == True:
                                r "The kid's got a point there... Like you said, it was Ailea who got you out."
                            t "..."
                            jump t_plan_menu_insert2
                else:
                    jump t_plan_menu_insert2

                    label t_plan_menu_insert2:
                    t "Sorry. I just don't think I'm the best person to help you."
                    menu:
                        "I didn't think I was the right person to help Ailea either. But here I am.":
                            $ t_points += 2
                            t "I... I see your point."
                            jump t_plan_menu
                        "Ugh, typical. Always on my own.":
                            $ t_points -= 2
                            t "Not always, Jack. Maybe this time, though."
                            jump t_plan_menu
label endings:
if t_points > 0:
    if t_rejection1 == True:
        j "OK. I guess I'm heading out then..."
        t "Wait... I've... I've changed my mind."
        j "You'll help?"
        t "If y'all need me to cover your escape... if it's for Ailea..."
        t "I'd never forgive myself if I didn't do everything I could to help."
        j "You mean it?"
        t "Yeah. You boys can count on me!"
        if r_companion == True:
            r "OK. Two hours, and then..."
        else:
            j "OK. I think if you give me... two hours, that'll be enough."
        t "Two hours until it's time for the next unnanounced underground Takeshi Musical Happening."
        t @ excited "With FIREWORKS."
        t "..."
        t @ nervous "By which I mean homebrew explosives."
        j @ happy "Nice."
        "(Takeshi will aid you in your quest!)"
    else:
        t "OK. We have a plan... all that's left is the execution. You ready?"
        j "Ready!"
        if r_companion == True:
            r "Ready as I'll ever be."
        "(Takeshi will aid you in your quest!)"
        return
if t_points <= 0 and t_rejection1 == False:
    t "OK. Sounds like we have a plan..."
    j "Great! Thanks for the help-..."
    t "I'm not helping for you. I owe Ailea a lot. Rakesh too. I'm not about to let you get them both killed."
    menu:
        "Understood.":
            t "Glad we understand each other."
            "(Takeshi will aid you in your quest!)"
        "Oh, blow it out your asshole, Takeshi.":
           t "See? This is exactly what I mean!"
           "(Takeshi will aid you in your quest!)"

if t_points <= 0 and t_rejection1 == True:
    t "But still... we've talked for a little bit now..."
    t "And frankly, I don't trust you or your motivations. Rakesh might be willing to work with you..."
    t "But like I said, I'm just a fun times music guy. I have a good life."
    t "I'm not going to risk it for you."
    "(Takeshi didn't trust you enough to lend hir aid.)"


return

label t_worstending:
t "OK, pal. Sorry we couldn't do business. See ya!"
scene neighborhood with fade
show jack depressed with moveinbottom
show jack depressed at center
"You convinced Takeshi to not help you. You won't have hir support when rescuing Ailea."
#jumps to level 3 without takeshi
return
