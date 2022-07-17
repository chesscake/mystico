label cd2_chat2():
    scene night
    play music the_way_home

    ri "Hi hi! You have reached another Lune chat !"
    ri "Please put a better one in its place! ^^"

    return

label cd2_chat2_expired():
    scene night
    play music the_way_home

    ri "Hi hi! You have reached another Lune chat !"
    ri "Please put a better one in its place! ^^"

    return

label cd2_chat2_outgoing_va:
    va "...."
    va "Oh. It's you again. You're up late"
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
