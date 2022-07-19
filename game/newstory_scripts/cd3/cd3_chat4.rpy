label cd3_chat4():
    #source of my inspiration

    $ ri.status = "A never ending fairy tale...I'm not sure if I want to experience such a thing"
    $ ri.cover_pic = "Cover Photos/Rika/r3a.jpg"
    $ ri.profile_pic = "Profile Photos/Rika/r3a.jpg"
    $ v.status = "How wonderful it would be to live in a world where good always wins"

    scene noon
    play music the_way_home

    enter chatroom ri

    ri "Oh my...yet another busy day is ahead of us"
    ri "Say, [name], how are you holding up?"
    menu:
        "I'm feeling great Rika! Can't wait to see what the day has to offer!":
            award heart ri
            msg ri "Oh my, you sure are eager today" glow
            ri "That's lovely to see! I hope you start every day as chipper as you are now"
            msg ri "I hope the rest of the members are feeling as good as you are" spike_s
        "I'm okay. Just as usual":
            msg ri "Ah, I hope I'm not repeating myself too much ^^;;" sigh_s
            ri "Glad to hear that you are doing okay."
            ri "I wonder how everyone else is feeling.."
        "My day started off kind of bad":
             msg ri "Sorry to hear that!!" ser1
             ri "I hope I can make it just that much better for you!"
             ri "Please stay healthy and happy everyone.."
    ri "Speaking about the members.."
    ri "I just realized I missed out on talking about musicals with Zen"
    msg ri "Guess I was too tired to think about that last night..."
    msg ri "I've been dying to talk about my thoughts on quite a few of them!" glow
    ri "What a shame..."
    ri "Zen is one us, and yet we barely get to discuss stuff like that"
    ri "Things can get...hectic around here"
    ri "Say..."
    menu:
        "Maybe you could discuss stuff like that with the others":
            ri "Yeah, maybe I could...I know for sure Jaehee is interested in some of the same stuff I am"
            ri "She may not look it, but she's a real sweetheart!"
            ri "However, I wouldn't want to burden her even more..."
            ri "Seven and Jumin are busy as always"
            ri "And Yoosung has his own issues to deal with..I suppose that leaves just the two of us !"
        "I'd love it if you would discuss it with me!":
            award heart ri
            msg ri "...Oh wow, that's exactly what I was about to suggest!" curly
            msg ri "You almost read my mind! That's impressive heh!" glow
            ri "I'd love to discuss musicals with you!"
            ri "In fact, I almost can't believe we haven't had the chance to do so yet!"
            msg ri "Get ready...I can get a bit too...passionate, at times " sigh_m
        "I'd prefer it if we stick to the real world. Musicals bore me":
            ri "That's...I understand! You must be busy"
            ri "I'm sorry for taking up your time , that wasn't my intention..."
            ri "I'll try to be brief and..."
            ri "If you get bored, feel free to leave at any time.."
            ri "Musicals aren't for everyone..."
    ri "So...I wanted to talk about my thoughts on one of the musicals in particular..."
    ri "The Kingdom of Evolution...I remember watching it and being awestruck"
    msg ri "Every actor played the role they were given perfectly" ser1
    ri "They all worked as one unit to bring the story to life, and they succeeded!"
    ri "I was transported to another world, with entirely different rules..."
    ri "Where the existance of magical princes and princesses was commonplace"
    msg ri "It's like I was really there...on the carnation-decked balconies, climbing the spyraling staircases and being carried by the winds of time" glow
    ri "What would you do if you got the chance to visit such a place?"
    menu:
        "I'd love visit a world like that for a day or two":
            award heart ri
            msg ri "I would too!" glow
            ri "Could you imagine all the adventures you could have ?"
            ri "Just thinking about it is making me excited..."
        "I wouldn't go. Fantasy can never compare to reality":
            award heart va
            ri "I suppose you're right, in a way"
            ri "The world trapped within the confines of that theater never truly existed"
            ri "....but I feel we can still learn a lot from it anyway"
        "I prefer to experience stuff like that through fiction than in real life":
            ri "That's an interesting take on it!"
            ri "Some things are just better experienced first hand however"
            ri "Though it's not like you could do that in this case"
    msg ri "As for me...I'd take the opportunity in a heartbeat" curly
    ri "However... think I'd eventually want to leave the fairy tale world, no matter how much fun I was having there"
    ri "Being separated from all my friends would make a wonderful dream into a cruel nightmare in the blink of an eye"
    msg ri "...I don't even want to imagine something like that happening" sigh_m
    ri "It seems I've steered a bit too far from the topic at hand... um.."
    ri "Back to what I was saying..."
    ri "Though the world of the story was captivating enough, the characters stick out in my mind too"
    ri "There was the  prince..."
    ri "And the two princesses, whose differences the story  focused on"
    ri "Though both were protagonists, they were very different - even the types of birds they could turn into differed"
    ri "The swallow princess - Anne, did her best to help the people of the world who suffered under the burden of poverty and pestilance"
    ri "While her friend Helena was madly in love with the prince, and doted on him every day on their walks through the castle"
    ri "The prince wasn't much of a character until the end...the story mainly focused on how he affected those around him"
    ri "The main conflict of the story was between Anne and Helena and their different views on the world"
    ri "Helena used her magic to entertain - a type of magic that didn't require much energy"
    ri "Annes magic was much different - it could help the people of the world, either by healing them or by creating whatever it is they needed"
    ri "That came at a price - a fragment of whatever it is that was being given out needed to be taken from somewhere else"
    ri "After Anne had given up most of what she had, she turned to the prince, and began dividing his fortune amongst the people of the world"
    ri "Though the prince suffered, the people prospered"
    ri "That is, until Helena broke Annes spell and set the prince free..."
    ri "Ah, I'm rambling...Say...Which of the characters do you like the most?"
    menu:
        "Annes approach is very noble...I like her the most":
            award heart ri
            ri "Oh my, I was just about to say that!"
            ri "You know..right after the musical had finished, I noticed her actress standing all alone in the corner of the stage"
            ri "No one had approached her or wanted to take a photo with her"
            msg ri "My heart broke at the sight of her..I made sure to take a ton of photos as soon as I got to her" glow
            msg ri "Other people don't seem to like her character as much as I do..." ser1
        "Helenas heroism is what saved the prince. I like her the most":
            ri "Helena is a great character as well! Though I don't really like the shift her character took at the end..."
            ri "Thinking back...her actress had to stay late and take photos with most of the audience members.."
            ri "I guess a lot of other people share your sentiment!"
        "The prince was the most righteous. He is my favorite":
            award heart v
            ri "Ah yes, the prince..."
            ri "After the show had premiered, fan blogs were filled with people who gushed about his good looks"
            ri "Due to his immense popularity, Zen was able to get a much better manager and a ton of new opportunities"
    ri "I know that all of the characters are important to the story..."
    ri "But Anne just had something about her that drew me to her"
    ri "I wish I could plainly explain what that something is but..."
    msg ri "I've been blanking on an answer for months" curly
    ri "Someting about the way she courageously and unabashedly attempted to bring the world happiness just...speaks to me"
    ri "Such a shame it all had to end.."
    ri "You see, at the end of the play, Anne is banished from the land , and Helena and the prince get together"
    ri "Critics were calling it the 'perfect end to a story filled with intrigue and romance' "
    ri "Sadly, I don't neccesarily agree with that conclusion.."
    ri "The story wasn't romantic at all..not until the very end that is"
    ri "And one of the main characters not getting to experince the happiness the others do? That's just unfair.."
    msg ri "Tell me...what do you think of this ending?" glow
    enter chatroom v
    v "Hello there. Did I interrupt anything?"
    ri "Um....Not really, I just wanted to ask [name] about her thoughts on something."
    v "I see you two are having a discussion about one of Zens old musicals"
    v "You know [name], Rika and I had  always had a love for the arts "
    v "Though our opinons on it have differed a lot over the years"
    v "One such example is this particular musical"
    v "Rika has always had a ...unique way of looking at things"
    v "What do you think of her assesment of the piece?"
    ri "Yeah, that's exactly what I wanted to ask [them]..."
    v "Is it? I didn't read the full chat log yet"
    ri "That's alright....What's on your mind [name]? ^^"
    menu:
        "I agree with Rika...I wish Anne got a better ending":
            award heart ri
            msg ri "Oh wow...Thank you !" glow
            ri "I just knew we'd agreee on this! So glad to have been proven right!"
            v "I guess you two are growing closer and closer these days"
            menu:
                "Rika has  been a huge help in getting me started in the R.F.A!":
                    award heart ri
                    ri "You're too kind..."
                    ri "But thank you, I really appreciate that!"
                    ri "It's as if you always know just what to say to!"
                    award heart ri
                "I'm just doing my job":
                    ri "Ah yes..."
                    ri "I hope the work you do for the R.F.A isn't too burdensome"
                    v "That might be the case. After all, [name] isn't exactly experienced with party coordination"
                    ri "..."
        "I think the ending fits the themes of the musical perfectly":
            award heart v
            v "I understand why you'd think that"
            v "Your opinion is one backed up by a lot of famous critics"
            ri "I see...thank you for answering"
    ri "You've been a great help in me settling my thoughts on this whole thing"
    msg v "You're welcome Rika" glow
    stop music
    msg ri "I was talking to [name], but...I suppose I should thank you too V" sigh_m
    ri "What else do you guys want to talk about ?"
    v "Perhaps you should take a rest Rika. You seem a bit tense"
    ri "I'm fine V. I'm just trying to make some more small talk with [name] "
    v "If that's what you want, I won't stop you"
    v "I just thought you seemed a bit on edge is all"
    pause 1.0*5
    msg v "Do you have anything you want to say?" bold
    msg ri "Oh no, I just...got lost in thought...and..." curly
    pause 1.0*5
    ri "Um...I think I have to go on a grocery run...See you guys soon!"
    msg ri "Goodbye [name], thank you for sharing your thoughts with me!" cloud_m
    exit chatroom ri
    menu:
        "I hope she's alright..I wanted to talk to her more..":
            award heart ri
            v "I'm sure she is. Rika gets like this from time to time"
            v "Though I'm usually there to help her get over it"
            v "You don't have to worry about it"
        "That was weird. She left so abruptly":
            v "Yes, she did. Such a shame"
            v "It might be a good thing. She was getting a bit worked up over the musical it seems"
            msg v "I hope the things you discussed didn't upset her" bold
    v "Oh well...I'll try calling her later to see how she's doing"
    v "Back to the subject at hand.."
    v "That musical. I remember Zen taking me to the rehersal back when  he was practicing his lines"
    v "He really wanted to get inspiration for the prince role, and said I was a perfect fit"
    msg v "I was honored, even if it meant getting yelled at by his director" glow
    v "The prince seemed like a charming fellow. He and Helena had a great bond"
    v "I wonder why Rika disagrees.."
    v "Look at the time. It seems I'm running late to my next shoot. See you then."
    exit chatroom v

    return


