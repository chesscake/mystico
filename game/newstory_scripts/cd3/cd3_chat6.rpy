label day_3_chatroom_6():



    $ va.status = "Remember to keep your info private , even in the chatroom"



    scene afternoon

    #play music ventheme


    enter chatroom va
    msg va "The day is coming to an end" glow
    msg va "I heard people get sentimental at times like this " ser1
    msg va "Guess being busy all the time has its perks" curly
    msg va "Ah, the very reason  my schedule is the way it is has decided to join me" ser1
    msg va "Hello [name]." ser1
    menu:
        "Hello! I was looking forward to seeing you in here":
            award heart va
            msg va "Looking forward to..." bold
            msg va "What exactly ?" bold
            msg va "...I guess you were trying to be nice. Thank you" sigh_m
        "You've been here a lot today. Is everything good with the messenger?":"
            msg va "Yes, everything is fine" ser1
            msg va "It's as secure as can be" ser1
            msg va "As for me being here a lot..." ser2
    msg va "I'm just doing some last minute changes before 707 gets back here" 
    msg va "The app is functioning perfectly without him , but there are still things I need to do before he comes back"
    msg va "The days of worrying if 707s code had somehow gone rogue will soon be behind me" glow
    msg va "Just the thought excites me" glow
    va "I almost can't believe it. It's only been a few days , but I got to know you all a lot more than I thought I would"
    msg va "You should all be more careful with private info like that. You never know what could happen to the messengers code" bold
    msg va "Especially the two coordinators" glow
    menu:
        "I'll be more careful from now on~":
            award heart va
            msg va "Glad you're listening to my advice" glow
            msg va "I can appreciate it when people make my job easier for me" glow
            msg va "Especially when it's someone I work with directly" underline
        "This should be a place for members to freely discuss whatever they like!":|
            award heart ri
            msg va "Alright then. But don't say I didn't warn you" curly
            msg va "Privacy should come before friendship or whatever but.."
            msg va "Not like I care much about what happens to your data anyway" bold
va "Sticking to my advice should help you keep your private life safe"
msg va "And, if you really want something gone..." ser2
#insert conmand for messege deletion here. Ven deletes his last message 
msg va "I could always pull some strings" glow
menu:
    "Don't do stuff like that anymore. These messages are important":
        award heart ri
        awart heart s 
        msg va "Whatever you say..." sigh_m
        msg va "I was just trying to show off a feature of the messenger " ser1
    "Wow, that's kind of cool!":
        award heart va
        msg va "I know right ?" glow
        msg va "It's so insanely convinient, and it gets rid of all the data in a flash" glow
    "A feature like that could keep things interesting around here..."
        #possible Mika option ? Unsure as of yet
        msg va "Keep things interesting?"curly
        msg va "Are you bored already ? This command is only supposed to be used to protect data" ser1
msg va "It's a wonder 707 hasnt implemented it yet" ser1
msg va "Especially with all the info involving the party guests being spread around "curly 
msg va "You guys know that's supposed to be kept secret, right ? " curly
msg va "Oh well. Your organization, your rules" ser1
msg va "I guess I'd be partially responsible if something goes awry though. So please be careful" glow

enter chatroom ja

msg va "Oh. Hello there" ser1
ja "...Hello"
ja "I came here looking for Mr. Han"
ja "I haven't been able to get in contact with him"
va "Seeing as he isn't here,  I should probably just try calling him again"
menu:
    "Why don't you stick around and rest for a bit ?":
        award heart ja
        msg ja "Maybe I should..." cloud_m
        msg ja "It's not like I'll be doing much in the meantime anyway"
    "Maybe you should check out what Vanderwood wrote before you leave":
        award heart va
        msg ja "I guess I could" ser1
        msg va "It's not that important, but thank you [name]" curly
ja "I see you two were talking about privacy"
msg ja "That's a touchy subject..." ser1
msg va "Not being open about your private life is kind of in your job description , no ?" curly
ja "Yes it is. But Rika has been encouraging me to be more personable"
    #perform heart check for Jaehee >10 hearts
    #msg ja "Come to think of it...so has [name]" glow
    #might cut this out
va "Well. Do whatever you like" 
va "I'm just about done reviewing all the built up data"
va "Everything looks good so far, so I guess I'll take my leave."
ja "Already ? You must be pretty busy."
va "Not really. The things I'm doing are pretty mundane, but they take a while to complete"
menu:
    "So soon ? Hope we get to talk more next time":
        award heart va 
        msg va "Getting to slack off work...Wouldn’t that be nice?" glow
        msg va "I guess I could try giving myself a little wiggle room for once." ser1
        msg va "Maybe next time we could talk about something more interesting"
    "Alright, hope you keep the messenger safe":
        va "Sure I will. Not like there's much else I'm supposed to be doing"
        va "Things are pretty praceful for now "
        va "I hope they stay that way"
va "Goodbye then. Both of you"

exit chatroom va

ja "..." 
msg ja "That was a bit awkvard , wasn't it ?" curly
msg ja "For once I felt like I wasn't being the weird one" round_m
msg ja "Not that Mister Vanderwood weird but " ser1
ja "..."
ja "What do you think about the things he said ? "
menu:
    "He's right! We should all be more careful":
        award heart va
        ja "You think so ?"
        ja "Maybe you're right...Even Ive begun to ease up"
        ja "I guess that's something to think about "
    "I don't really agree with what he said":
        ja "You can think that"
        ja "I can see what he's trying to get at , but I wouldn’t say I agree with him either"
        ja "Stuff like this will take time to get used to"
msg ja "In the meantime, I guess we'll continue as usual" glow
ja "Mr. Han hasn't called me back yet.."
ja "I wonder what he's up to"
msg ja "These days he seems rather interested in foreign cultures" ser1
msg ja "So recently I looked into organizations that specialise in that sort of thing..." ser1
ja "One in particular really stood out to me..."
ja "It was this agency that lets impoverished people travel to all sorts of interesting locations for free"
menu:
    "I'd prefer it if people worked to afford luxuries like that":
        ja "I can see your point"
        msg ja "But I don't really agree..." ser1
        msg ja "We don't know everyone's circumstances. Some people might genuinely need organizations like the one I mentioned" square_m
    "That organization sounds wonderful! Their goal is really noble":
        msg ja "Yes, you're right!" round_s
        msg ja "The work they do should absolutely be commended " glow
        msg ja "I hope they'll be able to continue with their mission" glow
        msg ja "Since you sound interested..." ser2
        msg ja "Would you like to invite them to the party ? I'll get in contact with them myself" ser2
        menu:
            "I'd love to have them attend":
                award heart ri
                ja "Good. I'll reach out to them immediately"
                ja "Glad you're taking the message of the R.F.A to heart"
            "Wouldn't really want to bother them...":
                ja "Oh , is that so? Alright then"
                ja "But I don't think extending them an invite would do much harm.... I suppose I'll pass their info along to Rika"
ja "Organizations like that are the heart and soul of any good charity party"
msg ja "I'm getting a bit sentimental..." glow 
msg ja "I should probably get back to work..." curly
ja "Goodbye"

exit chatroom ja

return
