label cd2_chat9():

    $ ri.status = "I'm up for it Jaehee! Let's discuss"
    $ y.status = "So many choices..."

    $ y.cover_pic = "Cover Photos/Yoosung/y2.jpg"

    scene evening
    play music same_old_fresh_air

    msg ri "It's been a long day for me..." sigh_l curly
    ri "But!"
    msg ri "I see Jaehee has suggested a hang out session" glow ser1
    ri "Of course I'll come!"
    msg ri "I love talking to her" bold big
    ri "{image=rika_happy}" (img=True)
    ri "Just call me as soon as you see this Jaehee"
    ri "We could organize a nice hang out through text too!"
    ri "Sorry for making plans like this."
    ri "We don't want to exclude you guys,"
    ri "Next time, we should all come together!"
    msg ri "After we meet in person, that is ^^" glow

    menu:
        "Hello.":
            ri "Hello!"
        "Hi Rika~ How are you?":
            ri "{image=rika_happy}" (img=True)
            ri "I'm fine, how about you?"
            menu:
                "I'm fine, thanks! ^^":
                    award heart ri
                    ri "That makes me happy"
                "I kinda expected to see someone else in the chat. Maybe Vanderwood!":
                    award heart va
                    ri "Oh."
                    ri "{image=rika_cry}" (img=True)
                    ri "I guess I'll make my talk brief..."
        "I felt excluded by Jaehee ):":
            break heart ja
            ri "I'm sure Jaehee didn't mean anything bad"
            ri "She is just shy."
            ri "Give her some time to warm up to you, [name]"
            ri "She needs time to get used to the messenger too!"


    ri "I just came back from talking with some potential guests for the new party.."
    ri "It's a lot of work"
    ri "But..."
    msg ri "I'm glad we are having another one!" glow ser2
    ri "So soon after the last one too.."
    msg ri "I've been thinking on how to improve the parties..." ser1
    msg ri "But I can't settle on just one thing" ser1
    ri "Mind helping me out with this?"

    menu:
        "I don't have any ideas either":
            ri "That's okay!"
            ri "I'll just have to try harder!"
        "Maybe we should try inviting guests from various groups of people.":
            award heart ri
            ri "All sorts of people should be able to attend"
            msg ri "I don't want the parties to become..." ser2
            msg ri "Some sort of elite club" ser2
            msg ri "They're meant for everyone ^^" ser2 square_m
        "Shouldn't you be doing that?":
            break heart ri
            ri "{image=rika_what}" (img=True)
            ri "I want all members to participate"
            ri "In the decision-making process"
            msg ri "We are all friends here ^^" glow


    ri "I'm curious about what the other members have to say"
    ri "Especially our newest official members"
    ri "That would be Jaehee and [name] ^^"
    ri "They only recently joined"
    ri "But they've been making a real effort"
    enter chatroom y
    msg ri "I hope we can all grow closer ^^" glow ser1 big
    y "Hello there!"

    timed menu:
        ri "hello there Yoosung ~"
        ri "I don't see you here much these days"
        "Hello Yoosung!":
            y "Hello,[name]!"
            award heart y
        "I wanted to chat with Rika alone ):":
            y "Am I interrupting?"
            ri "Not at all, Yoosung!"
            msg ri "You can always call or text me for that, [name]" glow

    y "I'm usually busy with studying"
    y "But I came here to chat with you"
    ri "Yes, I love talking with you too"
    ri "And I'm sure the others do as well"
    ri "Since you're the best little cousin ^^"
    y "Thank you Rika"
    y "{image=yoosung_thankyou}" (img=True)
    y "I just wish we could hang out more"
    y "Will we go to that place Jaehee suggested too?"
    ri "We will!"
    ri "And I'll make sure to help you out"
    ri "As soon as you graduate!"
    msg ri "I want to see you succeed" glow
    ri "And I'm sure you will ^^"
    y "Only if you're there Rika"
    y "I hope you'll have time"
    y "I was surprised to see you agree to hang out with her so fast"
    y "You said you were too busy visit me these days."
    ri "Ah, that's because..."
    y "Are you uncomfortable to visit my family?"

    menu:
        "Yoosung, please don't pressure her if she doesn't want to.":
           award heart ri
           y "Am I pressuring her?"
           msg y "I didn't meant to!" curly glow
           y "{image=yoosung_cry}" (img=True)
           ri "It's okay"
           msg ri "It didn't feel like that to me!" big glow
           ri "Please don't be sad, Yoosung!"
        "Are you avoiding Yoosung?":
           break heart ri
           msg ri "No!" ser1
           ri "Please don't say such things, [name]"
           ri "{image=rika_cry}" (img=True)
           ri "It would hurt me to see him sad!"


    y "I know your side of the family is estranged"
    y "But that shouldn't bother you!"
    ri "No, I uhm"
    ri "I didn't want to distract you from studying"
    ri "And my schedule doesn't match V's thesedays..."
    y "Yes, I didn't insist much"
    y "Since you also have to worry about the party"
    msg y "But you promised to visit me with V and Jumin after my exams are done!" ser2 glow
    y "I can't wait"
    y "I can maybe go back to help with the preparations again so you can stay longer than usual!"
    ri "Um...."
    ri "You don't have to worry about those things ^^"
    ri "[name] has been helping me out"
    ri "And as for V.."
    y "What is it ?"
    msg ri "Ah, its nothing ^^;" curly
    ri "You don't have to worry about that"
    y "If you say so..."
    y "You sound sort of sad"

    timed menu:
        ri "It must be your imagination haha ^^;"
        "Maybe she needs some time to think.":
            award heart ri
            y "I see."
            ri "Thank you, [name]"
        "You sound annoying, Yoosung.":
            break heart ri
            y "{image=yoosung_cry}" (img=True)
            break heart y
            ri "Yoosung is just worried."
            ri "Please, don't say such cruel things, [name]"

    ri "Anyways.."
    ri "Are there any hobbies you've gotten yourself into Yoosung ?"
    ri "I know you used to cross-stich"
    y "I don't really have the time"
    y "I'm putting all my efforts"
    y "Into getting into university"
    ri "Yes but..."
    ri "you should still think about it"
    ri "Studying all the time isn't good either"
    ri "Hmm..."
    ri "What do you think, [name]?"

    menu:
        "Gaming!":
            award heart y
            y "I know a couple of my school friends"
            y "Are super into this one game"
            y "I think it's name is LOLOL?"
            ri "Well, that sounds fun! ^^"
        "Reading comics!":
            y "I read romance ones already heh"
            ri "Me too!"
            msg ri "My favorite is 'Beware of the Villaness who turns the Marionettes upside down!'" glow ser2
            y "I still have to catch up with 'Who made you a lovely Princess?'"
            ri "yes! I like that one too!"
        "Watching Anime":
            ri "I already watch some!"
            msg ri "My favorite is 'Princess Chu Chu: Soldier of the Moon!'" ser1 glow
            msg ri "Does that sound too childish?" curly
            y "Not at all!" (PauseVal=3.0)
            ri "{image=rika_happy}" (img=True)
        "Watching Musicals!":
            award heart ja
            msg y "I don't think that's my style." curly
            ri "Yes"
            ri "I already tried inviting Yoosung to Zen's musicals"
            msg ri "Not his cup of tea, heh" sigh_m
        "Watching Dramas!":
            y "I already watch some!"
            ri "Don't! they are a bad influence for you!"
            msg ri "What if some day you want to slap someone with Kimchi?" curly glow
            y "I bet it would be fun lol"
            ri "haha ^^"
        "Maybe he should try volunteering?":
            award heart ri
            ri "He already does volounteer work with me"
            ri "But I'm really glad you suggested that ^^"
            ri "You seem very compassionate"



    ri "Whatever you decide on doing, Yoosung.."
    msg ri "I hope it makes you happy ^^" glow
    y "Thank you"
    y "{image=yoosung_thankyou}" (img=True)
    y "I'll try to find something after my exams are over"
    y "I have to go now Rika"
    y "I have a big exam coming up"
    ri "I'm sad to see you go"
    ri "I wish we could talk more..."
    y "It's alright!"
    y "Don't be sad!"
    y "I will be sad if you're too"
    ri "Yes, I guess you're right."
    ri "I should keep on being a good example."
    msg ri "Let's cheer up, Yoosung" glow big
    y "{image=yoosung_yahoo}" (img=True)
    ri "{image=rika_party}" (img=True)
    y "I'll call you as soon as I'm done!"
    ri "Thank you Yoosung ^^"
    ri "Good luck ~"
    exit chatroom y
    ri "Yoosung has always been so careful around me"
    ri "I appreciate his efforts to make me happy"
    ri "But I think what I need might be.."
    msg ri "Someone closer to my own world ^^" big bold ser2

    menu:
        "I want to be that person!":
            award heart ri
            ri "{image=rika_wow}" (img=True)
            ri "Is that so?"
            msg ri "I hope you can become that person for me then!" glow
        "You sound like a person with a world full of secrets.":
            award heart v
            ri "Do you think so?"
            ri "V has told me the same but..."
            ri "I really want the RFA be part of it sooner or later."
        "I hope you can find that person one day":
            ri "I already did once, I think."
            ri "I just have to find her again."
            menu:
                "Who?":
                    ri "Ah."
                    ri "No one."

    ri "Um... anyways"
    ri "I'll have to go too."
    ri "See you soon RFA ~"
    ri "Goodbye~"
    exit chatroom ri

    return

