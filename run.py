import sys
import time

a = 1

def type(text):
  words = text
  for char in words:
    time.sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()


#Play function
def play_game():
    print()
    print()
    print("""You follow the White Rabbit down a winding path that leads to a small door
    hidden in the roots of a large tree. Curiosity prompts you to open it, and you find
    yourself in a dimly lit tunnel. The walls of the tunnel are lined with shelves
    filled with strange objects:
    clocks that tick backwards, bottles with the words "Drink Me" 
     _
    {_}
    |(|
    |=|
   /   \\
   |.--|
   ||  |
   ||  |    
   |'--|  
   '-=-' written on them,
    and mirrors that seem to reflect worlds other than your own. 
    
    What you would like to do?

    1:Try a drink? 
    2:Explore the tunnel?""")

    choice = input("> ") #choice function
    if choice == "1":
        drink_me()
    elif choice == "2":
        explore_tunnel()
    else:
        print("Invalid choice. Please choose again.")
        play_game()

#Play >>> Drink Me
def drink_me():
    print("""You found the tiny bottle with the sign "Drink Me".You uncork the bottle and inhale the
    strange liquid. Feeling bold, you take a sip.
    Immediately, a warm sensation spreads through your body, and you begin to shrink! The tunnel
    and everything in it grow larger around you. Shelves full of unusual objects loom like towering
    buildings, and the once-narrow path stretches out like a vast road.
    You become so small that even the curious trinkets around you now resemble giant, otherworldly sculptures.
    The tunnel feels much more intimidating at this size, and the ticking sound grows louder, almost echoing.
    
    In your new, tiny size, you can now see hidden details in the tunnel's floors and walls - cracks and crevices
    you couldn't see before. In one of these cracks, you notice a small, shimmering key lying just out of reach.
    
      ooo,    .---.
     o`  o   /    |\________________
     o`   'oooo()  | ________   _   _)
    `oo   o` \    |/        | | | |
      `ooo'   `---'         "-" |_|

    What you would like to do?

    1: Take the Key 
    2: Leave the Key""")

    choice = input("> ") #choice function
    if choice == "1":
        take_key()
    elif choice == "2":
        leave_key()
    else:
        print("Invalid choice. Please choose again.")
        drink_me()

#Play >>> Drink Me >>> Take Key
def take_key():
    print("""You decide to pick up the tiny key. Its golden glow beckons you,
    and though you’re not sure what it unlocks, you sense that it’s important.
    Holding it tightly in your tiny hand, you continue down the tunnel that stretches endlessly before you.

              ____
             |  , =,( _________
             | ='  (VvvVvV--'
             |____(

    After what feels like an eternity of walking, you come to a small door built into the wall.
    At your current size, the door looks just the right height for you. You try the key, and it
    fits perfectly! The door creaks open, revealing another room, dimly lit but filled with familiar features:
    mismatched furniture, crooked picture frames, and—most importantly—a small table with another bottle on it.

    This bottle, like the first, has a label, but this one says “Drink Me Again.”

    Hesitantly, but eager to return to your normal size, you take a sip of the liquid. The moment she touches your lips,
    the familiar warm feeling returns and you begin to grow! The world around you shrinks to normal as her body stretches
    upward, and soon you are back to your normal size.

    Looking around, you notice a much larger door in front of you - a real exit, tall and inviting. You walk through it,
    leaving the strange tunnel behind.

    You find yourself in a vast, wondrous garden, filled with impossibly large mushrooms, flowers that seem to
    speak in whispers, and paths leading in every direction. The air is sweet with the scent of strange flowers,
    and distant, colorful creatures flutter across the sky.

    You realize that you have escaped the tunnel, but the strange world you have entered is far from home.
    It seems both enchanting and dangerous, full of secrets waiting to be explored.
    
    What will you do next?
    
    1: Explore the garden further?
    2: Look for the White Rabbit?
    3: Rest for a moment and observe?""")

    choice = input("> ") #choice function
    if choice == "1":
        explore_garden()
    elif choice == "2":
        look_for_rabbit()
    elif choice == "3":
        rest_in_garden()
    else:
        print("Invalid choice. Please choose again.")
        take_key()

