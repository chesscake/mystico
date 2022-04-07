label cd1_chat2():

    scene night

    enter chatroom z

    msg z "{size=+5}Hi~{/size}" sigh_m
    z "Everyone's getting busy for the party."
    #z "(posts picture of the musical with him in it)"
    z "Here's a quick pick me up" (bounce=True)
    z "while you're working so hard!" (bounce=True)
    z "{image=zen_wink}" (img=True)
    msg z "A fan sent me this lolol"
    msg z "{size=+5}Don't I look great in it?{/size}" cloud_m
    menu:
        "You look like AMAZING":
            award heart z
            z "-"


    enter chatroom s

    msg s "{size=+5}OMG o_o{/size}" bold
    s "It's so beautiful!! My eyes !!" (bounce=True, specBubble="round_m")
    z "Hey."
    msg s "Thank you Zenny ♥" curly big
    s "{image=seven_love}" (img=True)
    s "I feel so refreshed I no longer need to sleep!" (bounce=True, specBubble="round2_l")
    msg z "Hey." sser2 big xbold
    z "{image=zen_angry}" (img=True)
    z "I'm sorry, there was a mistake."
    z "I meant it for all the {u}hardworking girls{/u} in here. {b}Not you.{/b}" #if player is not female, this line is still the same but he's emphasizing Rika & Jaehee.
    msg s "Aw, don't be like that." cloud_m
    msg s "I was in the audience."
    z "Huh? You were?"
    s "I was so touched by your singing too." (bounce=True, specBubble="sigh_m")
    msg z "No way." blocky
    z "Who sent you there?"
    msg s "{size=+5}Aren't your perfomances open to the public ;;{/size}" ser2
    s "And Rika invited me, that's why"
    s "I"
    s "{size=+5}had{/size}"
    s "{size=+10}to{/size}"
    s "{size=+15}go★{/size}"
    msg s "Frankly, I'm a little sad you don't remember me..." sigh_m
    menu:
        "Newsflash! The world doesn't revolve around you!":
            break heart s
            s "O...okay? ;-;"
            z "She's right." #change pronouns here
            s "Arghh I know, I know!"
            s "{image=seven_cry}" (img=True)
        "I wish Rika invited me to go to musicals too.":
            award heart ri
            s "She's so nice to all of us"
            s "I'm sure she will!"
            s "{image=seven_smile}" (img=True)
        "Zen would remember me if I had gone <3~ wouldn't you, Zen <3?":
            award heart z
            z "Of course I would..."
            msg z "Ever since I saw your face I haven't forgotten you, not even once." square_m
            msg s "{size=+10}wow cringe!{/size}" blocky
    msg s "Anyway"
    msg s "It's one of my favorite memories!" cloud_l
    msg s "I had read that story before"
    msg s "but your musical transported me to that faery tale-like world!!" cloud_m
    s "And it all came alive before my eyes."
    msg s "The Eternal Kingdom made of gemstones and gold!" blocky
    msg s "The sacrificing suffering prince!" blocky
    msg s "The drama of the two bird princesses!" blocky
    msg s "{size=+10}And the singing!! There was lots of singing!!{size=+10}" ser1
    z "Omg... you're being genuine"
    msg z "{size=+5}and serious, for once?!?{/size}" bold
    menu:
        "Could it be? Seven is secretly a musical superfan?!":
            award heart s
            msg z "No way..." ser2 bold
            s "Eheh~ "
            s "Actually"
            s "A tiny seven read the book >.<"
            z "Huh?!"
            z "Oh, you mean,"
            z "you read the book when you're younger?"
            s "^w^"
            z "I will take that as a yes"
        "Bird princesses?":
            s "Yup"
            s "In the book they can shapeshift into birds~"
        "So dreamy! I wish I was there.":
            award heart z
            award heart ja
            s "..."

    z "{image=zen_cry}" (img=True)
    z "Thank you."
    msg z "Well, I guess I just have to be careful with my beauty since no one can resist it." square_l
    msg s "lolol what a sudden change of character?!?" ser2 bold
    z "I'm an actor, my craft is meant to be appreciated regardless of gender"
    msg z "Not your jokes." ser1
    msg s "lolol" cloud_s
    msg s "{size=+5}But don't you think there was something amiss in the story?{/size}" ser1
    s "It's more like a sad parting than a traditional happy end."
    z "What are you talking about?"
    z "The girl with the purest heart won over the prince and saved him." (bounce=True)
    z "Then they married and had they had their happily ever after." (bounce=True)
    z "As they stared lovingly in each other eyes..."
    z "..."
    z "Sigh."
    msg z "WHEN will MY happily ever after arrive?" sigh_m
    s "{size=+5}But{/size}"
    msg s "But when the evil bird princess" glow
    msg s "was shown clutching to one of the fallen feathers of the pure hearted one in her final moments" glow
    msg s "She had such a sorrowful expression..." glow
    s "{size=+15}OMG~{/size}"
    s "{size=+5}What if the one she truly loved was..!{/size}"
    menu:
        "Gasp!!":
            award heart s
            s "You get it!!"
        "Sounds like she was just jealous lol":
            award heart z
            z "That's how I saw it too."
            s "But would she look that sad?"
        "Were these two princessess... friends?":
            s "Ya!!"
            s "You aren't familar with the story, [name]?"
            z "You could say they were at some point."
            z "Their relationship is part of the main drama."
            z "{size=+10}They were connected!{/size}"
            s "More than friends, maybe they were...!"
    z "-__-"
    z "Are you kidding me now?"
    msg z "{size=+5}They were in love with me. Me.{/size}" bold
    msg z "Stop projecting your weird fantasies into it."
    s "lolololol are you suuure"
    s "."
    s "whoops, gotta go."
    s "Madam is calling me."
    z "Madam? Who is that?"

    exit chatroom s

    z "And off he goes."
    z "That guy, I can't get used how weird he is."
    z "I guess I will go too."

    exit chatroom z

