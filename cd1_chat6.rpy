label cd1_chat6():
###MISSING MC REPLIES
    scene night

    enter chatroom s
    s "NO WAY!"
    s "I can't believe I missed out on Jumin's robot opening a chatroom on her own!"
    s "Technology is amazing!! So cool >_<"
    s "Jumin, if you see this,"
    s "tell me where you ordered it!"
    s "I want one too!!"
    s "Then I could teach her how to hack"
    s "and split my workload in half."
    s "{image=seven_huff}" (img=True)
    s "Speaking of which"
    s "I need to leave for an urgent short day trip for work."
    s "I won't be here for awhile..."
    s "This came in short notice so I'm super super sorry"
    s "{image=seven_cry}" (img=True)
    s "However!"
    s "If all goes well"
    s "it will only be a few days"
    s "so no worries I will return in time for the party★!!"
    s "In the meantime"
    s "maybe the party coordinators 1 & 2 can rely on my assistant"
    s "in case there's a bug!?!"
    s "I coded this app pretty well though~ so good luck~ finding one~ ♥♥♥"
    s "I will drop her contact via text msg anyway lol"
    s "Rika and [name] remember to check your inbox!"
    s "If all goes badly though"
    s "I might not return in time for the party"
    s "or like ever."
    s "As in"
    s "forever?"
    s "which might be kind of an issue"
    s "now that I think about it."
    s "In this case..."
    s "[name], how much do you know about python and node.js!?"
    s "wait no!"
    s "Maybe it's better to write here my will, just in case."
    s "To Zen,"
    s "I leave you my Best of Cat Memes for Cat Lovers account with 36k subscribers."
    s "I'm sure you won't disappoint all those followers when you take over!!"
    s "To Yoosung,"
    s "I leave you my collection of wigs and costumes."
    s "You never know when you might need to leave the country and forge a new identity"
    s "to run away from crippling college debt?!"
    s "To Jaehee,"
    s "I will leave my tool kit box ready for you!"
    s "handy for when you might need to repair yourself lolol"
    s "lolololol"
    s "lolololo"
    s "oh no, I started laughing out loud and"
    s "the madam gave me a death glare"
    s "and barked `what the hell is so funny´ at me ;;"
    s "shivers ;;;"
    s "Of course this is all a big joke! It's just a boring business trip!!"
    s "like the one Jumin does, yeah!! Nothing out of the ordinary here"
    s "I will come back in time."
    s "..."

    return

label cd1_chat5_expired():

    scene night

    enter chatroom s
    s "NO WAY!"
    s "I can't believe I missed out on Jumin's robot opening a chatroom on her own!"
    s "Technology is amazing!! So cool >_<"
    s "Jumin, if you see this,"
    s "tell me where you ordered it!"
    s "I want one too!!"
    s "Then I could teach her how to hack"
    s "and split my workload in half."
    s "{image=seven_huff}" (img=True)
    s "Speaking of which"
    s "I need to leave for an urgent short day trip for work."
    s "I won't be here for awhile..."
    s "This came in short notice so I'm super super sorry"
    s "{image=seven_cry}" (img=True)
    s "However!"
    s "If all goes well"
    s "it will only be a few days"
    s "so no worries I will return in time for the party★!!"
    s "In the meantime"
    s "maybe the party coordinators 1 & 2 can rely on my assistant"
    s "in case there's a bug!?!"
    s "I coded this app pretty well though~ so good luck~ finding one~ ♥♥♥"
    s "I will drop her contact via text msg anyway lol"
    s "Rika and [name] remember to check your inbox!"
    s "If all goes badly though"
    s "I might not return in time for the party"
    s "or like ever."
    s "As in"
    s "forever?"
    s "which might be kind of an issue"
    s "now that I think about it."
    s "In this case..."
    s "[name], how much do you know about python and node.js!?"
    s "wait no!"
    s "Maybe it's better to write here my will, just in case."
    s "To Zen,"
    s "I leave you my Best of Cat Memes for Cat Lovers account with 36k subscribers."
    s "I'm sure you won't disappoint all those followers when you take over!!"
    s "To Yoosung,"
    s "I leave you my collection of wigs and costumes."
    s "You never know when you might need to leave the country and forge a new identity"
    s "to run away from crippling college debt?!"
    s "To Jaehee,"
    s "I will leave my tool kit box ready for you!"
    s "handy for when you might need to repair yourself lolol"
    s "lolololol"
    s "lolololo"
    s "oh no, I started laughing out loud and"
    s "the madam gave me a death glare"
    s "and barked `what the hell is so funny´ at me ;;"
    s "shivers ;;;"
    s "Of course this is all a big joke! It's just a boring business trip!!"
    s "like the one Jumin does, yeah!! Nothing out of the ordinary here"
    s "I will come back in time."
    s "..."

    return

######____TEXT MESSAGES____

label after_cd1_chat5:

    compose text s:
        s "Here is his phone number, the codename is Vanderwood."
        s "(phone number)"
        s "I left him a private repository of the app's code along with some notes."
        s "He can do several other things besides maintenance and patching bugs by the way."
        s "Cleaning, medical assistance and even personal defense. If there's any emergency, he's your guy."
        label reply_vanderwoodphonenumber

    return

label reply_vanderwoodphonenumber:
    menu:
        "Codename?":
            s "Don't ask. Just let him do the job if you need him, okay?"
        "How about food delivery?":
            s "Sure, why not?"
            s "It will annoy the heck out of him but he'll do it, enjoy~"
        "I will only call him if he's hot.":
            s "Oh my god?!?"
            s "Did I accidentally step in in one of these High School movies?"
            s "Uuh, he has a pretty good looking face, brown eyes, long eyelashes..."
            s "A shame about everything else ;;"
            s "Don't tell him I told you any of this though... He will kill me. Twice if needed."
        "Are you really going to be okay?"
            s "I have everything ready if the worst case scenario happens-"
            s "It's all going to be fine."

    return
