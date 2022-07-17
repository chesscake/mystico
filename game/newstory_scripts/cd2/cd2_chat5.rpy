label cd2_chat5():
    #art of tea

    $ ju.status = "Tea purifies the soul"

    $ ju.cover_pic = "Cover Photos/Jumin/ju3.jpg"

    scene noon
    play music urban_night_cityscape


    ju "Good Morning."
    ju "I just came back from a visit to the tea museum in London before going to France."
    ju "They had several exhibits on show, several of which piqued my interest. "
    ju "I see you're here too, [name]."
    menu:
        "Oh, I heard about that place before!":
            ju "Interesting. I was under the impression that not many people knew about it, since it's so small"
            award heart ju
            ju "I guess you're well-versed in subjects like this one"
        "I didn't know there was a tea museum out there.":
            ju "Yes, there is. As a person who frequently enjoys tea, getting to experience it was..."
            ju "Splendid would be the word I suppose"
    ju "The museum consists of several smaller rooms,"
    ju "with a large teahouse and teashop at its center. "
    ju "The exhibits are from all over the world... "
    ju "They display the history of tea in Europe,"
    ju "and the various ways of preparing it as well as tools used in the process."
    ju "I even saw some artifacts from Korea there."
    ju "It was an interesting place for sure."
    ju "What kinds of tea would you prefer? "
    menu:
        "Chamomile!":
            award heart v
            msg ju "Chamomile is V's favorite ." glow ser2
            ju "The brochure said that chanomile has a calming effect on the stomach and helps you fall asleep."
        "Mint!":
            award heart ri
            ju "Mint would be Rika's favorite."
            ju "The brochure said that it helps with respiratory issues, energises you and also freshens your breath. "
        "Black tea!":
            award heart ja
            ju "Assistant King prefers coffee but has Black tea whenever offered. "
            ju "The brochure said that black tea can lower cholesterol, help with coronary health and improve gut health."
        "Green tea!":
            award heart ju
            msg ju "Green tea would be my favorite." square_m ser1
            ju "The brochure said that green tea can improve brain function, has antioxidant properties, and has bioactive components."
        "Fruity tea!":
            award heart y
            ju "Fruit tea would be Yoosungs favorite."
            ju "The brochure said that fruity teas can often help with your mood, has plenty of vitamins and is full of antioxidants."
        "Roiboos tea!":
            award heart va
            ju "Finally, there is roiboos tea. I don't know anyone who favors that one."
            ju "The brochure said  that roiboos can prevent diabetes,  has an effect on heart disease and may also lower the chance of cancer "
    ju "Regardless, there was something there to suit anyone's interests."
    ju "Personally , I enjoyed walking around through the tea shop part the most "
    ju "Their business strategy is amazing . Perhaps it's something we should implement at C&R."
    ju "They entice you with the promise of tra all throughout the museum, then have a tea store waiting for you at the end . "
    ju "I was impressed and decided to meet up with the owner , and he seemed like a very interesting person "
    ju "He owns not only the museum and tea store , but  also runs a tea fanclub here in the U.K"
    ju "He would be an interesting guest to invite to the party"
    menu:
        "I'd love that. Please tell him to contact me":
            msg ju "I'm glad you seem interested" round_m
            ju "I'll rell Assistant Kang to get you in contact with him"
        "I don't really like tea. I'll pass on this one":
            ju "Alright then, it's your choice"
            ju "I'll double-check with Rika later"
    ju "The owner also said he would share some recipes with me "
    ju "Perhaps I will share them with the members..."
    enter chatroom ri
    ri "Oh my, so many messages."
    ri "Hello Jumin! Hi [name]!!!"
    menu:
        "Hello Rika, good to see you!":
            award heart ri
            ri "Good to see you too!"
            ju "It's nice to see you two getting along"
        "Hi":
            ri "Hi hi!"
            ju "A bit informal don't you think?"
            ri "Hehe, it's okay Jumin ^^;"
        "Say...where have you been?":
            award heart va
            ri "Me? Oh, nowhere really.."
            ri "I'm just taking a rest in my apartment"
    ri "I'm glad to see you back in here Jumin +_+"
    ju "We were talking about different types of tea."
    ri "Hehe, I enjoy most of them!"
    ri "Though.."
    msg ri "My favourite has always been mint, ever since I was a child " glow ser1
    ju "Did your parents give it to you a lot ?"
    ri "Um, something like that !"
    msg ri "The tea also reminds me of a very special person " cloud_l
    ju "I assume that would be V "
    ri "Well..."
    msg ri "him too I guess ^^" curly
    ri "Anyway..."
    ri "I love seeing how much fun you're having abroad "
    ri "That tea museum is such a clever idea too "
    ri "I want to visit it one day!"
    ju "You can, I'll book two tickets for V and you as soon as the party is done with ."
    ri "Oh, no need to rush!"
    ju "We can always do that later "
    ju "Alright then."
    ju "Just know that my help is always available."
    ri "Oh yes, I'm sure ^^"
    ri "All this talk about tea is making me crave it a bit.."
    ri "I should go make myself a cup "
    ju "Enjoy your tea."
    ju "I'll have the hotel staff make me some right now as well"
    ju "Then I shall leave."
    ju "Have a good day, both of you."
    exit chatroom ju
    ri "Ah, that was fast ..."
    ri "Jumin is really into travelling these days "
    ri "I love seeing him so energized "
    menu:
        "I do too! The R.F.A seems like such a happy place!":
            award heart ri
            msg ri "I'm so glad to hear you say that!!!" spike_s
            ri "I try my best to make the R.F.A the best it can be!"
        "You actually noticed a change? He seemed to be the same as he usually is.":
            ri "He has always been a bit mysterious when it came to his emotions."
            ri "But you learn to pick up subtle hints after being around him for a while."
    ri "I hope you  can become even closer to the RFA members from now on !"
    ri "This happy chatter I'm seeing these days..."
    ri "I really feel like the RFA is growing into something amazing ^^"
    ri "{image=rika_happy}" (img=True)
    ri "For now, I think I'll enjoy my tea "
    ri "I'll text you as soon as I'm done, so look out for that hehe"
    ri "Goodbye then! ~"
    exit chatroom ri

    return

