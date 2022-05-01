label day_1_chatroom_11():

    $ ri.status = "Good night R.F.A!"
    $ ri.prof_pic = "Profile Pics/Rika/rika-5.webp"
    $ ri.cover_pic = "Cover Photos/Rika/r3.jpg"

    scene night
    play music looking_for_happiness

    ri "Today has been so hectic.."
    msg ri "With [name] joining, our organization is steadily expanding ^^" square_l sser2
    msg ri "I'm so happy to see the RFA flourish!" glow
    ri "{image=rika_party}" (img=True)

    menu:
        "Hi Rika! I'm happy too~":
            award heart ri
            ri "Oh my! [name]!!!"
            ri "Sorry I didn't notice you before!"
            ri "And I'm so glad to hear that!"
            ri "I'm sure we'll make a wonderful party coordinator team!^^"
        "Hello":
            "Hi [name]! Glad to see that you're here!"
            "I was just about to talk about the parties we'll be holding ^^"


    ri "Though the parties themselves aren't what's most important"
    ri "Rather, it's the smiles we put on people's faces"
    ri "What we accomplished with the first party..."
    ri "I was so honored"
    ri "It felt so good, being surrounded by people with warm hearts"
    msg ri "They came from all sorts of organizations" ser1
    msg ri "Artists, scientists, common everyday people.." ser1
    msg ri "They were all there, with their hearts beating as one" ser1
    msg ri "It's a memory that shines with the passion of the sun ^^" ser1 glow

    menu:
        "How did the party planning for that party go?":
            ri "Well, we split responsibilities accordingly"
            ri "Jumin got in touch with the venue and the catering company!"
            ri "V's works were sold off"
            ri "Yoosung helped us get in touch with some youth organizations"
            ri "And I invited guests," 
            ri "decorated the venue" 
            ri "and designed the invitations!"
        "What was the goal of that party?":
            award heart ri
            ri "Back then..."
            ri "The goal was to get funds for Child-protective organizations"
            ri "We spent time researching the most suitable ones, delving deep into their history"
            ri "In the end,"
            ri "we were left with only two or three credible organizations, but we knew our funds would be well-spent"

    msg ri "All in all, it was a great success ^^" bold
    ri "I saw so many happy faces in that crowd"
    ri "And they all wanted one thing"
    msg ri "to help others" glow ser1 
    ri "We got so much support..."
    ri "I was so proud, seeing what we could accomplish if we put our mind to it"
    ri "However..."
    msg ri "I feel like it was not enough." ser1 big
    ri "We have to help even more people"
    msg ri "That is why I want to thank you for coming to us [name]" cloud_m
    ri "{image=rika_happy}" (img=True)
    ri "You will help us in our endless quest"

    menu:
        "I can't wait! I'm so excited to begin working with you guys":
            award heart ri
            ri "Oh my, you seem eager!"
            ri "That's what I like to see!"
            ri "I'm excited to work with you as well ^^"
        "I don't think you can permanently change the world like that":
            ri "Oh, perhaps you're right!"
            ri "But I'm sure we can at least try and improve the lives of the people living today!"

    msg ri "I know you've only just arrived.." ser2 
    msg ri "But I see you've already sparked discussion between the members.." ser2
    ri "I don't know how many of the chats you participated in.."
    ri "But I'm sure your presence helped the members feel like the RFA is truly ready for another party"
    ri "It's been a little while since we held our last one"
    msg ri "So naturally, the members were starting to get a bit bored ;;" curly
    msg ri "Now we can finally refocus our efforts into making others happy!" ser1 glow
    ri "Though,  some of our members seem to have woes of their own."
    ri "Would you mind if I talk about them for a bit?"

    menu:
        "I don't know, I think I heard enough":
            ri "Oh, I'm sure you've already interacted with them..."
            ri "So I'll try to keep this brief"
            ri "Hang in there"
        "Oh no, feel free to. I was getting worried about them myself":
            award heart ri
            ri "Why thank you [name]!!"
            ri "You seem very considerate"
            ri "I knew I made the right choice when I invited you"

    ri "After looking over todays chats it seeems that.."
    ri "Luciel is so busy.."
    msg ri "I wish he didn't have so much work" sigh_m
    ri "I didn't want him to be..."
    ri "So busy all the time"
    ri "{image=rika_cry}" (img=True)
    ri "I'll have to talk about that with.."
    ri "...nevermind"
    ri "Jumin is his old self"
    msg ri "I wish he'd stop drinking so much.." curly 
    msg ri "I appreciate him talking about Elizabeth 3rd, I'm really happy he's taken so well to her" ser2 round_l
    msg ri "I hope she could make him feel less lonely in that cold corporate world he lives in..."
    ri "As for Yoosung..."
    ri "He is so focused on school work!"
    ri "I'm proud of him but"
    msg ri "I wish he would do something for himself once in a while" glow ser2
    msg ri "School responsibilities must be overwhelming him" ser2
    msg ri "along with the family pressure" ser2
    ri "I'll need to check in with him about that"
    ri "I see Zen is having some money troubles..."
    ri "I'm worried, despite what he said"
    ri "He's a rising star but"
    msg ri "He shouldn't feel like he has to rely only on himself" glow ser2
    ri "I'll get him in touch with a theater company I recently found out about"
    ri "Jaehee and I will look into it Zen, don't worry ^^"
    ri "Your career is bound to be successful with every single one of us at your side"
    ri "Speaking of Jaehee..."
    msg ri "She is so adorable ^^" flower_s ser2
    ri "She doesn't have to be that careful about everything"
    ri "She seemed like she was afraid that if she made a wrong move on the messenger"
    ri "She would get fired ;;;"
    ri "That's not true at all.."
    ri "Besides..."
    msg ri "I would never allow it ^^" glow big ser1
    ri "And then..."
    ri "V was here too"
    ri "Hmmm"
    ri "He shouldn't be so suspicious of [name]..."
    ri "I made sure you were safe, made all the preparations.."
    ri "I did everything necessary before introducing you"
    msg ri "Luciel even did a check on [them] in the meantime" big glow ser1
    msg ri "I... hope my decision didn't anger any of you~" curly sigh_m

    menu:
        "I'm sorry I caused you guys trouble":
            ri "Oh no, you didn't"
            ri "I wanted you to be here for a reason!"
            ri "I know others might disagree.."
        "I don't know, inviting me here being so close to a big party does seem like a rash decision lol":
            break heart ri
            ri "Do you really think so?"
            award heart v
            ri "If even you're saying then..."
            ri "I guess I could have taken more time to come to an agreement"
        "I know the others might feel wary of me, but I'll make sure to do my best":
            award heart ri
            "I knew it!!"
            "From the moment we met, I was sure you were the right choice"
            "Others might not agree"
    
    ri "But I'm sure I made the right decision"
    ri "...let's meet up and talk, V"
    ri "Just to talk about this...person"
    ri "I'm sure we'll come to a resolution ^^"
    ri "Anyway..."
    msg ri "I'm getting sleepy now" curly 
    ri "I should head off to bed..."
    ri "And you should too [name]"
    msg ri "Don't think I don't see those late night chatrooms +_+" ser1 glow 
    msg ri "Good night RFA ^^" bold 
    msg ri "Good night [name]!" spike_l


    return

