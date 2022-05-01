label cd2_chat6():
#new arrival
    $ ri.prof_pic = "Profile Pics/Rika/rika-6.jpg"
    $ va.prof_pic = "Profile Pics/Vanderwood/va-1.webp"

    $ ri.cover_pic = "Cover Photos/Rika/r4.jpg"

    $ ri.status = "Uncertainity sure is a scary thing..."
    $ va.status = "Contact me only if something goes wrong"

    scene noon
    play music looking_for_happiness

    ri "I have been busier than usual"
    msg ri "I would have been delighted to be the first one to greet you in the app" glow
    msg ri "Nice to meet you, Vanderwood" bold cloud_m
    va "hey"

    menu:
        "Hello, Rika! I am glad to see you! ^^":
            award heart ri
            msg ri "hello, [name]!" glow big ser2
            ri "I'm happy to see you too ^^"
            ri "Let us both welcome Vanderwood!"
        "Hello there, Vanderwood. ":
            va "Hi."
            ri "So shy..."
        "Hello, both of you.":
            award heart va
            ri "Hi, hi, [name] ^^"
            va "Hello, [name] =)"
            ri "You seem to be in a good mood? ^^"
            va "I just like it when I'm not singled out lol"

    ri "I saw your chats earlier with V and Zen"
    ri "You seem rather eccentric, but..."
    ri "We all are in one way or another,"
    ri "so don't worry about it!"
    ri "{image=rika_happy}" (img=True)
    msg ri "The RFA will welcome you for the time being until Luciel is back" square_l ser1
    va "I am not exactly the best at first impressions like you"
    va "I see how you set your limits already,"
    va "I respect that"

    menu:
        "That's a relief, you don't need to get too close.":
            va "Don't worry, I won't if you don't want me."
            show banner well
            msg ri "please let's keep up a nice atmosphere between all members..." curly sigh_l
        "As long as you help us, you're welcome in the RFA for the time being.":
            award heart ri
            ri "Yes, that's it."
            ri "We are thankful for your help Vanderwood."
        "You're here because of Luciel's recommendation, so if he trusts you, trust us.":
            award heart va
            va "I'm mostly here because of V."
            va "And what you asked is easier said than done,"
            msg va "I'm trying though..." curly


    msg va "But I can assure you I am here taking my job seriously" glow ser2
    msg ri "Ah, you don't have to be so stiff ;;" curly
    ri "You can relax"
    ri "Luciel submitted this information about you."
    ri "cg va_2" (img=True)
    msg ri "I like your handwritting a lot!" bold
    ri "You said you're small and shy"
    ri "And that you like country music."
    msg va "SAY WHAT!?" blocky big glow
    msg va "I'LL GET HIM FOR THIS!" blocky big glow
    ri "{image=rika_what}" (img=True)
    ri "I see you're shy, but not quiet."
    msg ri "It's okay you lie a bit about your age, I understand."
    ri "I am sure Luciel has told you a lot about us already"
    va "not really"
    ri "Well,"
    msg ri "he didn't say anything about you either so I guess we are even :)" sser1
    ri "Let's talk, Mr. Stranger."
    va "wow, lady"
    va "You have some sass in you"
    va "I like that"
    va "I expected you to be some kind of Bisney princess, not gonna lie"
    msg ri "B-Bisney princess? ;;" curly sigh_s

    menu:
        "But Rika IS trying to help others with the RFA currently. Has the world turned too cold that charity seems unreal to you?":
            award heart ri
            ri "{image=rika_wow}" (img=True)
            va "Maybe my vision is a bit more cynical,"
            va "but don't let me stop you from that."
            va "I liked your retort, [name]"
            award heart va
            va "You have guts, I give you that."

        "Hey! Don't insult Rika ):<":
            va "But I'm not insulting her..."
            ri "Well, being a princess is not necessarily a bad thing..."
            msg ri "No matter what kind of woman you are..." ser2
            msg ri "a demure princess,"  glow ser2
            msg ri "a valiant Knight.." glow ser2
            msg ri "I believe they can all fend for themselves in their own ways" flower_m ser2
            msg ri "The comparison caught me off guard is all ^^;" curly

        "Didn't 707 say he was the princess of the RFA already?":
            award heart s
            ri "Yes, he did."
            ri "We should not take that title away from him heh"
            va "what the..."
            va "No, I won't ask."

    msg va "Hey, I'm not being condescending saying that" glow curly
    va "from what I read on that article you sure seemed like that"
    va "V looked pretty unrealistic himself too,"
    msg va "with that bubblegum hair..." curly
    ri "His hair IS quite unusual.."

    timed menu:
        msg ri "Then again, so is mine heh ;" curly
        msg ri "I guess we are both kind of unusual" curly
        "Your hair is funny too, Vanderwood!":
                va "Yes, well"
                va "707 cuts my hair"
                va "And I cut his..."
                ri "How cute, you sound like good friends!"
                msg va "More like enemies" glow ser2
                ri "Hahaha! ^^"
        "Rika's hair is majestic!":
                msg ri "It gets frizzy sometimes;;" curly
                ri "But thanks, [name] ^^"

    msg ri "Anyways..." glow
    ri "Ah, so you learned about us already..."
    ri "But not from Luciel?"
    msg va "I appreciate it when a person is this sharp" ser2 glow

    menu:
        "I would feel more comfortable working with people I know personally.":
            award heart ri
            ri "Me too, but I know I can trust Luciel"
            ri "so let us not worry that much."
        "I would like to know more about you too, Vanderwood.":
            award heart va
            va "I'm the IT person, that's it for now..."
            va "but we have time to learn about each other lol"
        "I can be sharp too!":
            ri "Oh my, so enthusiastic!"
            ri "You just sounded like Yoosung now,"
            award heart y
            msg ri "how cute ^^" glow


    va "I found this article about you on a magazine"
    va "cg ri_2" (img=True)
    msg ri "Oh, that one!" cloud_s bold
    msg ri "I have that one saved in my notebook!" glow bold
    ri "the original interview was longer but"
    ri "They had to cut it short for the article"
    ri "It's a pity I can't get a copy of the whole conversation"
    msg ri "It's sure a moment I will treasure in my heart" glow
    va "Yes, just like a Bisney Princess..."
    ri "Hm.."
    msg ri "I hope I am not being too direct right now but..." ser2
    msg ri "You said that you didn't want to sound condescending..." ser2
    ri "But I feel a bit of .... unfriendliness in your words perhaps"
    ri "As if you want to set boundaries with us.."
    ri "I assure you,"
    msg ri "there is no need for that!" big bold
    ri "I am so very glad to have another new member here!"
    ri "even if it turns out to be temporary"
    ri "I just don't want to alienate you too much"
    ri "It might feel like we belong to two different worlds,"
    ri "but I hope to bridge that gap soon ^^"

    menu:
        "There is nothing suspicious about us!":
            va "If you need to say something is not suspicious then it sounds like it is lol"
            msg va "I must be looking suspicious myself atm lol ;;" glow curly
        "Take your time to get to know us, you will see you can trust us.":
            award heart va
            va "It's what I will do, thank you."
        "Rika, you seem to know how to handle all kinds of people. ":
            award heart ri
            ri "{image=rika_love}" (img=True)
            ri "You're making me blush, [name]!"
            ri "Thank you?"
            ri "I am just treating Vanderwood like any other party guest,"
            ri "nothing you or anyone else can't do."

    va "hey,"
    va "I don't have anything against you or the ones like you"
    va "but it is true that we belong to different worlds"
    ri "Like darkness and light?"
    va "Ah, no ;;"
    va "More like people who belong in a group"
    msg va "and the ones who don't" glow bold
    ri "You might not be an official permanent RFA member..."
    ri "However, that doesn't mean we will kick you out"
    msg ri "I want to create an air of comfort and peace within the RFA." ser2
    msg ri "Where we can all belong without keeping up harmful appearances" ser2
    msg ri "A world where you can be accepted just as you are" ser2
    msg va "Yes, but that only works with people who can adjust well" glow bold ser1
    show banner well
    msg va "You should see my coworkers to tell how and why they shouldn't be considered lol" curly
    ri "But Luciel is one of your co-workers!"
    msg ri "And he fits in well in our world..." round_l big bold
    msg ri "So you can too ~" bold glow
    va "yes, Luciel might be different to all my fellows"
    va "NGL I thought he was joking when he mentioned he was in some charity group"
    ri "Why is that?"
    msg va "Oh." curly
    msg va "He..." curly
    va "{=curly} he jokes a lot haha ;; {/=curly}" (pauseVal=3.0)

    menu:
        "How come then Luciel didn't tell you about the RFA?":
            va "Maybe he might have told me and I forgot..."
        "I am really curious about the kind of working environment you work in...":
            award heart va
            va "Lmao, no you don't"
            va "the less you know the better when it comes to our job"
            va "I'm surrounded by clowns"
            va "And I feel one myself, sometimes"
            timed menu:
                ri "That sounds a bit harsh."
                ri "You really ARE Luciel's coworker ):"
                "Quit your job, lol":
                    va "Hah! I wish it was so easy."
                    ri "I want to do something to help you two!"
                    va "lol, thanks,"
                    va "we are fine though."
                "You're not a clown!":
                    award heart va
                    va "Thanks, [name]"
                    va "Finally someone that doesn't agree with me on that"
                    ri "Does Luciel call you clown?"
                    msg va "Not to my face, but he treats me like one" sigh_l curly

        "I think a world like Rika described is attainable! I also wish for other people's happiness!":
            award heart ri
            msg ri "It's so reassuring to hear those words from you, [name]!" glow
            msg ri "We can work to make it happen! ^^" sser2 big square_l
            ri "{image=rika_party}" (img=True)

    va "It's been nice talking to you"
    va "I have to go take a call from my boss now"
    ri "please, call me Rika."
    ri "I hope we can get along ^^"
    va "Me too"

    exit chatroom va

    ri "[name], thank you for being here with me,"
    ri "I think we started a bit stiff"
    ri "but I'm sure that we will be safe thanks to Luciel's decision of leaving Vanderwood with us."
    ri "I hope you didn't feel uncomfortable."

    menu:
        "Luciel didn't say he would leave a temporal replacement. V said he called Vanderwood himself.":
            break heart v
            ri "Yes..."
            ri "I also read V's chat."
            ri "V called Vanderwood but I was not told beforehand."
            ri "we should talk."
        "Not at all! I got to see how you handle difficult people live.":
            award heart ri
            ri "That's a relief,"
            ri "I want you to feel comfortable always."
        "I think I like Vanderwood already.":
            award heart va
            ri "I think he actually makes strong first impressions, heh"
        "Can we trust 707's judgement? I mean, is he trust worthy?":
            break heart s
            msg ri "Yes, he is." big bold  glow
            msg ri "I would trust him with my life." glow ser2
            ri "After all, I met him before V"
            ri "Luciel is like family to me."
            ri "I am sure he would give his best for the RFA,"
            ri "and that might include Vanderwood's recommendation..."

    ri "I have to leave for now."
    ri "Have a nice day, [name]!"
    exit chatroom ri

    return

