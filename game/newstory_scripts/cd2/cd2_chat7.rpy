label cd2_chat7():

    $ ja.prof_pic = "Profile Pics/Jaehee/jae-2.webmp"

    $ ja.cover_pic = "Cover Photos/Jaehee/ja2.jpg"

    $ ja.status = "What could be happening..."

    scene noon
    play music lonesome_practicalism

    enter chatroom ja

    ja "I just noticed 707 left some contact information for Rika and [name] yesterday..." ser1
    ja "I didn't expect a possible new member already" ser1
    ja "So soon after [name] too"
    ja "I guess it's necessary, to keep us safe"
    ja "I see you're in here [name]"
    ja "I don't know if the new member has talked to you yet"
    menu:
        "We did talk. I think they are interesting lol":
            award heart va
            msg ja "Good. I was a bit confused about their role in the R.F.A" glow
            ja "I think they're just supposed to take over for 707 "
            msg ja "I'm sure you're confused, I know I am" curly
            ja "But I'm pretty sure it's what they're doing"
        "I'm not sure how to feel about them":
            award heart ri
            ja "That's fine"
            ja "I had a similar feeling as well"
            ja "But 707 vouched for them"
        "We didn't talk yet":
            ja "Oh, so same as me then"
            ja "You must still be confused"
    msg ja "I am hoping to see what comes of this in the upcoming days"  ser1
    ja "Since I still don't know what to think" ser1
    ja "For now it may be best to keep our distance" ser1
    msg ja "Since we don't know them well" curly
    ja "It's different for you ..." glow
    ja "We had Rika vouch for you, and also speak to you beforehand" ser2
    ja "I guess we have 707's word but"
    msg ja "{image=jaehee_question}" (img=True)
    ja "It's not quite the same "
    ja "It felt a bit sudden"
    msg ja "I hope they don't take any offense to this" glow
    menu:
        "I'm sure they won't. They seem kind":
            award heart va
            ja "You think so?"
            ja "Well, that might be the case "
            msg ja "But I'm not convinced as of yet" ser1
        "I don't know. They might" :
            msg ja "Yes, that's what I thought " curly
    ja "Whether they're a permanent memeber of the RFA is yet to be determined"
    ja "I'm sure Rika will decide that soon enough" ser1
    ja "Oh, about Rika..." curly
    ja "I hope she's well" glow
    ja "I feel like she's cheered up considerably ever since you arrived but..she still feels a bit distant.." curly
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
        "Okay! Have fun Jaehee!":
            award heart ja
            ja "Thank you [name]!"
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

    ja "I just noticed 707 left some contact information for Rika and [name] yesterday..." ser1
    ja "I didn't expect a possible new member already" ser1
    ja "So soon after [name] too"
    ja "I guess it's necessary, to keep us safe"
    msg ja "I am hoping to see what comes of this in the upcoming days"  ser1
    ja "Since I still don't know what to think" ser1
    ja "For now it may be best to keep our distance" ser1
    msg ja "Since we don't know them well" curly
    ja "It's different for you ..." glow
    ja "We had Rika vouch for [name], and also speak to [them] beforehand" ser2
    ja "I guess we have 707's word but"
    msg ja "{image=jaehee_question}" (img=True)
    ja "It's not quite the same "
    ja "It felt a bit sudden"
    msg ja "I hope they don't take any offense to this" glow
    ja "Whether they're a permanent memeber of the RFA is yet to be determined"
    ja "I'm sure Rika will decide that soon enough" ser1
    ja "Oh, about Rika..." curly
    ja "I hope she's well" glow
    ja "I feel like she's cheered up considerably ever since [name] arrived but..she still feels a bit distant.." curly
    ja "Come to think of it"
    ja "Maybe we should have an outing today"
    ja "I am sure to be done with work at around 16 : 00 today"
    ja "Is that fine with you Rika ?"
    ja "{image=jaehee_happy}" (img=True)
    ja "We can meet up at that novelty cafe we talked about"
    msg ja "I heard the person who runs it is very kind" square_m
    ja "Then I should leave.."
    ja "Goodbye"

    exit chatroom ja

    return

    return
