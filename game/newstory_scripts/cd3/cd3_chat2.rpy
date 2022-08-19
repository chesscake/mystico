label cd3_chat2():
    #Tile: Coordinator Powers

    $ ri.status = "If you need help with the messenger - call me [name]!"
    $ ri.prof_pic = "Profile Pics/Rika/rika-7.jpg"
    $ ri.cover_pic = "Cover Photos/Rika/r5.jpg"

    scene night
    play music looking_for_happiness

    ri "I woke up to the sound of a buzzing phone!"
    msg ri "And what do you know ~ It was Jaehee, telling me all about the good news about ZEN's musical!!" flower_m ser2
    msg ri "THIS IS BIG" glow
    msg ri "I'm really excited!!" glow
    msg ri "I never thought I'd get to see that musical again" blocky cloud_l
    ri "{image=rika_party}" (img=True)
    menu:
        "Hello Rika! I'm excited as well ~":
            award heart ri
            ri "Oh, it's you! I'm so glad to see you!"
            ri "Thank you for supporting Zen!"
        "Good evening":
            ri "Good evening to you too!"
            ri "Glad to see you here!"
    ri "No one else seems to be here.."
    msg ri "It's late...." curly
    ri "Good!! We should sleep earlier!"
    ri "Though..."
    msg ri "not like I'm the best example of that, as I AM currently awake ;;" sigh_l
    ri "You know,"
    ri "it's ironic how I try to encourage the RFA members to live healthier lives.."
    msg ri "Yet sometimes I ignore my own advice hah..." curly
    ri "I suppose that is simply my nature"
    ri "When I'm the one giving out life advice..."
    ri "It's easier to ignore it"
    menu:
        "I'll remind you to take breaks then. We all want you safe and healthy!":
            award heart ri
            ri "Oh my...thank you so much"
            ri "I'm greatful to have someone like you looking over me"
        "Maybe Jaehee and you could watch out for one another":
            award heart ja
            ri "Oh, I guess we could"
            ri "But I don't want to put that kind of pressure on her, she's already swamped with work"
    ri "However"
    msg ri "I will do my best to stay healthy for the sake of the RFA!" cloud_l ser2 big
    ri "I think all of us should try to improve our health"
    ri "Whether it be mental or physical.."
    ri "for the sake of those close to us."
    ri "Seeing them in pain is the last thing we wish to happen,"
    ri "so we should be as healthy as possible, to rid them of those sorts of concerns."
    ri "I would hate to see you guys in pain!"
    msg ri "Talking about all this reminded me of something.." curly
    ri "One time, Zen got sick after a particularly exhausting play"
    ri "Both Jaehee and I were really worried about him"
    ri "Of course,"
    ri "due to his amazing recovery rate,"
    ri "He somehow came out of it better than ever"
    msg ri "However...that was still a scary time for us all" ser2
    msg ri "You never really get used to those around you being in pain..." sigh_m
    ri "I worry that a similar incident might happen now with Zen's new musical opportunity underway..."
    msg ri "It might be a long time before that musical happens but..."
    msg ri "I don't want to see something like that happen ever again." ser2 glow
    ri "{image=rika_cry}" (img=True)
    menu:
        "I'll make sure everyone stays healthy Rika!":
            award heart ri
            msg ri "Thank you! That would be a huge help to me!" glow
            ri "And I'm sure our members will appreciate it as well"
        "You should be taking better care of them":
            break heart ri
            ri "Ah, sorry..I am trying my best"
            ri "I hope the members don't think less of me for not being able to help them properly."
        "Perhaps we could bring in someone to watch over the members":
            award heart va
            ri "Bring someone in? What do you mean?"
            ri "{image=rika_shock}" (img=True)
            ri "I don't think we need anyone else! We're doing well by ourselves already."
    ri "Anyway..."
    ri "Looking over the logs, it seems like Zen isn't the only busy one"
    ri "Yoosung..."
    ri "He's got his hands full with his final exam preparation."
    ri "I hope he manages to pull through alright.."
    ri "Wouldn't want his stress to get to him"
    ri "Getting into a good school is important but..."
    ri "so is being healthy."
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
    msg ri "Save for Luciel himself of course." sigh_m
    ri "Perhaps, I should elaborate on the Messengers functions a bit more"
    ri "I know I've already talked about some of them  before, but never gave the full details..."
    ri "All registered users have the status function,"
    ri "and the ability to see other members status messages,"
    ri "profile pictures, banners..."
    ri "But there are certain features only available to certain accounts"
    ri "For example,"
    ri "Jaehees has access to a note-taking app,"
    ri "Luciels and mine are a bit different , as they act as a sort of control panel for the others ~"
    msg ri "Oh, and they have the ability to change the messengers code at will!" bold
    ri "...I haven't utilized that feature much"
    ri "I don't have the time to these days..."
    msg ri "Especially today, with all the work surrounding the guests..."
    menu:
        "Have you considered taking a break? All this work surely isn't good for you...":
            award heart ri
            ri "You're always extremely considerate, but..."
            ri "I'm fine, don't worry about me!"
            ri "The others probably have it harder than I do..."
        "I feel like the others are busier than you":
            ri "That might be the case..."
            ri "Everyone has their own struggles..."
            ri "And theirs are probably worse than mine"
        "I wonder what that musical was like":
            award heart z
            ri "Oh,you're going to love it! We should go and see it together once its back in theaters"
            ri "Maybe I should read the comic it's based on in the meantime"
    ri "I would like to make a proposal!"
    msg ri "If any of the members see this,"  ser2
    msg ri "Feel free to suggest any features you want to see." ser1
    msg ri "Of course, the floor is open to you too [name] " cloud_l big bold
    msg ri "Just make sure to discuss it with me first, ok?" ser1 glow
    ri "What would you like to see?"
    ri "I will inform Luciel,"
    ri "and I am sure he could eventually make it work, whatever it is..."
    msg ri "*Yawn...*" curly
    msg ri "I'm getting sleepier by the minute" curly
    ri "I will go make some tea for myself and get ready for bed..."
    menu:
        "I'm glad you're taking care of yourself":
            award heart ri
            ri "You're so kind..thank you"
            ri "I'll try to keep myself healthy then"
        "Good night.":
            ri "^^"
    ri "I can't wait to see you in person again soon [name]..."
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
    msg ri "And what do you know ~ It was Jaehee, telling me all about the good news about ZEN's musical!!" flower_m ser2
    msg ri "THIS IS BIG" glow
    msg ri "I'm really excited!!" glow
    msg ri "I never thought I'd get to see that musical again" blocky cloud_l
    ri "No one else seems to be here.."
    msg ri "It's late...." curly
    ri "Good!! We should sleep earlier!"
    ri "Though..."
    msg ri "not like I'm the best example of that, as I AM currently awake ;;" sigh_l
    ri "However"
    msg ri "I will do my best to stay healthy for the sake of the RFA!" cloud_l ser2 big
    ri "I think all of us should try to improve our health"
    ri "Whether it be mental or physical.."
    ri "for the sake of those close to us."
    ri "Seeing them in pain is the last thing we wish to happen,"
    ri "so we should be as healthy as possible, to rid them of those sorts of concerns."
    ri "I would hate to see you guys in pain!"
    msg ri "Talking about all this reminded me of something.." curly
    ri "One time, Zen got sick after a particularly exhausting play"
    ri "Both Jaehee and I were really worried about him"
    ri "Of course,"
    ri "due to his amazing recovery rate,"
    ri "He somehow came out of it better than ever"
    msg ri "However...that was still a scary time for us all" ser2
    msg ri "You never really get used to those around you being in pain..." sigh_m
    ri "I worry that a similar incident might happen now with Zen's new musical opportunity underway..."
    msg ri "It might be a long time before that musical happens but..."
    msg ri "I don't want to see something like that happen ever again." ser2 glow
    ri "{image=rika_cry}" (img=True)
    ri "Anyway..."
    ri "Looking over the logs, it seems like Zen isn't the only busy one"
    ri "Yoosung..."
    ri "He's got his hands full with his final exam preparation."
    ri "I hope he manages to pull through alright.."
    ri "Wouldn't want his stress to get to him"
    ri "Getting into a good school is important but..."
    ri "so is being healthy."
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
    msg ri "Save for Luciel himself of course." sigh_m
    ri "Perhaps, I should elaborate on the Messengers functions a bit more"
    ri "I know I've already talked about some of them  before, but never gave the full details..."
    ri "All registered users have the status function,"
    ri "and the ability to see other members status messages,"
    ri "profile pictures, banners..."
    ri "But there are certain features only available to certain accounts"
    ri "For example,"
    ri "Jaehees has access to a note-taking app,"
    ri "Luciels and mine are a bit different , as they act as a sort of control panel for the others ~"
    msg ri "Oh, and they have the ability to change the messengers code at will!" bold
    ri "...I haven't utilized that feature much"
    ri "I don't have the time to these days..."
    msg ri "Especially today, with all the work surrounding the guests..."
    ri "I would like to make a proposal!"
    msg ri "If any of the members see this,"  ser2
    msg ri "Feel free to suggest any features you want to see." ser1
    msg ri "Of course, the floor is open to you too [name] " cloud_l big bold
    msg ri "Just make sure to discuss it with me first, ok?" ser1 glow
    ri "What would you like to see?"
    ri "I will inform Luciel,"
    ri "and I am sure he could eventually make it work, whatever it is..."
    msg ri "*Yawn...*" curly
    msg ri "I'm getting sleepier by the minute" curly
    ri "I will go make some tea for myself and get ready for bed..."
    ri "Goodbye then!"

    return
