label cd2_chat2():
#Stressful morning
$ ju.status = "Meetings are a pain..."
    scene morning
    play music silly_smile_again
    enter chatroom y
    msg y "Whoa, what a beautiful day" glow
    msg y "Wonder how everyone else is holding up..."
    msg y "Oh, [name]! You're here!" 
    menu:
        "Hi hi Yoosung!":
            msg y "Hi hi!" ser1
            msg y "I see you're up bright and early!"
        "I'm feeling a little fuzzy..":
            msg y "Maybe you should go back to bed then.." curly
            msg y "I wish I could do the same..." sigh_m
    msg y "Can you guess what I'm doing today?" curly
    msg y "It's not very hard to guess so don't overthink it ;;;" bold
    menu:
        "Revising for the entrance exam!":
            award heart y
            msg y "BINGO!" spike_s
            msg y "The one thing I've been talking about these past few days" sigh_l
            msg y "I really wish I had something more interesting to talk about..." ser1
        "Learning about meowpox!":
            award heart s
            msg y "Not that again!" curly
            msg y "Is Seven rubbing off on you or something?"
            msg y "He's barely been in here these days and yet..." sigh_m
    msg y "I am still but a slave to the entrance exam" ser1
    msg y "Just came here for a breather"
    msg y "To take my mind off things for a little while"
    msg y "Before jumping right back into studying..."
    msg y "Have anything you want to talk about?"
    menu:
        "Let's talk about the R.F.A!":
            award heart ri
            msg y "The R.F.A? Sure thing !"
            msg y "What is it you want to know? I guess it makes sense you'd ask, since you're new here" ser1
            menu:
                "How did you end up joining R.F.A?":
                    award heart y
                    msg y "Oh, you want to know about me?" glow
                    msg y "Well, that's easy enough - Rika let me in since I'm her cousin"
                    msg y "We'd grown pretty close over the years, so when she was just starting out the R.F.A"
                    msg y "It was kind of a given she'd invite me to  join"
                "What are the members responsibilities in the R.F.A?":
                    msg y "Well...It depends!"
                    msg y "Rika and you are coordinators,and V is a co-founder"
                    msg y "Jumin provides the budget, Jaehee manages it. Zen is the face, and Seven deals with the messenger"
                    msg y "And I....am the only regular member, I suppose ;" curly
                "Do you know why Rika started the R.F.A?":
                    award heart ri
                    msg y "Of course! She started it with one goal in mind - to help others!"
                    msg y "Another important aspect of the R.F.A is never to make money - just raise it!" glow
                    msg y "We tried really hard to make the party as accessible as possible last time." ser1
                    msg y "But with your help, we'll hopefully we able to do much more" bold
        "Do you trust everyone in the R.F.A?":
            award heart mi 
            msg y "Well, we've all known each other for a while now..." ser1
            msg y "So of course I do! Anything specific you want to know?"
            $ intern_mentioned = False
            menu:
                "What was Rika like in the past?":
                $ intern_mentioned = False
                    award heart mi 
                    award heart ri
                    msg y "Woah, that's direct ! I don't know how I'd answer that ;;" curly
                    msg y "She's been pretty much the same ever since the day we first met"
                    msg y "Always hard-working and doing her best to help others around her" glow
                    msg y "The only thing that's different is that she's a bit more open these days." ser1
                "Why did the others join the R.F.A?":
                $ intern_mentioned = False
                    msg y "They all had their reasons!" ser1
                    msg y "V is her boyfriend, so of course he ended up joining. Jumin is his longtime friend and he also grew pretty close to Rika"
                    msg y "I don't know how Seven and Rika know each other, but he was one of the original members as well"
                    msg y "Zen joined a bit later after talking with V, and Jaehee joined because Jumin made her ;;" curly
                "Who do you get along with most here?":
                $ intern_mentioned = True
                    award heart y
                    msg y "Everyone is pretty great! Though sometimes Sevens jokes get way to annoying" ser1
                    msg y "If I had to pick one person, I guess it'd be Rika!"
                    msg y "We've known each other the longest, and share a family bond. That has to count for something, right?" ser2
                    msg y "Other than her, I suppose Jumin and I also get along. He even offered me an internship not too long ago!"
        "What do you think about the fact someone else is overseeing the messenger?":
            award heart va
            msg y "Oh, you mean since Seven isn't here anymore?"
            msg y "He did leave that number for you and Rika to call if there are any issues. Have you done that already?"
            menu:
                "I have! The person seems really nice":
                    award heart va
                    msg y "Glad to hear that! I was kind of worried when Seven said he'd leave a stranger in charge of us"
                    msg y "But since you seem to trust them, I guess everything is okay after all" ser2
                    msg y "Maybe I should call them up myself , just to see what they're like-"
                    msg y "Or not...I still have to study" sigh_m
                "No I've not...Don't have the time":
                    msg y "Then we're in the same boat! I know how that is."  bold
                    msg y "This entrance exam has been keeping me pretty busy..."
                    msg y "There's so much I want to do, but I guess I'll push through for a little while longer" curly
                    msg y "....this better be worth it ;;;" bold
                "If only Seven were still here...":
                    award heart s
                    msg y "Oh, are you worried about the messenger being in danger while Seven is away?" curly
                    msg y "I don't think you should be! We've never been under attack or something lol"
                    msg y "The messenger isn't that kind of place. The most drama we had is when Zen hurt his ankle"
                    msg y "Whined about it for an entire day, then got right back up and started practicing the next" sigh_m
    msg y "Anyway...I'm glad we had this talk" glow
    msg y "Helped me take my mind off things for a bit"
    msg y "Still not completely over the fact I have to study more as soon as this chatroom ends ;" curly
    msg y "So I'll try to drag this along as much as possible if you don't mind"
    msg y "So...How are you finding the R.F.A now that a few days have passed?"
    msg y "Are the guests coming along nicely?"
    menu:
        "Already invited quite a few people ":
            award heart ri
            msg y "That's nice ! You should invite as many people as possible ."
            msg y "Maybe try sticking to some sort of theme though"
            msg y "So our guests don't feel out of place"
        "Kind of struggling here...":
            msg y "Oh no !That sucks! :("
            msg y "I wouldn't sweat it too much though..."
            msg y "You still have plenty of time left ! I'm sure Rika will help you as well"
    msg y "The reason I asked is because I just thought of someone to invite!"
    msg y "They're an ultra famous...Cram school director ;"
    msg y "Can you tell how much this exam has taken over my life ^^?" bold
    msg y "What do you say ?"
    menu:
        "Ugh, cram school? Brings back bad memories. I'll pass":
            msg y "I understand! " sigh_s
            msg y "I'll probably feel the same way once this is over"
            msg y "Just wanted to help out!"
        "Sure thing ! Give them my contact info!":
       #invite gues @cram
            msg y "Glad I could be of help!" glow
            msg y "They might seem strict at first, but..." ser1
            msg y "...yeah no buts. They just are. Good luck ;;"
    msg y "I have no doubt that this party will be the best one yet!"
    msg y "Everyone just has to do their thing-" glow
    enter chatroom ju
    play_music urban_night_citytscape
    ju "Right you are"
    msg y "Oh wow, hi Jumin!" ser1
    ju "Hello you two."
    menu:
        "Good to see you Jumin!":
            award heart ju 
            ju "Good to see you as well [name]"
            ju "I hope you're ready for the day ahead."
        "Hi..."
            ju "You don't seem too enthused"
            ju "Maybe you should consider going back to bed"
    ju "Just got done with preparing some documents for an upcoming meeting."
    ju "So I thought I'd come in here and relax a bit before the big event"
    msg y "I'm kind of trying to do the same thing actually;" ser1
    msg ju "Is this about your entrance exam? You'll be fine, so long as you studied enough" sser1
    msg y "I sure hope I did enough...all those months of hard work" curly
    msg ju "They'll pay off alright. It's good practice for the work you'll have to do in the future"
    if intern_mentioned:
        msg ju "I see you mentioned my internship offer to [name]" ser1
        msg y "Yes I did...Was I not supposed to do that?" curly
        msg ju "Oh, no, just an observation I had" round_m
        msg ju "We are all members of the R.F.A. Besides, that's nothing confidential"
    else:
        msg ju "You know [name], I offered Yoosung here an internship not too long ago."
        msg y "Yeah, you did! Was kind of afraid to bring it up.." ser1
        msg ju "You don't need to be worried about that."
        msg ju "It'll be known to everyone eventually, so no need to worry." bold
    msg y "Why do you think I'm a good pick for the internship ?" 
    msg y "I never thought to ask before..." curly
    msg ju "I think the answer to that question is really quite simple" ser1
    msg ju "You're a hard worker with a good head on your shoulders" ser1
    msg ju "All I did was take notice to that and offer you an entrant-level position" sser1
    msg ju "We'll learn just how good of a worker you actually are when you actually begin working, and we'll proceed from there"
    msg ju "I hope this deal of ours can someday lead to something like a full-time contact" sser2
    msg y "Woah, so these are Jumins smooth-talking skills in action" glow
    msg y "I almost forgot you were talking about employment for a second" sigh_m
    msg ju "A good businessman knows how and when to sweeten the pot. That's what my father always says."
    menu:
        "I think Yoosung will be a very good and obedient employee?":
            msg y "Huh? What makes you say that ;;;" curly
            award heart ju
            msg ju "I agree. How perceptive of you to notice that." blocky_m
            msg y "You guys are weird. I have no idea what you're talking about" sigh_m
            msg ju "Our opinion will be proven in due time" glow
            msg y "That doesn't sound too good..." curly
            msg ju "{image=jumin_smile}" (img=True)
        "Aren't you hiring Yoosung out of nepotism lol?":
            msg y "Well, [they][are] not entirely wrong.."
            msg ju "I disagree. This isn't at all what I'd call nepotism" ser1
            msg ju "It would be nepotism if I were hiring you just because you're Rika's cousin"
            msg ju "When I'm hiring you on your own merit"
            msg y "So me being her cousin has nothing to do with it?" glow
            msg ju "I wouldn't go that far" blocky_s
            msg y "{image=yoosung_cry}" (img=True)
    msg ju "I almost forgot... I have something to announce."
    msg y "Really? What is it Jumin?"
    msg y "{image=yoosung_question}" (img=True)
    msg ju "Oh, it's nothing major. However, considering the fact we don't have the guest list finalized as of yet..."
    msg ju "How about inviting Montana Bones to the party?"
    msg ju "She is an adventurer famous for her globe-trotting"
    msg ju "We are thinking of convincing her to participate in a climbing competition with C&R as her sponsor"
    msg ju "It would help raise our brand awareness even in foreign countries" glow
    msg y "That's so cool! She is kind of a celebrity isn't she? Wouldn't it be better for Rika to deal with her"
    msg ju "I called her beforehand. She said she trusts [name] will do a good enough job of convincing her" ser1
    #invite guest @adventurer 
    msg y "Wow, [name]...Seems like Rika really believes in you!" glow
    menu:
        "I hope I don't disappoint...Seems like a lot of pressure":
            y "I'm sure you won't! Rika thought you'd do well, that's why she entrusted you with this guest"
            msg y "And Rika is never wrong about anything!" glow
            msg ju "Just make sure you sweeten the deal, and she'll come for sure "
        "Then I'll have to do well and make her proud!":
            award heart ri
            msg y "That's the spirit!" glow
            msg ju "Of course. Exactly  what I'd expect from someone Rika hired." bold
            msg y "Don't make it sound so business-like ;;;" curly
        "A celebrity? Wonder what we could do with that...":
            award heart mi
            msg ju "Well, her appearance will draw more attention to the party, that much is certain" ser2
            msg y "Yeah...I think that's alright though. It's just like Rika said- the more the merrier" cloud_m
            msg ju "Let's just hope [name] is up to the task of inviting her" ser1
    msg y "Have you had any luck in convincing her to make a deal with you guys?" 
    msg ju "Not really, no. She's rather stubborn and refuses to work with most corporations outright." ser1
    msg ju "It's kind of frustrating how hard people like that are to convince"
    msg ju "{image=jumin_sigh}" (img=True)
    msg y "Oh yeah, now I remember...she's a pretty big environmentalist too. Good luck with convincing her to join up..."
    msg ju "I seriously doubt we'll have much success with her, but it's worth giving it a try."
    msg ju "After all, C&R makes regular donations to environmental efforts. That might sway her."
    msg y "I dunno...I feel like that's not enough." curly
    msg y "Would you accept something like that [name]?"
    menu:
        "I'd be scared to. Big corporations are rarely good.":
            msg ju "You wouldn't be saying that if you were a part of our team." underline
            msg ju "Corporations only do what the consumers want them to - nothing more and nothing less."
            msg y "I don't think so Jumin...C&R may be good, but not every corporation is like that" curly
            award heart ri
            msg ju "We'll have to agree to disagree for now." sigh_m
        "A chance to work with Jumin? Sign me up~":
            msg ju "I'm not involved in these types of projects, just approve them" ser1
            msg ju "Besides, what difference does it make whether it's me or someone else from C&R?"
            msg y "Perhaps [name] wants to get to know you better..."
            msg ju "If that's the case, there's plenty of opportunity to do so via the messenger."
        "Maybe- Depends on the contract.":
            award heart ju
            msg ju "That's very prudent of you. All contracts should be thoroughly examined before you sign them" blocky_m
            msg y "The only contracts I got to sign were the ones for doing volunteer work with Rika" 
            msg ju "Even those you have to be careful with. Make sure you read every last word."
            msg y "Maybe I will...But at this point, I'd sign away my life to get rid of all this stress" sigh_m
    msg ju "Anyway...I should really wrap things up and get ready for the meeting"
    msg y "That means I'm going back to studying..."
    msg y "{image=yoosung_cry}" (img=True)
    msg y "Wish me luck you guys!" glow
    menu:
        "Good luck with the meeting Jumin!":
            award heart ju
            msg ju "I trust I won't end well, but thank you anyway."
            msg ju "It'll be interesting to see how it'll turn out."
        "Yoosung, I feel you. Hang in there!":
            award heart y
            msg y "Thank you! I'll do my best" square_s
            msg y "I can only hope the studying gods will be kind to me..." curly
        "Maybe I should call up that tech support guy..."
            award heart va
            msg y "Him? Wow, have you already started talking?"
            msg ju "I wonder just who that person is..."
    msg ju "I'll be heading out then. Goodbye you two."
    msg y "Yup! Talk to you later!!"
    exit chatroom ju
    exit chatroom y
     