label day_1_chatroom_11_expired():

    $ ri.status = "Good night R.F.A!"
    $ ri.prof_pic = "Profile Pics/Rika/rika-5.webp"
    $ ri.cover_pic = "Cover Photos/Rika/r3.jpg"

    scene night
    play music looking_for_happiness

    ri "Today has been so hectic.."
    msg ri "With [name] joining, our organization is steadily expanding ^^" square_l sser2
    msg ri "I'm so happy to see the RFA flourish!" glow
    ri "{image=rika_party}" (img=True)
    ri "But it's not all about the parties"
    ri "The smiles we put on people's faces with the first party..."
    ri "I was so honoured"
    ri "It felt so good, being surrounded by people with warm hearts"
    msg ri "They came from all sorts of organizations" ser1
    msg ri "Artists, scientists, common everyday people.." ser1
    msg ri "They were all there, with their hearts beating as one" ser1
    msg ri "to me, It's a memory as warm as the sun ^^" ser1 glow
    ri "Back then..."
    ri "The goal was to get funds for Children protective organizations"
    msg ri "And it was a great success ^^" bold
    ri "I saw so many happy faces in that crowd"
    ri "They all wanted one thing"
    msg ri "to help others" glow ser1 
    ri "We got so much support..."
    ri "Yet it was not enough, we have to help even more people"
    msg ri "Thank you for coming to us [name]" cloud_m
    ri "{image=rika_happy}" (img=True)
    msg ri "I know you've only just arrived.." ser2 
    msg ri "But I see you've already sparked discussion between the members.." ser2
    ri "I don't know how many of the chats you participated in.."
    ri "But I'm sure your presence helped the members feel like the RFA is truly ready for another party"
    ri "It's been a little bit since we held our last one"
    msg ri "So naturally, the members were starting to get a bit bored ;;" curly
    msg ri "Now we can finally refocus our efforts into making others happy!" ser1 glow
    ri "Though,  some of our members seem to have woes of their own."
    ri "Luciel is so busy.."
    msg ri "I wish he didn't have so much work" sigh_m
    ri "I didn't want him to be..."
    ri "So busy all the time"
    ri "{image=rika_cry}" (img=True)
    ri "I'll talk about that with.."
    ri "..."
    ri "Jumin is his old self"
    msg ri "I wish he'd stop drinking so much.." curly 
    msg ri "I appreciate him talking about Elizabeth 3rd, I'm really happy he's taken so well to her" ser2 round_l
    msg ri "I hope she could make him feel less lonely in that cold corporate world he lives in..."
    ri "Yoosung is so focused on school work"
    ri "I'm proud of him but"
    msg ri "I wish he would do something for himself once in a while" glow ser2
    msg ri "School responsibilities must be overwhelming him" ser2
    msg ri "along with the family pressure" ser2
    ri "I'll need to check in with him about that"
    ri "I see Zen is having some money troubles..."
    ri "I'm worried, despite what he said"
    ri "He's a rising star but"
    msg ri "He shouldn't feel like he has to rely only on himself" glow ser2
    ri "I'll get him in touch with a theater company I recently found out about"
    ri "Jaehee and I will look into it Zen, don't worry ^^"
    ri "Your career is bound to be successful with every single one of us at your side"
    ri "Speaking of Jaehee..."
    msg ri "She is so adorable ^^" flower_s ser2
    ri "She doesn't have to be that careful about everything"
    ri "She seemed like she was afraid that if she made a wrong move on the messenger"
    ri "She would get fired ;;;"
    ri "That's not true at all.."
    ri "Besides..."
    msg ri "I would never allow it ^^" glow big ser1
    ri "And then..."
    ri "V was here too"
    ri "Hmmm"
    ri "He shouldn't be so suspicious of [name]..."
    ri "I made sure she was safe, made all the preparations.."
    ri "I did everything necessary before introducing her"
    msg ri "Luciel even did a check on [them] in the meantime" big glow ser1
    msg ri "I... hope my decision didn't anger any of you~" curly sigh_m
    ri "But I'm sure i made the right decision"
    ri "...let's meet up and talk, V"
    ri "Just to talk about this...person"
    ri "I'm sure we'll come to a resolution ^^"
    ri "Anyway..."
    msg ri "I'm getting sleepy now" curly 
    ri "I should head off to bed..."
    ri "All of you should too"
    msg ri "Don't think I don't see those late night chatrooms +_+" ser1 glow 
    msg ri "Good night RFA ^^" curly round_m
    
    return


