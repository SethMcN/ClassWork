def UserName():
    name = input(f"\nTo start the game please enter a username: ")
    return name

def EndingIgnore():
    print("\nYou decide not to tempt fate. “We don’t need to play hero today,” you say to Jules, turning away from the signal. He exhales in relief. “Good call, Commander. That place has bad news written all over it.” You adjust the ship’s course, leaving Station IX behind. As the distant light of the station fades from view, you can’t shake the feeling that you’ve just turned your back on something...or someone. Your mission continues without incident, but in the quiet moments, you wonder—what if? The End!")

def Start(name):
    print(f"You are Commander {name}, captain of The Starfinder, a seasoned explorer of the galaxsy’s farthest reaches. While charting an unmarked sector in deep space, your ship picks up something strange—a faint distress signal coming from Station IX, an abandoned outpost long thought to be lost. Station IX was decommissioned over a decade ago, its crew vanished, and rumors of strange occurrences have kept anyone from returning. But now, its distress beacon flickers to life.")
    print("\n1. Ignore it and continue on your way.")
    print("2. Respond to the signal.")
    decision = int(input(": "))

    if decision == 1:
        EndingIgnore()

    if decision == 2:
        print("our curiosity wins out. “Set course for Station IX,” you say to your co-pilot, Jules. His brow furrows, clearly uneasy. “You sure about this, Commander? There’s a reason that place was left off the maps.” “We’re explorers,” you remind him. “We don’t run from the unknown.” As the ship speeds toward the abandoned station, its massive silhouette looms in the viewport. Dark, derelict, and eerily silent, Station IX floats like a graveyard in space. “We’ve docked,” Jules reports, but the tension in his voice is palpable. You suit up and prepare to board the station. The airlock hisses open, and you step into the cold, dimly lit corridor. The station seems...too quiet. Suddenly, a faint noise reaches your ears—whispers, echoing down the hallway.")
        print("\n1.Investigate the source of the whispers.")
        print("2.Ignore the signal and continue your mission.")
        decision = int(input(": "))
        Stage1(decision)

def Stage1(decision):
    if decision == 1:
        print("You signal Jules to follow you as you cautiously move toward the whispers. The sound grows louder, though you can’t make out the words. The corridor bends sharply, and as you turn the corner, the lights flicker ominously. You pause. Up ahead, you see a figure in the shadows—a crew member, or what’s left of one. Its suit is tattered, and its face is hidden beneath a shattered visor. You approach carefully, but as you get closer, you realize something is horribly wrong. The figure is moving, but its movements are jerky, unnatural. Before you can react, the creature snaps its head in your direction. Its hollow eyes stare through you, and its mouth opens wide in a silent scream.")
        print("1. Fight the creature")
        print("2. flee back to your ship")
        decision = int(input(": "))
        FightMonster(decision)

    elif decision == 2:
        print("Ignoring the whispers, you lead Jules toward the control center. You need answers, and the main terminal should have logs of what happened here. The control center is a wreck. Broken consoles, shattered glass, and...bodies. Skeletal remains of the crew lie slumped in their chairs, their bones twisted in unnatural ways. Jules steps back, a look of horror on his face. “What the hell happened here?” he whispers. You approach the main terminal and power it up. The screen flickers to life, revealing a series of logs. You scroll through them, and one stands out—EXPERIMENT X-009. Just as you begin to read, the lights in the room dim, and a cold wind seems to sweep through the station. The terminal screen glitches and a strange, distorted voice fills the air. “You shouldn’t have come.”")

def FightMonster(decision):
    if decision == 1:
        print("Heart pounding, you draw your plasma pistol and fire at the creature. The shot hits it square in the chest, but it doesn’t fall. Instead, it convulses violently, emitting a high-pitched shriek that reverberates down the hallway. The lights overhead flicker faster, as if the station itself is reacting to the creature’s pain. Jules grabs your arm. “We need to get out of here!” But before you can retreat, more figures emerge from the shadows. Dozens of them, all wearing tattered space suits, their forms twisted and broken. They close in on you, and you realize with chilling clarity—these were once the crew of Station IX.")
        print("\n1. Try to escape through a maintenance hatch")
        print("2. Stand your ground and keep fighting")
        decision = int(input(": "))

    elif decision == 2: 
        print("")

name = UserName()
Start(name)