#Play >>> Drink Me >> Take Key >>> Look For Rabbit >>> End of the Game
def look_for_rabbit():
    print("""You wander through the magic garden, enchanted by the vibrant colors and strange,
    talking flowers. The garden seems alive with energy, every step revealing new wonders.
    As you move through the towering mushrooms and glowing blossoms, she catches a glimpse
    of white fur darting between the tall plants.

    Excited, you hurry forward and soon find yourself face-to-face with the White Rabbit.
    He’s standing by a large mushroom, anxiously checking his pocket watch, as always. 
    The moment he sees you, his eyes widen, though not with surprise this time. Instead,
    there’s a look of relief.

    "Oh, there you are! I've been looking for you everywhere," the Rabbit says in his
    hurried voice. "This garden can be quite a tricky place, but lucky for you, I know the way out."

    You smile, feeling a wave of relief herself. "Thank you! I’ve been trying to find a way
    home for what feels like forever."

    The Rabbit, always in a rush, nods quickly. “Yes, yes, no time to waste. Follow me!”

    He hops ahead, and You follow closely as they weave through the garden. The landscape
    around you shifts strangely, as if the plants are moving out of their way, and the path
    constantly changes beneath your feet. But the Rabbit seems to know exactly where to go,
    never hesitating as he turns sharp corners and ducks under arching flowers.

    After what feels like just a few minutes of walking, you reach the edge of the garden,
    where a large gate stands. Beyond it, you can see the familiar sight of your world:
    a calm meadow leading back to your home.

    The Rabbit stops at the gate and gestures toward it. “There’s your way home,” he says. 
    “Once you pass through, you’ll be back in your world. But remember, Wonderland has a way
    of calling you back, so don’t be surprised if you return someday.”

    You look at the gate, your heart filled with both gratitude and a strange sadness.
    Wonderland has been strange, confusing, and often challenging, but it’s also been 
    magical. Still, she knows it’s time to go.

    “Thank you, Rabbit,” you say warmly. “For everything.”

    The White Rabbit gives her a quick nod, checking his watch once more. “Oh dear,
    I’m late again. Best of luck, Alice! Until we meet again!”

    With a final wave, you step through the gate. As she does, the garden fades behind you,
    replaced by the familiar warmth of her world. The sky is bright, the grass soft beneath 
    your feet, and in the distance, you can hear the comforting sounds of home.

    You smile, knowing you are safe and sound, but with the memory of Wonderland forever in your heart.""")


#Play >>> Drink Me >> Take Key >>> Rest in the garden
#Play >>> Explore Tunnel >>> Drink Me >>> Explore Garden >>> Rest in the garden
#Play >>> Explore Tunnel >>> Call For Help >>> Explore Garden >>> Rest in the garden
def rest_in_garden():
    print("""You decide to sit and rest for a while on the soft grass of the clearing.
    The garden seems alive, and you sense that by rushing forward you may miss something
    important. As you settle in, the whispers fade into the background, leaving only the
    gentle rustling of leaves and the soft hum of the air around you.

    The longer you sit, the more the garden seems to open up. The flowers nearby shift their
    positions slightly, as if turning towards you, and their glow intensifies, casting an ethereal
    light over the area. The spiral tree in the center with three doors seems almost to breathe,
    its bark shimmering in soft waves.

    As you watch, small details become clear:

    * * The red door (with the clock symbol) seems to pulse faintly, almost as if in sync with 
    the ticking sound she heard earlier in the tunnel. * *

    * * The blue door (with the heart symbol) radiates a faint warmth, and she hears the distant
    echo of laughter, though she cannot tell whether it is joyful or sinister. * *
    
    * *Faint shimmers float around the green door (with the crown symbol), like a magical trail,
    and for a moment you notice something glittering in the air near it, like the edge of a golden crown. * *

    As you look at the doors, the whispers begin to return, but this time they feel different.
    It is as if the garden is trying to communicate with you - not in words, but in feelings.
    The red door evokes a sense of urgency, as if time is of the essence. The blue door evokes
    a sense of curiosity mixed with caution as if it holds deep and complex emotions. 
    The green door hints at power, authority, and something grandiose, but also unknown.

    The garden seems to be giving you a choice, but not in a hurry - it is waiting for you to decide.
    
    What will You do next?
    
    1: Open the red door?         .-.-.     Symbol
                             ((  (__I__)  ))
                               .'_....._'.
                              / / .12 . \ \\
                             | | '  |  ' | |
                             | | 9  /  3 | |
                              \ \ '.6.' / /
                               '.`-...-'.'
                                /'-- --'\          
   
     2: Open the blue door  ,-"-,-"-.        Symbol
                           (         )
                            ".     ."
                              "._." 
    
    3: Open the green door     <>           Symbol   
                             .::::.             
                         @\\/W\/\/W\//@         
                          \\/^\/\/^\//     
                           \_O_<>_O_/""")

    choice = input("> ") #choice function
    if choice == "1":
        red_door()
    elif choice == "2":
        blue_door()
    elif choice == "3":
        green_door()
    else:
        print("Invalid choice. Please choose again.")
        rest_in_garden()
    
    

