label cd4_chat4():
#Wings of change
    $ v.status = "I just can't understand"
    $ ju.status = "Wonder how Elizabeth is doing.."

    scene day
    play music urban_night_cityscape

    msg ju "Hello [name]." ser1
    ju "Good morning. Or rather, afternoon"
    ju "I see Yoosung has headed off for his entrance exam."
    msg ju "Hopefully his results will live up to the expectations I have for him." ser1
    menu:
        "Seems like he would be a good fit for C&R":
            award heart ju
            msg ju "Then we are of the same opinion." round_m
            msg ju "You were able to recognize in the span of these short few days." ser2
            msg ju "That means I have made the right call once more." glow
        "Don't put so much pressure on him ;;":
            award heart y
            msg ju "When did I do that?" ser1
            msg ju "I was commending him for his previous work."  ser1
            msg ju "Whether or not he'll live up to it remains to be seen." glow
    ju "The entrance exam is fairly easy, so I doubt he'll have much trouble with it" 
    msg ju "I was able to pass it without much trouble on my part." ser1
    msg ju "The wait times were a real inconvenience however" sigh_m
    msg ju "Such an exam shouldn't last longer than an hour" glow
    msg ju "That's how long it took me anyway"
    menu:
        "That sounds scary...Not all of us are robots like you Jumin":
            msg ju "Robots? You must be thinking of assistant Kang" square_m
            ju "I am no robot - my suggestion would greatly improve efficiency" 
            msg ju "Maybe I should talk about it to the minister of education over lunch" glow
        "I heard Rika also scored well on the exam!":
            award heart ri
            ju "I've seen her score myself, so I can confirm"
            ju "She did exceptionally well in most subjects, all except for math"
            msg ju "Isn't that strange ? That's the easiest one."
    msg ju "With that out of the way..." curly
    ju "Let us end the talk about the entrance exam here"
    msg ju "Seeing as I'm about to embark on my journey home" glow
    msg ju "I hope Assistant Kang has kept everything exactly how I instructed her to" ser2

    enter chatroom v

    msg ju "I would hate for my darling Elizabeth to be feeling unwell when I'm away" glow
    ju "She's so sensitive to my absence...I can't help but worry"
    msg ju "{image=jumin_sad}" (img=True)
    v "I'm sure Elizabeth is feeling alright Jumin"
    msg v "{image=v_well}" (img=True)
    ju "Strange of you to assume such a thing. You never know what might happen"
    v "She's doted on constantly by your employees. I made sure to confirm that"
    msg ju "Of course. Wouldn't expect less from you" glow
    msg ju "You have your own worries as well." ser1
    msg ju "Have you checked up on Rika? I'm sure you saw her messages from earlier" curly
    v "I haven't yet. She should really try calling me first before things go awry"
    v "Instead of immediately logging onto the messenger"
    menu:
        "It makes sense for her to come here - this is where her friends are":
            award heart ri
            v "You couldn't have known but..."
            v "Rika and I always deal with these kinds of situations in private"
            ju "That's true. However, [name] has a point as well. We all have an interest in keeping Rika healthy"
            msg v "I'm sure you all do. But this is different" glow
        "Yeah, isn't the messenger only supposed to be used for planning parties?":
            ju "If it was, we wouldn't be having this conversation right now"
            msg v "You do have a point there [name]" glow
            v "We should be more prudent about that sort of thing"
    ju "It's possible she didn't want to worry you, seeing as her incident happened late at night"
    msg v "Even so, she always calls me about that sort of thing" ser1
    msg v "It makes sense for me to deal with it as her fiancee" ser1
    v "Especially because we're so close"
    msg v "{image=v_smile}" (img=True)
    msg ju "Of course you are. I just think Rika is slowly opening up" glow
    ju "She's always been active in the messenger, but I've been seeing her here more and more"
    msg ju "Could it be because we have a new member now?" glow
    v "I just wish she'd act more like herself"
    v "I'm getting worried about her"
    msg ju "She seems to be feeling fine, so you don't need to worry" ser1
    menu:
        "Rika  looks to be pretty unstable...":
            break heart ri
            award heart v
            ju "How can you say that when you barely even know her"
            v "If even [name] thinks that, then maybe Rika should be more careful about how she uses the messenger"
            msg v "I'll talk to her about that" curly
        "I'm sure Rika will bounce back - she seems like a really nice person":
            award heart ri
            v "That's what everyone who knows her says"
            ju "You're right [name]. Rika has always been that way"
            msg ju " I'm sure she'd appreciate what you just said" ser1
    v "What could she be feeling on the inside..."
    ju "I don't see why you don't just simply call her and confirm it for yourself"
    v "Maybe I should. Thank you for your advice Jumin"
    msg ju "{image=jumin_smile}" (img=True)
    v "When do you think you'll arrive back home?"
    msg ju "That remains a mystery. My chauffeur refuses to be specific about the time of arrival" ser1
    msg ju "Which makes me very annoyed" curly
    msg ju "{image=jumin_well}" (img=True)
    v "Chauffeur..? Aren't you traveling by plane?"
    msg v "{image=v_shock}" (img=True)
    ju "It's a private jet driven by a rather famous pilot"
    msg ju "I'd rather call my chauffeur however. The role is the same anyway" ser1
    ju "She's rather famous in her field. Perhaps she'd be a good guest for the party?"
    menu:
        "A pilot...? I'll pass":
            ju "You shouldn't discriminate because of her profession"
            ju "Then...V, try to get Rika to invite her instead"
            msg v "I'll see what I can do" curly
        "She sounds really interesting. Give her my contact information":
            ju "I'll provide her with your details"
            ju "It seems you've taken well to your coordinator role"
            v "Since Rika isn't feeling well, I'm glad someone has taken up her responsibilities"
    v "I haven't been traveling much as of late"
    v "Do you have any spots you'd recommend?"
    ju "I had a few in mind ever since I first heard you and Rika were thinking of getting married"
    ju "Now that I've been to a lot of those myself, I have to say that most are  worthy destinations"
    msg ju "France and the UK especially are great spots with a rich history"  glow
    v "I'm sure I'd get plenty of interesting shots there"
    v "But for now, I'm staying here in Korea. For Rika's sake"
    ju "I'd do the same thing if I were in your shoes"
    msg v "Perhaps that's why we're such good friends" glow
    msg v "{image=v_smile}" (img=True)
    ju "Of course. Wouldn't have it any other way"
    msg ju "{image=jumin_smile}" (img=True) #bonding over being psychos 
    ju "I think I'll arrange for Assistant Kang to wait for me at the airport"
    ju "She already got her break earlier in the week, so it should be fine"
    msg ju "We're experiencing some turbulence. I'll have to end this chat early" curly
    msg ju "Farewell to you both" 

    exit chatroom ju

    v "I'll have to leave in a bit as well."
    v "However...Something's been on my mind as of late"
    v "You wouldn't happen to know where Rika is right now?"
    menu:
        "Why do you want to know?":
            v "Is that so strange?"
            v "I'm her fiancee, we're supposed to tell each other everything"
            v "Unless it's something she doesn't want me to know.."
            menu:
                "Rika has the right to keep some things private":
                    award heart ri
                    v "..Yes, of course"
                    v "You've barely acquainted yourself with her and  yet..."
                    v "Oh well. I should've known you'd say that"
                "Why would she keep secrets from you?":
                    v "Well, how should I know?"
                    v "She can do as she likes I suppose"
                    msg v "I'll just have to keep watch on her in case she feels down" bold
        "No, I don't":
            v "Alright. Thank you for being honest"
            msg v "It's nothing important, I just thought I'd ask you since you two seemed close"
    msg v "I'm a bit concerned is all" curly
    v "I guess I'll have to call her myself then"
    v "Goodbye"

    exit chatroom v

