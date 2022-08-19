label cd1_chat3():

    $ ju.cover_pic = "Cover Photos/Jumin/ju2.jpg"
    $ v.cover_pic = "Cover Photos/V/v2.jpg"

    $ ju.status = "Wine, the most bitter remedy "
    $ v.status = "Chocolate, the sweetest poison"

    scene earlyMorn
    play music urban_night_cityscape

    enter chatroom ju

    ju "What a peaceful morning"
    ju "Another productive day is ahead of us"
    ju "Wouldn't you agree [name]?"
    menu:
        "I'm not too sure about that. I'm still sleepy":
            ju "You should probably head back to bed then"
            msg ju "Unless your employer is as punctual as I am" square_m
            msg ju "In which case...I'd like to commend him" glow
        "On mornings like this, I feel like heading straight to work":
            award heart ju
            ju "Your productivity is commendable"
            msg ju "I'd love to have more employees like you"
            ju "{image=jumin_smile}" (img=True)
        "I wonder how Rika is doing...":
            award heart ri
            ju "She's probably still sleeping"
            ju "It's amazing how you're already interested in her well-being"
            ju "You've only just joined the R.F.A after all"
    ju "No matter how you're feeling"
    ju "I hope your day is as packed  as mine is"
    ju "I should contact assistant Kang about our newest projects"
    ju "I'd like a full report on the following developments"
    ju "The oil industry is in an unprecedented deficit"
    ju "Our investments will have to be dealt with carefully from this point on"
    ju "The housing market has also remained stagnant. I want a detailed report on every C&R operated apartment complex in the general area by tommorow morning"
    ju "Then, the agriculture sector is expanding just as we predicted. I'll need a chart comparing our prediction to the current state of affairs"
    ju "That will be all for now"
    menu:
        "Dont't you think that's way too much work for Jaehee to handle?":
            award heart ja
            ju "I understand that she might not be able to finish the reports on time. I'll extend the deadline by two hours"
            ju "But why are you so interested in whether Assistant Kang will finish her reports on time"
            menu:
                "I think having less work might make her more productive":
                    award heart ju
                    ju "What a practical way of looking at things"
                    msg ju "Your idea isn't exactly standard practice, but you might be onto something there" bold
                    ju "{image=jumin_smile}" (img=True)
                "I'm worried about her health..":
                    award heart ri
                    award heart ja
                    ju "Rika told me something similar recently"
                    ju "I think the both of you are overly concerned with Assistant Kang"
                    ju "She has a job to do and can quit if she so desires"
                "Workers deserve more respect from their respective organizations":
                    award heart ja
                    ju "I see. So that's how you view bussines"
                    ju "I can't say I disagree with that"
                    ju "Though I think the two of us would disagree over exactly what 'respect' means"
        "Wow. I'm impressed by how expansive C&R's bussines dealings are!":
            award heart ju
            msg ju "That's exactly the image we want to project" square_m
            msg ju "I'll have to send a formal thank you to our marketing department" bold
        "Yaaawn... I'm not reading all of that?!":
            break heart ju
    ju "C&R will  continue to expand no matter what"
    ju "That I can guarantee"

    enter chatroom v

    ju "Welcome V"
    msg ju "So good to see you here" glow
    v "I'm glad to see you too Jumin"
    v "{image=v_smile}" (img=True)
    v "And hello to you too [name]"
    ju "You see V, I was relaying important information on C&R-related bussines just before you arrived"
    v "You've always been a natural at that"
    ju "Of course. Just as much a natural as you are a photography"
    v "I think those two might not be as comparable as you think"
    ju "No matter. They work for the analogy"
    v "Say, have you tasted any wines to your liking recently?"
    ju "My trip around Europe has allowed to experince a wide range of tastes"
    msg ju "The wineries in France were particularly enticing" glow
    v "What a worldy man you have become"
    v "I haven't been travelling around lately"
    ju "That's a shame. You're missing out"
    ju "Back to the wines..."
    menu:
        "Do you prefer red or white wine?":
            award heart ju
            award heart v
            ju "While I do indulge in the common chardonnay here and there"
            ju "I much prefer the richness and depth that red wine offers"
            v "Jumin is one of the leading experts in red wine production these days"
        "You should probably consider lowering your alcohol intake..":
            award heart ri
            v "Rika tells us that all the time"
            ju "I can't bring myself to agreee with her"
            ju "Wine lets me experience the culture of a country summed up into one lowly cup"
        "Ugh, I hate the smell of wine. Whateverrr. Go talk about your old people drink elsewhere.":
            award heart s
            v "Uh"
            v "I'm sorry, [name], we will try to be brief."
            ju "That's quite an interesting reply actually"
            v "We haven't had many chances to talk lately, forgive us."
            v "It is? ;;"
            ju "Yes. At the first party, I remember our bespectacled programmer giving me one heinous glare."
            ju "If I had to pinpoint what he was thinking, that would definitely be one of his thoughts, word for word."
            v "You mean Luciel?"
            v "That's not like him at all..."
            ju "Indeed. Now it is not like him at all."
            ju "I used to be different too. This was before I welcomed my beloved Elizabeth the 3rd into my arms."
            ju "Rika's influence has changed us, wouldn't you say so, V?"
            v "I suppose so..."
            ju "Anyway, let me just talk about this and I will move on."
    ju "Out of the wines I tried on my trip, the one I liked the most was...unexpected. To say the least"
    v "Really? What might that one be?"
    ju "You see, it was this special kind of wine, made with the highest quality grapes..."
    ju "And enriched with cocoa beans"
    v "How strange!"
    v "{image=v_shock}" (img=True)
    msg ju "That's what I thought too" bold
    msg ju "Until I tasted it that is..."
    ju "It was one of the best wines I have ever had the pleasure of tasting"
    ju "The aromas worked out surprisingly well together"
    ju "The owner even gave me a complimentary chocolate bar on my way out."
    menu:
        "Do you even like chocolate Jumin?":
            award heart ju
            msg ju "Not really. Sweets never really appealed to me, even as a child" ser1
            ju "Though I would occasionally eat some whenever V visited" 
            msg ju "My maid would always bring out a platter of pure Belgian chocolate. Can't say I didn't somewhat enjoy that" square_l
            v "Even when he was a kid, he'd refuse to eat cheap chocolate."
            ju "{image=ju_smile}" (img=True)
        "Do you like chocolate V?":
            award heart v
            v "I like it a lot. The texture always appealed to me"
            msg v "Sometimes I'd even get stomach aches from eating too much" sigh_m
            v "Hot chocolate especially. My mother and I used to drink it on winter nights"
            ju "When V was a child, he'd eat any piece of chocolate he could find"
            v "{image=v_well}" (img=True)
        "I wonder if Rika likes chocolate...":
            award heart ri
            v "You'd have to ask her that yourself."
            ju "Shouldn't you know that V?"
            v "We don't know everything about each other."
            ju "That's fair. Though something like that is hard to miss?"
    ju "Chocolate remains a popular export product of many countries"
    ju "Our rivals, Osung, are the biggest importers of it"
    v "Have you considered undercutting them by importing from different sellers"
    msg ju "Yes actually. This trip isn't purely for work reasons." square_m
    v "I should have expected nothing less from C&R."
    v "{image=v_smile}" (img=True)
    ju "Regardless of whatever Osung is planning, we'll have to consider getting into the market regardless"
    ju "More and more people are interested in buying luxury chocolates"
    ju "And sales are especially high during Valentines day."
    msg v "I wonder how you could innovate on the idea of chocolate?"
    ju "I've been wondering that as well. Any ideas for the perfect gift?"
    v "No clue. I like eating chocolate, but I don't really see how to improve on it."
    ju "What about you [name]?"
    menu:
        "I haven't really thought about it myself":
            ju "Do you not like chocolate then?"
            v "That could be it"
            ju "I wonder what percentage of people dislike chocolate...I should have Assistant Kang write me a report on that."
        "What about selling chocolate coupled with wine?":
            award heart v
            v "That would be ideal for me, as I like enjoying them separately"
            v "I wouldn't neccessarily like eating them together"
            ju "Wouldn't that cheapen the experience of eating the chocolate?"
            ju "Data shows that customers are less likely to buy products like that"
        "Why don't you just import the wine you had in France?":
            award heart ju
            ju "That would be the easiest and most practical solution"
            ju "I could see it selling well amongst more afluent consumers"
            v "That wouldn't be the most creative move however"
            v "And these days, creativity is valued a lot more"
        "How about  selling chocolate with a wine filling?":
            award heart v
            ju "I hadn't thought about it before, that's pretty straighforward."
            v "It would make the experience of eating chocolate a lot richer"
            v "And if we choose the right kinds of cocoa beans and grapes..."
    ju "Thank you for your feedback. I'll talk with the appropriate department later."
    ju "I think I have something in mind now... An utterly unique gift that follows their requirements."
    v "All this talk about chocolate has reminded me..."
    v "I know this famous chocolatier. Would you be interested in employing him, Jumin?"
    msg ju "I'll tell Assistant Kang to handle it" square_m
    ju "In the meantime, he might be a good guest for our party. Are you interested [name]?"
    menu:
        "Yes I am! Tell him to contact me":
            #add party guest chocolatier
            v "WIll do as soon as I get around to it"
        "No, I don't think he'll be able to contribute":
            ju "So be it then."
    v "Now seems like a good time for me to leave. Thank you for chatting with me Jumin"
    ju "My plesure. I'll go take a stroll around at a nearby museum. See you [name]."

    exit chatroom v
    exit chatroom ju

    return


