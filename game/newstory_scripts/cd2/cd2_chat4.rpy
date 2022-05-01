label cd2_chat4():
    #mysterious letter

    $ ri.status = "Maybe I should consider opening a P.O box in R.F.As name..."

    scene night
    play music looking_for_happiness

    enter chatroom ri

    msg ri "The night is slowly retreating" glow
    msg ri "Even though it's pretty early in the morning, I feel rather...invigorated!" bold
    ri "I'm so glad you're here as well [name]! Though you should really be sleeping at this time in the morning!"
    menu:
        "I woke up as soon as I heard a chatroom opened!":
            ri "Oh my, I didn't mean to wake you up!"
            msg ri "You really should be getting your sleep in for the night" sigh_m
            msg ri "I don't want you getting sick!" glow
        "I was already awake. I tend to get up pretty early":
            ri "Do you now? That's interesting"
            msg ri "Now that I think about it...a lot of our members are like that actually!" curly
            msg ri "I don't know what that says about us as an organization.." sigh_m
        "Shouldn't you be asleep as well?":
            msg ri "You're probably right!" ser1
            msg ri "You see...I woke up to the Moons light shining through my window!" glow
            msg ri "And I just couldn't get myself to fall back asleep. Isn't that silly?" curly
    msg ri "Despite my protests, I'm actually glad you're here" bold
    msg ri "You see..I wanted to ask you about something" ser1
    ri "While I was cleaning up around my apartment complex yesterday, I stumbled upon this envelope.."
    ri "It was just...there, lying near  the door to my apartment. Seeing as it was addressed to me , I brought it inside"
    ri "At first I thought it was my electricity bill and the postmen missed my mailbox or something but.."
    msg ri "Once I opened it, I discovered it was a letter, hand-written by someone who claims to be an R.F.A admirer" bold
    msg ri "The author said how much the R.F.A parties mean to them  , and how important the work we do is.." glow
    msg ri "That warmed my heart...I'm so glad the R.F.A was able to reach so many people!" glow
    menu:
        "That letter is proof that the work the R.F.A does is truly magical!":
            award heart ri
            msg ri "Thank you so much [name]!" bold
            msg ri "I'm so glad I'm in a position where I can receive letters like this one.." curly
            msg ri "But the support that comes from other members is just as meaningful"
        "I'd love to receive a letter like that someday":
            ri "I'm sure you will, especially once the second party is full swing"
            msg ri "The work you and the other members are doing is bound to get rewarded" bold
            msg ri "Of course, I could also write one for you! Wouldn't that be fun?" glow
        "Who even writes letters anymore? Electronics are way more practical":
            award heart va
            ri "That might be true, but I think letters have a charm of their own"
            msg ri "Expressing yourself through choosing the right kind of stationary and experimenting with different fonts can be so exhilarating" glow
            ri "I wish they were more popular...You can truly feel a persons spirit through them"
    msg ri "I got a bit side-tracked there, didn't I?" sigh_m
    ri "What I actually wanted to ask you about were the final few lines of the letter.."
    msg ri "The author mentioned how they always felt out of place, and how the R.F.A was the thing to show them they could be loved while still being themselves" underline
    msg ri "That part really made me wish I could help them more.." glow
    msg ri "So I thought about writing a response ...but nothing really came to mind" sigh_m
    ri "I've been stumped since yesterday. Finally, I couldn't take it anymore and decided coming here could help me clear up my thoughts"
    msg ri "So...[name]..I know this might be a bit annoying of me but..What do you think I should say to them?"
    menu:
        "They should try being more social with the people around them.":
            msg ri "While that's very sound advice..." ser1
            msg ri "I don't think it's necessarily the thing that will help this person specifically" curly
            ri "Opening up to those around you can be so hard, even if you know them well"
        "If only they would do something productive instead of sulking!":
            msg ri "I don't think that's possible for everyone..." curly
            ri "I don't know what their circumstances are, but..."
            ri "It can be really hard to get yourself to things, especially if you're not feeling up to the task"
        "Maybe they just need someone who's like them who they can talk to?":
            award heart ri
            msg ri "You might be right! That seems to be what's missing from their life" glow
            msg ri "I wish everyone had that kind of person!" ser1
            ri "Someone you can confide in no matter what...I wonder what that's like"
    ri "Regardless, I'm so glad you were here to help me solve this conundrum of mine"
    msg ri "You were a lot of help ^^. I think I know what I should say to them" glow
    ri "I'll tell them they can write to me any time, and that they'll be sure to receive a response!"
    msg ri "I hope this makes them happy but ...I wish I could do more for them" sigh_m
    ri "Oh well...I guess that's something  I should think about on a later date"
    ri "For now...this'll have to do!"
    ri "I wonder where I should leave my response..They didn't even write down their name"
    msg ri "Now that I think about it.." curly
    msg ri "Isn't it kind of weird how this person knew my address? I never give that out to people..." ser2
    ri "Not even our members know where I live.."
    msg ri "How strange.." curly
    ri "I'm sure it's nothing..they could have seen me enter this building at some point. They could also be living here themselves"
    ri "I guess there's no use in mulling over it for too long.."
    ri "Once my response is done, I can just leave it in the place where I found the other letter"
    ri "Hopefully that'll be enough for them to find it.."
    msg ri "What stationery do you think I should use?"
    menu:
        "Just choose whatever, does it really matter that much?":
            ri "Those kinds of things do matter do me though.."
            ri "I know it's silly, but I like it.."
        "How about animal print?":
            award heart va
            award heart s
            msg ri "That sounds really cute! I'm sure I have some leopard print stationery lying around..." glow
            ri "I bet it'll make them smile...Perfect!"
        "Florals are the best!":
            award heart ri
            msg ri "You read my mind! That's exactly what I was thinking about using!" cloud_m
            msg ri "I have so many varieties...I guess I'll pick one most people would enjoy, like roses or carnations.."
    ri "Whatever I end up choosing, I hope my message will get across to the recipient"
    msg ri "That being that they are loved for who they are and can always friend in me and the R.F.A" glow
    ri "That about does it I think.."
    ri "Once I'm done writing, I'll drop it off and continue on with my day"
    ri "I really hope I didn't bother you too much..."
    msg ri "I know it's still pretty early in the morning, so if you feel like going back to bed, please go right ahead" curly
    ri "I think I'll stay up and wait for the sun to come out"
    ri "That usually helps me find my bearing. That'll be necessary if I plan on finishing this any time soon ;;"
    msg ri "Thank you for being in here with me, I really appreciate it!" glow
    msg ri "I think I'll leave you to rest now. Goodbye ~" bold

    exit chatroom ri

