label cd2_chat10():
#Well Brewed Discussion
    $ ri.status = "Too much coffee..."
    $ ja.status = "Never enough coffee"

    $ ja.prof_pic = "Profile Pics/Jaehee/jae-3.webmp"

    scene noon
    play music looking_for_happiness

    enter chatroom ri

    enter chatroom ja

    ri "Ah, how wonderful..."

    ri "This coffee is simply delicious"

    ja "That's your third cup Rika ;;;"

    msg ri "You're also on your third cup hehe" sser1

    ri "{image=rika_happy}" (img=True)

    ja "Right..."

    ja "{image=jaehee_sad}" (img=True)

    msg ja "You needn't remind me ;;" curly

    msg ja "I'm just so tired from work these days" sigh_m

    ri "I know ! We discussed it for a bit before"

    msg ri "So I won't scold you....too much" cloud_s

    ri "You should still try to  keep yourself healthy though!"

    ri "{image=rika_happy}" (img=True)

    msg ri "Oh, [name] is in here too !" glow

    msg ri "Hi [name]!!!" blocky

    ja "Hello there"

    menu:

        "Hi! Are you guys having fun ?":
            award heart ri

            ja "We are , thank you for asking "

            msg ri "Yes ! I'm so glad we managed to get together like this !" glow

            msg ri "Of course ~ I wish you could have come along but.." sigh_s

            ri "I'm sure there will be more opportunities for that in the future "

        "Is the coffee that good ?":
            award heart ja
            ri "I'll let Jaehee talk about this, she's the expert here heh"
            ja "Expert? How so?"
            msg ri "You seemed to really enjoy it, that's all!" ser1
            ja "Well...in my opinion,  yes! The coffee is good "
            msg ja "The notes are subtle" glow
            msg ja "Yet there is some...bite to it" curly
            msg ja "It's wonderful" square_m
            ja "The top notes are deep and rich"
    ri "Jaehee ordered the dark coffee! She said she liked the way it sounded"

    msg ja "The bitter taste.." glow

    msg ja "The amazing feeling of the coffee clinging to the insides of your cheeks.." square_m

    msg ja "The sweet release of tannins ..." sser1

    ja "I love it all "

    ri "And I..."

    ri "Got the one chock-full of milk ×_×...of course"

    ri "It's the closest thing to the instant ones I usually get "

    ja "Those are no good Rika "

    ja "You get none of the flavour there"

    msg ri "What can I do ? I'm addicted " sigh_s

    ri "{image=rika_sad}" (img=True)

    msg ja "I need to get you some more varieties of coffee to try" sser2

    ja "My dream is to have my own coffee grinder one day "

    ri "That dream might be within your grasp hehe "

    ja "What do you mean ?"

    msg ri "..I won't say another word for now :)" cloud_s

    ja "Hmmm"

    ja "That grin  you have on your face is very suspicious"

    ri "Jaehee , don't you worry !"

    ri "You'll find out soon enough! "

    menu:

        "Lol, are you guys chatting while sitting across one another ?":

            ja "We are"

            ri "Yes actually ! I know it's strange but "

            ri "We like the silence between us while we enjoy our coffee"

            ja "We talked for over an hour straight before this "

            ja "Besides, Rika's voice seems a bit strained"

            ja "Why is that Rika?"

            ri "Oh, it's nothing...don't worry about it"

        "I'm jealous of Jaehee. I want to be there with Rika":

            ri "Hmm"

            ri "THere's no need  to be jealous !"

            ri "Jaehee and I are friends !"

            msg ri "As are we!" cloud_s

            ri "We'll all be to gather  here  soon anyways!"

        "I want to be there with you guys":
            award heart ri
            award heart ja

            ri "We want that too!"

            ri "{image=rika_party}" (img=True)

            ja "It could be fun "

            ri "We could talk more than in the chatroom "

            ri "I already know what you look like , but Jaehee doesn't "

            ja "You told me about what she looks like , so I at least have a picture in my mind "

            msg ri "Ah yes, I did... Hope you don't mind [name] ^^;" sigh_m


    ja "Rika also took a picture of us "

    msg ri "Yes, I did indeed"  glow

    msg ja "I don't look the best in it"  sigh_s

    ri "Perish the thought!  I think you look beautiful in it "

    ja "Maybe.."

    ja "I was just caught a bit off-guard "

    ja "Though we were both tuckered out from our conversation though, so it did help lighten the mood"

    ri "Ah yes, that would be true..."

    msg ri "Here everyone!  Have the photo of the two of us I took " square_m

    ri "{image=rika_jaehee_CG}" (img=True)

    menu:
        "Jaehee looks so awkward in the picture lol":
            break heart ri

            ja "Told you..."

            ri "[name]! please don't say that:("

            ri "{image=rika_sad}" (img=True)

            ri "I think she looks wonderful"

            ri "It's my fault for catching her off-guard anyway..."


        "You two look beautiful!":
            award heart ri

            ja "If that's what you think "

            ri "See Jaehee ? [name] agrees +_+"

    ri "We should take another photo like this with you someday [name]"

    ri "All us R.F.A members in one picture ^^"

    ja "Yes, that's true "

    ri "Anyways...Should we head out now?"

    ja "Just a little more...I'll need some time to ask the barista about the recipe "

    ri "Ah yes! Go ahead!"

    ja "Goodbye !"

    exit chatroom ja

    ri "That reminds me..."

    ri "The owner of this cafe is this really sweet lady"

    ri "And she's known for giving away pastries for free..."

    ri "I feel someone with such a big heart should be given a chance to attend the party"

    ri "I'll get you in contact with her [name] ^^"

    ri "I'm sure you'll get along well"

    ri "Well then...I'll be taking my leave"

    ri "...after getting more of this delicious coffee ;;;"

    menu:

        "Goodbye Rika ! Please don't drink too much or you'll get sick":
            award heart ri

            ri "Oh, no need to worry ! ^^"

            ri "I'll get some decaf for a change !"

            msg ri "But...thank you for caring ^^" glow

        "Lol, another one ? Goodbye then":

            ri "Yes yes +_+"

    ri "Take care [name] !"

    ri "Goodbye !"

    exit chatroom ri

    return