return

label cd4_chat4_expired():
    #Wings of change

    $ v.status = "I just can't understand"
    $ ju.status = "Wonder how Elizabeth is doing.."

    scene day
    play music urban_night_cityscape

    ju "Good morning. Or rather, afternoon"
    ju "I see Yoosung has headed off for his entrance exam."
    msg ju "Hopefully his results will live up to the expectations I have for him." ser1
    ju "The entrance exam is fairly easy, so I doubt he'll have much trouble with it" 
    msg ju "I was able to pass it without much trouble on my part." ser1
    msg ju "The wait times were a real inconvenience however" sigh_m
    msg ju "Such an exam shouldn't last longer than an hour" glow
    msg ju "That's how long it took me anyway"
    msg ju "With that out of the way..." curly
    msg ju "'m about to embark on my journey home" glow
    msg ju "I hope Assistant Kang has kept everything exactly how I instructed her to" ser2

    enter chatroom v

    msg ju "I would hate for my darling Elizabeth to be feeling unwell when I'm away" glow
    ju "She's so sensitive to my absence...I can't help but worry"
    msg ju "{image=jumin_sad}" (img=True)
    v "I'm sure Elizabeth is feeling alright Jumin"
    msg v "{image=v_well}" (img=True)
    ju "Strange of you to assume such a thing. You never know what might happen"
    v "She's doted on constantly by your employees. I made sure to confirm that"
    msg ju "Of course. Wouldn't expect less from you" glow
    msg ju "You have your own worries as well." ser1
    msg ju "Have you checked up on Rika? I'm sure you saw her messages from earlier" curly
    v "I haven't yet. She should really try calling me first before things go awry"
    v "Instead of immediately logging onto the messenger"
    ju "It's possible she didn't want to worry you, seeing as her incident happened late at night"
    msg v "Even so, she always calls me about that sort of thing" ser1
    msg v "It makes sense for me to deal with it as her fiancee" ser1
    v "Especially because we're so close"
    msg v "{image=v_smile}" (img=True)
    msg ju "Of course you are. I just think Rika is slowly opening up" glow
    ju "She's always been active in the messenger, but I've been seeing her here more and more"
    msg ju "Could it be because we have a new member now?" glow
    v "I just wish she'd act more like herself"
    v "I'm getting worried about her"
    msg ju "She seems to be feeling fine, so you don't need to worry" ser1
    v "What could she be feeling on the inside..."
    ju "I don't see why you don't just simply call her and confirm it for yourself"
    v "Maybe I should. Thank you for your advice Jumin"
    msg ju "{image=jumin_smile}" (img=True)
    v "When do you think you'll arrive back home?"
    msg ju "That remains a mystery. My chauffeur refuses to be specific about the time of arrival" ser1
    msg ju "Which makes me very annoyed" curly
    msg ju "{image=jumin_well}" (img=True)
    v "Chauffeur..? Aren't you traveling by plane?"
    msg v "{image=v_shock}" (img=True)
    ju "It's a private jet driven by a rather famous pilot"
    msg ju "I'd rather call my chauffeur however. The role is the same anyway" ser1
    ju "She's rather famous in her field. Perhaps she'd be a good guest for the party?"
    ju "Her profession is needed more and more these days"
    ju "V, you should try and get Rika to invite her"
    msg v "I'll see what I can do" curly
    v "I haven't been traveling much as of late"
    v "Do you have any spots you'd recommend?"
    ju "I had a few in mind ever since I first heard you and Rika were thinking of getting married"
    ju "Now that I've been to a lot of those myself, I have to say that most are  worthy destinations"
    msg ju "France and the UK especially are great spots with a rich history"  glow
    v "I'm sure I'd get plenty of interesting shots there"
    v "But for now, I'm staying here in Korea. For Rika's sake"
    ju "I'd do the same thing if I were in your shoes"
    msg v "Perhaps that's why we're such good friends" glow
    msg v "{image=v_smile}" (img=True)
    ju "Of course. Wouldn't have it any other way"
    msg ju "{image=jumin_smile}" (img=True) #bonding over being psychos 
    ju "I think I'll arrange for Assistant Kang to wait for me at the airport"
    ju "She already got her break earlier in the week, so it should be fine"
    msg ju "We're experiencing some turbulence. I'll have to end this chat early" curly
    msg ju "Farewell to you, V" 

    exit chatroom ju

    v "I'll have to leave in a bit as well."
    v "However...Something's been on my mind as of late"
    v "I had hoped [name] would be here so I could ask her something"
    msg v "I'm a bit concerned about Rika is all" curly
    v "Oh well. I guess I'll have to call her myself then"
    v "Goodbye"

    exit chatroom v