label cd2_chat9_expired():

    $ ri.status = "I'm up for it Jaehee! Let's discuss"
    $ y.status = "So many choices..."

    $ y.cover_pic = "Cover Photos/Yoosung/y2.jpg"

    scene evening
    play music same_old_fresh_air

    msg ri "It's been a long day for me..." sigh_l curly
    ri "But!"
    msg ri "I see Jaehee has suggested a hang out session" glow ser1
    ri "Of course I'll come!"
    msg ri "I love talking to her" bold big
    ri "{image=rika_happy}" (img=True)
    ri "Just call me as soon as you see this Jaehee"
    ri "Next time you might also offer to hang out through text"
    ri "Maybe"
    ri "So no one feels excluded"
    ri "Oh, no one else is in here..."
    ri "I just came back from talking with some potential guests for the new party.."
    ri "It's a lot of work"
    ri "But..."
    msg ri "I'm glad we are having another one!" glow ser2
    ri "So soon after the last one too.."
    msg ri "I've been thinking on how to improve the parties..." ser1
    msg ri "But I can't settle on just one thing" ser1
    ri "Mind helping me out with this you guys?"
    ri "All sorts of people should be able to attend"
    msg ri "I don't want the parties to become..." ser2
    msg ri "Some sort of elite club" ser2
    msg ri "They're meant for everyone ^^" ser2 square_m
    ri "I want all members to participate"
    ri "In the decision-making process"
    msg ri "We are all friends here ^^" glow
    ri "I'm curious about what you guys have to say"
    ri "Especially our newest official members"
    ri "That would be Jaehee and [name] ^^"
    ri "They only recently joined"
    ri "But they've been making a real effort"
    enter chatroom y
    msg ri "I hope we can all grow closer ^^" glow ser1 big
    ri "Oh, hello there Yoosung ~"
    ri "I don't see you here much these days"
    y "I'm usually busy with studying"
    y "but I came here to chat with you"
    y "I see no one got here before me!"
    ri "Yes, I love talking with you too"
    ri "And I'm sure the others do as well"
    ri "Since you're the best little cousin ^^"
    y "Thank you Rika"
    y "{image=yoosung_thankyou}" (img=True)
    y "I just wish we could hang out more"
    y "Will we go to that place Jaehee suggested too?"
    ri "We will!"
    ri "And I'll make sure to help you out"
    ri "As soon as you graduate!"
    msg ri "I want to see you succeed" glow
    ri "And I'm sure you will ^^"
    y "Only if you're there Rika"
    y "I hope you'll have time"
    y "I was surprised to see you agree to hang out with her so fast"
    y "You said you were too busy visit me these days."
    ri "Ah, that's because..."
    y "Are you uncomfortable to visit my family?"
    y "I know your side of the family is estranged"
    y "But that shouldn't bother you!"
    ri "No, I uhm"
    ri "I didn't want to distract you from studying"
    ri "And my schedule doesn't match V's thesedays..."
    y "Yes, I didn't insist much"
    y "Since you also have to worry about the party"
    msg y "But you promised to visit me with V and Jumin after my exams are done!" ser2 glow
    y "I can't wait"
    y "I can maybe go back to help with the preparations again so you can stay longer than usual!"
    ri "Um...."
    ri "You don't have to worry about those things ^^"
    ri "[name] has been helping me out"
    ri "And as for V.."
    y "What is it ?"
    ri "Ah, its nothing ^^"
    ri "You don't have to worry about that"
    y "If you say so..."
    y "You sound sort of sad"
    ri "It must be your imagination haha ^^;"
    ri "Anyways.."
    ri "Are there any hobbies you've gotten yourself into Yoosung ?"
    ri "I know you used to cross-stich"
    y "I don't really have the time"
    y "I'm putting all my efforts"
    y "Into getting into university"
    ri "Yes but..."
    ri "you should still think about it"
    ri "Studying all the time isn't good either"
    ri "Hmm..."
    y "I know a couple of my school friends"
    y "Are super into this one game"
    y "I think it's name is LOLOL?"
    ri "Well, that sounds fun! ^^"
    ri "Whatever you decide on doing.."
    msg ri "I hope it makes you happy ^^" glow
    y "Thank you"
    y "{image=yoosung_thankyou}" (img=True)
    y "I'll try to find something after my exams are over"
    y "I have to go now Rika"
    y "I have a big exam coming up"
    ri "I'm sad to see you go"
    ri "I wish we could talk more..."
    y "It's alright!"
    y "Don't be sad!"
    y "I will be sad if you're too"
    ri "Yes, I guess you're right."
    ri "I should keep on being a good example."
    msg ri "Let's cheer up, Yoosung" glow big
    y "{image=yoosung_yahoo}" (img=True)
    ri "{image=rika_party}" (img=True)
    y "I'll call you as soon as I'm done!"
    ri "Thank you Yoosung ^^"
    ri "Good luck ~"
    exit chatroom y
    ri "Yoosung has always been so careful around me"
    ri "I appreciate his efforts to make me happy"
    ri "But I think what I need might be.."
    msg ri "Someone closer to my own world ^^" big bold ser2
    ri "Um... anyways"
    ri "I'll have to go too."
    ri "See you soon RFA ~"
    ri "Goodbye~"
    exit chatroom ri

    return