#Play >>> Drink Me >>> Take Key >>> Explore Garden
#Play >>> Explore Tunnel >>> Drink Me >>> Explore Garden
#Play >>> Explore Tunnel >>> Call For Help >>> Explore Garden
def explore_garden():
    print("""You reached into the garden, your curiosity drawing you deeper into this strange,
    beautiful world. The vibrant colors and strange shapes of the plants around you make everything
    seem surreal. Flowers with faces whisper to each other, and huge mushrooms tower over you like trees.

    As you walk down the winding path, you notice something strange - the deeper you go, the more the
    garden seems to shift and change. The sky above shimmers between bright daylight and dark twilight,
    as if time is out of whack. The air hums with a strange energy, and the plants seem to move slightly
    when you're not looking.

    A rustling sound suddenly catches your attention. Peering ahead, you notice something flickering
    between the huge leaves. It's fast, too fast for you to see clearly, but you catch a flash of white.
    Could it be the White Rabbit? Or something else entirely?

    As you move cautiously forward, you come upon a strange sight: a large table set for tea in the center
    of the garden, completely out of place among the wild greenery. The table is covered with mismatched
    cups and saucers, some overturned, others stacked precariously high. There are empty chairs around it,
    though one at the far end has its back to her.

                  _
                  _(_)_                          wWWWw   _
      @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
     @@()@@ wWWWw  (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)
      @@@@  (___)     `|/    Y    (_)@(_)  @@@@   \|/   (_)\\
       /      Y       \|    \|/    /(_)    \|      |/      |
    \ |     \ |/       | / \ | /  \|/       |/    \|      \|/
    \\|//   \\|///  \\\|//\\\|/// \|///  \\\|//  \\|//  \\\|// 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Just as you are about to investigate, a voice calls out from behind you. "You're late, you know!"

    You turn to see a familiar face - the Cheshire Cat. He is lounging lazily on the branch of a nearby tree,
    his wide grin glittering in the changing light.

    "Well, well, what a curious traveler we have here," the Cat purrs, his eyes twinkling mischievously.
    
    What You will do next?
    
    1: Talk to the Cheshire Cat
    2: Look for a way out of the garden""")


    choice = input("> ") #choice function
    if choice == "1":
        talk_to_cat()
    elif choice == "2":
        avoid_table()
    else:
        print("Invalid choice. Please choose again.")
        explore_garden()


#Play >>> Drink Me >>> Take Key >>> Explore Garden >>> Talk to Cat
#Play >>> Explore Tunnel >>> Drink Me >>> Explore Garden >>> Talk to Cat
#Play >>> Explore Tunnel >>> Call For Help >>> Explore Garden >>> Talk to Cat
def talk_to_cat():
    print(""""Lost again, are we?" the Cheshire Cat purrs, his grin widening.
    "You do have a habit of getting yourself into the most curious of predicaments, don't you?"

    You, frustrated but trying to stay calm, look up at him. “Yes, I am lost,” you admit.
    “I’ve been wandering this strange place for too long. Can you show me the way home?”

    The Cheshire Cat tilts his head, his grin never fading. “Home? Hmm, now that’s a tricky
    thing to define here in Wonderland, isn’t it? What exactly is home? But... if you insist
    on leaving this delightful place, I might be persuaded to help.”

    You watch him carefully, knowing the Cheshire Cat loves to toy with words and play tricks.
    “I just want to go back to where I came from,” you say firmly. “My world. Can you show me the way?”

    The Cheshire Cat’s eyes twinkle with amusement. “Well, if that’s what you truly want, I can
    certainly point you in the right direction. But you must be careful. Wonderland has a way of
    holding onto its visitors, especially those with a curious mind like yours.”

    With a slow stretch, the Cheshire Cat points his paw down one of the twisting paths behind him.
    “Follow that way, and you’ll come to a crossroads. Take the left path, and you’ll find a gate.
    Once you pass through it, you’ll be back in your world.”

    He begins to fade away again, starting with his tail and ending with that ever-present grin.
    “But remember,” his voice lingers as he disappears completely, “the path you take may not always
    be the one you expect.”

    You watch the Cheshire Cat vanish, a sense of both relief and uncertainty washing over you.
    Though his directions were vague, she had a way to go now.
    
    What You will do next?
    
    1: Follow the path Cat shows You?
    2: You tired and want to take a rest?
    3: Call Rabbit to find way home?""")

    choice = input("> ") #choice function
    if choice == "1":
        follow_cat()
    elif choice == "2":
        rest_in_garden()
    elif choice == "3":
        go_home()
    else:
        print("Invalid choice. Please choose again.")
        talk_to_cat()