return

label cd4_chat4_vn_ri():

    scene bg v_home with fade
    pause
    show rika thinking at vn_right
    ri "Now where did I put those documents.."
    ri "They should be around here somewhere.."
    ri neutral "...looks like this place hasn't been dusted in a while."
    ri "Ah...there they are.. I  can finally leave and.."
    play sound door_open_sfx
    v "Am I to assume I'm forgiven?"
    play music light_and_daffodils_piano1
    show v side unsure at vn_left with ease
    ri neutral "I really don't have anything to say to you now V"
    ri  "Especially after all the things you said to me  a few days ago..."
    v thinking "The things I said? I just remember you hanging up on me and running off to the cafe with Jaehee."
    v "You haven't returned a single one of my phone calls since"
    ri thinking "Interesting how you left out everything else that happened that day. How convenient"
    v unsure "I'm not leaving anything out. I'm just explaining how your actions have hurt me and the others."
    ri dark "Hurt? By what V? What did I do to hurt you?"
    v neutral "..."
    ri "And what did I do to hurt the members? Can I not talk to them without your permission? It's my organization, what gives you the right to-"
    v "I was simply stating the facts Rika. Your outburst concerned them a whole lot - it's all they've been talking about today"
    v "The members...are learning more and more about your other side. Even Yoosung seems to be affected by it, and on the day of his entrance exam no less"
    v "Please...let me be the only one in harms way... They deserve to stay ignorant of our problems"
    ri thinking "..."
    v "I also need you to move back here so I can make sure you're keeping up with your medication and staying out of trouble"
    ri sob "Oh V...I'm so hurt...I'm constantly drowned in darkness..How will I ever make it out without you by my side?"
    show v happy
    ri "I'm always frightened at how.."
    hide v 
    scene bg black with fade
    show rika dark at vn_center 
    ri "...you cannot stop behaving like a broken record"
    play music mysterious_clues_v2
    scene bg v_home with fade
    show rika  dark at vn_right
    show v side surprised at vn_left
    v "Rika..? "
    ri "You heard me right V. All you've been doing these past few days is repeating yourself and hoping I'll be dumb enough to believe you"
    ri "And why wouldn't you believe that? I've already been done that exact thing before. But I know better now"
    ri "I know what hides behind your words..You won't take me away this time"
    v neutral "....You're not well Rika. I am simply trying to get you to realize that before you end up hurting someone"
    v "If your outbursts continue...God knows what you'll be capable of"
    ri "I don't plan on 'hurting' anyone. All I want is.... to save the R.F.A from suffering, Save everyone on this Earth."
    ri "You keep standing in the way of that. I can't let you do that anymore."
    v thinking "..."
    ri thinking "I just want to create a world where everyone can be happy...And for once.."
    ri neutral "Someone has given me hope that such a thing is possible"
    ri "Is that so bad? Is everything I want to accomplish evil to you?"
    v neutral "I think I've heard enough. I'm sorry to say this Rika but..."
    v "You....your ideas are delusional. The things you want to do are impossible"
    v "But if you stay here and promise not to leave again...I can help you recover from all of that."
    v "We can continue sharing our love, like we've done for the past few years. And you'll be happy again. "
    ri crazy "De..delusional? You think my ideas are pure delusion?"
    ri dark "Ha..figures you'd say that. Of course. I am delusional. And you..you're the rational one."
    ri "The man who insists on calling himself the Sun and sacrificing himself onto me believes he is the normal one. "
    ri happy ".....that's  just too funny, I'm almost crying"
    ri "Well then. I guess you'll have your delusions and I'll have mine. I'm tired of this pointless conversation."
    stop music
    v "Rika you can't-"
    ri thinking "I think I just did. This conversation is over"
    hide v 
    hide rika
    scene bg black with fade
    show rika thinking at vn_center 
    play music mint_eye_piano
    ri thinking "V is a weird man...the things he says are in opposition to his actions"
    ri "I did the right thing by leaving just now. But...something isn't right.."
    ri "Was he right? Am I a delusional girl filled with nothing but darkness?"
    ri "Am I destined to fail, and sink deeper into my trauma? And if I am then...."
    ri sob "...Why am I yet living today?"

return
