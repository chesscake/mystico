label cd3_chat8():
    #title: dark magic

    $ ri.status = "Do witches dream of bats instead of sheep?"
    $ ri.prof_pic = "Profile Pics/Rika/rika-8.jpg"
    $ ri.cover_pic = "Cover Photos/Rika/r6.jpg"

    $ ju.cover_pic = "Cover Photos/Jumin/ju4.jpg"
    $ ju.status = "Dark magic is just below the surface."

    scene night
    play music lonesome_practicalism

    ju "Good evening"
    menu:
        "You again? Just like I predicted!":
            award heart ju
            ju "Of course"
            msg ju "Seems like you noticed the pattern" glow
            ju "I was just about to talk about that"
        "Hello Jumin":
            ju "Hello [name]"
            ju "Glad to see my monologue will have an audience "
    ju "It's been a long  day..."
    ju "However, I am very glad to  be back into the messenger"
    ju "Some of you might have noticed something about my participation"
    msg ju "These late night chats are becoming more frequent" ser1
    ju "I suppose it will help the other members get to know cultures they know little to nothing about"
    msg ju "Travelling...it soothes the soul" glow
    ju "That's what V always says anyway"
    ju "I'm inclined to agree, seeing as oftentimes, a well-travelled man is a cultured man"
    ju "Sometimes I wonder how common people get around not having the funds to travel"
    menu:
        "We manage! Just interacting with differents kinds of people is enough ":
            award heart ri
            ju "I suppose that might be enough for some people"
            ju "For me however...seeing things for myself is half the fun"
        "Even rich people don't get to explore the world all the time ":
            award heart va
            ju "I suppose some truly do not"
            msg ju "How uncouth though..." bold
        "I have no idea. Travelling completes us!":
            award heart ju
            ju "I fully agree"
            msg ju "A life spent in one place is no life at all" glow
    ju "Whatever the case might be, I would reccomend that everyone who is able should travel as much as possible"
    ju "During my trip around Europe, I met some of the strangest, yet supremely interesting people"
    ju "Such people include many celebrities, CEOs, even salt of the earth working class people...they can all contain this mystical air around them"
    enter chatroom ri
    ri "Hello there you guys!"
    ri "I hope I'm not interrupting something here ;;;"
    ri "I've noticed we've been bumping into each other a lot these days Jumin"
    ju "Hello there Rika. Pleasure seeing you here"
    menu:
        "Hello Rika! So good to see you":
            award heart ri
            ri "Awww shucks! Thank you guys"
            msg ri "Aren't you the sweetest?"  glow
        "Hello. What have you been up to?":
            award heart va
            ri "Ah, you know..."
            msg ri "This and that! Mostly preparing for the party" ser1
    ri "Glad to see you both in here!"
    ri "I scrolled up and..."
    msg ri "I see culture hour with Jumin Han continues yet again~" spike_m
    ju "That's an apt thing to call it I suppose"
    ju "You came at just the right time. I was discussing the mystical auras certain people have about them"
    ju "I believe you've experinced such a phenomenon, considering you have something close to it"
    msg ri "Ah, I suppose I am a little unusal" sigh_s
    ju "I meant it as a good thing. Your aura of positiviy is one of your stand-out features"
    ri "I don't think that's the case... It's easy to put on a friendly disposition, especially when surrounded by people like the R.F.A"
    menu:
        "It's the truth! That demeanor is what drew me to here in the first place":
            award heart ri
            msg ri "Why thank you [name]..." glow
            ri "It means a lot!"
        "Are you sure an aura like that actually a good thing?":
            ju "I would consider it one"
            ri "Ah, [name] probably has her reasons for thinking of it in that way"
            msg ri "Though I doubt I could even come close to having an aura like that" ser2
    msg ri "Anyways..." sigh_s
    ri "What was it you wanted to talk about Jumin?"
    ju "Well..the talk about auras was only a jumping off point. You see, I came across some very strange people during my travels"
    ri "Ah yes...You talked to us about a few of the more interesting ones"
    ju "Yes, that's right. Europe is filled with them. Some even practice the dark arts, and that's always amusing"
    ri "Oh yes, you do seem to have taken to learning more about that sort of thing. Like that dark magic book V got you"
    ju "I've read it cover to cover over three times at this point. It's come in handy in everyday life. If only I could figure out how to make Zen more prone to the charm of cats"
    ri "Jumin ;;;;"
    msg ju "I apologize. Regardless, I'm sure any spell I'd throw at him would bounce off of him like water off a ducks back" bold
    ju "Ahem....While trying to find out more about this little hobby of mine, I came across this organization of people passionate about performing helpful deeds  for the good of the world"
    ju "They even wrote one of the books in my collection. Quite a remarkable group they are"
    ri "Wow, what kind of people are they?"
    msg ju "Witches" square_s
    ri "!?!"
    ju "Yes, it came as a shock to me too. Their organization has branches all over the world. I met up with the London representative today to question her about about their work"
    ju "They're annoyed when people compare them to that childrens' book"
    ri "The one about the boy wizard trapped in an attic?"
    ju "Yes. I don't recall the author of that work"
    ri "If you can't remember, it's probably not important ^^"
    ri "But...wow, do people like that really exist? That reminds me of Zen's newest play"
    menu:
        "Witches are scary":
            award heart v
            ju "That's a valid view of them. Though these ones were quite different"
            ri "I....like witches ^^"
        "Witches seem like really interesting people":
            award heart ri
            ju "What an interesting way of looking at them"
            msg ri "I agree! ~ I think they're just misunderstood" spike_l
        "I don't believe in stuff like that lol":
            award heart va
            ju "I like examining the supernatural"
            ri "I don't neccesarily believe in magic either...But it's fun to think about"
    ju "Regardless of your opinion of them, I think they'd make interesting guests for the party"
    ri "Yes, I agree!~ They could engage in conversation with some of other guests. I heard some of the reccomendations were quite...interesting"
    ju "What do you think [name]?"
    menu:
        "I like them! We should keep them in mind" :
            award heart ri
            ju "I will ask Assistant Kang to contact them"
            msg ri "Thank you so much for inviting them ^^" glow
        "I don't think they'd fit into the party theme":
            ju "Fair enough"
            ri "Well...Please send them my contact information Jumin"
            ju "Of course"
    ri "I'd love to have more guests at this party~"
    ju "That's a noble goal Rika"
    ri "^^"
    ri "Say Jumin...did those people  have any black cats with them?"
    ju "No. I wouldn't have suggested them if they did. Don't want Luciel messing with them"
    msg ju "That would be a cat-astrophe @Rika" square_m
    ri "Hehe, that's funny Jumin ^^"
    ju "Well then...I guess it's time for me to take my leave"
    ju "Goodbye Rika and [name]"
    exit chatroom ju
    ri "Ah yes..I guess I should leave too"
    ri "All this talk about witches.."
    ri "I wonder why the world sees them all as evil.."
    ri "I hope Zen's play doesen't have such a view on them. The comic book didn't so..fingers crossed"
    ri "I'll leave now I suppose.."
    ri "Thank you for listening to me ^^"
    menu:
        "Goodbye Rika ~ Don't let the witches get you!":
            award heart v
            ri "Heh, that's kind of funny"
            ri "But you don't have to worry about that"
        "Bye bye~ May the witches  of the world look over you":
            award heart ri
            ri "I'm sure they will! "
            ri "..I think I know one such kind witch myself heh"
    ri "Goodbye then! Take care!"
    exit chatroom ri

    return




