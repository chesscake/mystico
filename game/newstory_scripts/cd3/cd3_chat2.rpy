label cd3_chat2():
    #Tile: Coordinator Powers

    $ ri.status = "If you need help with the messenger - call me [name]!"
    $ ri.prof_pic = "Profile Pics/Rika/rika-7.jpg"
    $ ri.cover_pic = "Cover Photos/Rika/r5.jpg"

    scene night
    play music looking_for_happiness

    ri "I woke up to the sound of a buzzing phone!"
    msg ri "And what do you know ~ It was Jaehee, telling me the good news about ZEN's musical!!" flower_m ser2
    msg ri "THIS IS BIG" glow
    msg ri "I'M SO EXCITED!" glow
    msg ri "CONGRATULATIONS, ZEN!" blocky cloud_l
    ri "{image=rika_party}" (img=True)
    menu:
        "I'm excited too! Welcome Rika!":
            award heart ri
            ri "Oh, it's you! I'm so glad to see you!"
            ri "Thank you for supporting Zen!"
        "Good evening":
            ri "Good evening to you too!"
            ri "So good seeing you here!"
    ri "No one else seems to be here.."
    msg ri "It's so late...." curly
    ri "Good!!We should all go to sleep earlier!"
    ri "Though..."
    msg ri "not like I'm the best example of that, as I AM currently awake ;;" sigh_l
    ri "You know,"
    ri "it seems so funny how I try to encourage the RFA members to live healthier lives.."
    msg ri "Yet I sometimes ignore my own advice heh" curly
    ri "I suppose that is just my nature"
    ri "When I'm the one dealing out life advice..."
    ri "It just feels easier to ignore it"
    menu:
        "I'll remind you to take breaks then! We all want you safe and healthy!":
            award heart ri
            ri "Oh my...thank you so much"
            ri "I'm thankfull to have someone like you looking over me"
        "Isn't that kind of hypocritical?":
            ri "I guess it is!"
            ri "I just can't help myself"
        "Maybe you and Jaehee could watch out for one another":
            award heart ja
            ri "Oh, I guess we could"
            ri "But I don't want to put that kind of pressure on her, she's already swamped with work"
    ri "However"
    msg ri "I will do my best to stay healthy for the sake of the RFA!" cloud_l ser2 big
    ri "I think each and every one of us should at least try to improve our health"
    ri "Whether it be mental or physical.."
    ri "for the sake of our loved ones"
    ri "Seeing them in pain is the last thing we want to do,"
    ri "so we should be as healthy as possible so they do not worry about us"
    ri "I'd hate to see you guys in pain!"
    ri "I remember one time that Zen got sick after a particularly exhausing play"
    ri "Both Jaehee and I were really worried about him"
    ri "Of course,"
    ri "due to his strong constitution,"
    ri "Somehow, he came out of it better than ever"
    msg ri "But it was scary for all of us" ser2
    ri "I worry that something similar might happen now, with Zen's new musical opportunity underway.."
    msg ri "I don't want to see that happen ever again with anyone of you" ser2 glow
    ri "{image=rika_cry}" (img=True)
    menu:
        "I'll make sure everyone stays healty Rika!":
            award heart ri
            msg ri "Thank you! That would be a huge help to me!" glow
            ri "And I'm sure our members would appreciate it as well"
        "You should be taking better care of them":
            break heart ri
            ri "Ah, sorry..I'm doing my best"
            ri "I hope the members don't think less of me for not being able to help them"
        "Perhaps we could bring in someone to watch over the members":
            award heart va
            ri "Bring someone in? What do you mean?"
            ri "{image=rika_shock}" (img=True)
            ri "I don+t think we neeed anyone else! We're doing well for ourselves hah"
    ri "Anyway..."
    ri "Looking over the logs, it seems like Zen isn't the only busy one"
    ri "So is Yoosung..."
    ri "Who is  busy with his final exam preparation."
    ri "I hope he will try to stay healthy as well"
    ri "Getting into a good school is important but..."
    ri "so is you being healthy!"
    ri "As sad as it makes me to see you guys sick"
    msg ri "you should never hide it from me ~" glow bold
    ri "Besides..."
    ri "I can see what you input into the search feature! *-*"
    ri "In case some of you don't know..."
    ri "It is only a feature available on specific chat accounts"
    ri "I don't believe you have it [name].."
    ri "I remember when we implemented it!"
    ri "It was Luciel's idea originally"
    ri "He suggested it so that our members could browse the internet freely, safe from anything or anyone malicious"
    ri "Well..."
    msg ri "Save for Luciel himself of course~" sigh_m
    ri "Perhaps I should elaborate on the Messengers functions a bit more"
    ri "All registered users  have the status function,"
    ri "as well as the abillity to see other members status messages,"
    ri "profile pictures and banners..."
    ri "But there are certain features only available to certain accounts"
    ri "For example,"
    ri "Jaehees has access to a note-taking app,"
    ri "And Jumins and Zens accounts also make certain features much more easily accesible.."
    msg ri "Don't think Luciel expected them to be able to handle the more complex version of the app the rest of us have" ser1
    ri "Luciels and mine are a bit different , as they act as a sort of control panel for the others!"
    msg ri "Oh, and they have the abillity to change the messengers code at will!" bold
    ri "...I haven't utilised that feature much"
    ri "I just don't have the time these days..."
    msg ri "Especially today, with all the work surrounding Zens Musicals , as well as the guests..."
    menu:
        "Have you considered taking a break? All this work isn't good for you...":
            award heart ri
            ri "You're always so considerate!"
            ri "I'm fine, don't worry about me!"
            ri "I'm sure the others have it harder than I do..."
        "I feel like the others are busier than you":
            ri "That might be the case..."
            ri "Everyone has their own struggles..."
            ri "And theirs are probably worse than mine"
        "I wonder what that musical will be like":
            award heart z
            ri "I'm curious too! I can't wait to see what comes of it!"
            ri "Maybe I should read the comic it's based on in the meantime"
    ri "I'd like to make a proposal!"
    msg ri "If any of the members see this,"  ser2
    msg ri "Feel free to suggest any features you want in!" ser1
    msg ri "Of course, the floor is open to you too [name] " cloud_l big bold
    msg ri "Just make sure to discuss it with me first, Ok?" ser1 glow
    ri "What would you like to see?"
    ri "I will inform Luciel,"
    ri "and I am sure he could eventually make it work, whatever it is..."
    msg ri "*Yawn...*" curly
    msg ri "I'm getting sleepier by the minute" curly
    ri "I should make some tea for myself and get ready for bed..."
    menu:
        "I'm glad you're taking care of yourself":
            award heart ri
            ri "You're so kind..thank you"
            ri "I'll try to keep myself healthy then"
        "Good night.":
            ri "^^"
    ri "I can't wait to see you in person soon [name]..."
    ri "Goodbye then!"
    ri "And good night!"

    return