label cd1_chat3_expired():

    #$ ju.cover_pic = "Cover Photos/Jumin/ju2.jpg"
    #$ v.cover_pic = "Cover Photos/V/v2.jpg"

    $ ju.status = "Wine, the most bitter remedy "
    $ v.status = "Chocolate, the sweetest poison"

    scene earlyMorn
    play music urban_night_cityscape

    enter chatroom ju

    ju "What a peaceful morning"
    ju "Another productive day is ahead of us"
    ju "I should contact assistant Kang about our newest projects"
    ju "I'd like a full report on the following developments"
    ju "The oil industry is in an unprecedented deficit"
    ju "Our investments will have to be dealt with carefully from this point on"
    ju "The housing market has also remained stagnant. I want a detailed report on every C&R operated apartment complex in the general area by tommorow morning"
    ju "Then, the agriculture sector is expanding just as we predicted. I'll need a chart comparing our prediction to the current state of affairs"
    ju "That will be all for now"
    ju "C&R will  continue to expand no matter what"
    ju "That I can guarantee"

    enter chatroom v

    ju "Welcome V"
    msg ju "So good to see you here" glow
    v "I'm glad to see you too Jumin"
    v "{image=v_smile}" (img=True)
    ju "You see V, I was relaying important information on C&R-related bussines just before you arrived"
    v "You've always been a natural at that"
    ju "Of course. Just as much a natural as you are a photography"
    v "I think those two might not be as comparable as you think"
    ju "No matter. They work for the analogy"
    v "Say, have you tasted any wines to your liking recently?"
    ju "My trip around Europe has allowed to experince a wide range of tastes"
    msg ju "The wineries in France were particularly enticing" glow
    v "What a worldy man you have become"
    v "I haven't been travelling around lately"
    ju "That's a shame. You're missing out"
    ju "Back to the wines..."
    ju "While I do indulge in the common chardonnay here and there"
    ju "I much prefer the richness and depth that red wine offers"
    v "In case some of you don't know, Jumin is one of the leading experts in red wine production these days"
    ju "Out of the wines I tried  on my trip, the one I liked the most was...unexpected. To say the least"
    v "Really? What might that one be?"
    ju "You see, it was this special kind of wine, made with the highest quality grapes..."
    ju "And enriched with cocoa beans"
    v "How strange!"
    v "{image=v_shock}" (img=True)
    msg ju "That's what I thought too" bold
    msg ju "Until I tasted it that is..."
    ju "It was one of the best wines I have ever had the pleasure of tasting"
    ju "The aromas worked out surprisingly well together"
    ju "The owner even gave me a complimentary chocolate bar on my way out"
    ju "I like it to a certain extent."
    ju "The Belgian kind appeals to my taste buds, though I don't consume it all that often"
    ju "Sweets aren't all that appealing to me"
    v "Even when you were a kid, you'd refuse to eat cheap chocolate"
    ju "{image=ju_smile}" (img=True)
    v "I like it well enough"
    v "Hot chocolate especially. My mother and I used to drink it on winter nights"
    ju "When you were a child, you'd eat any piece of chocolate you could find"
    v "{image=v_well}" (img=True)
    ju "Chocolate remainds a popular export product of many countries"
    ju "Our rivals, Osung, are the biggest importers of it"
    v "Have you considered undercutting them by importing from different sellers"
    msg ju "Yes actually. This trip isn't purely for work reasons you know" square_m
    v "I should have expected nothing less from C&R"
    v "{image=v_smile}" (img=True)
    ju "Regardless of whatever Osung is planning, we'll have to consider getting into the market regardless"
    ju "More and more people are interested in buying luxury chocolates"
    ju "And sales are especially high during Valentines day"
    msg v "I wonder how you could innovate on the idea of chocolate?"
    ju "I've been wondering that as well. Any ideas?"
    v "No clue. I like eating chocolate, but I don't really see how to improve on it"
    ju "What about selling chocolate coupled with wine?"
    v "That would be ideal for me, as I like enjoying them separately"
    v "I wouldn't neccessarily like eating them together"
    ju "Wouldn't that cheapen the experience of eating the chocolate?"
    ju "Data shows that customers are less likely to buy products like that"
    v "Why don't you just import the wine you had in France?"
    ju "That would be the easiest and most practical solution"
    ju "I could see it selling well amongst more afluent consumers"
    v "That wouldn't be the most creative move however"
    v "And these days, creativity is valued a lot more"
    ju "Thank you for your feedback. I'll be sure to talk about it with the appropriate department"
    v "All this talk about chocolate has reminded me.."
    v "I know this famous chocolatier. Would you be interested in employing him Jumin?"
    msg ju "I'll tell Assistant Kang to handle it" square_m
    ju "In the meantime, he might be a good guest for our party. Would Rika or [name] be interested?"
    v "I'm not sure. Neither of them are here right now"
    v "Now seems like a good time for me to leave. Thank you for chatting with me Jumin"
    ju "My plesure. I'll go take a stroll around a nearby museum. See you V!"

    exit chatroom v

    exit chatroom ju

    return

######____TEXT MESSAGES____

label after_day_1_chatroom_2:

    compose text ju:
        ju "If you've read the discussion we had, you'd know how much I value wine."
        ju "Do you drink?"
        label reply_wine

    return

label reply_wine:
    menu:
        "No. I prefer to stay sober.":
            award heart ri
            award heart s
            ju "I respect your decision."
            ju "Rika doesn't like alcohol very much either."
            ju "And if I'm not wrong, Seven is of your mindset as well."
        "Wine is the spice of life":
            award heart ju
            ju "Such a creative way of looking at it"
            ju "You are right, wine truly is amazing."
        "I love a good beer!":
            award heart z
            ju "I don't like beer..."
            ju "But someone else in our group loves it."
            ju "Why don't you bond over it with him?"
            ju "Not all of us can have good taste, unfortunately."
    ju "Anyway, I need to think of the perfect gift that will expand C&R bussines further."
    ju "What if every household on Earth could have our brand?"
    ju "I wonder if such goal is attainable...?" #the answer is MEOW POX!! /jk


    return
