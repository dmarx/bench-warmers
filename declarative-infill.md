# declarative infill

motivating idea: https://www.youtube.com/watch?v=GAPwMrDGAfE

given the video input, how could we prompt that effect? "animate a blood splatter effect whenever a combatant delivers a successful sword strike" -> `WHEN <condition> ATTEND TO <subject> TRANSFORM TO <prompt>`

scene understanding is a slightly tangential task here. the more fundamental subtask here is prompting for targeted, isolated, synthesized inpainting. so really just `ATTEND TO <subject> TRANSFORM TO <prompt>`

DETR learned positional queries feels useful here, as usual...