label day_3_chatroom_4_expired():

    $ ri.status = "A never ending fairy tale...I'm not sure if I want to experience such a thing"
    $ ri.cover_pic = "Cover Photos/Rika/r3a.jpg"
    $ ri.profile_pic = "Profile Photos/Rika/r3a.jpg"
    $ v.status = "How wonderful it would be to live in a world where good always wins"

    scene noon
    play music the_way_home

    enter chatroom ri

    ri "Oh my...yet another busy day is ahead of us"
    ri "Please stay healthy and happy everyone.."
    ri "Speaking about the members.."
    ri "I just realized I missed out on talking about musicals with Zen"
    msg ri "Guess I was too tired to think about that last night..." sigh_m
    msg ri "I've been dying to talk about my thoughts on quite a few of them!" glow
    ri "What a shame..."
    ri "Zen is one us, and yet we barely get to discuss stuff like that"
    ri "Things can get...hectic around here"
    ri "There's no one else in here but.."
    ri "I guess I'll leave my thoughts here anyway"
    ri "I'll try to be brief and..."
    ri "If you guys get bored, feel free to skim through it.."
    ri "I know musicals aren't for everyone..."
    ri "So...I wanted to talk about my thoughts on one of the musicals in particular..."
    ri "The Kingdom of Evolution...I remember watching it a few months back and being awestruck by it"
    msg ri "Every actor played the role they were given perfectly" ser1
    ri "They all worked as one unit to bring the story to life, and they succeeded!"
    ri "I was transported to another world, with entirely different rules..."
    ri "Where the existance of magical princes and princesses was commonplace"
    ri "It's like I was really there...on the carnation-decked balconies, climbing the spyraling staircases and being carried by the winds of time"
    ri "Could you imagine all the adventures you could have ?"
    ri "Just thinking about it is making me excited..."
    ri "However... think I'd eventually want to leave the fairy tale world, no matter how much fun I was having there"
    ri "Being separated from all my friends would make a wonderful dream into a cruel nightmare in the blink of an eye"
    msg ri "...I don't even want to imagine something like that happening" sigh_m
    ri "It seems I've steered a bit too far from the topic at hand... um.."
    ri "Back to what I was saying..."
    ri "Though the world of the story was captivating enough, the characters stick out in my mind too"
    ri "There was the  prince..."
    ri "And the two princesses, whose differences the story  focused on"
    ri "Though both were protagonists, they were very different - even the types of birds they could turn into differed"
    ri "The swallow princess - Anne, did her best to help the people of the world who suffered under the burden of poverty and pestilance"
    ri "While her friend Helena was madly in love with the prince, and doted on him every day on their walks through the castle"
    ri "The prince wasn't much of a character until the end...the story mainly focused on how he affected those around him"
    ri "The main conflict of the story was between Anne and Helena and their different views on the world"
    ri "Helena used her magic to entertain - a type of magic that didn't require much energy"
    ri "Annes magic was much different - it could help the people of the world, either by healing them or by creating whatever it is they needed"
    ri "That came at a price - a fragment of whatever it is that was being given out needed to be taken from somewhere else"
    ri "After Anne had given up most of what she had, she turned to the prince, and began dividing his fortune amongst the people of the world"
    ri "Though the prince suffered, the people prospered"
    ri "That is, until Helena broke Annes spell and set the prince free..."
    ri "Speaking of Anne.."
    ri "Right after the musical had finished, I noticed her actress standing all alone in the corner of the stage"
    ri "No one had approached her or wanted to take a photo with her"
    msg ri "My heart broke at the sight of her..I made sure to take a ton of photos as soon as I got to her" glow
    msg ri "Other people don't seem to like her character as much as I do..." ser1
    ri "I know that all of the characters are important to the story..."
    ri "But Anne just had something about her that drew me to her"
    ri "I wish I could plainly explain what that something is but..."
    msg ri "I've been blanking on an answer for months" curly
    ri "Someting about the way she courageously and unabashedly attempted to bring the world happiness just...speaks to me"
    ri "Such a shame it all had to end.."
    ri "You see, at the end of the play, Anne is banished from the land , and Helena and the prince get together"
    ri "Critics were calling it the 'perfect end to a story filled with intrigue and romance' "
    ri "Sadly, I don't neccesarily agree with that conclusion.."
    ri "The story wasn't romantic at all..not until the very end that is"
    ri "And one of the main characters not getting to experince the happiness the others do? That's just unfair.."
    enter chatroom v
    v "Hello there. Did I interrupt anything?"
    ri "Um....Not really, I was just"
    v  "You were talking  about one of Zens old musicals?"
    v "You and I had  always had a love for the arts "
    v "Though our opinons on it have differed a lot over the years"
    v "One such example is this particular musical"
    v "You always had a ...unique way of looking at things"
    v "Most people seemed to believe that it had a fitting end to it"
    v "It is the opinion backed up by a lot of famous critics"
    ri "Yes I'm aware..."
    ri "Doesn't mean I agree with it though.."
    ri "What else do you  want to talk about ?"
    v "Perhaps you should take a rest Rika. You seem a bit tense"
    ri "I'm fine V. I really am"
    v "I just thought you seemed a bit on edge is all"
    pause 1.0*5
    msg v "Do you have anything you want to say?" bold
    msg ri "Oh no, I just...got lost in thought...and..." curly
    pause 1.0*5
    ri "Um...I think I have to go on a grocery run...See you soon!"
    exit chatroom ri
    v "..."
    v "Nothing to worry about guys. Rika gets like this from time to time"
    v "Though I'm usually there to help her get over it"
    v "You don't have to worry about it"
    v "Oh well...I'll try calling her later to see how she's doing"
    v "Back to the subject at hand.."
    v "That musical. I remember Zen taking me to the rehersal back when  he was practicing his lines"
    v "He really wanted to get inspiration for the prince role, and said I was a perfect fit"
    msg v "I was honored, even if it meant getting yelled at by his director" glow
    v "The prince seemed like a charming fellow. He and Helena had a great bond"
    v "I wonder why Rika disagrees.."
    v "Look at the time. It seems I'm running late to my next shoot. Enough small talk for the day I suppose"
    exit chatroom v

    return

    label after_cd3_chat4:

    compose text ri:
        ri "Sorry for leaving so suddenly..."
        ri "Hope I didn't offend you , as that wasn't my intention"
        ri "Did you enjoy our chat?"
        label reply_musical

    return