#Play >>> Drink Me >>> Take Key >>> Explore Garden >>> Follow cat >>> End the game
#Play >>> Explore Tunnel >>> Drink Me >>> Explore Garden >>> Follow cat >>> End the game
#Play >>> Explore Tunnel >>> Call For Help >>> Explore Garden >>> Follow cay >>> End The game
def follow_cat():
    print("""You decide to trust the Cheshire Cat’s directions, even with the lingering sense
    of mystery. You take a deep breath and head down the winding path he pointed out, your heart
    beating a little faster with every step. The flowers and plants around you seem to sway as
    if watching you, but you keep moving forward, determined to find a way home.

    After walking for a while, you come to a crossroads, just as the Cheshire Cat had said. The left
    path looks slightly darker, shaded by towering trees, but there’s a faint glow in the distance
    as if something important lies at the end. Without hesitation, you turn left, your steps quicker
    now as you feel you getting closer to the goal.

    As you follow the path, the air grows warmer, and you can hear the sound of wind rustling through
    the trees. In the distance, you spot a large gate, golden and ornate, standing tall against the
    backdrop of the ever-shifting Wonderland sky. The gate seems to shimmer, almost calling to you.

    Yours heart leaps — this must be the way home.

    You approach the gate, and as you reach out to touch it, the latch clicks open, almost on its own.
    Beyond the gate, you see a familiar sight: the rolling green hills of your world, the soft, comforting
    colors of the landscape you had been so eager to return to. The air smells fresher, and the sky is the
    perfect shade of blue.

    You step through the gate, leaving the curious world of Wonderland behind. As you cross the threshold,
    you feel a strange, light sensation, as if the weight of Wonderland’s madness is lifting from your shoulders.
    The gate swings shut behind you with a soft click, and when you turn to look back, there’s nothing but the
    peaceful meadow of your home.

    With a sigh of relief, you know you are finally back.

    The familiar sounds of your world surround you: birds singing, the gentle breeze blowing through the grass,
    and the distant voices of your family calling your name. You smile, feeling both exhausted and exhilarated.
    The adventures of Wonderland are behind you now, but you know that the memories will stay with you forever.

    As you begin walking back toward your home, you wonder if you ever return to Wonderland. The Cheshire Cat’s
    words echo in your mind — “Wonderland has a way of holding onto its visitors.” Perhaps one day, when the time
    is right, you’ll find herself back there again.

    But for now, your home.""")


#Play >>> Drink Me >>> Take Key >>> Explore Garden >>> Avoid Table
#Play >>> Explore Tunnel >>> Drink Me >>> Explore Garden >>> Avoid Table
#Play >>> Explore Tunnel >>> Call For Help >>> Explore Garden >>> Avoid Table
def avoid_table():
    print("""You turn away from the tea table and the Cheshire Cat, deciding to follow
    one of the many twisting paths ahead. The garden seems to be full of possibilities,
    and your curiosity pulls you forward. You choose the nearest path, a narrow trail lined
    with glowing, luminescent flowers that seem to sway with you every step.

    The path twists and turns, the garden growing wilder and stranger with every turn. The leaves
    overhead grow so thick that they almost block out the sky, creating a canopy that bathes the
    trail in dappled shadows. As you venture further, you hear faint whispers carried on the breeze.
    The voices seem to be coming from everywhere and nowhere all at once, but you can't quite make 
    out what they're saying.

    Soon, the path opens into a small, circular clearing. In the middle of the clearing stands a tall, 
    spiraling tree with bark that shimmers in different colors as the light touches it. Its branches seem 
    to reach out like arms, and at the base of the tree, there are three distinct doors carved into its trunk, 
    each a different color: one red, one blue, and one green. Above each door, a symbol is etched: a clock,
    a heart, and a crown.

    The whispers grow louder now as if the tree itself is speaking to you. The doors beckon, each promising
    a different path ahead.

    What will You do next?
    
    1: Open the red door?         .-.-.     Symbol
                             ((  (__I__)  ))
                               .'_....._'.
                              / / .12 . \ \\
                             | | '  |  ' | |
                             | | 9  /  3 | |
                              \ \ '.6.' / /
                               '.`-...-'.'
                                /'-- --'\          
   
     2: Open the blue door  ,-"-,-"-.        Symbol
                           (         )
                            ".     ."
                              "._." 
    
    3: Open the green door     <>           Symbol   
                             .::::.             
                         @\\/W\/\/W\//@         
                          \\/^\/\/^\//     
                           \_O_<>_O_/""")

    choice = input("> ") #choice function
    if choice == "1":
        red_door()
    elif choice == "2":
        blue_door()
    elif choice == "3":
        green_door()
    else:
        print("Invalid choice. Please choose again.")
        avoid_table()