label cd2_chat9_incoming_ri:

    ri "Hello! It's me, Rika!"

    ri "I hope you can hear me , as I am in the middle of the city right now"

    ri "True to my word, I am attempting to gather guests for the party"

    ri "I just spoke with representatives of several charity organizations!"

    ri "They were delighted to be invited to the party"

    ri "I was so glad to see that word of the R.F.A had already spread so far"

    ri "It is moments like this that make me realize how famous we have gotten"
    menu:
        extend''
        "That's a bit conceited":
            ri "Ah, I did not mean it that way..."
        "Wow, that is really cool":
            ri "You really think so?"

    ri "I only meant that..."

    ri "The words of people like that are what keep me going"

    ri "I don't know where I would be without such supportive people around me"

    ri "Such as the R.F.A , the people from my local cathedral and you of course"

    ri "You are all a part of this amazing feeling I have"
    menu:
        extend''
        "You are the reason we are here in the first place":
            ri "That might be true but... I'm still really glad."
        "Will that feeling last forever?":
            ri "Well...I hope so"

    ri "I love seeing everyone smiling and being happy"

    ri "It's amazing what a little kindness can do for a person"

    ri "We talked about studies with Yoosung"

    ri "I loved learning about different cultures and people while I was in school"

    ri "I could have made it far , if I had the will to socialise with my classmates.."

    ri "Regardless, I graduated with honours, and was one of the students with the best grades"

    ri "I was thinking of pursing medicine or social studies before V happened"

    ri "That reminds me... One of my classmates became an astronaut"

    ri "He now grows an amoeba colony on Mars"

    ri "Maybe we can talk about old times at the party"

    ri "Should I get him in touch with you?"
    menu:
        extend''
        "Good idea! Invite him":
            ri "I will get in touch then"
        "He sounds too silly. Pass":
            ri "Hmm, alright then"
    ri "Anyway, I should hang up now."

    ri "I want to talk more but..duty calls"

    ri "Please have a wonderful day!"

    return