label cd2_chat6_expired():

    $ ri.prof_pic = "Profile Pics/Rika/rika-6.jpg"
    $ va.prof_pic = "Profile Pics/Vanderwood/va-1.webp"

    $ ri.cover_pic = "Cover Photos/Rika/r4.jpg"

    $ ri.status = "Uncertainity sure is a scary thing..."
    $ va.status = "Contact me only if something goes wrong"

    scene noon
    play music looking_for_happiness

    ri "I have been busier than usual"
    msg ri "I would have been delighted to be the first one to greet you in the app" glow
    msg ri "Nice to meet you, Vanderwood" bold cloud_m
    va "hey"
    ri "I saw your chats earlier with V and Zen"
    ri "You seem rather eccentric, but..."
    ri "We all are in one way or another,"
    ri "so don't worry about it!"
    ri "{image=rika_happy}" (img=True)
    msg ri "The RFA will welcome you for the time being until Luciel is back" square_l ser1
    va "I am not exactly the best at first impressions like you"
    va "I see how you set your limits already,"
    va "I respect that"
    msg va "But I can assure you I am here taking my job seriously" glow ser2
    msg ri "Ah, you don't have to be so stiff ;;" curly
    ri "You can relax"
    ri "Luciel submitted this information about you."
    ri "cg va_2" (img=True)
    msg ri "I like your handwritting a lot!" bold
    ri "You said you're small and shy"
    ri "And that you like country music."
    msg va "SAY WHAT!?" blocky big glow
    msg va "I'LL GET HIM FOR THIS!" blocky big glow
    ri "{image=rika_what}" (img=True)
    ri "I see you're shy, but not quiet."
    msg ri "It's okay you lie a bit about your age, I understand."
    ri "I am sure Luciel has told you a lot about us already"
    va "not really"
    ri "Well,"
    msg ri "he didn't say anything about you either so I guess we are even :)" sser1
    ri "Let's talk, Mr. Stranger."
    va "wow, lady"
    va "You have some sass in you"
    va "I like that"
    va "I expected you to be some kind of Bisney princess, not gonna lie"
    msg ri "B-Bisney princess? ;;" curly sigh_s
    msg va "Hey, I'm not being condescending saying that" glow curly
    va "from what I read on that article you sure seemed like that"
    va "V looked pretty unrealistic himself too,"
    msg va "with that bubblegum hair..." curly
    ri "His hair IS quite unusual.."
    msg ri "Then again, so is mine heh ;" curly
    msg ri "I guess we are both kind of unusual" curly
    msg ri "Anyways..." glow
    ri "Ah, so you learned about us already..."
    ri "But not from Luciel?"
    msg va "I appreciate it when a person is this sharp" ser2 glow
    va "I found this article about you on a magazine"
    va "cg ri_2" (img=True)
    msg ri "Oh, that one!" cloud_s bold
    msg ri "I have that one saved in my notebook!" glow bold
    ri "the original interview was longer but"
    ri "They had to cut it short for the article"
    ri "It's a pity I can't get a copy of the whole conversation"
    msg ri "It's sure a moment I will treasure in my heart" glow
    va "Yes, just like a Bisney Princess..."
    ri "Hm.."
    msg ri "I hope I am not being too direct right now but..." ser2
    msg ri "You said that you didn't want to sound condescending..." ser2
    ri "But I feel a bit of .... unfriendliness in your words perhaps"
    ri "As if you want to set boundaries with us.."
    ri "I assure you,"
    msg ri "there is no need for that!" big bold
    ri "I am so very glad to have another new member here!"
    ri "even if it turns out to be temporary"
    ri "I just don't want to alienate you too much"
    ri "It might feel like we belong to two different worlds,"
    ri "but I hope to bridge that gap soon ^^"
    va "hey,"
    va "I don't have anything against you or the ones like you"
    va "but it is true that we belong to different worlds"
    ri "Like darkness and light?"
    va "Ah, no ;;"
    va "More like people who belong in a group"
    msg va "and the ones who don't" glow bold
    ri "You might not be an official permanent RFA member..."
    ri "However, that doesn't mean we will kick you out"
    msg ri "I want to create an air of comfort and peace within the RFA." ser2
    msg ri "Where we can all belong without keeping up harmful appearances" ser2
    msg ri "A world where you can be accepted just as you are" ser2
    msg va "Yes, but that only works with people who can adjust well" glow bold ser1
    msg va "You should see my coworkers to tell how and why they shouldn't be considered lol" curly
    ri "But Luciel is one of your co-workers!"
    msg ri "And he fits in well in our world..." round_l big bold
    msg ri "So you can too ~" bold glow
    va "yes, Luciel might be different to all my fellows"
    va "NGL I thought he was joking when he mentioned he was in some charity group"
    ri "Why is that?"
    msg va "Oh." curly
    msg va "He..." curly
    va "{=curly} he jokes a lot haha ;; {/=curly}" (pauseVal=3.0)
    va "It's been nice talking to you, lady"
    va "I have to go take a call from my boss now"
    ri "please, call me Rika."
    ri "I hope we can get along ^^"
    va "Me too"

    exit chatroom va
    exit chatroom ri

    return