# Play >>> Drink Me >>> Leave the Key (End of the Game)
def leave_key():
    print("""You stare at the small, glimmering key in the crack of the tunnel floor,
    but for reasons you can’t quite explain, you decide to leave it behind.
    Perhaps it’s your curiosity leading you onward, or maybe you simply don’t realize the key’s significance.
    You continue down the tunnel, your small size making everything feel much more intimidating and vast.

    As you venture deeper, the tunnel twists and turns, never offering a way out. The ticking grows louder,
    and the air feels heavier like it’s closing in on you. Every corner you turn looks the same as the last,
    and the once curious objects on the shelves now seem menacing, like they’re watching you.

    Time passes, but you can’t tell how long. It feels like hours, days, maybe even longer. The walls feel tighter,
    the shadows longer. You try calling out again, but your voice is lost in the endless echo.

    Without the key, You are stuck in the tunnel, unable to find a way out. The door behind you has disappeared,
    and no other exits reveal themselves. The ticking clock is the only constant, marking time in a world that feels like it's stopped.

    Over time, the tunnel becomes your entire world — a strange, shifting place with no escape.
    The objects that once seemed curious now feel like permanent companions, and the shadows that dance on the walls never leave you alone.
    """)


#Play >>> Explore Tunnel
def explore_tunnel():
    print("""A few steps in, and the door behind you slams shut. The tunnel narrows,
    and you feel the walls pressing in slightly. Your heartbeat quickens as you search
    for another exit, but the tunnel stretches forward, twisting in impossible ways.

    You attempt to retrace your steps, but the door behind you has vanished. You realize you are trapped
    in a room where the air is thick with the unsettling feeling that you are not alone. Shadows move in
    the dim light, and somewhere deep within the tunnel, you hear the faint ticking of a clock that you cannot see.

    What will you do next?
    1: Explore the tunnel further, searching for hidden mechanisms in the objects around you?
    2: Or do you call for help?""")

    choice = input("> ") #choice function
    if choice == "1":
        drink_me()
    elif choice == "2":
        call_for_help()
    else:
        print("Invalid choice. Please choose again.")
        explore_tunnel()


#Play >> Explore Tunnel >> Call For Help
def call_for_help():
    print("""Feeling a mixture of frustration and determination, you decide to call for help again.
    Your voice echoes through the dim tunnel, bouncing off the walls as you shout, “Help! Is anyone there?”

    For a moment, everything is silent. Just when you’re starting to lose hope, you hear the familiar patter
    of little feet approaching you. The White Rabbit appears, his eyes wide with worry.

    “Oh my god! Oh my god! What have you gotten yourself into?” he exclaims, slightly out of breath. “You really
    shouldn’t be wandering around here. Follow me, I’ll show you the way home!”

    Reassured, you quickly follow the Rabbit as he hops nimbly through the twisting paths of the tunnel.
    He looks back at you, a mixture of urgency and excitement on his face.

    “Stay close! "This tunnel can be quite tricky if you don't know your way around," he calls, leading 
    you through narrow passages and around sharp corners. The ticking of the invisible clock seems to grow
    quieter as they move deeper into the tunnel, and the air feels lighter.

    After a few minutes of hurried travel, they reach a door that glows faintly at the end of a long, winding
    corridor. The White Rabbit stops, pushing it open with a flourish.

    "There! You're almost home!" he says, his voice full of encouragement.

    Beyond the door is a vibrant garden, similar to the one you saw earlier, but this one is bursting with color
    and life. Flowers bloom in every hue, and the air is filled with sweet scents. In the distance, you see a familiar
    path leading back to the entrance to your world.

    "Just follow this path, and you'll be back where you belong," the White Rabbit assures you. "But remember,
    Wonderland has a way of calling you back.
    
    What will you do next?
    
    1: Thank the White Rabbit and head home?
    2: Explore the garden a bit more?""")

    choice = input("> ") #choice function
    if choice == "1":
        go_home()
    elif choice == "2":
        explore_garden()
    else:
        print("Invalid choice. Please choose again.")
        call_for_help()

