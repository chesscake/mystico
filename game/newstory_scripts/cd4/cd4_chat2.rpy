label cd4_chat2():

    $ ri.status = "Thank you for hearing me out [name]!"

    scene night
    play music looking_for_happiness

    enter chatroom ri

    msg ri "Is anyyone there?" bold
    msg ri "Jaehee, [name], anyone..." glow
    msg ri "Am I really alone ?" ser1
    menu:
        "I'm here !!! Are you okay Rika?":
            award heart ri
            ri "[name]!!!"
            ri "You're here...everything is..."
            ri "..."
        "Pull yourself together Rika":
            ri "{image=rika_cry}"(img=True)
            ri "..."
            ri "I will...it's just that"
    ri "I'm glad there's someone else here"
    ri "I dont know what I'd do if I was alone"
    ri "Sorry for frightening you"
    ri "....I woke up and everything felt so wrong and"
    ri "Why am I like this..."
    menu:
        "You must have had a bad dream...You're not alone now, don't worry":
            award heart ri
            ri "I'm glad you're being so supportive..."
            ri "You really know just what to say to cheer me up"
            ri "Your words are a great comfort to me"
        "Snap out of it and tell me what's going on":
            ri "Ah yes, of course..."
            ri "I must have made you uncomfortable,  I'm sorry"
            ri "It won't happen again, I promise..."
    ri "I get like this from time to time"
    ri "I'm sure you guys don't know this but..."
    ri "I get like this from time to time"
    ri "This time, it was a nightmare and and..."
    ri "I really wish this didn't happen..."
    ri "Must be a side-effect of staying cooped up in this apartment all the time"
    ri "Yes, that must be it..."
    msg ri "I should really get out more..." sigh_m
    ri "If anyone sees this, please know that I am perfectly fine"
    ri "This will all pass soon enough..."
    ri "I'm being silly aren't I?"
    ri "I'll just go ahead and delete these messages, don't want anyone to feel uncomfortable..."
    ri "What was that command again...?"

    enter chatroom z

    ri "I'll consult the manual Luciel gave me, hold on..."
    msg z "What is going on here?" ser1
    menu:
        "Hello Zen! Rika was just a bit shaken up, that's all!":
            award heart ri
            z "I still don't understand"
            z "{image=zen_confused}"(img=True)
        "Oh thank god, this conversation was getting sooo suffocating":
            break heart ri
            z "Omg really?"
            z "What happened in here lol?"
        "Hi Zen~ How is rehersal going?":
            award  heart z
            z "It's been going great! Thanks for asking!"
            z "{image=zen_glow}"(img=True)
    ri "I found it!!!! Great! Now all I gotta do is..."
    ri "..."
    z "Lol, hi Rika!"
    ri "Um,,, Hello Zen!"
    z "Did I come at a bad time?"
    ri "Oh no, not at all, it's just that.."
    z "Wait , hold on, I'll just read the log"
    show shake
    msg ri "WAIT; HOLD ON" bold
    show shake
    ri " 'TASKKILL /IM 'CHATLOG067' "
    z "Okay, I'm back! I read everything and.."
    z "um...what are you doing Rika?"
    msg ri "It didn't work...." ser1
    msg ri "It's..it's nothing Zen, don't worry ^^" sigh_s
    z "How can I not? Are you okay there?"
    ri "Oh yes, I am, don't worry about it!"
    z "You sure? You seem pretty shaken up, even now"
    z "That must have been one hell of a nightmare huh?"
    ri "Yeah,  I guess it was.."
    z "I mean, you're always so composed, seeing you like that was so..."
    menu:
        "I know right? Can't believe she'd open up the floodates like that because of some dumb nightmare":
            break heart ri
            msg ri "I knew it... It only made you guys uncomfortable" bold
            z "No, that's not what I meant!"
        "It must have been quite the shock, but Rika's feelings are more important in a situation like this":
            award heart ri
            award heart z
            ri "...thank you.."
            z "Yeah, that's what I was getting at"
    ri "I wish I reacted to it better..."
    msg z "Hey now! You can't control stuff like that. These things just happen sometimes" glow
    ri "Yeah, you may have a point..."
    z "Of course I do! "
    z "Tell you what..."
    msg z "I may deliver that surprise for you and Jaehee earlier than intended..." flower_m
    ri "{image=rika_shock}"(img=True)
    ri "You shouldn't do that just because I had my little hissy fit.."
    msg z "Nope, it's no use! I've already decided~" glow
    z "You deserve it! The party planning is stressing you out, and I just know this'll fix you right up"
    z "Watch out you two! This'll take some time to arrange but..."
    z "I bet the both of you will LOVE it!"
    ri "Thank you Zen.."
    msg ri "That means a lot!" glow
    ri "{image=rika_happy}"(img=True)
    z "Now that's the Rika I know!"
    menu:
        "What about me? Why won't I get a gift?":
            z "Um, no offense, but we kind of don't know each other well enough for that"
            z "{image=zen_angry}"(img=True)
            ri "Don't worry, I'll fix something up for you the next time we meet ^^"
        "Why don't you give a gift to Vanderwood as well?":
            award heart va
            z "Whaaa? That guy??? No way in hell"
            ri "Let's be nice , he might be reading this..."
        "I'm so glad Rika is getting the recongition she deserves":
            award heart ri
            msg ri "Oh my...thank you for thinking so highly of me" glow
            ri "I'm glad we're able to get along this well..."
    z "Anywaysm,, I hope my gift cheers you up!"
    z "Now go to bed! You clearly need some more sleep"
    z "I'll head off to make sure your surprise is right on time. Goodbye!"

    exit chatroom z

    ri "And he's gone..."
    ri "That gift ...awfully kind of him, don't you think?"
    ri "About the whole nightmare thing..."
    ri "Say...do you think I overreacted ?"
    menu:
        "That's what I've been telling you the whole time.":
            ri "So you think so too?"
            ri "I guess I should be more aware of the feelings of others..."
        "No! I think you handled yourself the best you could":
            award heart ri
            msg ri "Thank you!~" glow
            ri "{image=rika_flirt}"(img=True)
            ri "I'm lucky you were here to help me along"
    ri "I should probably doze off back to dreamland now..."
    ri "Good night!!!"

    exit chatroom ri

    return


