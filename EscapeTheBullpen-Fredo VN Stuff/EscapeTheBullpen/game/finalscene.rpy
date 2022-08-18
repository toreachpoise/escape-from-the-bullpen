#Closing Cutscene

#lead-in from level 4
label end_cutscene:
play music "audio/taurus.wav"
scene finalscene_shot1 with fade
pause 1.0
play sound "audio/door_kick.mp3"
scene finalscene_shot2 with vpunch
pause 1.5
play sound "audio/door_kick.mp3"
scene finalscene_shot3 with hpunch
pause 2.0
play sound "audio/door_kick_hard.mp3"
scene finalscene_shot4 with hpunch and vpunch
pause .5
scene finalscene_shot5 with dissolve
ta "HRAAAH!"
scene finalscene_shot6
a "Gah! Muscle-man!"
h "*gasp*"
m "Oh no!"
scene finalscene_shot 7
r "Is that..."
j "IT'S TAURUS!"