label cd1_chat2_expired():

    scene night

    enter chatroom z

    msg z "{size=+5}Looks like no one is here...{/size}" sigh_m
    z "Everyone's so busy for the party."
    #z "(posts picture of the musical with him in it)"
    z "Here's a quick pick me up" (bounce=True)
    z "while you're working so hard!" (bounce=True)
    z "{image=zen_wink}" (img=True)
    msg z "A fan sent me this lolol"
    msg z "{size=+5}Don't I look great in it?{/size}" cloud_m

    enter chatroom s

    msg s "{size=+5}OMG o_o{/size}" bold
    s "It's so beautiful!! My eyes !!" (bounce=True, specBubble="round_m")
    z "Hey."
    msg s "Thank you Zenny ♥" curly big
    s "{image=seven_love}" (img=True)
    s "I feel so refreshed I no longer need to sleep!" (bounce=True, specBubble="round2_l")
    msg z "Hey." sser2 big xbold
    z "{image=zen_angry}" (img=True)
    z "I'm sorry, there was a mistake."
    z "I meant it for all the {u}hardworking girls{/u} in here. {b}Not you.{/b}" #if player is not female, this line is still the same but he's emphasizing Rika & Jaehee.
    msg s "Aw, don't be like that." cloud_m
    msg s "I was in the audience."
    z "Huh? You were?"
    s "I was so touched by your singing too." (bounce=True, specBubble="sigh_m")
    msg z "No way." blocky
    z "Who sent you there?"
    msg s "{size=+5}Aren't your perfomances open to the public ;;{/size}" ser2
    s "And Rika invited me, that's why"
    s "I"
    s "{size=+5}had{/size}"
    s "{size=+10}to{/size}"
    s "{size=+15}go★{/size}"
    msg s "Frankly, I'm a little sad you don't remember me..." sigh_m
    msg s "Anyway"
    msg s "It's one of my favorite memories!" cloud_l
    msg s "I had read that story before"
    msg s "but your musical transported me to that faery tale-like world!!" cloud_m
    s "And it all came alive before my eyes."
    msg s "The Eternal Kingdom made of gemstones and gold!" blocky
    msg s "The sacrificing suffering prince!" blocky
    msg s "The drama of the two bird princesses!" blocky
    msg s "{size=+10}And the singing!! There was lots of singing!!{size=+10}" ser1
    z "Omg... you're being genuine"
    msg z "{size=+5}and serious, for once?!?{/size}" bold
    z "{image=zen_cry}" (img=True)
    z "Thank you."
    msg z "Well, I guess I just have to be careful with my beauty since no one can resist it." square_l
    msg s "lolol what a sudden change of character?!?" ser2 bold
    z "I'm an actor, my craft is meant to be appreciated regardless of gender"
    msg z "Not your jokes." ser1
    msg s "lolol" cloud_s
    msg s "{size=+5}But don't you think there was something amiss in the story?{/size}" ser1
    s "It was more like a sad parting than a traditional happy end."
    z "What are you talking about?"
    z "The girl with the purest heart won over the prince and saved him." (bounce=True)
    z "Then they married and had they had their happily ever after." (bounce=True)
    z "As they stared lovingly in each other eyes..."
    z "..."
    z "Sigh."
    msg z "WHEN will MY happily ever after arrive?" sigh_m
    s "{size=+5}But{/size}"
    msg s "But when the evil bird princess" glow
    msg s "was shown to be clutching to one of the fallen feathers of the pure hearted one in her final moments" glow
    msg s "She had such a sorrowful expression..." glow
    s "{size=+15}OMG~{/size}"
    s "{size=+5}What if the one she truly loved was..!{/size}"
    z "-__-"
    z "Are you kidding me now?"
    msg z "{size=+5}They were in love with me. Me.{/size}" bold
    msg z "Stop projecting your weird fantasies into it."
    s "lolololol are you suuure"
    s "."
    s "whoops, gotta go."
    s "Madam is calling me."
    z "Madam? Who is that?"

    exit chatroom s

    z "And off he goes."
    z "That guy, I can't get used how weird he is."
    z "I guess I will go too."

    exit chatroom z

    return

######____TEXT MESSAGES____

label after_cd1_chat2:

    compose text ri:
        ri "Hello, [name]!"
        ri "Have you ever read The Eternal Kingdom and Other Tales?"
        label reply_eternalkingdom1

    return

label reply_eternalkingdom1:
    menu:
        "No, what is it?":
            ri "That's the book the musical was based on."
            ri "It's a collection of short stories written by __, published after his disappearance."
        "YES. I'm in an online fanclub and I've watched the musicals!":
            ri "Wow! Amazing!"
            ri "Ah, er... by any chance have you seen moonchild8?" 
            ri "If you have, that's me, eheh. "
    ri "But... That chat had me thinking about something..."
    ri "There's rumors the Eternal Kingdom story is actually incomplete."
    ri "If that's true I wonder what the original ending was supposed to be..."
    ri "What if beneath that happy ending it was all meant to be a tragedy?"

    return
