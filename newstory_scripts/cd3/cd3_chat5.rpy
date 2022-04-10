label day_3_chatroom_5():

    $ ja.prof_pic = "Profile Pics/Jaehee/jae-31.png"
    $ z.prof_pic = "Profile Pics/Zen/zen-35.png"

    $ ja.cover_pic = "Cover Photos/Jaehee/ja3.png"
    $ z.cover_pic = "Cover Photos/Zen/z5.png"


    $ ja.status = "Workload increased again..."
    $ z.status = "Out on a jog"

    scene noon
    play music lonesome_practicalism 

    enter chatroom ja

    msg ja "I finally have some free time from all the work today" ser1
    msg ja "It's been so hectic. I hope everyone else is feeling well" ser1
    msg ja "...Is that appropriate to say?" curly
    menu:
        "Welcome Jaehee! Of course it is, don't worry!":
            award heart ja
            ja "Hello  [name]"
            msg ja "I'm glad there was someone else in the chatroom" glow
            ja "Otherwise this could have been a lot more awkward than it already is"
        "Why would it not be appropriate lol?":
            msg ja "I didn't notice you were here too" ser1
            msg ja "Sorry for making things awkward" curly
    msg ja "I was just worried how I could come off" ser1
    msg ja "Today I haven't really had the chance to visit the messenger..." sigh_m
    msg ja "Wish I could stay more up to date on R.F.A matters. It is a part of my job after all" ser2
    msg ja "Said job does also require my undivided attention at all times however" bold
    msg ja "So it's no wonder I haven't been able to catch up yet" curly
    $ is_idiot = False 
    menu:
        "Those sound like excuses to me...":
            $ is_idiot = True
            break heart ja
            msg ja "You are free to think of it that way..." curly
            msg ja "However, if you knew the amount of work required to do the job that I do" spike_m
            pause 1.0*5
            msg ja "I apologize. That was not professional of me"
        "You must be really busy. I understand":
            $ is_idiot = False
            award heart ja
            msg ja "I'm glad you are understanding of my position" glow
            msg ja "You'd be right, I am pretty busy these days.." curly
            msg ja "Though Rika is handling most of the work regarding your integration within the R.F.A....for that I'm thankful" round_m
    msg ja "Regardless, I have to admit...with C&R  continuously expanding, I'm finding less and less time to focus on anything that isn't my job" sigh_m
    msg ja "Let alone anything regarding my personal time" ser1
    msg ja "Though I still try and find time for the things I enjoy, like musicals" glow
    msg ja "Especially that last one Zen was involved in..I can't believe I missed out on the DVD" glow
    msg ja "You think they're still selling that coupled with the poster??" glow
    msg ja "As soon as I get off work, I'll be heading straight to the store!" cloud_m
    pause 1.0*5
    msg ja "... back to the topic at hand" curly
    msg ja "This upwards trend we're having is bound to increase with the upcoming party" ser1
    msg ja "So we should stay ahead of the game and prepare for what's to come" ser1
    menu:
        "I'm kind of curious about that musical thing..tell me more!":
            award heart ja
            msg ja "I..I see! I'd love to talk about that" glow
            msg ja "I just wasn't sure if it was appropriate, especially since I already discussed it a day or two ago" sigh_m
            msg ja "But if it's fine with you then..." curly
        "You know Jumin isn't here, right? You can talk normally lol":
            msg ja "I am aware that Mr. Han is not here" ser2
            msg ja "Talking about my personal interests just doesn't feel appropriate for this kind of environment" ser2
            msg ja "However, I suppose I COULD make an exception this time around" ser2
    ja "..."
    ja "Alright then, I suppose I will"
    ja "I was recently reviewing my collection of DVDs, when I noticed that one was missing"
    msg ja "For the life of me, I can't figure out where I put it.." curly

    enter chatroom z

    msg ja "And it's been bugging me for such a long time" curly
    msg ja "How did I manage to misplace it?" ser2
    pause 1.0*5
    msg z "Jaehee, [Name], hi! What were you guys talking about ?" glow
    msg ja "That's..umm.we were just.." sigh_m
    msg z "Actually , I should just go and check.." 
    pause 1.0*3
    msg ja "I don't think that's necessary, I could just " big
    msg z "OHHH, were you talking about my musicals??" glow
    msg z "Glad to see our newest member has taken an interest in a topic like that" square_m
    msg ja "...yes, I'm glad as well. Sorry if I said anything weird, I was just.." curly
    msg z "Weird? I didn't notice anything weird lol" ser1
    msg z "You shouldn't worry about stuff like that Jaehee. We are all friends here" glow
    menu:
        "Yeah Jaehee, stop being so weird":
            break heart z
            z "That's not what I meant [name]!"
            z "Jaehee is new here, just like you are"
            z "Try and be more understanding"
        "Yes! The R.F.A is one big happy family!":
            msg z "That's what Rika always says!" glow
            z "So no need to be  stiff with us!"
            ja "I'll...keep that in mind"
    msg z "The thing you said about your personal life clashing with your professional one" curly
    msg z "I totally get that! I have the same issue" bold
    msg z "Sometimes I feel like I'm losing myself in the process" sigh_m
    msg z "But this chatroom helps me a lot . I come here occasionally to clear my head and chat with you guys" glow
    msg z "And it helps me get over whatever it is I'm feeling" bold
    msg ja "That sounds wonderful...Is that why your performances always feel so captivating?" glow
    msg z "Woah, that's a huge compliment coming from you!" cloud_m
    z "And ...yeah, that might be it. I can't say it's the only thing that goes into it...but it definitely helps"
    msg z "Setting time aside to do the things you like is always a plus too!" glow
    z "I think that's the only way to avoid having your professional life cross into your personal life"
    msg ja "Thank you for explaining.." glow
    z "Lol, no problem! Hope that helped"
    z "Gonna go on a run now. See you guys later"

    exit chatroom z

    msg ja "He's gone..." sigh_m
    msg ja "I'm thankful for the words he said. I feel a  bit more liberated now" 
    msg ja "Maybe I should try and relax while talking to you guys..." cloud_m
    if is_idiot:
        ja " I don't expect you to take my complaints seriously"
        ja "Since you seem to think it's all a lot of excuses.."
    msg ja "However, I also wanted to hear your opinion on it" ser1
    ja "Would you share it with me?"
    menu:
        "Please do! Talking to the members is my favorite part of being here":
            award heart ri 
            award heart ja
            msg ja "Spoken like a true coordinator" round_s
            msg ja "I'm sure Rika would be glad to hear that"  glow
            msg ja "...Not to assume, of course."
        "I'm not sure either. It still feels a bit awkward. I feel like I don't fit in here":
            award heart va
            ja "I can understand feeling like that"
            ja "Especially since you've joined fairly recently"
            msg ja "It'd be wise to take your time and get to know everyone first" glow
    msg ja "Thank you for answering my question!" glow
    msg ja "I will try to be more open to the people here" curly
    msg ja "That is , until Mr.Han calls to remind me of my work, using this very messenger" sigh_m
    ja "That's something I'll have to consider I suppose.."
    ja "I'll have to leave now, my break is almost over"
    menu:
        "I wonder what Rika is doing right now...":
            award heart ri
            ja "She's probably out there talking to a potential guest"
            msg ja "Whatever it is, I hope she's having more fun than me" sigh_m
        "Goodbye Jaehee! Good luck with work":
            award heart ja
            ja "Thank you [name]! I appreciate it"
            ja "Have a great day!"
    ja "Goodbye then!"