label cd4_chat2_expired():

    $ ri.status = "..."

    scene night
    play music looking_for_happiness

    enter chatroom ri

    msg ri "Is anyyone there?" bold
    msg ri "Jaehee, [name], anyone..." glow
    msg ri "Am I really alone ?" ser1
    ri "RFA...at a time like this.."
    ri "No no what am I saying...it's not you guys' fault Im..:"
    ri "....I woke up and everything felt so wrong and"
    ri "No one was there, and it was just like this and I"
    ri "I dont want taht to happen I dontwant to"
    ri "....I should "
    ri " Snap out of it and tell you what's going on"
    ri "I'm sure you guys don't know this but..."
    ri "I get like this from time to time"
    ri "This time, it was a nightmare and and..."
    ri "I really wish this didn't happen..."
    ri "Must be a side-effect of staying cooped up in this apartment all the time"
    ri "Yes, that must be it..."
    msg ri "I should really get out more..." sigh_m
    ri "If anyone sees this, please know that I am perfectly fine"
    ri "This will all pass soon enough..."
    ri "I'm being silly aren't I?"
    ri "I'll just go ahead and delete these messages, don't want anyone to feel uncomfortable..."
    ri "What was that command again...?"
    ri "It was in  that manual Luciel gave me....."
    msg z "What is going on here?" ser1
    z "What happened ?"
    ri "I found it!!!! Great! Now all I gotta do is..."
    ri "..."
    z "Lol, hi Rika!"
    ri "Um,,, Hello Zen!"
    z "Did I come at a bad time?"
    ri "Oh no, not at all, it's just that.."
    z "Wait , hold on, I'll just read the log"
    show shake
    msg ri "WAIT; HOLD ON" bold
    show shake
    ri " 'TASKKILL /IM 'CHATLOG067' "
    z "Okay, I'm back! I read everything and.."
    z "um...what are you doing Rika?"
    msg ri "It didn't work...." ser1
    msg ri "It's..it's nothing Zen, don't worry ^^" sigh_s
    z "How can I not? Are you okay there?"
    ri "Oh yes, I am, don't worry about it!"
    z "You sure? You seem pretty shaken up, even now"
    z "That must have been one hell of a nightmare huh?"
    ri "Yeah,  I guess it was.."
    z "I mean, you're always so composed, seeing you like that was so..."
    ri "...I know right? Can't believe I opened up the floodates like that because of some dumb nightmare"
    msg ri "I knew it... It only made you uncomfortable" bold
    ri "I wish I reacted to it better..."
    msg z "Hey now! You can't control stuff like that. These things just happen sometimes" glow
    ri "Yeah, you may have a point..."
    z "Of course I do! "
    z "Tell you what..."
    msg z "I may deliver that surprise for you and Jaehee earlier than intended..." flower_m
    ri "{image=rika_shock}"(img=True)
    ri "You shouldn't do that just because I had my little hissy fit.."
    msg z "Nope, it's no use! I've already decided~" glow
    z "You deserve it! The party planning is stressing you out, and I just know this'll fix you right up"
    z "Watch out you two! This'll take some time to arrange but..."
    z "I bet the both of you will LOVE it!"
    ri "Thank you Zen.."
    msg ri "That means a lot!" glow
    ri "{image=rika_happy}"(img=True)
    z "Now that's the Rika I know!"
    z "Anyways,, I hope my gift cheers you up!"
    z "Now go to bed! You clearly need some more sleep"
    z "I'll head off to make sure your surprise is right on time. Goodbye!"

    exit chatroom z

    ri "And he's gone..."
    ri "That gift ...awfully kind of him, don't you think guys?"
    ri "About the whole nightmare thing..."
    ri "I guess I should be more aware of the feelings of others..."
    ri "..."
    ri "I should probably doze off back to dreamland now..."
    ri "Good night!!!"

    exit chatroom ri

    return



label after_cd4_chat2:

    compose text ri:
        ri "Hello...I wasn't able to sleep, so I wanted to text you"
        ri "I hope this doesn't make you uncomfortable"
        ri "After that rant I had and all."
        label my_reply_1

    return

label my_reply_1:
    menu:
        "No, I wanted to talk to you more! You seemed unwell...":
            award heart ri
            ri "You're so kind, you know that, right?"
        "I did get kind of bored...":
            ri "I knew it...I'm sorry..."
    ri "I'll make sure our next conversation is bathed in the glow of happiness"


    return