label cd2_chat10_expired():

    $ ri.status = "Too much coffee..."
    $ ja.status = "Never enough coffee"

    $ ja.prof_pic = "Profile Pics/Jaehee/jae-3.webmp"

    scene noon
    play music looking_for_happiness

    enter chatroom ri

    enter chatroom ja

    ri "Ah, how wonderful..."

    ri "This coffee is simply delicious"

    ja "It's your third cup Rika ;;;"

    msg ri "You're also on your third cup hehe" sser1

    ri "{image=rika_happy}" (img=True)

    ja "Right..."

    ja "{image=jaehee_sad}" (img=True)

    msg ja "You needn't remind me ;;" curly

    msg ja "I'm just so tired from work these days" sigh_m

    ri "I know ! We discussed it for a bit before"

    msg ri "So I won't scold you....too much" cloud_s

    ri "You should still try to  keep yourself healthy though!"

    ri "{image=rika_happy}" (img=True)

    ri "No one else is in here huh?"

    ja "Sure seems like it"

    msg ri "No matter! I'm still so glad we managed to get together like this  at all!" glow

    msg ri "Of course I wish [name] could have come along but.." sigh_s

    ri "I'm sure there will be more opportunities for that in the future "

    ri "As for the quality of the coffee..."

    ri "I'll let Jaehee talk about that, she's the expert here heh"
    
    ja "Expert? How so?"
    
    msg ja "You just seemed to enjoy it a lot, that's all!" ser1

    ja "In my opinion,  the coffee is amazing "

    msg ja "The notes are subtle" glow

    msg ja "Yet there is some...bite to it" curly

    msg ja "It's wonderful" square_m

    ja "The top notes are deep and rich"

    ri "Thank you ~"

    ri "Anyways.."

    ri "Jaehee ordered the dark coffee! She said she liked the way it sounded"

    msg ja "The bitter taste.." glow

    msg ja "The amazing feeling of the coffee clinging to the insides of your cheeks.." square_m

    msg ja "The sweet release of tannins ..." sser1

    ja "I love it all "

    ri "And I..."

    ri "Got the one chock-full of milk ×_×...of course"

    ri "It's the closest thing to the instant ones I usually get "

    ja "Those are no good Rika "

    ja "You get none of the flavour there"

    msg ri "What can I do ? I'm addicted " sigh_s

    ri "{image=rika_sad}" (img=True)

    msg ja "I need to get you some more varieties of coffee to try" sser2

    ja "My dream is to have my own coffee grinder one day "

    ri "That dream might be within your grasp hehe "

    ja "What do you mean ?"

    msg ri "..I won't say another word for now :)" cloud_s

    ja "Hmmm"

    ja "That grin  you have on your face is very suspicious"

    ri "Jaehee , don't you worry !"

    ri "You'll find out soon enough! "

    ri "If you were wondering if we are chatting in here while sitting across from each other.."

    ja "We are"

    ri "Yes actually ! I know it's strange but "

    ri "We like the silence between us while we enjoy our coffee"

    ja "We talked for over an hour straight before this "

    ja "Besides, Rika's voice seems a bit strained"

    ja "Why is that Rika?"

    ri "Oh, it's nothing...don't worry about it"

    ja "If you say so..."

    ja "Rika also took a picture of us "

    msg ri "Yes, I did indeed"  glow

    msg ja "I don't look the best in it"  sigh_s

    ri "Perish the thought!  I think you look beautiful in it "

    ja "Maybe.."

    ja "I was just caught a bit off-guard "

    ja "Though we were both tuckered out from our conversation though, so it did help lighten the mood"

    ri "Ah yes, that would be true..."

    msg ri "Here everyone!  Have the photo of the two of us I took " square_m

    ri "{image=rika_jaehee_CG}" (img=True)

    ri "We should take another photo like this with [name] someday"

    ri "All us R.F.A members in one picture ^^"

    ja "Yes, that's true "

    ri "Anyways...Should we head out now?"

    ja "Just a little more...I'll need some time to ask the barista about the recipe "

    ri "Ah yes! Go ahead!"

    ja "Goodbye !"

    exit chatroom ja

    ri "That reminds me..."

    ri "The owner of this cafe is this really sweet lady"

    ri "And she's known for giving away pastries for free..."

    ri "I feel someone with such a big heart should be given a chance to attend the party"

    ri "I'll get [name] in contact with her ^^"

    ri "I'm sure they'll get along well"

    ri "Well then...I'll be taking my leave"

    ri "...after getting more of this delicious coffee ;;;"

    ri "Goodbye !"

    exit chatroom ri

    return