return


label cd2_chat4_expired():

    $ ri.status = "Maybe I should consider opening a P.O box in R.F.As name..."

    scene night
    play music looking_for_happiness

    enter chatroom ri

    msg ri "The night is slowly retreating" glow
    msg ri "Even though it's pretty early in the morning, I feel rather...invigorated!" bold
    ri "I hope everyone is sleeping soundly..."
    msg ri "Looking at te chat logs..a lot of our members stay up for way too long!" curly
    msg ri "I don't know what that says about us as an organization.." sigh_m
    msg ri "As for me..I woke up to the Moons light shining through my window!" glow
    msg ri "And I just couldn't get myself to fall back asleep. Isn't that silly?" curly
    msg ri "...despite me hoping everyone was asleep, I wish I had someone to bounce ideas off os" bold
    msg ri "I wanted to ask you guys about something" ser1
    ri "While I was cleaning up around my apartment complex yesterday, I stumbled upon this envelope.."
    ri "It was just...there, lying near  the door to my apartment. Seeing as it was addressed to me , I brought it inside"
    ri "At first I thought it was my electricity bill and the postmen missed my mailbox or something but.."
    msg ri "Once I opened it, I discovered it was a letter, hand-written by someone who claims to be an R.F.A admirer" bold
    msg ri "The author said how much the R.F.A parties mean to them  , and how important the work we do is.." glow
    msg ri "That warmed my heart...I'm so glad the R.F.A was able to reach so many people!" glow
    ri "I know letters are old fashioned, but I think they have a charm of their own"
    msg ri "Expressing yourself through choosing the right kind of stationary and experimenting with different fonts can be so exhilarating" glow
    ri "I wish they were more popular...You can truly feel a persons spirit through them"
    msg ri "....I got a bit side-tracked there, didn't I?" sigh_m
    ri "What I actually wanted to talk  about were the final few lines of the letter.."
    msg ri "The author mentioned how they always felt out of place, and how the R.F.A was the thing to show them they could be loved while still being themselves" underline
    msg ri "That part really made me wish I could help them more.." glow
    msg ri "So I thought about writing a response ...but nothing really came to mind" sigh_m
    ri "I've been stumped since yesterday. Finally, I couldn't take it anymore and decided coming here could help me clear up my thoughts"
    msg ri "Seeing as no one is in here...I guess I should try and think of what I should say to them on my own"
    ri "Maybe I should think about what you guys would say.."
    ri "Zen would probably say they should try being more social with the people around them."
    msg ri "And while that's very sound advice..." ser1
    msg ri "I don't think it's necessarily the thing that will help this person specifically" curly
    ri "Opening up to those around you can be so hard, even if you know them well"
    ri "Jumin would probably say they should do something productive instead of sulking ;"
    msg ri "But I don't think that's possible for everyone..." curly
    ri "I don't know what their circumstances are, but..."
    ri "It can be really hard to get yourself to things, especially if you're not feeling up to the task"
    msg ri "This isn't really helping..." sigh_s
    msg ri "Maybe all they need is some to talk to...someone like them.." curly
    msg ri "I wish everyone had that kind of person!" ser1
    ri "Someone you can confide in no matter what...I wonder what that's like.."
    msg ri "hmmm...I think I know what I should say to them!" glow
    ri "I'll tell them they can write to me any time, and that they'll be sure to receive a response!"
    msg ri "I hope this makes them happy but ...I wish I could do more for them" sigh_m
    ri "Oh well...I guess that's something  I should think about on a later date"
    ri "For now...this'll have to do!"
    ri "I wonder where I should leave my response..They didn't even write down their name"
    msg ri "Now that I think about it.." curly
    msg ri "Isn't it kind of weird how this person knew my address? I never give that out to people..." ser2
    ri "Not even our members know where I live.."
    msg ri "How strange.." curly
    ri "I'm sure it's nothing..they could have seen me enter this building at some point. They could also be living here themselves"
    ri "I guess there's no use in mulling over it for too long.."
    ri "Once my response is done, I can just leave it in the place where I found the other letter"
    ri "Hopefully that'll be enough for them to find it.."
    ri "As for stationery.."
    msg ri "I have so many varieties...I guess I'll pick one most people would enjoy, like roses or carnations.."
    ri "Whatever I end up choosing, I hope my message will get across to the recipient"
    msg ri "That being that they are loved for who they are and can always friend in me and the R.F.A" glow
    ri "That about does it I think.."
    ri "Once I'm done writing, I'll drop it off and continue on with my day"
    ri "I hope this isn't too much of a bother to read through..."
    ri "As for me...I think I'll stay up and wait for the sun to come out"
    ri "That usually helps me find my bearing. That'll be necessary if I plan on finishing this any time soon ;;"
    msg ri "I should really get to writing... Goodbye everyone ~" bold

    exit chatroom ri

