label cd1_chat7():

    $ y.status = "Busy with school..."

    scene noon

    enter chatroom ri

    ri "I see Yoosung already left."
    #rika sigh relieved emoji
    ri "He's been pulling all nighters to study."
    ri "His grades are top of the class but he still won't put down his books even for a second."
    ri "I told him I'm feeling better."
    ri "I wish he'd stop and take care of his health..."
    ri "I don't want him to get sick."
    ri "It can't happen again..."
    #cry emoji
    menu:
        "It? Has something happened?":
            award heart ri
            #emoji
            ri "It was before you joined us..."
            ri "Something terrible..."
            ri "I... I think it's best I tell you about it one day..."
            ri "For now, don't worry about it."
        "He's going to bite the dust.":
            break heart ri
            ri "That's horrible..."
            #rika cry emoji
            ri "Why would you say something like that, [name]?"
    ri "... I just thought of something."
    msg ri "A belief is a powerful thing, isn't it?" glow
    msg ri "It can fundamentally change us." glow
    ri "When I first met Yoosung, he..."
    ri "He felt powerless, bored."
    msg ri "Like nothing he did ever mattered." ser2
    ri "Going through the motions every day..."
    ri "Of course..."
    ri "To outlookers, someone like that might come across as lazy."
    ri "He believed no matter what he did, it was all meaningless."


    return

label cd1_chat7_expired():

    $ y.status = "Busy with school..."

    scene noon


    enter chatroom ri

    ri "I see Yoosung already left."
    ri "..."
    ri "He's been pulling all nighters to study."
    ri "His grades are top of the class but he still won't put down his books even for a second."
    ri "I told him I'm feeling better"
    ri "but he still insists he needs to excel..."
    ri "In order to prevent it from happening again."
    ri "Actually, I was just thinking."
    msg ri "A belief is a powerful thing, isn't it?" glow
    msg ri "It can fundamentally change us." glow
    ri "When I first met Yoosung, he..."
    ri "He felt powerless, bored..."
    msg ri "Like nothing he did ever mattered." ser2
    ri "Of course..."
    ri "To outlookers someone like that might come across as lazy."
    ri "He believed no matter what he did, in the end it was all meaningless."

    return

######____TEXT MESSAGES____

label after_cd1_chat7:

    compose text v:
        v "Hello, I'm sorry I'm not logging in often."
        v "I'd like to talk personally with you on the phone."
        v "May I call you tomorrow morning?"
        label reply_vmessage

    return

label reply_vmessage:
    menu:
        "Why? Is there any issue?":
            v "No, no, not at all."
            v "Only some friendly advice."
        "I'm phone shy...":
            v "I understand. Don't worry, you don't need to speak much."
            v "I only want you to listen to what I have to say, it won't take long."
        "Yes, call me, baby.":
            v "I'm sorry...?"
            v "I suppose Luciel's sense of humor is somewhat contagious..."

    return
