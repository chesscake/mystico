label cd3_chat3():

    $ v.status = "Change is inevitable."
    $ v.prof_pic = "Profile Pics/V/v-9.jpg"
    $ v.cover_pic = "Cover Photos/V/v4.jpg"

    $ ri.status = "How time flies..."

    scene noon
    play music looking_for_happiness

    y "Hello, [name] and Rika!"
    y "I can't wait anymore!"
    msg ri "Do you mean the upcoming party!?" glow bold
    ri "{image=rika_party}" (img=True)
    y "it was mostly waiting for the exam season to be over"
    y "But yes,"
    msg y "I am also excited for the second RFA party!" glow
    y "{image=yoosung_yahoo}" (img=True)

    menu:
        "I'm also doing my best for the party!":
            award heart ri
            ri "{image=rika_happy}" (img=True)
        "I don't know what to expect from the party":
            ri "Uh? Why is that?"
            menu:
                "I don't like going to parties that much. I like to lay low":
                    award heart va
                    ri "I see."
                    ri "You know?"
                    ri "Luciel doesn't come to all parties either"
                    msg ri "But his help in the RFA is still most appreciated!" glow ser2 big
                    ri "Just take it easy, [name]"
                    ri "We understand we are all different!"
                "I am an introvert.":
                    ri "I see."
                    ri "You don't need to talk to guests when you're at the party."
                    ri "That's my job!"
                    ri "{image=rika_happy}" (img=True)
                    ri "You can relax and take it easy after working this much to invite them."
                "I never went to a charity party.":
                    ri "That makes it more exciting then!"
                    ri "You will probably love them!"
                    y "I agree!"
                    msg y "The food and drinks are delicious!" glow
                    msg y "And you can meet different groups of people!" glow
                    ri "Right he is."

    ri "I'm so excited about it!"
    ri "I can't believe its almost here "
    ri "Time is slowly running out..."
    ri "I feel like..."
    ri "There should be moments in our lives that we could hold onto forever."
    ri "For me, preparing for parties is one such moment"
    ri "Would there be any way to turn a few seconds into eternity "
    y "Yes, but when it's exam season it should be over asap"
    y "{image=yoosung_huff}" (img=True)

    enter chatroom v

    ri "Hello, V"
    y "Hello, V"

    timed menu:
        msg y "Jinx!" bold
        "Hello V":
            msg y "Double Jinx!" glow blocky
            award heart y
            y "{image=yoosung_wow}" (img=True)
            ri "{image=rika_happy}" (img=True)
        "Hi.":
            y "Almost a double Jinx"
            y "{image=yoosung_huff}" (img=True)
            ri "Maybe next time, Yoosung."
            msg ri "Don't give up!"

    v "hello ^^"
    v "I'm glad you are happy about the coming party"
    v "I was reviewing the collection that we will be auctioning."
    ri "Yes, I wonder how people will react to them.."
    msg ri "Some of my favorite pieces are on that list~" cloud_m sser2
    ri "Some I haven't seen in a while!"
    msg ri "Can't wait to experience again the feelings they brought out " bold
    y "I want to help more with the preparations for the party"
    msg y "Maybe even talk to some guests!" glow ser1
    y "I will be less busy after exams and the festival activities"
    v "{image=v_shock}" (img=True)
    v "that's too many responsibilities"
    y "Yes, I'm the class rep"
    msg ri "Don't worry, Yoosung." glow big
    msg ri "I know you need to focus on your studies for now" ser1
    msg ri "It's your future on the line,"  ser1
    msg ri "and all on your shoulders too..." ser1
    ri "Do tell me if it gets too difficult to bare."
    ri "I could arrange a small hangout for the two of us to wind down..."
    ri "or even help you study!"
    ri "I know a thing or two myself you know? ^^"
    v "That probably won't be necessary Rika"
    v "But I do agree."
    v "your studies should come first"

    menu:
        "Don't try to take away my job as party coordinator, Yoosungie 0.<":
            y "{image=yoosung_what}" (img=True)
            msg y "I wasn't trying to do so!" blocky glow
            ri "[name] is clearly joking, Yoosung, heh"
        "V, will you show me your works?":
            award heart v
            v "It could be a nice chance for you and Rika to come visit me."
            msg ri "Maybe another time." curly sigh_s
        "Rika, tell me what you think when you review the works! ^^":
            award heart ri
            msg ri "That would be my pleasure! ^^ " glow


    v "You can take care of these tasks one after the other, Yoosung ^^"
    ri "Right!"
    ri "Besides..."
    ri "While your help is highly appreciated,"
    ri "I can always ask the others!"
    msg ri "Nowadays, that duty would mostly be [name]'s~" square_l sser2 big
    ri "[name]'s help has motivated me to go bigger for this party,"
    ri "and I really hope to achieve what we set out to do"
    v "Yes, I can see [name] has had a great impact on you"

    menu:
        "Why is that? What did i do?":
            ri "You're inspiring to me! ^^"
        "I could say the same about you, Rika. The RFA wouldn't exist without you.":
            award heart ri
            ri "You're making me blush, [name]"
            ri "{image=rika_love}" (img=True)
        "The RFA grew bigger because of everyone's compromise.":
            award heart va
            ri "Yes, exactly."
            ri "I agree, everyone's work is important."
            ri "From the ones that stand in the light being social"
            ri "To those ones working behind curtains like Luciel"


    msg y "I hope I can make Rika proud once I have more time to dedicate to the party preparations!" cloud_l bold
    ri "Yoosung..."
    msg ri "I am already so proud of you!" glow bold
    ri "You're the best little cousin a girl could ask for"
    ri "But"
    ri "The RFA parties are not made for me alone.. "
    ri "It's true charity work that makes me feel happy,"
    ri "and helps spread that feeling around"
    ri "But you shouldn't do this for my sake alone ;;"
    y "oh."
    msg y "Maybe I phrased it wrongly!" sigh_m curly
    msg y "sorry!" glow blocky
    y "I don't want to feel that I'm not helping!"
    msg y "I feel the most motivated when I think about you" ser2
    ri "There is no need for you to apologize"
    ri "I didn't intend to come across as scolding you."
    msg ri "I'm sorry" sigh_s
    ri "I understand you didn't mean anything bad by it.."
    msg ri "Whatever you choose to do should come from your own convictions and beliefs! ^^" glow ser1
    ri "and your convictions come from within your heart"
    ri "That applies to everything."
    ri "For example."
    msg ri "Yoosung, choose your career to be happy yourself!" glow

    menu:
        "But the world isn't so nice. You adjust to the ones you need or want to impress.":
            award heart va
            ri "{image=rika_what}" (img=True)
            ri "The RFA is actually trying to make the world a bit nicer though."
            ri "So everyone can be happy!"
        "Yoosung, please don't do things because you want to impress Rika. You might regret it later!":
            award heart ri
            y "But I chose my major to help people like her."
            ri "Yes, but..."
            ri "I am me."
            ri "And those people are those people."
            msg ri "Choose something that makes YOU happy ^^" ser1 glow

    v "Rika, you just sounded as if you were Yoosung's mom ^^"
    y "{image=yoosung_what}" (img=True)
    msg y "She is nothing like my mom though!" blocky
    y "I thought you already knew my mom?"
    v "{image=v_well}" (img=True)
    msg v "Now I am the one that is phrasing what I meant wrong haha ^^;;" curly
    msg v "It's just that her words are reminiscent of someone who inspired me profoundly" ser1 glow
    v "Which reminds me"
    v "I contacted my sign language teacher as I thought she could be interested in our party"
    ri "Mhm~"
    msg ri "That sounds great! ^^ " cloud_s

    menu:
        "Yes! let's invite the teacher!":
           award heart v
           ri "Alright!"
           award heart ri
           ri "I really think such a person could help widen the scope of the types of people we are inviting"
           ri "I'm glad I can count on [name]'s help for situations like this~"
        "I will think about it.":
           ri "I will leave it in your hands, [name]"

    y "Sign Language?"
    y "{image=yoosung_question}" (img=True)
    y "I didn't know you knew sign language, V"
    v "I don't, but for some time I was interested in learning"
    v "Although, maybe it was already too late"
    msg ri "It is never late to learn something new~" glow bold
    v "Yes, you are right..."
    v "Although I lack the motivation I had before"
    y "So that means you wanted to learn sign language to talk with someone you can't see anymore?"
    msg y "Could that person be related to V's comment about Rika being like a mother?" glow bold
    msg ri "Yoosung, you're so sharp~" cloud_m
    ri "My my, how you've grown up!"
    msg ri "Detective Yoosung is on the case +_+" blocky
    ri "It seems you really can do anything you want!"
    ri "Your potential is endless at this stage "
    v "I agree on that, you can do anything if you put your mind and heart onto it"
    v "{image=v_smile}" (img=True)
    y "{image=yoosung_wow}" (img=True)
    y "I would rather have V being more direct with his answers"
    y "I don't like to guess everything like this"
    msg y "What if I don't find the answers sometime and when I realize it's too late?" sigh_l curly
    ri "{image=rika_happy}" (img=True)
    ri "I doubt that will ever happen, you are rather reliable and smart..."
    ri "That's what I think anyways "
    y "Thank you Rika!"
    y "{image=yoosung_thankyou}" (img=True)

    menu:
        "V, I don't think you should project your feelings towards your mother onto Rika.":
            award heart ri
            v "{image=v_well}" (img=True)
            v "I don't think that is the case"
            msg v "But thanks for your genuine concern, [name]" glow
            v "I might be working myself wrong today."
        "I wish to learn some sign language":
            ri "Is that so?"
            ri "Vanderwood mentioned she knew some during a call with me."
            ri "You should talk to her! ^^"
        "The worst part of that would be that no one would listen to you, Yoosung.":
            ri "That sounds sad"
            ri "{image=rika_cry}" (img=True)
            ri "Like the myth of Kassandra"
            ri "In greek mythology, she was a priestess"
            ri "But no one believed her predictions."
            y "{image=yoosung_cry}" (img=True)
            msg y "I hope you believe me at least, [name] " glow big


    y "My mom just called me, I have to go now but"
    y "I'll be back soon!"
    y "bye for now!"
    exit chatroom y

    play music i_draw

    v "I want to ask you something personal, Rika" (pauseVal=5.0)

    timed menu:
        v "That is"
        v "If [name] is not uncomfortable"
        "Should I leave you two alone?":
            v "Do you wish to leave?"
            menu:
                "Yes.":
                    v "I see."
                    v "Take care, [name]"
                    ri "See you later, [name]"
                    v "I will call you, Rika."
                    exit chatroom m

                    return

                "No":
                    v "I will be brief then."

        "I'm fine. Carry on.":
           v "Well, then."


    v "Is it true that I am not clear when I speak about something?"
    ri "Sometimes I feel as if you don't let yourself be direct or let your feelings be known..."
    ri "I think that's because you think about how others will perceive you,"
    msg ri "perhaps to an extreme." bold
    v "I think you have a way of understanding people that goes beyond words"
    ri "My understanding..."
    ri "Maybe it comes from accepting all the negative things about life"
    msg ri "Pain," ser2
    msg ri "suffering," ser2
    msg ri "sadness," ser2
    msg ri "melancholy..." ser2
    msg ri "Everyone has felt like that at one point in their lives." glow ser2

    menu:
        "Rika, it seems you let yourself be hurt to help others.":
           award heart ri
           ri "Do you think so?"
           ri "I really never saw it that way"
        "Sadness can be beautiful too. I use those feelings to inspire my art.":
           award heart V
           v "we might be similar a lot, [name]"
           v "I see why Rika has taken to you."
           ri "Maybe that might be it."
        "Don't let your life become a tragedy for others' sake. Your life should be yours, even if you help others":
           award heart va
           ri "Yes, you might be right, [name]"

    v "Is sadness a means to appreciate happiness to you, Rika?"
    ri "yes, I firmly believe that."
    ri "That's why it feels safe to reach out and lend a helping hand "
    v "But I wish you are never sad."
    v "And that I could make you happy."
    ri "Sometimes I am..."
    ri "I can't just pretend I'm happy forever"
    ri "and if I can use these feelings as my motivation"
    msg ri "Perhaps we can make this world at least that much better by helping others" cloud_m ser2
    v "It sounds like you depend on negative emotions"
    ri "If i could, I want to save people from them."
    msg ri "There is nothing I wish more than that." glow ser2

    menu:
        "You can't force people to be happy or sad to your convenience. Feelings come and go naturally.":
            award heart ri
            ri "I feel suffocated sometimes if I have to wear a happy mask."
            ri "I want to be in a world surrounded by truth."
            ri "Even if it turns to be an ugly truth."
            menu:
                "I also feel that honesty is the best policy":
                    award heart ri
                    ri "We are the same, [name]"
                    ri "It's important to be surrounded by people who accept you"
                    ri "And that want to improve with you."
                    ri "Working together to be happy."
                "Sometimes keeping appearances for the happiness of others is necessary":
                    ri "I see..."
                    ri "I also think so..."
                    ri "But it gets tiring..."
        "Rika, I see V is trying to make you happy. You should accept what he wants for you.":
            award heart v
            ri "I..."
            ri "Need some time."
            v "My photo collection will be waiting and so will I"
            v "{image=v_smile}" (img=True)


    v "Does saving others make you happy, Rika?"
    ri "If I was happy all the time,"
    ri "I would become insensitive"
    ri "I would be no one, nothing"
    ri "No one wants to be erased, abandoned or replaced"
    v "Does that mean that..."
    msg ri "Sorry for hanging you up with all this talk! " curly
    ri "It seems like I really have to go now"
    ri "I have to take this call."
    ri "It's from one of the potential guests..."
    msg ri "I think you'll find them quite intriguing everyone ~" round_l
    v "good luck, I hope we can talk later again ^^"
    v "I'll take my leave for now"
    ri "Take care then ~"
    v "Take care you two"
    exit chatroom v
    exit chatroom ri

    return