label cd3_chat8_expired():

    $ ri.status = "Do witches dream of bats instead of sheep?"
    $ ri.prof_pic = "Profile Pics/Rika/rika-8.jpg"
    $ ri.cover_pic = "Cover Photos/Rika/r6.jpg"

    $ ju.cover_pic = "Cover Photos/Jumin/ju4.jpg"
    $ ju.status = "Dark magic is just below the surface."

    scene night
    play music lonesome_practicalism

    ju "Good evening"
    ju "It's been a long  day..."
    ju "However, I am very glad to  be back into the messenger"
    ju "Some of you might have noticed something about my participation"
    msg ju "These late night chats are becoming more frequent" ser1
    ju "I suppose it will help the other members get to know cultures they know little to nothing about"
    msg ju "Travelling...it soothes the soul" glow
    ju "That's what V always says anyway"
    ju "I'm inclined to agree, seeing as oftentimes, a well-travelled man is a cultured man"
    ju "Sometimes I wonder how common people get around not having the funds to travel"
    ju "Whatever the case might be, I would reccomend that everyone who is able should travel as much as possible"
    ju "During my trip around Europe, I met some of the strangest, yet supremely interesting people"
    ju "Such people include many celebrities, CEOs, even salt of the earth working class people...they can all contain this mystical air around them"
    enter chatroom ri
    ri "Hello there!"
    ri "I hope I'm not interrupting something here ;;;"
    ri "I've noticed we've been bumping into each other a lot these days Jumin"
    ju "Hello there Rika. Pleasure seeing you here"
    ri "I scrolled up and..."
    msg ri "I see culture hour with Jumin Han continues yet again~" spike_m
    ju "That's an apt thing to call it I suppose"
    ju "You came at just the right time. I was discussing the mystical auras certain people have about them"
    ju "I believe you've experinced such a phenomenon, considering you have something close to it"
    msg ri "Ah, I suppose I am a little unusal" sigh_s
    ju "I meant it as a good thing. Your aura of positiviy is one of your stand-out features"
    ri "I don't think that's the case... It's easy to put on a friendly disposition, especially when surrounded by people like the R.F.A"
    msg ri "Anyways..." sigh_s
    ri "What was it you wanted to talk about Jumin?"
    ju "Well..the talk about auras was only a jumping off point. You see, I came across some very strange people during my travels"
    ri "Ah yes...You talked to us about a few of the more interesting ones"
    ju "Yes, that's right. Europe is filled with them. Some even practice the dark arts, and that's always amusing"
    ri "Oh yes, you do seem to have taken to learning more about that sort of thing. Like that dark magic book V got you"
    ju "I've read it cover to cover over three times at this point. It's come in handy in everyday life. If only I could figure out how to make Zen more prone to the charm of cats"
    ri "Jumin ;;;;"
    msg ju "I apologize. Regardless, I'm sure any spell I'd throw at him would bounce off of him like water off a ducks back" bold
    ju "Ahem....While trying to find out more about this little hobby of mine, I came across this organization of people passionate about performing helpful deeds  for the good of the world"
    ju "They even wrote one of the books in my collection. Quite a remarkable group they are"
    ri "Wow, what kind of people are they?"
    msg ju "Witches" square_s
    ri "!?!"
    ju "Yes, it came as a shock to me too. Their organization has branches all over the world. I met up with the London representative today to question her about about their work"
    ju "They're annoyed when people compare them to that childrens' book"
    ri "The one about the boy wizard trapped in an attic?"
    ju "Yes. I don't recall the author of that work"
    ri "If you can't remember, it's probably not important ^^"
    ri "But...wow, do people like that really exist? That reminds me of Zen's newest play"
    ri "I....like witches ^^"
    ju "What an interesting way of looking at them"
    msg ri "I think they're just misunderstood" spike_l
    ju "Regardless of your opinion of them, I think they'd make interesting guests for the party"
    ri "Yes, I agree!~ They could engage in conversation with some of other guests. I heard some of the reccomendations were quite...interesting"
    ri "Please send them my contact information Jumin"
    ju "Of course"
    ri "I'd love to have more guests at this party~"
    ju "That's a noble goal Rika"
    ri "^^"
    ri "Say Jumin...did those people  have any black cats with them?"
    ju "No. I wouldn't have suggested them if they did. Don't want Luciel messing with them"
    msg ju "That would be a cat-astrophe @Rika" square_m
    ri "Hehe, that's funny Jumin ^^"
    ju "Well then...I guess it's time for me to take my leave"
    ju "Goodbye Rika and [name]"
    exit chatroom ju
    ri "Ah yes..I guess I should leave too"
    ri "All this talk about witches.."
    ri "I wonder why the world sees them all as evil.."
    ri "I hope Zen's play doesen't have such a view on them. The comic book didn't so..fingers crossed"
    ri "I'll leave now I suppose.."
    ri "Goodbye then! Take care!"
    exit chatroom ri

    return
