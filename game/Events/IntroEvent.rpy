

init:
    $ talkedOnce = False
    $ learnName = False


label prologue:

        update "Body is compatible and stabilized, muscle is forming nicely, brain activity is minimal. Seems like everything is going smoothly"

        update "All that's left is to wait for callibration tests to run and check for any abnormalities."

        update "Soon our new component will be complete and we will have a new addition to our family."

        "You hear a loud bang indicating a door somewhere has been thrown open"

        gigas "YEAAAAAAAAH ANOTHER BROTHER IS GOING TO BE GREAT. LET ME SEE HIS SEXY FACE."

        update "HEY SHUTUP HE'S GOING TO BE MY BROTHER THIS TIME."

        gigas "I THINK NOT DICK FOR BRAINS!"

        update "I HAVE HALF A MIND TO THROW YOU IN THE TOILET."

        update "I FIND THAT UNLIKELY SINCE YOU NEED A BRAIN TO HAVE HALF A MIND."

        update "You're both idiots and share 1 brain cell now get out of my room."

        update "I will not be bringing another component into this world while you oafs scream over his body."

        update "AW man. I wanted to be the first thing he sees."

        update "Then you can wait outside but personally, I'd prefer he didn't become either of you guys since you seem to think with your muscles."

        update "Now get out of my and you'll see him when he's moving around"

        update "(Grunting noises)"

        update "Now then I know you've heard all of that mess. Seems your family is eager to meet you though I would respect your decision if you choose not to open your eyes."

        menu:
            "Open eyes":
                jump openeyes
            "Stay asleep":
                jump predeath1

        return

label predeath1:

    "..." "Haha, yeah they can be a handful sometimes but you should probably at least open your eyes so I can confirm the initial configurations are working as planned.
    I would hate to have to tell C I messed up again"

    menu:
        "Open eyes":
            jump openeyes
        "Stay asleep":
            jump predeath2

label predeath2:

    "..." "Hmmm, I guess you didn't hear everything then. Great C's going to be mad at me for fucking up yet another time. Damn it."

    "You hear a loud buzz saw near your ear"

    "..." "Damn I really gotta cut open another one. Promise me one thing, please do not start screaming because the last time this happened everyone heard it. And I had to choose
    between stopping midway or continuing to stop them from screaming."

    menu:
        "Open eyes":
            jump openeyes
        "Stay asleep":
            jump predeath3

label predeath3:

    "Die"

    return

label openeyes:

    scene bg openeyes

    "You open your eyes"

    "You are then greeted by a large muscular robot with a weird destiny-esque look to their face"

    "For a robot, it's very muscular and he seems to be almost naked save for his pants"

    "You can tell it's a robot (or at least non-human) because his head is missing human features"

    "At the very leasts it's at least humanoid"

    show byte at left

    show update at right

    update "Seems like everything is in working order"

    update "Just to be sure let's do some quick manual tests to double check your settings"

    update "Please stand up and lift your arms"

    menu:
        "Lift Arms":
            $ update = Character("Mysterious Robot")
            jump LiftArms
        "Stare at him":
            jump StareAtHim

    return

label LiftArms:
    update "Good, good."

    "The [update] continues writing notes in his tablet. His inhuman head lacks any room for simple expressions to tell what he's thinking"

    "Contrary to being a robot his body itself is riddled with slabs of muscle and... veins?"

    "On top of his unnecessarily excessive musculature, he is naked... and for that matter you look down towards the rest of your body and you see you are also naked."

    "...Except he's packing a soft 9 maybe 10 incher? And on top of that you yourself are missing your own metallic extension."

    update "Seems like everything is perfectly fine. Nothing seems out of the ordinary."

    update "Now I am preparing your initial body scans. After which, I will have you do a set of tests of varying difficulty."

    "You hear a small hum come from the tablet"

    update "Finally, we will do 1 final scan checking for any abnormalities that may have occurred during or after the tests."

    "This might be the best time to ask questions"

    menu IntroQuestion:
        "Ask who is he":
            jump AskWhoIsHe
        "Ask him about missing 'dick'":
            jump AskMissing
        "Ask him about where you are":
            jump AskLocation
        "Continue":
            jump DoingTests

    "You should not see this"

label AskWhoIsHe:

    $ learnName = True

    update "Ah yes, how rude of me. My name is very simple, I am called Update. I am, what is called, a mechanic of sorts."

    update "I fix machine people, robots, subhumans and in this case create machine people"

    update "I also specialize in memory alloy repairing and upgrading"

    menu:
        "Interesting.":
            call Interesting
        "What?":
            call WhatIsThat

label Interesting:
    "That seems interesting"

    update "You have no idea what I just said do you"

    "Nope"

    update "Of course"

    jump IntroQuestion