label day_3_chatroom_2_expired():

    $ ri.status = "If you need help with the messenger - call me [name]!"
    $ ri.prof_pic = "Profile Pics/Rika/rika-7.jpg"
    $ ri.cover_pic = "Cover Photos/Rika/r5.jpg"

    scene night
    play music looking_for_happiness

    ri "I woke up to the sound of a buzzing phone!"
    msg ri "And what do you know ~ It was Jaehee, telling me the good news about ZEN's musical!!" flower_m ser2
    msg ri "THIS IS BIG" glow
    msg ri "I'M SO EXCITED!" glow
    msg ri "CONGRATULATIONS, ZEN!" blocky cloud_l
    ri "{image=rika_party}" (img=True)
    msg ri "It's so late...." curly
    ri "It seems like no one else is awake..."
    ri "Good! We should all go to sleep earlier!"
    ri "Though..."
    msg ri "not like I'm the best example of that, as I AM currently awake ;;" sigh_l
    ri "You know,"
    ri "it seems so funny how I try to encourage the RFA members to live healthier lives.."
    msg ri "Yet I sometimes ignore my own advice heh" curly
    ri "I suppose that is just my nature"
    ri "When I'm the one dealing out life advice..."
    ri "It just feels easier to ignore it"
    ri "However"
    msg ri "I will do my best to stay healthy for the sake of the RFA!" cloud_l ser2 big
    ri "I think each and every one of us should at least try to improve our health"
    ri "Whether it be mental or physical.."
    ri "for the sake of our loved ones"
    ri "Seeing them in pain is the last thing we want to do,"
    ri "so we should be as healthy as possible so they do not worry about us"
    ri "I'd hate to see you guys in pain!"
    ri "I remember one time that Zen got sick after a particularly exhausing play"
    ri "Both Jaehee and I were really worried about him"
    ri "Of course,"
    ri "due to his strong constitution,"
    ri "Somehow, he came out of it better than ever"
    msg ri "But it was scary for all of us" ser2
    ri "I worry that something similar might happen now, with Zen's new musical opportunity underway.."
    msg ri "I don't want to see that happen ever again with anyone of you" ser2 glow
    ri "{image=rika_cry}" (img=True)
    ri "Looking over the logs, it seems like Zen isn't the only busy one"
    ri "So is Yoosung..."
    ri "Who is  busy with his final exam preparation."
    ri "I hope he will try to stay healthy as well"
    ri "Getting into a good school is important but..."
    ri "so is you being healthy!"
    ri "As sad as it makes me to see you guys sick"
    msg ri "you should never hide it from me ~" glow bold
    ri "Besides..."
    ri "I can see what you input into the search feature! *-*"
    ri "In case some of you don't know..."
    ri "It is only a feature available on specific chat accounts"
    ri "I don't believe [name] has it..."
    ri "I remember when we implemented it!"
    ri "It was Luciel's idea originally"
    ri "He suggested it so that our members could browse the internet freely, safe from anything or anyone malicious"
    ri "Well..."
    msg ri "Save for Luciel himself of course~" sigh_m
    ri "Perhaps I should elaborate on the Messengers functions a bit more"
    ri "All registered users  have the status function,"
    ri "as well as the abillity to see other members status messages,"
    ri "profile pictures and banners..."
    ri "But there are certain features only available to certain accounts"
    ri "For example,"
    ri "Jaehees has access to a note-taking app,"
    ri "And Jumins and Zens accounts also make certain features much more easily accesible.."
    msg ri "Don't think Luciel expected them to be able to handle the more complex version of the app the rest of us have" ser1
    ri "Luciels and mine are a bit different , as they act as a sort of control panel for the others!"
    msg ri "Oh, and they have the abillity to change the messengers code at will!" bold
    ri "...I haven't utilised that feature much"
    ri "I just don't have the time these days..."
    msg ri "Especially today, with all the work surrounding Zens Musicals , as well as the guests..."
    ri "However..."
    msg ri "If any of the members see this,"  ser2
    msg ri "Feel free to suggest any features you want in!" ser1
    msg ri "Of course, the floor is open to you too [name] " cloud_l big bold
    msg ri "Just make sure to discuss it with me first, Ok?" ser1 glow
    ri "What would you like to see?"
    ri "I will inform Luciel,"
    ri "and I am sure he could eventually make it work, whatever it is..."
    msg ri "*Yawn...*" curly
    msg ri "I'm getting sleepier by the minute" curly
    ri "I should make some tea for myself and get ready for bed..."
    ri "I can't wait to see you in person soon [name]..."
    ri "Goodbye then!"
    ri "And good night!"

    return