label after_day_1_chatroom_11 ():
  
$ space_thoughts.new_choices([
    SpaceThought(ja, "I should get some headache suppressants..."),
    SpaceThought(ja, "Now that Mr.Han isn't here, I could just leave...Nevermind, Han Senior just entered the office"),
    SpaceThought(ja, "Only a bit more time..."),
    SpaceThought(ju, "I heard Elizabeth lost weight recently...perhaps she needs an assistant of her own"),
    SpaceThought(ju, "This day has been so hectic...I hope V's fine"),
    SpaceThought(ju, "Biscuits and tea..what a strange combination."),
    SpaceThought(s, "I hope the R.F.A is okay"),
    SpaceThought(s, "Hacked, hacked,you're all hacked...Would you laugh if you were here?"),
    SpaceThought(s, "This code is a mess...but it's my mess"),
    SpaceThought(y, "Have to get my notes in order"),
    SpaceThought(y, "Pastries? I'm no good at making those..."),
    SpaceThought(y, "What did she say? My classmates are too loud"),
    SpaceThought(z, "This fabric is so tacky."),
    SpaceThought(z, "Who thought this script was a good idea?"),
    SpaceThought(z, "Would me howling bring this role to life?"),
    SpaceThought(ri, "Would [name] prefer coffe or tea? Let's stock up on both!"),
    SpaceThought(ri, "Jaehees excited chatter is adorable."),
    SpaceThought(ri, "Friend..foe...something in between...Who is he?"),
    SpaceThought(v, "Didn't I see that person at the docks yesterday?"),
    SpaceThought(v, "I'll handle the paperwork..wouldn't want to encounter prying eyes"),
    SpaceThought(v, "This suitcase looks great! And the hidden compartment might come in handy..."),
    SpaceThought(va, "A new assignemnt already?"),
    SpaceThought(va, "These people are so strange...stay focused"),
    SpaceThought(va, "The sky is clear. I'll go out for a smoke")
    ] )