label cd2_chat5_expired():

    $ ju.status = "Tea purifies the soul"

    $ ju.cover_pic = "Cover Photos/Jumin/ju3.jpg"

    scene noon
    play music urban_night_cityscape

    ju "Good Morning."
    ju "I just came back from a visit to the tea museum in London before going to France."
    ju "They had several exhibits on show, several of which piqued my interest. "
    ju "The museum consists of several smaller rooms,"
    ju "with a large teahouse and teashop at its center. "
    ju "The exhibits are from all over the world... "
    ju "They display the history of tea in Europe,"
    ju "and the various ways of preparing it as well as tools used in the process."
    ju "I even saw some artifacts from Korea there."
    ju "It was an interesting place for sure."
    ju "What kinds of tea would [name] prefer? "
    ju "My personal favorite is green tea"
    ju "There is something regal about it that appeals to me" square_m
    ju "Regardless, there was something there to suit anyone's interests."
    ju "Personally , I enjoyed walking around through the tea shop part the most "
    ju "Their business strategy is amazing . Perhaps it's something we should implement at C&R."
    ju "They entice you with the promise of tra all throughout the museum, then have a tea store waiting for you at the end . "
    ju "I was impressed and decided to meet up with the owner , and he seemed like a very interesting person "
    ju "He owns not only the museum and tea store , but  also runs a tea fanclub here in the U.K"
    ju "He would be an interesting guest to invite to the party"
    ju "The owner also said he would share some recipes with me "
    ju "Perhaps I will share them with the members..."
    enter chatroom ri
    ri "Oh my, so many messages."
    ri "Hello Jumin ! I'm glad to be back in here +_+"
    ju "Hello to you too Rika"
    ju "I was wondering if people would enjoy these teas I tasted"
    ri "I know I would ~"
    ri "And yes, I can confirm:"
    msg ri "My favourite has always been mint, ever since I was a child " glow ser1
    ju "Did your parents give it to you a lot ?"
    ri "Um, something like that !"
    msg ri "The tea also reminds me of a very special person " cloud_l
    ju "I assume that would be V "
    ri "Well..."
    msg ri "him too I guess ^^" curly
    ri "Anyway..."
    ri "I love seeing how much fun you're having abroad "
    ri "That tea museum is such a clever idea too "
    ri "I want to visit it one day!"
    ju "You can, I'll book two tickets for V and you as soon as the party is done with ."
    ri "Oh, no need to rush!"
    ju "We can always do that later "
    ju "Alright then."
    ju "Just know that my help is always available."
    ri "Oh yes, I'm sure ^^"
    ri "All this talk about tea is making me crave it a bit.."
    ri "I should go make myself a cup "
    ju "Enjoy your tea."
    ju "I'll have the hotel staff make me some right now as well"
    ju "Then I shall leave."
    ju "Have a good day Rika."
    exit chatroom ju
    ri "Ah, that was fast ..."
    ri "Jumin is really into travelling these days "
    ri "I love seeing him so energized "
    ri "He has always a bit mysterious when it came to his emotions."
    ri "But you learn to pick up subtle hints after being around him for a while."
    ri "I hope [name] can become even closer to the RFA members from now on !"
    ri "This happy chatter I'm seeing these days..."
    ri "I really feel like the RFA is growing into something amazing ^^"
    ri "{image=rika_happy}" (img=True)
    ri "For now, I think I'll enjoy my tea "
    ri "Goodbye then! ~"
    exit chatroom ri

    return


    label after_cd2_chat5:

    compose text ri:
        r "I'm currently enjoying my tea ! I hope you're also snuggled up and safe on this lovely afternoon ~ "
        label reply_tea

    return

label reply_tea:
    menu:
        "I am! Thank  you for asking":
            award heart ri
            ri "I'm very glad ! I hope the two of will get to enjoy tea together someday!"
            ri "Yes...someday together ^^"
        "I'm fine. I guess":
            ri "I see...please contact me if you're not feeling well..:"
    ri "I hope the two of us can grow closer!"

    return