label WhatIsThat:
    "You have no idea what that means"

    update "Basically if someone's arm or head is torn off for any reason. I'm the person you call for a new head."

    "How did he-"

    update "Although it is not important at the moment, I can actually read your thoughts on my holotab here. Did you forget I was scanning you since you woke up?"

    update "And for your memory records, it's 9.5 inches but I must admit you were very close"

    "His lack of facial expressions is stlil hiding his emotions. And you can't make out if he's flirting with you or being coy"

    jump IntroQuestion

label AskMissing:
    #if talkedOnce not True:
    #    $ talkedOnce = True
    #    update "So you can speak already. Wonderful. Usually it takes days or months and, once before, a whole year for you guys to learn to speak."

    update "Do not worry about your privates so soon. I have not even finished my diagnosis of your body let alone even asked what you want to be called."

    update "After my scan is complete I will know everything about you that I cannot immediately see."

    "You worry if he will also see you've been staring at his dick."

    jump IntroQuestion

label AskLocation:
    "You ask him where we are?"

    update "As much as I would love to entertain you, I believe you will find all of this out soon enough"

    jump IntroQuestion

label DoingTests:

    update "Now, you will undergo several of my tests to ensure you are in good stable condition."

    update "The Motor Controls test will check your physical capabilities and to make sure you don't break from hitting your toe on the door"

    "That was oddly specific"

    update "Oh trust me. While you are the first unit I've built this way, almost everyone does this."

    update "Moving on, the Flexibilty test will check reflexes, thinking power, and your ability to adapt and..."

    "How flexible I am?"

    update "Correct"

    update "Visual test for your eyes to make sure they are synced up and you are not blind"

    "He moves closer to you to study your eyes but as he closes in his dick caresses your arm. It is almost as if he's taunting to you with it."

    update "And I will make sure you-"

    "You hear a loud ding come from his tablet-like device and he quickly shifts his focus to it."

    "While he is distracted his dick still rests on your arm will you grab it?"

    menu:
        "Yes":
            jump GrabDick
            $ Update.affection + 10
        "No":
            jump WaitPatiently

label GrabDick:

    "Seizing the opportunity you quickly grab his metal meat cannister and much to your surprise he doesn't even flinch"

    update "As usual you Bytes tend to be very outward with your advances. Ah well I'm sure you're fine"

    "You have sex with him"

    "Place holder sex scene"

    jump Continue

label WaitPatiently:

    "You decide to wait patiently until Update has finished"

    update "Well that is interesting. You seem to have a nasty virus running amok inside you."

    update "Normally this would be expected however, you were just created e mere second ago."

    update "How you got a virus of this caliber is beyond my imagination."

    update "(Sigh) And unfortunately, I was expecting this to be a simple routine check so I didn't even bring any of antivirus gear with me"

    update "Alright look. Don't tell anyone about this except for 'C'. He is the only one that should know about your condition."

    update "He will have to reschedule my appearance immediately and I will be able to come and extract that virus."

    menu:
        "What is a virus?":
            jump WhatIsAVirus
        "(Continue)":
            jump WaitPatiently2

label WhatIsAVirus:

    update "A normal computer virus is basically code that replicates itself."

    update "However, for shades like you its like being sick and for robots its like catching a deadly disease"

    update "If left uncheck you can accidentally infect other people with it and cause even more damage"

    update "Strangly the one you are currently inflicted with has 2 main functions"

    update "The first one being replicating itself as a normal virus does."

    update "The second one being to change the inflicted if they come into contact with the source of the virus."

    update "Clearly someone infected you with this. Its even possible they are in this unit right now."

    update "We wouldn't want that person to infect other people or do something even worse."

    jump Continue

label Continue:

    "He quickly cleans up the area and prepares records all the information in his tablet"

    update "WHen you talk to C have him- no, he will reschedule me to come back afterwards"

    "You begin to ask him what about the other guys until-"

    update "Oh I am terribly sorry it had almost slipped my mind"

    player "What did?"

    player "Wait"

    "With no warning you are given an outside voice"

    update "Simply put, I was supposed to give you your outside voice after the various tests but because of the sudden emergency..."

    update "I have to leave to protect myself from that virus you are holding"

    player "But wait I still have questions"

    update "C will answer all of them for your but promise me"

    update "Under no circumstances are you to talk, interact or even see anyone other than C and me"

    player "How do I find him?"

    update "After you exit this room take a left, and then a right at the end of the corridor"

    update "I'm sure the bytes and ROMs are fucking each other and preparing cake in the next room for your awakening and once I leavea they will swarm this room."

    update "For the sake of this Unit, do not interact with them you must hide"

    player "Is there anything you can give me to help?"

    "As quickly as you said that his body is enveloped in a bright flash of light followed by a noisy buzzing sound"

    "When the light disappears the robot is gone and you are here alone"

    player "What the fuck he can teleport but he can't take me with him?"

    "Now where do you want to go?"

    jump MainMapScreen

label DoNothing:

    update "Hmmm. It seems as if you are unable to move. Well at least we know you are functioning right now"