return

label after_cd2_chat4:

    compose text ri:
        ri "I hope I didn't take up too much of your time..."
        ri "I just wasn't able to think of a proper response"
        ri "You being there helped me a lot. Thank you, once again!"
        label reply_letter

    return

label reply_letter:
    menu:
        "I'm so glad I was able to help!":
            award heart ri
            ri "You are too kind...The R.F.A feels so much brighter ever since you joined"
            ri "I truly appreciate the time you spent on talking to me"
        "You woke me up. Again":
            break heart ri
            ri "Oh...I'm really sorry..."
            ri "I didn't mean to do that, I promise"
        "I don't know if I was much help":
            ri "Oh no, you were, trust me!"
            ri "Oftentimes I get way too in my own head, and it really helps to talk to someone else"
    ri "I will try to bother you less from now on though ;"
    ri "Your time is very precious to me"

    return

label day_2_chatroom_2_outgoing_ri:
    ri "...Yes?"
    ri "Oh my, it's you [name]!"
    ri "I didn't think you'd call back so fast after our chat..."
    ri "Can't say it's not a pleasant surprise though!"
    menu:
        extend ''
        "I wanted to talk to you more":
            award heart ri
            ri "You did? That's so nice of you to say!"
            ri "I thought I was being a bit annoying, but I guess you didn't mind it too much"
            ri "Thank you, I really appreciate it!"
        "Yeah, I was just bored":
            ri "Well, I hope talking to me can make you feel better!"
            ri "...That was a bit much, sorry. Talking to me isn't that exciting I imagine"
            ri "I'm glad you called though, no matter what the reason might be"
    ri "*Yawn*"
    ri "Oh no! I didn't mean to do that! I think I'm starting to doze off, despite my best efforts"
    ri "This letter is taking more time than I thought it would. I thought that everything would come naturally but"
    ri "I'm still having a bit of trouble..."
    menu:
        extend ''
        "Is there any way I can help you out more?":
            ri "Oh no, you really don't have to !"
            ri "You already helped me out a lot, and I'm really thankful for that!"
            ri "But....you could tell me about how your day is panning out to be so far!"
            menu:
                extend ''
                "I'm feeling great! Talking to you is always a pleasure":
                    award heart ri
                    ri "..You really are too kind! I'm a bit embarrassed haha"
                    ri "That means a lot! Thank you!"
                    award heart ri
                    ri "And..I'm glad I could make your day just a tiny bit better"
                "My day has been pretty so-so so far":
                    ri "I see! I wish I knew how to make it at least a tiny bit better for you"
                    ri "Whenever I'm feeling down, I try having a cup of tea to relax and wind down"
                    ri "I hope I can recommend you some teas I like the next time we meet!"
        "Do you want me to leave you alone for a bit then?":
            ri "No no, it's really not like that"
            ri "This is very much on me, I'm sorry!"
            ri "I'll try to clear up my head a bit and get back to writing"
    ri "This conversation has been great!"
    ri "Thank you so much for calling, it really cheered me up"
    ri "I think I'll really have to  get back to writing though"
    ri "I'm sure this person would want me to respond quickly...Goodbye then!"