label reply_musical:
    menu:
        "I did! I hope you're feeling okay":
            award heart ri
            ri "Oh yes, I am! Especially after your reply"
            ri "I hope the two of us can continue having these conversations long into the future"
        "I was a bit bored until V showed up honestly":
            ri "That's...I'll try talking about something more interesting next time"
            ri "I'm sorry..."
    ri "I hope our next interaction will be a pleasent one"

    return

label cd3_chat4_vn_z():
     
     
    scene hallway

     "" "A year ago.."
     
    "Director" "Is everyone ready to begin?"
    "Actor1" "Where is our prince? Is he still not here? He should have been here hours ago.."
    "Director" "I have to say I did expect more from someone employed by our production company... What could be holding him up?"
    pause
    play sound door_open_sfx

    show zen front happy at vn_right with ease
    play music narcissistic_jazz
    z "Hello everyone! Sorry for  not being here on time!"
    z "I had some trouble on the way here."
    "Actor2" "Well, that isn't a very good excuse... The rest of us showed up on time..."
    show zen front upset
    "Director" "Sigh..It's not that big of a deal... Why aren't you in your costume?"
    show zen front neutral
    z "Ah, about that..."
    show cg v_1
    z "I decided to bring a very good friend of mine along. He reminded me of the character , so I thought I'd bring him over as an inspiration."
    "Actor1" "He did what?? "
    "Director" "Unauthorized personnel aren't allowed to attend rehearsal. I'd have to ask your friend to leave."
    z "Please don't! I'm the one who invited him here.I just thought he'd be of great help to us! He's an artist himself, and his works are known all around the world."
    v "I can leave if it's too much of a bother. I understand that I'm somewhat of an intruder here."
    "Director" "You couldn't have known, Hyun should have told you about it. Listen Hyun, just don't make a habit out of doing stuff like this okay? This is a serious production we are running here."
    scene hallway
    show zen front worried
    z "Of course! I'll make sure to notify you before I invite any other guests."
    "Director" "I'd prefer if you didn't do it at all, but I guess it can't be helped now."
    "Actor1" "I can't believe he's getting off scot-free.."
    "Actor2" "I know right? Everyone else is giving it their all, and he's getting by with his looks!"
    show zen front upset
    "Director" "Everyone, get into positions...Today we'll be going over the final scene. You should all have your lines memorized by now!"
    "Director" "Our guest can stand over there near the prop table."
    v "Alright then. I'll try to make myself more useful. Do you mind me snapping a few pictures?"
    "Director" "Not until the musical is officially released, no. Just having you here is a liability."
    v "Ah, I understand. I apologize"
    z "Come on, get it together Hyun..."
    "Director" "What was that? Did you say anything?"
    show zen front happy
    z "Ah, no sir, I didn't. I'll get into character now!"
    "Director" "What's with you today? No matter.. We don't have time for this!"
    "Director" "Begin scene - The vanquishing of the witch!"

    pause
    scene arena
    play music mint_eye_piano
    "Actress1" "Now all has been revealed ! The prince you were after for so long was nothing but a mirage."
    "Actress2" "That can't be true... He has to be real! My prince, my savior... I would have never been here if it weren't for him."
    "Actress1" "Can't you see you were fooled? He only wanted you here to take advantage of you and your power! I tried to warn you, but you wouldn't  listen."
    "Actress1" "I hate princesses who just cry and wait.. You could have done so much more if it hadn't been for your sttuborn belief in your prince."
    "Actress2" "You're just bitter aren't you? That the prince didn't choose you? I was his choice all along, because I believed in him!"
    "Actress1" "Can't you see that bickering like this is exactly what he wants? If we're the ones fighting, nothing is stopping him from taking the power that lie beyond the gate of time!"
    "Actress2" "Who's to say you're not about to do the same! You're a witch after all. "
    "Actress1" "Does our friendship mean nothing to you anymore? Tell me Helena, is that what we've come to?"
    "Actress2" "Our friendship ended the moment you betrayed my prince!  Now you need to be banished from this land. Dear prince, come and save me from this wicked witch!"
    "Actress1" "I see now that our friendship  was a mere illusion, just like your darling prince..."
    play music dark_secret
    show zen side angry at vn_right with moveinleft
    z "When the heart of a lady calls for me , I appear! I have been reborn Helena! Come to me."
    "Actress2" "Oh my sweet prince...I've always believed in you... Take me away."
    show zen side wink
    z "Of course my love! But first..."
    show zen side upset
    z "The witch must be vanquished from this world once and for all!"
    "Narrator" "And so the witch dissapeared in a cloud of smoke, never to be seen again..."
    stop music
    pause
    play music narcissistic_jazz
    "Director" "Great work everyone. That wraps up practice for today. I will see you all tommorow"
    show zen front happy
    z "Great! Thank you ! I'll take my leave then. Let's go V!"
    v "Alright Hyun. Thank you for this experience. It's been very insightfull."
    z "Goodbye everyone! Have a great rest of your week!"
    "Actor1" "Wow...I can't deny that the guy is talented..."
    "Actor2" "I know right? I'd hate to have to audition for the same role as him"
    "Actor1" "Shame he's so unprofessional...I mean seriously? Bringing a rando to something like this?"
    "Actor2" "I know right? That guy he brought along was kind of a weirdo don't you think? Did you see how he kept texting someone all throughout our set?"
    "Actor1" "Looked pretty normal to me. Didn't really pay much attention to him. Now get on with it, we need to clean up and get out of here"
    
    return
