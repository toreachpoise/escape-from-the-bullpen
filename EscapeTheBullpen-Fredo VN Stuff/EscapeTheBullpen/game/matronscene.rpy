#New Dramatis Personae
define ma = Character("Matron", image="matron", who_color="#b585be")

label BC_gates:
    scene bcgates with fade
    if r_companion == True:
        jump BC_gates_withr
    if r_companion == False:
        show jack cow at right with moveinright
        j "Oh god... here we go..."
        j "Uh... hello? "
        show matron main at left with moveinleft
        ma "Hellooooo!"
        j "It's, y'know, me. I've come back!"
        ma "Ah... J********. Welcome home!"
        j "That's not my name."
        ma "Hmph!"
        ma "Then explain all these records that correspond to your facial scans (within a margin of error)..."
        extend " DNA particulate screening..."
        extend " retinal imaging..."
        ma "Our scanners even got a match with gait analysis, thanks to those woefully unfashionable pneumatic pants of yours."
        j "They're {i}hydraulic{/i} pants."
        ma "All righty, then."
        j "Are you going to let me in or not?"
        ma "Of course, J********. These gates stand ever open to the fertile and virile."
        hide matron main with moveoutleft
        j "Yeah... unless you're inside..."
        show matron suspicious at left with moveinleft
        ma "What was that?"
        j "Nothing."
        jump hospitalharem

label BC_gates_withr:
    show jack main at right with moveinright
    show rakesh main at center_right with moveinright:
            xzoom -1
    j "Rakesh? You're up, buddy."
    r "OK, just give me one moment."
    show rakesh main at left with moveoutleft
    show rakesh lockpicking with dissolve:
        xzoom -1
    "(A moment passes)"
    pause 1.0
    show rakesh main at left with dissolve:
        xzoom 1
    r "There we go. Let's move fast, get to Ailea."
    j "Damn, Rakesh. You weren't kidding."
    r @ happy "Like I said. No problem at all."
    j "What would I do without you?"
    r "Suffer."
    show jack happy
    show rakesh main at left:
        xzoom -1
    hide rakesh with moveoutleft
    pause 1.0
    jump hospitalharem