label cd3_chat3_expired():

    $ v.status = "Change is inevitable."
    $ v.prof_pic = "Profile Pics/V/v-9.jpg"
    $ v.cover_pic = "Cover Photos/V/v4.jpg"

    $ ri.status = "How time flies..."

    scene noon
    play music looking_for_happiness


    y "I can't wait anymore!"
    msg ri "Do you mean the upcoming party!?" glow bold
    ri "{image=rika_party}" (img=True)
    y "it was mostly waiting for the exam season to be over"
    y "But yes,"
    msg y "I am also excited for the second RFA party!" glow
    y "{image=yoosung_yahoo}" (img=True)
    ri "I'm so excited about it!"
    ri "I can't believe its almost here "
    ri "Time is slowly running out..."
    ri "I feel like..."
    ri "There should be moments in our lives that we could hold onto forever."
    ri "For me, preparing for parties is one such moment"
    ri "Would there be any way to turn a few seconds into eternity "
    y "Yes, but when it's exam season it should be over asap"
    y "{image=yoosung_huff}" (img=True)

    enter chatroom v

    ri "Hello, V"
    y "Hello, V"
    msg y "Jinx!" glow blocky
    y "{image=yoosung_wow}" (img=True)
    ri "{image=rika_happy}" (img=True)
    v "hello ^^"
    v "I'm glad you two are happy about the coming party"
    v "I was reviewing the collection that we will be auctioning."
    ri "Yes, I wonder how people will react to them.."
    msg ri "Some of my favorite pieces are on that list~" cloud_m sser2
    ri "Some I haven't seen in a while!"
    msg ri "Can't wait to rexperience the feelings they brought out " bold
    y "I want to help more with the preparations for the party"
    y "I will be less busy after exams and the festival activities"
    v "{image=v_shock}" (img=True)
    v "that's too many responsibilities"
    y "Yes, I'm the class rep"
    msg ri "Don't worry, Yoosung." glow big
    msg ri "I know you need to focus on your studies for now" ser1
    msg ri "It's your future on the line,"  ser1
    msg ri "and all on your shoulders too..." ser1
    ri "Do tell me if it gets too difficult to bare."
    ri "I could arrange a small hangout for the two of us to wind down..."
    ri "or even help you study!"
    ri "I know a thing or two myself you know? ^^"
    v "That probably won't be necessary Rika"
    v "But I do agree"
    v "your studies should come first"
    v "You can take care of these tasks one after the other ^^"
    ri "Besides..."
    ri "While your help is highly appreciated,"
    ri "I can always ask the others!"
    msg ri "Nowadays, that duty would mostly be [name]'s~" square_l sser2 big
    ri "[name]'s help has motivated me to go bigger for this party,"
    ri "and I really hope to achieve what we set out to do"
    v "Yes, I can see [name] has had a great impact on you"
    msg y "I hope I can make Rika proud once I have more time to dedicate to the party preparations!" cloud_l bold
    ri "Yoosung..."
    msg ri "I am already so proud of you!" glow bold
    ri "You're the best little cousin a girl could ask for"
    ri "But"
    ri "The RFA parties are not made for me alone.. "
    ri "It's true charity work that makes me feel happy,"
    ri "and helps spread that feeling around"
    ri "But you shouldn't do this for my sake alone ;;"
    y "oh"
    msg y "Maybe I phrased it wrongly!" sigh_m curly
    y "sorry!"
    y "I don't want to feel that I'm not helping!"
    msg y "I feel the most motivated when I think about you" ser2
    ri "There is no need for you to apologize"
    ri "I didn't intend to come across as scolding you,"
    msg ri "I'm sorry" sigh_s
    ri "I understand you didn't mean anything bad by it.."
    msg ri "Whatever you choose to do should come from your own convictions and beliefs!  ^^" glow ser1
    ri "and your convictions come from within your heart"
    v "Rika, you just sounded as if you were Yoosung's mom ^^"
    msg y "She is nothing like my mom though!" blocky
    y "I thought you already knew my mom?"
    v "{image=v_well}" (img=True)
    msg v "Now I am the one that is phrasing what I meant wrong haha ^^;;" curly
    msg v "It's just that her words are reminiscent of someone who inspired me profoundly" ser1 glow
    v "Which reminds me"
    v "I contacted my sign language teacher as I thought she could be interested in our party"
    ri "Mhm~"
    msg ri "That sounds great! ^^ " cloud_s
    ri "I really think such a person could help widen the scope of the types of people we are inviting "
    ri "I would love to reach out personally yet.."
    msg ri "My hands are full for the time being" sigh_m
    ri "I'm glad I can count on [name]'s help for situations like this~"
    y "Sign Language?"
    y "{image=yoosung_question}" (img=True)
    y "I didn't know you knew sign language, V"
    v "I don't, but for some time I was interested in learning"
    v "Although, maybe it was already too late"
    msg ri "It is never late to learn something new~" glow bold
    v "Yes, you are right..."
    v "Although I lack the motivation I had before"
    y "So that means you wanted to learn sign language to talk with someone you can't see anymore?"
    msg y "Could that person be related to V's comment about Rika being like a mother?" glow
    msg ri "Yoosung, you're so sharp~" cloud_m
    ri "My my, how you've grown up!"
    msg ri "Detective Yoosung is on the case +_+" blocky
    ri "It seems you really can do anything you want!"
    ri "Your potential is endless at this stage "
    v "I agree on that, you can do anything if you put your mind and heart onto it"
    v "{image=v_smile}" (img=True)
    y "{image=yoosung_wow}" (img=True)
    y "My mom just called me, I have to go now but"
    y "I would rather have V being more direct with his answers"
    y "I don't like to guess everything like this"
    y "What if I don't find the answers sometime and when I realize it's too late?"
    ri "{image=rika_happy}" (img=True)
    ri "I doubt that will ever happen, you are rather reliable and smart..."
    ri "That's what I think anyways "
    y "Thank you Rika! "
    y "{image=yoosung_thankyou}" (img=True)
    y "bye for now!"
    exit chatroom y

    play music i_draw

    v "I want to ask you something, Rika" (pauseVal=5.0)
    v "is it true that I am not clear when I speak about something?"
    ri "Sometimes I feel as if you don't let yourself be direct or let your feelings be known..."
    ri "I think that's because you think about how others will perceive you,"
    msg ri "perhaps to an extreme." bold
    v "I think you have a way of understanding people that goes beyond words"
    ri "My understanding..."
    ri "Maybe it comes from accepting all the negative things about life"
    msg ri "Pain," ser2
    msg ri "suffering," ser2
    msg ri "sadness," ser2
    msg ri "melancholy..." ser2
    msg ri "Everyone has felt like that at one point in their lives." glow ser2
    v "Is sadness a means to appreciate happiness to you?"
    ri "yes, I firmly believe that."
    ri "That's why it feels safe to reach out and lend a helping hand "
    v "But I wish you are never sad."
    v "And that I could make you happy."
    ri "Sometimes I am..."
    ri "I can't just pretend I'm happy forever"
    ri "and if I can use these feelings as my motivation"
    msg ri "perhaps we can make this world at least that much better by helping others" cloud_m ser1
    v "It sounds like you depend on negative emotions"
    ri "If i could, I want to save people from them."
    msg ri "There is nothing I wish more than that." glow ser2
    v "Does saving others make you happy?"
    ri "If I was happy all the time,"
    ri "I would become insensitive"
    ri "I would be no one, nothing"
    ri "No one wants to be erased, abandoned or replaced"
    v "Does that mean that..."
    msg ri "Sorry for hanging you up with all this talk! " curly
    ri "It seems like I really have to go now"
    ri "I have to take this call."
    ri "It's from one of the potential guests..."
    msg ri "I think you'll find them quite intriguing everyone ~" round_l
    v "good luck, I hope we can talk later again ^^"
    ri "Take care then ~"
    exit chatroom v
    exit chatroom ri

    return