label cd2_chat9_vn_ri():

    scene cafe with fade
    play music lonesome_practicalism
    pause

    "Two hours later"

    show rika happy at vn_right
    show jaehee glasses neutral at vn_left

    ri "After that little curfuflle in the line, I was surprised we still had a chance to reserve a table after all"
    ja "Yes, the barista didn't look too pleased when the people behind us skipped the line"
    ri "We still managed to snag this table, so jokes on them haha"
    ri "Back to what I was saying.."
    ri "I'm so glad we can meet up like this from time to time Jaehee!"
    ri "Jumin loves giving you overtime"
    ri "So I'm not surprised your only chances at respite are when he's off travelling" 
    ja "Mr. Han occasionally grants me time off work"
    ja "Of course,  I have to make up for it as soon as it's over"
    show jaehee glasses sad
    ri "That's such a shame.... What does Jumin usually make you do?"
    show rika neutral
    ri "I know he can be quite demanding"
    ja "You got that right. Mr. Han is  rather specific about the way he wants things to be done"
    ja "I mostly do my duties as an assistant, as well as taking care of Elizabeth. However, my job is open-ended - there is no one thing I have to do"
    ja "For example, Mr.Han could call an unplanned bussines meeting, and I have to move his schedule around to account for it, as well as making myself available "
    ja "I also  have to make sure that Elizabeth's status is known at all times"
    ja "And whenever he wants me to stand in for him at meetings, he'll just come up to my desk and take me there himself"
    ri "Oh my! It seems like you're always doing something or other for our dear friend Jumin"
    ri "I wonder what made him like Elizabezh so much...."
    ri "Of course, I'm glad to hear how invested he is in her and her needs but"
    ri "Sometimes I feel guilty about giving him that cat."
    ri "At the time, it seemeded like a great idea. He was so lonely, and I had to do something about it"
    ri "I didn't account for the fact that his employees might have to take over her care in his absence"
    ri "I think the fact he trusts you with Elizabeth shows that he knows how reliable you are"
    ri "However...is it really worth all that extra work?"
    ja "Don't worry too much about me."
    show jaehee glasses happy
    ja "I'll manage. You had the best intentions at heart when you gave him Elizabeth."
    ja "I'm glad to see how caring you are towards your friends"
    ri "Why thank you Jaehee! I'm so glad that you of all people have such a high opinion of me, even though we met not too long ago"
    ri "Just know that I will always be your friend, no matter what happens."
    ja "I think that  it has taken me some time to get used to having such a close female friend. I only recently joined , due to Mr.Han of course, but I feel very welcome in this association"
    ri "Hmm...Don't think of it like that ! I wanted you to be a part of the RFA too. You have so much potential. I could see it from the moment I met you"
    ri "Hmmm..This migh seem silly and a bit off-topic but...do you think the RFA can truly help people? I've been having some doubts recently and I'm not sure if we are doing enough"
    ri "Do you have any suggestions as to what you want us to do next?"
    show jaehee glasses neutral
    ja "Well, I can't say I thought about that much. I feel as though the RFA is doing what it was intended for. I'm not exactly sure what else can be done. Sorry about that"
    ri "Oh, no matter! It's just me having my silly little thoughts again, please don't mind!"
    show rika happy
    ri "I asked you that because...I have always been amazed at what you've done with your life after your parents...weren't there anymore"
    ja "It really shows how strong of a person you really are!"
    ja "Thank you. I'm glad you see that in me, though I just did what I had to. My mother taught me how to stand on my own, even after her passing"
    ri "Oh yes, your mother...she seemed like a wonderful woman!I'm sad I never got to meet her. I think I could learn a lot from someone like that"
    ja "And she would be flattered to hear it. She was always interested in charity work and helping those less fortunate than us"
    ja "I think she would have liked you. Come to think of it...she did meet someone who resembled you a bit."
    ri "Oh really ? Who might that be ?"
    show rika neutral
    show jaehee glasses neutral
    ja "Well...it was the nurse who took care of her after her accident. She had quite a strong personality"
    ja "The details are fuzzy in my mind but..."
    ja "I remeber that she had long blond hair, and extremely striking eyes, as well as being extremely personable"
    ja "Come to think of it...she resembled you quite a bit!"
    ja "Her name was somewhat unusual, it didn't sound fully Korean, though I might have been imagining it"
    show rika thinking
    ri "How interesting! Do you perhaps remember what it sounded like?"
    ja "It's been a long time since that day and my memory might be messing with me but...I remember it being quite different than any I've heard before."
    ja "The thing that sticks out in my mind the most is the way her eyes lit up whenever she talked about her little sister and how much she missed her"
    ja "I never thought to ask exactly why she wasn't able to see her anymore"
    ri "..."
    show jaehee glasses surprised
    ja "Oh, I'm sorry!I don't want to make you sad with my story! Should we change the subject?"
    ri "Nurse...little sister...I wonder.."
    ja "What was that? Sorry, I can't quite hear you Rika! Your voice seems to be trembling a little, and all this chatter around is making it hard to make out"
    show rika neutral
    ri "Oh, It's  nothing...I just got lost in thought, pay it no mind.."
    ri "Um....You know what? Let's take a photo to commemorate this new chapter of the RFA Jaehee! So that we can  remember this moment! Always and forever"

    return