#Play >>> Explore Tunnel >> Call for Help >> Call for Rabbit (End of the Game) 
#Play >>> Drink Me >>> Take Key >>> Explore Garden >>> Call for Rabbit >>> End the game
#Play >>> Explore Tunnel >>> Drink Me >>> Explore Garden >>> Call for Rabbit >>> End the game
#Play >>> Explore Tunnel >>> Call For Help >>> Explore Garden >>> Call for Rabbit >>> End The game
def go_home():
    print("""You turn to the White Rabbit, gratitude shining in your eyes.
    “Thank you so much for your help!” you exclaim. “I wouldn’t have found 
    my way without you!”

    The White Rabbit nods, adjusting his tiny vest. “Oh, nothing! Just doing my job,” he replies,
    looking back at the tunnel with a hint of worry. “But be careful out there. Wonderland can be
    quite unpredictable!”

    With one last wave, you walk through the door and onto the busy path that leads back to her world.
    The sun shines brightly overhead, illuminating the colorful flowers that seem to dance in the
    gentle breeze. You feel the warmth of the sunlight on her face, a calming reminder of home.

    As you walk, you pause for a moment to appreciate the beauty of the garden. Each flower is a riot
    of color, and a sweet scent fills the air. You notice butterflies fluttering about, their delicate
    wings sparkling like jewels in the sun. For a moment, you want to linger, to explore this magical
    place a little longer.

                      __ \/ __
     /\^/`\          /o \{}/ o\   
    | \/   |         \   ()   /     
    | |    |          `> /\ <`   ,,,     
    \ \    /  @@@@    (o/\/\o)  {{{}}                 _ _
     '\\//'  @@()@@  _ )    (    ~Y~       @@@@     _{ ' }_
       ||     @@@@ _(_)_   wWWWw .oOOo.   @@()@@   { `.!.` }
       ||     ,/  (_)@(_)  (___) OO()OO    @@@@  _ ',_/Y\_,'
       ||  ,\ | /)  (_)\     Y   'OOOO',,,(\|/ _(_)_ {_,_}
   |\  ||  |\\|// vVVVv`|/@@@@    _ \/{{}}}\| (_)@(_)  |  ,,,
   | | ||  | |;,,,(___) |@@()@@ _(_)_| ~Y~ wWWWw(_)\ (\| {{{}}
   | | || / / {{}}} Y  \| @@@@ (_)#(_) \|  (___)   |  \| /~Y~
    \ \||/ /\\|~Y~ \|/  | \ \/  /(_) |/ |/   Y    \|/  |//\|/
     `\\//`,.\|/|//.|/\\|/\\|,\|/ //\|/\|.\\\| // \|\\ |/,\|/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    But her heart pulls you forward. You know you need to return to your world, to the familiar comfort
    of your home.

    As you walk along the path, you hear the soft sound of running water nearby. Curiosity piqued, you
    wander a little off the main path to see a small stream running through the garden, its waters
    sparkling like diamonds. It flows peacefully, meandering through the flowers and leading to the distant horizon.

    Suddenly, you realize you can’t stay.
    With one last look around, you return to the main path and continue on your way. Soon you reach the
    edge of the garden, where the flowers give way to a familiar landscape. The soft rolling hills, the 
    bright green grass, and the distant sound of her family calling her name fill you with joy.

    As you step through the door back into her world, you feel a sense of completion. She looks back one
    last time at Wonderland, the magical place that took you on an incredible adventure.

    “I will never forget you,” you whisper to the garden.

    With a deep breath, you step forward into your reality.

    Back in your garden, you hear the sounds of your family enjoying a lovely picnic. The aroma of freshly
    baked treats wafts through the air and laughter echoes around you.

    You smile, knowing that even though your adventure in Wonderland has come to an end, the memories will
    forever remain in your heart. And who knows? Perhaps one day you will return.""")