exit chatroom ja

return 

label day_3_chatroom_5_expired():
    $ ja.prof_pic = "Profile Pics/Jaehee/jae-31.png"
    $ z.prof_pic = "Profile Pics/Zen/zen-35.png"

    $ ja.cover_pic = "Cover Photos/Jaehee/ja3.png"
    $ z.cover_pic = "Cover Photos/Zen/z5.png"


    $ ja.status = "Workload increased again..."
    $ z.status = "Out on a jog"

    scene noon
    play music lonesome_practicalism 

    enter chatroom ja

    msg ja "I finally have some free time from all the work today" ser1
    msg ja "It's been so hectic. I hope everyone else is feeling well" ser1
    msg ja "Finally, I've got some free time.." curly
    ja "....there is no one else in here though, so that only makes things awkward"
    msg ja "Today I haven't really had the chance to visit the messenger..." sigh_m
    msg ja "Wish I could stay more up to date on R.F.A matters. It is a part of my job after all" ser2
    msg ja "Said job does also require my undivided attention at all times however" bold
    msg ja "So it's no wonder I haven't been able to catch up yet" curly
    msg ja "I have to admit...with C&R  continuously expanding, I'm finding less and less time to focus on anything else" sigh_m
    msg ja "Let alone anything regarding my personal time" ser1
    msg ja "Though I still try and set time aside for the things I enjoy, like musicals" glow
    msg ja "Especially that last one Zen was involved in..I can't believe I missed out on the DVD" glow
    msg ja "I hope they're still selling that coupled with the poster..." glow
    msg ja "As soon as I get off work, I'll be heading straight to the store!" cloud_m
    pause 1.0*5
    msg ja "Hope that was okay to say...Back to the topic at hand.." curly
    msg ja "This upwards trend we're having is bound to increase with the upcoming party" ser1
    msg ja "So we should stay ahead of the game and prepare for what's to come" ser1
    msg ja "I did really want to talk about something though..."
    ja "..."
    ja "Alright then, I suppose I will, even if it's something personal"
    ja "I was recently reviewing my collection of DVDs, when I noticed that one was missing"
    msg ja "For the life of me, I can't figure out where I put it.." curly

    enter chatroom z

    msg ja "And it's been bugging me for such a long time" curly
    msg ja "How did I manage to misplace it?" ser2
    pause 1.0*5
    msg z "Hi Jaehee! What were you talking about?" glow
    msg ja "That's..umm...I was just.." sigh_m
    msg z "Actually , I should just go and check.." 
    pause 1.0*3
    msg ja "I don't think that's necessary, I could just " big
    msg z "OHHH, were you talking about my musicals??" glow
    msg ja "Sorry if I said anything weird, I was just.." curly
    msg z "Weird? I didn't notice anything weird lol" ser1
    msg z "You shouldn't worry about stuff like that Jaehee. We are all friends here" glow
    msg z "We are one big family here, just like Rika always says" glow
    msg z "The thing you said about your personal life clashing with your professional one" curly
    msg z "I totally get that! I have the same issue" bold
    msg z "Sometimes I feel like I'm losing myself in the process" sigh_m
    msg z "But this chatroom helps me a lot . I come here occasionally to clear my head and chat with you guys" glow
    msg z "And it helps me get over whatever it is I'm feeling" bold
    msg ja "That sounds wonderful...Is that why your performances always feel so captivating?" glow
    msg z "Woah, that's a huge compliment coming from you!" cloud_m
    z "And ...yeah, that might be it. I can't say it's the only thing that goes into it...but it definitely helps"
    msg z "Setting time aside to do the things you like is always a plus too!" glow
    z "I think that's the only way to avoid having your professional life cross into your personal life"
    msg ja "Thank you for explaining.." glow
    z "Lol, no problem! Hope that helped"
    z "Gonna go on a run now. See you later"

    exit chatroom z

    msg ja "He's gone..." sigh_m
    msg ja "I'm thankful for the words he said. I feel a  bit more liberated now" 
    msg ja "Talking to the members can be a lot of fun I suppose" cloud_m
    msg ja "Maybe I should consider letting my guard down a bit..." curly
    msg ja "That is , until Mr.Han calls to remind me of my work, using this very messenger" sigh_m
    msg ja "That's something I'll have to consider ." sigh_m
    ja "I'll have to leave now, my break is almost over"

    exit chatroom ja


