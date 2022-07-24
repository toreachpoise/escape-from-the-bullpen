#dramatis personae vol. 4
define a = Character("Ailea", image="ailea", who_color="#e5c620")
define m = Character("Mona", image="mona", who_color="#aad7f2")
define h = Character("Heloise", image="Heloise", who_color="#a90000")

label hospitalharem:
    scene harem bg with fade
    show jack main at right with moveinright
    show ailea main at left with moveinleft
    #if r_companion == True:
    #    show rakesh main at centerright with moveinright