return

label cd2_chat4_outgoing_ja:
    ja "Yes Mr.Han?"
    ja "Oh...it's you...Do you know how early it is?"
    ja "The only reason my phone is on is because Mr. Han can call at any time"
    ja "I sincerely hope you have a reason for doing something like this"
    menu:
        extend ''
        "Um...nor really?":
            break heart ja
            ja "Oh really? Then you're wasting my time"
            ja "...that was harsh, wasn't it...I'm sorry..I really don't want to come across as mean but.."
            ja "...just don't do this kind of thing anymore, please."
        "I wanted to check up on you":
            award heart ja
            ja "That's....Unexpected. Thank you. I suppose"
            ja "That's the kind of thing Rika usually does"
            ja "I can see why you two got along so well"
    ja "Well, now that you're on the line, I guess we can talk about something"
    ja "Just make it quick, please"
    ja "I have to get to work soon"
    menu:
        extend ''
        "Do you usually get up this early in the morning?":
            ja "Yes. On any given day, I have to get up at around half past four in the AM to get ready"
            ja "The C&R building is somewhat further away from my apartment , so I really need the extra time"
            ja "I suppose that's why I'm a bit on edge. There's still time before my ride arrives but.."
        "What do you do once you wake up?":
            ja "Nothing unusual really. I just wake up, brush my teeth, and get ready for work"
            ja "Things most working people do. It's all I'm really required to do in terms of appearance"
            ja "The C&R offices are no beauty contest, and for that I'm thankful"
    ja "Thank you for calling. I'll check if I have time in my schedule to visit the chatroom today"
    ja "My ride will soon be here. Goodbye"

return