return


label cd2_chat2_expired():
#Stressful morning
$ ju.status = "Meetings are a pain..."
    scene morning
    play music silly_smile_again
    enter chatroom y
    msg y "Whoa, what a beautiful day" glow
    msg y "Wonder how everyone else is holding up..."
    msg y "Because I am not doing well ;;;" curly
    msg y "I wish I could go back to bed so badly" sigh_s
    msg y "Can you guys guess what I'm doing today?" curly
    msg y "It's not very hard to guess so don't overthink it ;;;" bold
    msg y "It's...." ser1
    msg y "My entrance exam!!!" spiky_s
    msg y "...I warned you guys it was nothing exciting, so I don't want to hear any complaints;"
    msg y "I am still but a slave to it" ser1
    msg y "Just came here for a breather"
    msg y "To take my mind off things for a little while"
    msg y "Before jumping right back into studying..."
    msg y "Since no one is here, guess I'll have to entertain myself"
    msg y "Oh, I know!!" bold
    msg y "Since [name] is new here, I'll talk a little about the R.F.A!"
    msg y "I guess the most interesting thing about us is how we all have different responsibilities"
    msg y "Rika and [name] are coordinators,and V is a co-founder"
    msg y "Jumin provides the budget, Jaehee manages it. Zen is the face, and Seven deals with the messenger"
    msg y "And I....am the only regular member, I suppose ;" curly
    msg y "But I don't let that deter me!" glow
    msg y "I'm working my butt off to get into a good university."
    msg y "Jumin even promised to make me an intern at C&R once I'm done with college!!!"
    msg y "As for how the R.F.A got its start..."
    msg y "Rika always wanted to help those around her - I suppose that's how the idea came to her" glow
    msg y "Anyway...I'm glad I had this monologue" glow
    msg y "Helped me take my mind off things for a bit"
    msg y "Still not completely over the fact I have to study more as soon as this chatroom ends ;" curly
    msg y "So I'll try to drag this along as much as possible ...."
    msg y "I wonder how [name] is finding the R.F.A now that a few days have passed?"
    msg y "Hopefully the guests are coming along nicely"
    msg y "Rika always put a lot of effort into those, so I hope [name] is doing the same!"
    msg y "Actually...I had someone I wanted to invite to the party"
    msg y "They're an ultra famous...Cram school director ;"
    msg y "Can you guys tell how much this exam has taken over my life ^^?" bold
    msg y "I wonder what [name] would think...maybe I'll forward their info to Rika just in case."
    msg y "I have no doubt that this party will be the best one yet!"
    msg y "Everyone just has to do their thing-" glow
    enter chatroom ju
    play_music urban_night_citytscape
    ju "Right you are"
    msg y "Oh wow, hi Jumin!" ser1
    ju "Hello Yoosung, good to see you."
    ju "Just got done with preparing some documents for an upcoming meeting."
    ju "So I thought I'd come in here and relax a bit before the big event"
    msg y "I'm kind of trying to do the same thing actually;" ser1
    msg ju "Is this about your entrance exam? You'll be fine, so long as you studied enough" sser1
    msg y "I sure hope I did enough...all those months of hard work" curly
    msg ju "They'll pay off alright. It's good practice for the work you'll have to do in the future"
    msg ju "I see you mentioned my internship offer in the chatroom" ser1
    msg y "Yes I did...Was I not supposed to do that?" curly
    msg ju "Oh, no, just an observation I had" round_m
    msg ju "We are all members of the R.F.A. Besides, that's nothing confidential"
    msg ju "It'll be known to everyone eventually, so no need to worry." bold
    msg y "Why do you think I'm a good pick for the internship ?" 
    msg y "I never thought to ask before..." curly
    msg ju "I think the answer to that question is really quite simple" ser1
    msg ju "You're a hard worker with a good head on your shoulders" ser1
    msg ju "All I did was take notice to that and offer you an entrant-level position" sser1
    msg ju "We'll learn just how good of a worker you actually are when you actually begin working, and we'll proceed from there"
    msg ju "I hope this deal of ours can someday lead to something like a full-time contact" sser2
    msg y "Woah, so these are Jumins smooth-talking skills in action" glow
    msg y "I almost forgot you were talking about employment for a second" sigh_m
    msg ju "A good businessman knows how and when to sweeten the pot. That's what my father always says."
    msg ju "I almost forgot... I have something to announce."
    msg y "Really? What is it Jumin?"
    msg y "{image=yoosung_question}" (img=True)
    msg ju "Oh, it's nothing major. However, considering the fact we don't have the guest list finalized as of yet..."
    msg ju "How about inviting Montana Bones to the party?"
    msg ju "She is an adventurer famous for her globe-trotting"
    msg ju "We are thinking of convincing her to participate in a climbing competition with C&R as her sponsor"
    msg ju "It would help raise our brand awareness even in foreign countries" glow
    msg y "That's so cool! She is kind of a celebrity isn't she? Wouldn't it be better for Rika to deal with her"
    msg ju "I called her beforehand. She said she trusts [name] will do a good enough job of convincing her" ser1
    #invite guest @adventurer 
    msg y "Wow, [name]...Seems like Rika really believes in [them]!" glow
    msg ju "We can only hope [they] live up to the expectations."
    msg y "Have you had any luck in convincing her to make a deal with you guys?" 
    msg ju "Not really, no. She's rather stubborn and refuses to work with most corporations outright." ser1
    msg ju "It's kind of frustrating how hard people like that are to convince"
    msg ju "{image=jumin_sigh}" (img=True)
    msg y "Oh yeah, now I remember...she's a pretty big environmentalist too. Good luck with convincing her to join up..."
    msg ju "I seriously doubt we'll have much success with her, but it's worth giving it a try."
    msg ju "After all, C&R makes regular donations to environmental efforts. That might sway her."
    msg y "I dunno...I feel like that's not enough." curly
    msg ju "I don't think the meeting will end well either, but what can you do?"
    msg ju "Anyway...I should really wrap things up and get ready for the meeting"
    msg y "That means I'm going back to studying..."
    msg y "{image=yoosung_cry}" (img=True)
    msg y "Wish me luck!" glow
    msg ju "Just make sure you've learned everything you need to."
    msg y "Ughhh, you're not helping..."
    msg y "Goodbye then!"
    msg ju "Lets talk at another time."
    exit chatroom y
    exit chatroom ju