def blue_door():
    print("""You, drawn by curiosity, approach the blue door with the heart symbol etched above it.
    You hesitate for just a moment, then take a deep breath and open the door. A soft glow spills out,
    and without another thought, You step through.

    As soon as You pass the threshold, the world around changes. You find yourself in a large, beautiful room
    with high ceilings, draped in rich blue and purple silks. The floor is a black-and-white checkerboard, and
    the air is filled with the scent of roses. In the distance, You can hear the soft tinkling of music, as if a
    grand ball is taking place somewhere nearby.

    At the center of the room, a massive, ornate throne stands, with a heart-shaped crest at the top. And sitting on 
    the throne is a figure that You immediately recognize — the Queen of Hearts.

    The Queen’s sharp eyes fixed on You the moment she entered the room. "Ah, there you are," the Queen says with a
    mix of amusement and suspicion. "I wondered when you would find your way here. You’ve come through my door, so 
    you must want something. Speak up, please!"

    You take a cautious step forward. “I… I didn’t mean to intrude. I just followed the path and found this door.”

    The Queen of Hearts raises an eyebrow, clearly unimpressed. "Didn’t mean to intrude? In Wonderland, everything
    has meaning, whether you know it or not. Now, what do you seek, here? Adventure? Answers? Or perhaps you’re here
    to challenge me?"

    Your heart races. You remember the stories of the Queen’s temper, but also know that this might be your chance to
    learn something important — or perhaps even find a way home.
    
    What will You do next?
    
    1: Ask the Queen for help finding her way home?
    2: Challenge the Queen?
    3: Explore the room quietly, to look for an exit?""")

    choice = input("> ") #choice function
    if choice == "1":
        ask_queen()
    elif choice == "2":
        challenge_queen()
    elif choice == "3":
        explore_garden()
    else:
        print("Invalid choice. Please choose again.")
        rest_in_garden()
    
def ask_queen():
    print("""You, feeling both nervous and hopeful, decide to speak to the Queen of Hearts directly.
    You know the Queen is a powerful figure in Wonderland, but you hope that by being polite,
    you might get the help you need to find her way home.

    “Your Majesty,” You begin, bowing slightly, “I didn’t mean to disturb you, but I’ve been lost
    in Wonderland for quite some time now. I only wish to return to my world. Could you, perhaps,
    help me find my way home?”

    The Queen of Hearts narrows her eyes for a moment, studying You. Her expression is unreadable,
    but after a long silence, the Queen’s lips curl into a small smile.

    “Hmm… A bold request,” the Queen muses, tapping her fingers on the arm of her throne.
    “Most who come to Wonderland rarely wish to leave. But I suppose you are not most, are you?”

    The Queen rises from her throne with a flourish of her red and gold robes. She steps down gracefully,
    her eyes still locked on You. “Very well. You’ve amused me, and I do so appreciate those with manners.
    I will help you — but only because it pleases me to do so.”

    You feel a wave of relief, though you remain cautious, knowing the Queen’s temper could turn at any moment.

    The Queen waves her hand, and suddenly, a small, ornate mirror appears floating in the air beside her.
    The frame is shaped like a heart and the glass shimmers with a strange light.

    “This mirror,” the Queen says, “is a portal. It will show you the way back to your world. But remember,
    once you leave Wonderland, you may not be able to return as easily.”

    You step closer to the mirror, her heart pounding with anticipation. “Thank you, Your Majesty,”
    you say sincerely. “I’m ready to go home.”

    The Queen smirks. “Very well. Step through, and you shall find yourself where you belong.”

    You take a deep breath, then reach out and touch the surface of the mirror. As soon as your fingers
    make contact, the glass ripples like water. You feel a strange pull, and before you know it,
    you being gently drawn into the mirror.

   The world around you swirls in a kaleidoscope of colors and lights, and for a brief moment,
   you feel weightless. Then, with a soft thud, you land on her feet.

   When Alice opens your eyes, you find yourself standing in a familiar meadow. The sky is bright,
   the air is warm, and in the distance, you can see home. You are back in your world.

   You take a deep breath, filled with relief and wonder. Though your time in Wonderland had been
   full of strange and dangerous adventures, you were grateful for the experience. And though you
   are home now, you know that the magic of Wonderland will stay with you always.

   With one last look at the horizon, You head home, your heart lighter and mind filled with
   memories of the incredible journey.
   """)

