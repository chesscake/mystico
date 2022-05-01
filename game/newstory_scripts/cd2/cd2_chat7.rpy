label cd2_chat7():

    $ ja.prof_pic = "Profile Pics/Jaehee/jae-2.webmp"

    $ ja.cover_pic = "Cover Photos/Jaehee/ja2.jpg"

    $ ja.status = "What could be happening...Let's go Rika!"

    scene noon
    play music lonesome_practicalism

    enter chatroom ja

    ja "I see there is a new member in our midst"
    ja "I didn't expect one to arrive here"
    ja "So soon after [name] too"
    ja "I'm not sure  what I feel about her"
    ja "She seems somewhat strange"
    ja "I guess it's necessary, to keep us safe"
    ja "I see you're in here [name]"
    ja "I don't know if the new member has talked to you yet"
    menu:
        "We did talk. I think they are interesting lol":
            award heart va
            msg ja "Good. I was a bit confused about their gender" glow
            ja "I think it's a girl though"
            msg ja "I'm sure you're confused, I Know I am" curly
            ja "But I'm pretty sure it's a girl "
        "We talked. I'm wary of them":
            award heart ri
            ja "That's fine"
            ja "I had a similar feeling as well"
            ja "But V vouched for them"
        "We didn't talk yet":
            ja "Oh, so same as me then"
            ja "You must still be confused"
    msg ja "I am hoping to see her more these days" ser1 ser1
    ja "Since I still don't know what to think"
    ja "I guess we can invite her to a few RFA outings too."
    ja "When we get to know each other better that is"
    ja "For now it may be best to keep our distance"
    msg ja "Since we don't know her well" curly
    ja "It's different for you ..."
    ja "We had Rika vouch for you, and also speak to you beforehand"
    ja "I guess we have V's word but"
    msg ja "{image=jaehee_question}" (img=True)
    ja "It's not quite the same "
    ja "It felt a bit sudden"
    msg ja "I hope miss Vanderwood doesn't take any offense to this" glow
    msg ja "We are just flustered over having a new member" ser2
    menu:
        "I'm sure they won't. They seem kind":
            award heart va
            ja "You think so?"
            ja "Well, that might be the case "
            msg ja "But I'm not convinced as of yet" ser1
        "I don't know. They might" :
            msg ja "Yes, that's what I thought " curly
            ja "Hopefully she won't get too mad "
    ja "Regardless of whether she gets mad or not "
    msg ja "I apologize in advance" sigh_m
    ja "Still, their status in the RFA is yet to be determined"
    ja "I'm sure Rika will decide that soon enough"
    ja "She seemed so flustered at the sudden arrival of this new member"
    ja "I hope she's well"
    ja "Come to think of it"
    ja "Maybe we should have an outing today"
    ja "I am sure to be done with work at around 16 : 00 today"
    ja "Is that fine with you Rika ?"
    ja "{image=jaehee_happy}" (img=True)
    ja "We can meet up at that novelty cafe we talked about"
    msg ja "I heard the person who runs it is very kind" square_m
    menu:
        "Can I go too ? I want to see Rika in person again":
            award heart ri
            ja "I don't think that's possible as of yet.."
            ja "But soon, I am sure we can have our outings together"
            ja "And Rika and you will go on plently of guest scouting missions"
        "Perhaps Vanderwood would enjoy getting to know you better":
            award heart va
            ja "Um.."
            ja "Well"
            ja "That's Rikas decision to make"
        "Okay! Have fun Jaehee!":
            award heart ja
            ja "Thank you [name]!"
    ja "Regardless..."
    msg ja "I hope to see some more information on this person over the following days" glow
    ja "For now, I'll leave this to Rika and V"
    ja "Then I should leave.."
    ja "Goodbye"

    exit chatroom ja

    return


label cd2_chat7_expired():

    $ ja.prof_pic = "Profile Pics/Jaehee/jae-2.webmp"

    $ ja.cover_pic = "Cover Photos/Jaehee/ja2.jpg"

    $ ja.status = "What could be happening...Let's go Rika!"

    scene noon
    play music lonesome_practicalism

    enter chatroom ja

    ja "I see there is a new member in our midst"
    ja "I didn't expect one to arrive here"
    ja "So soon after [name] too"
    ja "I'm not sure  what I feel about her"
    ja "She seems somewhat strange"
    ja "I guess it's necessary,  to keep us safe"
    ja "I see no one else is in here"
    ja "I just finished skimming the chat logs"
    ja "SO I don't know if the new member has talked to you guys yet"
    ja "I was a bit confused about their gender"
    ja "I think it's a girl though"
    msg ja "I am hoping to see her more these days" ser1 glow
    ja "Since I still don't know what to think"
    ja "I guess we can invite her to a few RFA outings too."
    ja "When we get to know each other better that is"
    ja "For now it may be best to keep our distance"
    ja "Since we don't know her well"
    ja "It's different for [name] ..."
    ja "We had Rika vouch for [them] , and also speak to [them] beforehand"
    ja "I guess we have Vs word but"
    ja "{image=jaehee_question}" (img=True)
    ja "It's not quite the same "
    ja "It felt a bit sudden "
    msg ja "I hope miss Vanderwood doesn't take any offense to this" glow
    ja "I am just flustered over having a new member"
    ja "Hopefully she won't get too mad "
    ja "Regardless of whether she gets mad or not "
    msg ja "I apologize in advance" sigh_m
    ja "Still, their status in the R.F.A is yet to be determined"
    ja "I'm sure Rika will decide that soon enough"
    ja "She seemed so flustered at the sudden arrival of this new member"
    ja "I hope she's well"
    ja "Come to think of it"
    ja "Maybe we should have an outing today"
    ja "I am sure to be done with work at around 16 : 00 today"
    ja "Is that fine with you, Rika ?"
    ja "{image=jaehee_happy}" (img=True)
    ja "We can meet up at that novelty cafe we talked about"
    msg ja "I heard the person who runs it is very kind" square_m
    ja "I don't [name] joining us is possible as of yet.."
    ja "But soon, I am sure we can have our outings together"
    js "And Rika and [them] will go on plently of guest scouting missions"
    ja "As for Vanderwood.."
    ja "Um.."
    ja "Well"
    ja "That's Rikas decision to make"
    ja "Regardless..."
    msg ja "I hope to see some more information on this person over the following days" glow
    ja "For now , I'll leave this to Rika and V"
    ja "Then I should leave.."
    ja "Goodbye"

    exit chatroom ja

    return
