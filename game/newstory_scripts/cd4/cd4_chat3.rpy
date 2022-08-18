label day_4_chatroom_3():
#Eventfull morning
    $ ri.status = "Nature accepts all with its giving hands.."
    $ y.status = "Wish me luck everyone!"

    scene morning
    play music the_way_home

    enter chatroom ri

    msg ri "Hello everyone!" glow
    msg ri "What a fine morning. Can't wait to head out for the day! ^^" ser2
    menu:
        "It's not nice out where I am":
            ri "Is that so? Such a shame..."
            msg ri "The sky is a nice blue where I am" glow
            msg ri "I'd love to share the view with you ^^" curly
        "Maybe I should head out as well":
            ri "I'd highly recommend it!!"
            msg ri "Even the passerby I see outside my window seem to be in a good mood" glow
            ri "And those guys are almost always frowning ^^;;;"
    ri "Before I continue.."
    msg ri "I feel like I should apologize for what happened last night ;;" 
    msg ri "It was pretty rude of me to suddenly barge into the chatroom like that" ser1
    msg ri "From now on, I'll try to keep stuff like that to a minimum" ser1
    msg ri "Maybe all these new responsibilities regarding the party are getting to me" curly
    ri "Regardless....I shouldn't have allowed you guys to see me like that.."
    ri "From now on, I promise to be the bright and positive Rika you're used to seeing!!"
    ri "To make up for that...I was hoping you'd all tell me what your plans for today were"
    msg ri "So I can help you with them as much as possible" glow
    menu:
        "I was just planning on chatting with you guys":
            msg ri "Oh wow, really??" round_m
            msg ri I'm so glad you're already used to being one of us" glow
            ri "But please make sure to go outside and get some fresh air as well!!"
        "Maybe I should just go back to sleep...":
            ri "I understand. There's a whole day ahead of us, so no need to rush"
            msg ri "Don't want to nag you about that sort of thing" ser1
            ri "As soon as you're ready though, I'd recommend trying to go out and having some fun"
        "On days like this, I just want to spend all my time outside":
            msg ri "I felt like you would say that ^^" glow
            ri "You seem like a person who'd enjoy that sort of thing"
            msg ri "That is a compliment, of course" glow
    ri "Hmm...Now I'm curious about the other members"
    ri "I guess I'll just have to wait until one of them shows up"
    ri "In the meantime...We could talk about whatever you'd like!"
    ri "Have anything you're passionate about ?"
    menu:
        "Just busy living life...":
            ri "Oh no, you sound a bit sad..."
            ri "Please don't fret! If you ever need any help, don't hesitate to call me"
            ri "I'll always be there if you need me!"
        "I recently got a new hobby!":
            ri "Those are always fun!"
            ri "Make sure you're always taking time away from your day to spend on hobbies and other fun activities" 
            msg ri "Without them, life can get pretty dull ;;;" sigh_m
        "Trying to find ways to improve the R.F.A"
            award heart ri
            msg ri "My my, aren't you a hard worker?" glow
            msg ri "The fact you're already thinking about that sort of thing makes me really happy!" cloud_m
            msg ri "Thank you for keeping us in your thoughts" glow

    enter chatroom y

    ri "Oh, hello there Yoosung! So good to see you!"
    ri "Wait...isn't today the day?"
    msg y "You don't need to remind me"  sigh_m
    y "It's all that's on my mind"
    y "So I came here to try and  blow off some steam"
    ri "Of course!! I think I'd feel the same way"
    ri "The entrance exam has probably gotten a lot harder since I took it"
    msg y "Your score was really impressive! Can't believe you didn't end up enrolling" ser1
    ri "Hmm..I had a lot on my plate at the time, so it wasn't really a possibility"
    msg ri "However..Thanks to that, the R.F.A came into existence ! So all is well! glow
    ri "The day I took the exam sure was a hectic one..Wasn't nearly as sunny out as it is now"
    ri "I suppose you'd rather we switch the subject away from that though ^^;;"
    y "...yes please ;;"
    y "Yesterday was really tough, since I spent most of the day studying"
    msg y "And today,  when I finally went out on a walk..." curly
    msg y "The world seemed to be laughing at me" sigh_m
    y "The sun was beginning to rise, and even saw a few flowers blooming"
    msg ri "That sounds beautiful.." glow
    y "Yeah, it was. You'd probably appreciate it more. I know how much you like plants"
    ri "Do you have any plants [name]? I'm curious !"
    menu:
        "Mine always seem to die":
            ri "They sure are tricky! I understand completely"
            ri "Back when I started out, mine were also feeling a little under the weather"
            y "Now you're a real green-thumb All the photos you send of them look really good "
        "Don't really like things like that":
            y "Me neither. I prefer animals to plants."
            msg ri "I think both are equally as important and beautiful! " glow
            ri "A world without one or the other doesn't sound too good..."
        "I have quite a few! They're a hobby of mine":
            award heart ri
            msg ri "Wow, another thing we have in common! Isn't that nice? ^^" glow
            ri "I'd love it if we could swap tips regarding plant care"
            ri "We should do that the next time we meet "
    pause 1.0*5
    y "Umm...Do you have a favorite plant or flower?"
    msg y "(Trying really hard not to think of the impending doom that awaits me)" sigh_m
    msg ri "I appreciate the effort ^^" glow
    ri "Hmm..never thought about that.."
    ri "If I had to pick, I guess I'd choose daffodils!"
    y "Any particular reason for picking those?"
    pause 1.0*3
    play music mint_eye_piano
    ri "Well...they wake up at the first signs of spring, stretching their heads towards the sky and breaking through the snow"
    ri "Then they bloom in a brilliant flash of yellow, proudly towering above its icy prison"
    ri "Swaying in the breeze, it spends its youthful days filled with happiness"
    msg ri "But then.."  curly
    ri "It begins to wither, slowly but surely. It retracts from the outside world and spends its days in  solitude before departing the world"
    msg ri "I find its story inspiring..." glow 
    pause 1.0*3
    ri "...Did I say something weird? ;;"
    menu:
        "I agree with you...Daffodils represent something meaningful to me as well":
            award heart ri
            msg ri "Thank you so much [name]! I just knew you'd be able to understand me" round_m
            msg ri "I thought I'd said something a bit strange but..." curly
            msg ri "Turns out you were on the same track as well. Isn't that amazing?" cloud_m
        "How could you get all that from a flower?"
            ri "Simple! By observing it and seeing the way it rises above its harsh conditions"
            msg ri "But...You might be right, I am assigning a lot of human attributes to a flower" curly
            msg ri "I should've been a bit more objective about it" ser1
    y "Sorry for not saying anything."
    y "I just wasn't really able to understand what you were getting at"
    msg y "You sounded very serious. I was kind of taken aback" ser1
    ri "Oh...Is that so?"
    ri "Ah, I said I'd be more careful about saying stuff like that in the chatroom earlier and yet"
    msg ri "Seems like I messed up again.." ser2
    y "I didn't want to comment on that but...it WAS very unlike you"
    y "But don't worry, you didn't mess up or anything"
    msg y "Just didn't seem like the you I know" bold
    menu:
        "Hey now..Rika should be able to express herself any way she wishes":
            y "I never said she couldn't..."
            ri "Of course you didn't ! It's just that I can get sensitive about that sort of thing"
            award heart ri
            msg ri "Thank you for saying that , [name]. I really appreciate it" glow
        "Be careful with revealing private info. I feel a bit uneasy regarding that these days"
            award heart va
            ri "I don't think that'll be an issue.."
            y "We have really good security in the messenger [name]! Don't worry about it"
            msg ri "I'll be more careful from now on though.." curly
    ri "Regardless...I did break my promise to be more positive here"
    y "It doesn't matter Rika! We all know how bright and positive you always are"
    y "You inspire me to be a better person just be existing . That's a pretty amazing thing you can do"
    msg ri "Ah, of course...I'm glad to be of help to you" ser1
    ri "But maybe you should try and"
    y "Hmm?"
    ri "Never mind. I'll talk to you about it after you're done with the exam ^^"
    y "Oh no...You just reminded me I still need to check if I have everything ready for that"
    y "I should probably leave now"
    menu:
        "Good luck with the entrance exam Yoosung!":
            award heart y
            y "Thank you [name]!! I'll do my best"
            y "Especially since the whole R.F.A seems to be cheering me on"
        "Don't mess up too badly":
            y "Don't say stuff like that T_T"
            y "You're making me even more nervous"
    msg ri "You know I'm always cheering for you!" glow
    ri "Go out there and show them all that you can do"
    msg y "Will do Rika!! With you on my side, I know I'll do well!" glow
    y "Goodbye now!!"

    exit chatroom y

    ri "Wow..Can't believe he's already grown up"
    ri "Just a few more months and he'll be ready to start with college"
    ri "It's been quite a ride, but I'm really proud of everything he's accomplished"
    ri "He's done so much better than what everyone around him was expecting"
    msg ri "But I knew he was full of potential the day I first laid my eyes on him" glow
    menu:
        "I think you're full of potential too Rika. I'd like to help you achieve it!":
            award heart ri
            pause 1.0*3
            ri "You mean....You want to help me?"
            msg ri "...Thank you so much for saying that!" cloud_m
            msg ri "I'd like to hep you achieve your potential as well!" cloud_m
            msg ri "Let's guide each other on that journey!!" glow
            award heart ri
        "He sure is! For a high-schooler, he seems rather intelligent":
            award heart y
            ri "Sure is! He's at the top of his class for most subjects"
            ri "And his teachers are all very proud of him as well"
            msg ri "I can't express how happy his success makes me ^^"
        "Hmm..I wonder how he can be useful to you.."
            #Mika vibes (?)
            ri "Useful to me? What do you  mean?"
            ri "He's an amazing student and a great help to the R.F.A"
            ri "Most things he does are useful but...it's not the wording I would use"
    ri "I'm sure he'll return with good news later on in the day"
    ri "For now...everyone, please cheer for Yoosung's success! He's sure to make us proud"
    msg ri "And with that...I should take my leave!" ser2
    ri "Hope everyone has an amazing day ahead !"
    ri "Goodbye then!"

    exit chatroom ri

    return 