def challenge_queen():
    print("""You, feeling bold and defiant, straighten your back and look the Queen of Hearts
    in the eyes. You know the Queen can be dangerous, but you are no longer the same timid
    person who first stumbled into Wonderland. Your adventures have made you stronger,
    and if you have to stand up for yourself to get home, you are ready to do it.

    “Your Majesty,” You begin, your voice steady, “I didn’t come here to beg for help. I’ve
    faced many challenges in Wonderland, and I’m not afraid of one more. If you want me to
    earn my way home, then I challenge you.”

    The Queen of Hearts raises an eyebrow, clearly surprised by your boldness. For a moment,
    there’s silence in the grand throne room. Then, a slow smile spreads across the Queen’s face.

    “A challenge, you say?” the Queen purrs, amused. “How delightful. I do love a good contest,
    especially when I’m confident I’ll win. But be warned, child — no one has ever beaten me in
    a challenge before.”

    You hold your ground, determined. “I’ll take that risk.”

    The Queen claps her hands and the room around them shifts. The walls seem to melt away,
    replaced by a vast arena with towering hedges and flickering lanterns. In the center stands
    a tall chessboard, its squares gleaming under the lights.

    “We shall play a game,” the Queen declares. “A game of wits and strategy. If you win, I will
    grant you passage home. If you lose… well, I’m sure you can guess the consequences.”

    The game begins and you quickly realize that the Queen is as clever as she is ruthless.
    The pieces move almost on their own, following subtle commands from the players. The Queen
    plays with precision, her knights and queens sweeping across the board with fierce intent.

    But you, having learned to think quickly and cleverly in Wonderland, anticipate the Queen’s 
    moves. She makes bold plays of her own, guiding her pieces with a combination of logic and 
    intuition. The Queen’s frustration grows with each passing move, her confident smirk slowly fading.

    Finally, after a tense series of moves, you see an opening. With a triumphant smile, she moves
    her final piece into place and declares, “Checkmate.”

    The Queen of Hearts freezes, staring at the board in disbelief. For the first time, someone
    has bested her. Her face flushes with anger, but instead of lashing out, she lets out a slow,
    controlled breath.

    “Well, well,” the Queen says, her voice tight but controlled. “It seems you’ve won. I suppose
    I must honor my word.”

    The chessboard vanishes, and the grand arena melts away, leaving them back in the throne room.
    The Queen waves her hand, and once again, the magical mirror appears, shimmering in the air beside her.

    “This mirror will take you home,” the Queen says, though her tone is far less amused than before.
    “I suggest you take it before I change my mind.”

    Your heart racing from the intensity of the game steps toward the mirror. You look back at the
    Queen one last time, offering a polite but firm nod. “Thank you, Your Majesty.”

    The Queen simply waves her off, her eyes smoldering but silent. Without wasting another second,
    You touch the surface of the mirror and feel the familiar pull.

    In an instant, you are back in your world, standing in the same meadow where your adventure began.
    The sky is blue, the air fresh, and the sounds of Wonderland fade into distant memories. You home at last.

    You look around, your heart light and full of pride. You had stood up to the Queen of Hearts and won.
    Wonderland may have been strange, but it taught you that you were stronger and braver than you ever knew.

    With a smile, You turn and begin to walk back home, knowing that you carry the lessons of Wonderland
    with you forever.""")
 

#Welcome
print("""    _    _ _            _                            
   / \  | (_) ___ ___  (_)_ __                       
  / _ \ | | |/ __/ _ \ | | '_ \                      
 / ___ \| | | (_|  __/ | | | | |                     
/_/   \_\_|_|\___\___| |_|_| |_| _                 _ 
\ \      / /__  _ __   __| | ___| | __ _ _ __   __| |
 \ \ /\ / / _ \| '_ \ / _` |/ _ \ |/ _` | '_ \ / _` |
  \ V  V / (_) | | | | (_| |  __/ | (_| | | | | (_| |
   \_/\_/ \___/|_| |_|\__,_|\___|_|\__,_|_| |_|\__,_|""")
print()
print()
name = input("Please enter your name: ")
time.sleep(a)
print()
print("Hello, " + name + "! Happy to see you!")
time.sleep(a)
print()
print()

#Welcome text    
type("""Welcome to the Magical World of Wonderland!
Enter a world where the ordinary becomes extraordinary, and every turn is a new adventure! 
In this magical land, the curious and the brave are invited to join Alice on her whimsical 
journey through enchanted gardens, tea parties with unusual characters, and mind-bending 
mysteries.
Get ready to meet talking animals, mischievous Cheshire Cats, and a Queen who isn't afraid 
to shout, "Off with their heads!" As you navigate this fantastical world, your decisions 
will shape the story, revealing secrets and challenges around every corner.
Are you brave enough to follow the White Rabbit down the rabbit hole? Embrace the madness,
let your imagination run wild, and let the adventure begin!
Remember: in Wonderland, nothing is quite what it seems. Are you ready to find out what's
behind the mirror?""")
print()
print()
print("""    /\\
        _   / /\\
       | \  \/_/
       \_\| / __              
          \/_/__\           .--='/~\\
   ____,__/__,_____,______)/   /{~}}}
   -,-----,--\--,-----,---,\'-' {{~}}
           __/\            '--=.\}/
          /_/ |\\
              \/""")

#Start game function
startGame = input('Would You like to play? (Y/N): ')
if startGame == 'N' or startGame == "n":
    print("""That's totally okay!
    Adventure games can be a real journey. If you change your mind,
    just let me know and we can dive back into the whimsical world of Wonderland!""")
elif startGame == 'Y' or startGame == "y":
    play_game()