return 


    label after_day_3_chatroom_5:

    compose text ja:
        ja "I hope I didn't come off too serious in that conversation.."
        ja "It's just that I feel a bit awkward about using this messenger is all"
        ja "What do you think?"
        label reply_lonesomejaehee

    return

    compose text z:
        z "I didn't want to bring it up in the chatroom but.."
        z "It was kind of exciting to see you and Jaehee talking about my musicals"
        z "Do you want me to get you guys some merchandise lol?"
        label reply_zenmerch

    return

label reply_lonesomejaehee:
    menu:
        "You did great! Don't be afraid to talk more in the messenger": 
            award heart ja
            ja "I'm glad you think of it that way" 
            ja "Rika actually told me the same thing"
            ja "Maybe I should take your advice to heart..."
        "It did feel a bit awkward":
            ja "I see. I'll definitely take that into account"
            ja "Hope I can improve in the future"
            ja "Wouldn't want to make anyone else feel uncomfortable"
    ja "I'll try to be more engaging in the future"

    return

label reply_zenmerch:
    menu:
        "OMG OFFICIAL ZEN MERCH OMG OMG": 
            award heart z
            z "I'll take that as a yes then lol"
            z "Consider it done. I'll bring some to the party"
            z "Make sure you bring something to carry it all in"
        "Please give some to Rika as well":
            award heart ri
            z "That's very thoughtful of you"
            z "Rika has always  been a fan of mine, so I'm sure she'd appreciate it"
            z "Thank you for giving me that idea!"

    return