return


label cd2_chat2_outgoing_va:
    va "...."
    va "Oh. It's you again. You're up early"
    va "After yesterday, I wasn't sure you'd call back. Seems like you've decided talking to me is worth wasting your time"
    va "Whether that decision is one or not, I can't tell"
    menu:
        extend ''
        "Am I bothering you?":
            va "Seeing as my task is to respond to your phone calls...not really"
            va "But it might start bothering me if you keep calling me for no reason at all"
            va "I'd prefer it if you had something of importance you needed to tell me about"
        "I liked the conversation we had yesterday":
            award heart va
            va "Did you really? Was talking about security issues really that interesting to you?"
            va "You sure have some strange tastes. It might be novel to you, but for me, it's all a part of the job"
            va "Though, if you're really interested in stuff like that, I guess I don't mind talking about it to you"
    va "After all, my job here is to replace 707 as the messengers overseer"
    va "That other coordinator person he told me about is yet to call me "
    va "It seems like she isn't too interested in what I have to offer. I don't really care either way"
    va "Is there anything you wanted to ask me?"
    menu:
        extend ''
        "Yes there is!":
            va "Is there now? Well then,say it. I haven't got all day"
            menu:
                extend ''
                "Is there any way I can help you?":
                    award heart va
                    va "...I see. While I appreciate the offer, I don't really think I can accept your help"
                    va "Unless it's reporting a bug you encountered or something like that"
                    va "Beyond that, our interactions are supposed to be pretty limited. Thank you anyway"
                "Are you a cat person or a dog person?":
                    va "Is that it? Why do you need to know that? There's no reason for you to."
                    va "I hope you didn't  call me just to waste my time like this"
                    va "However, if you really want to know....Though both tend to be messy, I must say I prefer cats"
        "Not really. I just wanted to chat":
            va "Oh really? Is that all ?"
            va "Are you really that bored? Can't say I blame you though."
            va "From the way 707 described it, that R.F.A organization sure seems like a lot of work"
    va "Well...Now that we cleared that up....It's my turn to ask you something"
    va "Say...Do you guys get along with the other members?"
    va "I've been wondering that ever since I noticed you only joined the organization officially yesterday"
    va "The others don't seem all that cautious however. Isn't that strange?"
    menu:
            extend ''
            "We get along well. We are all friends here in the R.F.A!":
                va "I should have known you'd have given me a response like that"
                va "You R.F.A people seem like a bunch of hippies. How can you say that after knowing them for all of one day?"
                va "I guess  this is why 707 can't seem to shut up about you guys..."
            "I'm not sure yet. I feel a bit weird about being the only newbie here":
                award heart va
                va "Is that so ? I don't really blame you. I think I'd feel the same"
                va "It was like that when I ...nevermind. Forget I said that. But yeah, I get how you feel"
                va "I guess we're not that different after all"
    va "Regardless...Thank you for answering. I wasn't really expecting you to"
    va "That about does it I'd say. I have to get back to work now and cut this conversation here"
    va "Talk to you later then. Goodbye"

return