label day_4_chatroom_3_expired():

    $ ri.status = "Nature accepts all with its giving hands.."
    $ y.status = "Wish me luck everyone!"

    scene morning
    play music the_way_home

    enter chatroom ri

    msg ri "Hello everyone!" glow
    msg ri "What a fine morning. Can't wait to head out for the day! ^^" ser2
    msg ri "The sky is a nice blue where I am" glow
    msg ri "I'd love to share the view with you guys" curly
    msg ri "Even the passerby I see outside my window seem to be in a good mood" glow
    i "And those guys are almost always frowning ^^;;;"
    ri "Before I continue.."
    msg ri "I feel like I should apologize for what happened last night ;;" 
    msg ri "It was pretty rude of me to suddenly barge into the chatroom like that" ser1
    msg ri "From now on, I'll try to keep stuff like that to a minimum" ser1
    msg ri "Maybe all these new responsibilities regarding the party are getting to me" curly
    ri "Regardless....I shouldn't have allowed you guys to see me like that.."
    ri "From now on, I promise to be the bright and positive Rika you're used to seeing!!"
    ri "To make up for that...I was hoping you'd all tell me what your plans for today were"
    msg ri "So I can help you with them as much as possible" glow
    ri "[name] isn't here but.."
    ri "I feel like [they] [are] the type of person who'd head outside on a day like this"
    msg ri "That's a compliment, of course ^^" glow
    ri "Hmm...Now I'm curious about the other members"
    ri I guess I'll have to wait until one of you guys shows up.."
    pause 1.0*5

    enter chatroom y

    ri "Oh, hello there Yoosung! So good to see you!"
    ri "Wait...isn't today the day?"
    msg y "You don't need to remind me"  sigh_m
    y "It's all that's on my mind"
    y "So I came here to try and  blow off some steam"
    ri "Of course!! I think I'd feel the same way"
    ri "The entrance exam has probably gotten a lot harder since I took it"
    msg y "Your score was really impressive! Can't believe you didn't end up enrolling" ser1
    ri "Hmm..I had a lot on my plate at the time, so it wasn't really a possibility"
    msg ri "However..Thanks to that, the R.F.A came into existence ! So all is well! glow
    ri "The day I took the exam sure was a hectic one..Wasn't nearly as sunny out as it is now"
    ri "I suppose you'd rather we switch the subject away from that though ^^;;"
    y "...yes please ;;"
    y "Yesterday was really tough, since I spent most of the day studying"
    msg y "And today,  when I finally went out on a walk..." curly
    msg y "The world seemed to be laughing at me" sigh_m
    y "The sun was beginning to rise, and even saw a few flowers blooming"
    msg ri "That sounds beautiful.." glow
    y "Yeah, it was. You'd probably appreciate it more. I know how much you like plants"
    ri " Oh yes! But back when I started out, my first plants always looked a bit sad and droopy"
    y "Now you're a real green-thumb All the photos you send of them look really good "
    y " Me however...I prefer animals to plants."
    msg ri "I think both are equally as important and beautiful! " glow
    ri "A world without one or the other doesn't sound too good..."
    y "Umm...Do you have a favorite plant or flower?"
    msg y "(Trying really hard not to think of the impending doom that awaits me)" sigh_m
    msg ri "I appreciate the effort ^^" glow
    ri "Hmm..never thought about that.."
    ri "If I had to pick, I guess I'd choose daffodils!"
    y "Any particular reason for picking those?"
    pause 1.0*3
    play music mint_eye_piano
    ri "Well...they wake up at the first signs of spring, stretching their heads towards the sky and breaking through the snow"
    ri "Then they bloom in a brilliant flash of yellow, proudly towering above its icy prison"
    ri "Swaying in the breeze, it spends its youthful days filled with happiness"
    msg ri "But then.."  curly
    ri "It begins to wither, slowly but surely. It retracts from the outside world and spends its days in  solitude before departing the world"
    msg ri "I find its story inspiring..." glow 
    pause 1.0*3
    ri "...Did I say something weird? ;;"
    y "Sorry for not saying anything."
    y "I just wasn't really able to understand what you were getting at"
    msg y "You sounded very serious. I was kind of taken aback" ser1
    ri "Oh...Is that so?"
    ri "Ah, I said I'd be more careful about saying stuff like that in the chatroom earlier and yet"
    msg ri "Seems like I messed up again.." ser2
    y "I didn't want to comment on that but...it WAS very unlike you"
    y "But don't worry, you didn't mess up or anything"
    msg y "Just didn't seem like the you I know" bold
    ri "....I guess I did break my promise to be more positive here"
    y "It doesn't matter Rika! We all know how bright and positive you always are"
    y "You inspire me to be a better person just be existing . That's a pretty amazing thing you can do"
    msg ri "Ah, of course...I'm glad to be of help to you" ser1
    ri "But maybe you should try and"
    y "Hmm?"
    ri "Never mind. I'll talk to you about it after you're done with the exam ^^"
    y "Oh no...You just reminded me I still need to check if I have everything ready for that"
    y "I should probably leave now"
    msg ri "You know I'm always cheering for you!" glow
    ri "Go out there and show them all that you can do"
    msg y "Will do Rika!! With you on my side, I know I'll do well!" glow
    y "Goodbye now!!"

    exit chatroom y

    ri "Wow..Can't believe he's already grown up"
    ri "Just a few more months and he'll be ready to start with college"
    ri "It's been quite a ride, but I'm really proud of everything he's accomplished"
    ri "He's done so much better than what everyone around him was expecting"
    msg ri "But I knew he was full of potential the day I first laid my eyes on him" glow
    ri "I'm sure he'll return with good news later on in the day"
    ri "For now...everyone, please cheer for Yoosung's success! He's sure to make us proud"
    msg ri "And with that...I should take my leave!" ser2
    ri "Hope everyone has an amazing day ahead !"
    ri "Goodbye then!"

    exit chatroom ri

    return 
