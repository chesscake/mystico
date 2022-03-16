label cd1_chat1():

    #$ ri.prof_pic = "Profile Pics/Rika/rika-4.webp"
    #$ ja.prof_pic = "Profile Pics/Jaehee/jae-11.webp"
    #$ z.prof_pic = "Profile Pics/Zen/zen-2.webp"
    #$ y.prof_pic = "Profile Pics/Yoosung/yoo-42.webp"
    #$ va.prof_pic = "Profile Pics/V/v-7.webp"
    #$ ju.prof_pic = "Profile Pics/Jumin/ju-13.webp"
    #$ s.prof_pic = "Profile Pics/Seven/sev-1.webp"
    #$ v.prof_pic = "Profile Pics/V/v-2.webp"

    #$ ri.cover_pic = "Cover Photos/Rika/r1.webp"
    #$ ja.cover_pic = "Cover Photos/Jaehee/ja1.jpg"
    #$ z.cover_pic = "Cover Photos/Zen/z1.jpg"
    #$ y.cover_pic = "Cover Photos/Yoosung/y1.jpg"
    #$ ju.cover_pic = "Cover Photos/Jumin/ju1.jpg"
    #$ s.cover_pic = "Cover Photos/Seven/s1.jpg"
    #$ v.cover_pic = "Cover Photos/V/v1.jpg"

    $ ri.status = "Welcome to the R.F.A [name]!"
    $ ja.status = "Workload slightly decreased..."
    $ z.status = "Ready or not, here we go!"
    $ y.status = "It's always nice to see the organization grow"
    #$ va.status = "MEMBER NOT AVAILABLE"
    $ ju.status = "I wonder what Elizabeth the 3rd is up to..."
    $ s.status = "Meow Meow"
    $ v.status = "A new chapter begins..."

    scene night
    #play music looking_for_happiness

    ri "[name]!"
    ri "It's late and so much has happened today."
    ri "Are you tired?"
    menu:
        "I'm usually awake at this hour! And very excited to begin this.":
            award heart ri
            ri "I'm so pleased to hear that!!"
        "ZZzzzz...hot guys... zzzZzz... gimme hotties...":
            #big dumbfounded emoji if there's one, like ( ' - ' ) ..."
            ri "I... I see..."
            ri "Now that you mention it, the RFA does have a lot of attractive people..."
            ri "I've seen a photo of Jaehee before she joined us and"
            ri "you could see how gorgeous she is!"
            ri "And of course you too are beautiful, [name] ^^"
        "I'm about to go to bed actually. Will this take too long?":
            ri "I will be brief."
    ri "{image=rika_happy}" (img=True)
    ri "..."
    ri "{size=+5}Oh!!{/size}"
    ri "I should tell Saey- I mean Luciel to implement your own set of emoji too!!"
    ri "Each member gets one, as you likely noticed."
    ri "It makes chatting more exciting, don't you think?" #(bounce=True, specBubble="cloud_s")
    menu:
        "I can have my own set too? Yes! Make me cute!!":
            ri "Of course you can! You're an official member too."
            msg ri "I wonder what kind of expressions you want?" glow curly
            msg ri "I know this great artist..." glow
            msg ri "They'll surely create something that conveys your unique charm ^^" glow
            msg ri "Then I will ask Luciel to implement them once he's available" blocky
            msg ri "This will be so much fun!" curly
        "They're childish, I don't need them.":
            break heart ri
            "Do... Do you really think so?"
    ri "As for your avatar,"
    ri "you can change it any time as soon as you join."
    ri "Just go to your status and click your icon"
    ri "and select any of the available pictures."
    menu:
        "I already changed it!":
            ri "So you already knew how!"
            ri "You're very astute after all."
            ri "{image=rika_happy}" (img=True)
        "Can I upload anything I want?":
            ri "Yes, you can."
            ri "You can upload any picture you want or"
            ri "choose among a selection of avatars already provided."
            ri "These are a little special since the other members can react to them."
    ri "You can also change any other configurations you find!"
    ri "I hope it's intuitive to use."
    ri "I designed this application closely with Saeyoung,"
    menu:
        "Can Seven program an app for me too?":
            ri "Do you have ideas for a project?"
            ri "Unfortunately, Luciel's schedule is quite packed"
            ri "I'm not sure when he'll be available..."
            ri "It's even hard to make room for my requests."
            ri "{image=rika_sad}" (img=True)
        "Were the sky backgrounds your idea?":
            ri "That..."
            ri "That was his idea ^^"
            award heart s
            ri "The sky is very comforting to him."
            ri "And we wanted something that felt like home."
        "Can you code too, Rika?":
            award heart ri
            ri "Unfortunately, no. I cannot."
            ri "I do know about it and read several articles"
            ri "on the different programming languages available"
            ri "but in practice, alas..."
            ri "However, that aside,"
    ri "I wanted to make sure it was the most accomodating as possible for every different member."
    msg ri "In fact, each application has different features" glow
    msg ri "our version, for example," glow
    msg ri "has access to an e-mailing system." glow
    msg ri "Other members' versions can do other things..."
    msg ri "But I won't bore you with more details." blocky
    ri "It's past midnight."
    ri "More importantly,"
    ri "I opened this chat to tell you that"
    msg ri "I hope" glow
    msg ri "you find solace in the RFA." glow
    ri "Don't stress yourself with attending every chat,"
    ri "or inviting every guest."
    ri "You don't need to."
    msg ri "Do things at your own place." blocky
    msg ri "I want this place to be a comfort for you, not a chore." glow
    menu:
        "How many chats can I miss? Is it okay to be away?":
            ri "As long as it's not the majority of the day"
            ri "You'll do just fine."
        "What if I don't do a good job?":
            ri "Well..."
            ri "We can always try again, can't we?"
            ri "{image=rika_happy}" (img=True)
            ri "By that what I mean is-"
            ri "I do plan to throw more parties!"
    msg ri "I wonder if you've thought about the kind of party you want?" glow
    ri "I eagerly await your suggestions!"
    ri "Now"
    ri "it's time for me to sleep too."
    menu:
        "Good Night, Rika!":
            award ri heart
            ri "Good night, [name]!"
        "I'm not sleepy yet! Can I call someone at 3 am?":
            ri "You can do anything you want, [name]."
    ri "Sweet dreams and have fun with the other members."

    return

label cd1_chat1_expired():

    #$ ri.prof_pic = "Profile Pics/Rika/rika-4.webp"
    #$ ja.prof_pic = "Profile Pics/Jaehee/jae-11.webp"
    #$ z.prof_pic = "Profile Pics/Zen/zen-2.webp"
    #$ y.prof_pic = "Profile Pics/Yoosung/yoo-42.webp"
    #$ va.prof_pic = "Profile Pics/V/v-7.webp"
    #$ ju.prof_pic = "Profile Pics/Jumin/ju-13.webp"
    #$ s.prof_pic = "Profile Pics/Seven/sev-1.webp"
    #$ v.prof_pic = "Profile Pics/V/v-2.webp"

    #$ ri.cover_pic = "Cover Photos/Rika/r1.webp"
    #$ ja.cover_pic = "Cover Photos/Jaehee/ja1.jpg"
    #$ z.cover_pic = "Cover Photos/Zen/z1.jpg"
    #$ y.cover_pic = "Cover Photos/Yoosung/y1.jpg"
    #$ ju.cover_pic = "Cover Photos/Jumin/ju1.jpg"
    #$ s.cover_pic = "Cover Photos/Seven/s1.jpg"
    #$ v.cover_pic = "Cover Photos/V/v1.jpg"

    $ ri.status = "Welcome to the R.F.A [name]!"
    $ ja.status = "Workload slightly decreased..."
    $ z.status = "Ready or not, here we go!"
    $ y.status = "It's always nice to see the organization grow"
    #$ va.status = "MEMBER NOT AVAILABLE"
    $ ju.status = "I wonder what Elizabeth the 3rd is up to..."
    $ s.status = "Meow Meow"
    $ v.status = "A new chapter begins..."

    scene night
    #play music looking_for_happiness
    ri "It's late and so much has happened today."
    ri "You aren't here, [name]"
    ri "so I hope you are already in bed peacfully sleeping."
    ri "{image=rika_happy}" (img=True)
    ri "..."
    ri "{size=+5}Oh!!{/size}"
    ri "I should tell Saey- I mean Luciel to implement your own set of emoji too!!"
    ri "Each member gets one, as you likely noticed"
    ri "It makes chatting more exciting, don't you think?" #(bounce=True, specBubble="cloud_s")
    msg ri "I wonder what kind of expressions you want?" glow curly
    msg ri "I know this great artist..." glow
    msg ri "They'll surely create something that conveys your unique charm ^^" glow
    msg ri "Then I will ask Luciel to implement them at his earliest convenience!" blocky
    msg ri "This will be so much fun!" curly
    ri "As for your avatar,"
    ri "you can change it any time as soon as you join."
    ri "Just go to your status and click your icon"
    ri "and select any of the available pictures."
    ri "You can also change any other configurations you wish too!"
    ri "I hope it's intuitive to use"
    ri "I designed this application closely with Saeyoung,"
    ri "I wanted to make sure it was the most accomodating as possible for every different member."
    msg ri "In fact, each application has different features" glow
    msg ri "our version, for example," glow
    msg ri "has access to an e-mailing system." glow
    msg ri "Other members' versions can do other things..."
    msg ri "But I won't bore you with more details." blocky
    ri "It's past midnight."
    ri "More importantly,"
    ri "I opened this chat to tell you that"
    msg ri "I hope" glow
    msg ri "you find solace in the RFA." glow
    ri "Don't stress yourself with attending every chat,"
    ri "or inviting every guest."
    ri "You don't need to."
    msg ri "Do things at your own place." blocky
    msg ri "I want this place to be a comfort for you, not a chore." glow
    ri "Whenever you feel lonely,"
    ri "whenever you feel sad,"
    ri "or if you're just bored..."
    msg ri "Please come to us."
    msg ri "I want you to feel better." glow
    ri "{image=rika_happy}" (img=True)
    msg ri "Besides wanting to throw an amazing party, of course!" curly
    ri "Our goals are one and the same after all"
    ri "so I'm certain you'll do great!"
    ri "A cohesive party theme for example"
    ri "is bound to be a success and will raise more funds."
    msg ri "I wonder if you've thought about the kind of party you want?"
    ri "I eagerly await your suggestions!"
    ri "Now"
    ri "it's time for me to sleep too."
    ri "Sweet dreams and have fun with the other members."
    ri "If any problem arises don't hesitate to call me."

    return

######____TEXT MESSAGES____

label after_cd1_chat1:

    compose text ri:
        ri "I've never had an assistant before."
        ri "I think now I will have an idea why Jumin can't live without one."
        label reply_assistantri

    return

label reply_assistantri:
    menu:
        "Assistant [name] here. Ready at your every command, Miss Kim.":
            ri "No, no! My name is Rika! Just Rika, please!"
            ri "I don't really have a surname."
            ri "Wait... was that... a Jaehee impression?"
        "I'm nobody's assistant.":
            ri "Of course, you're a fellow precious member!"
            ri "The RFA is my only family..."
            ri "I'm sorry if it sounded like I wanted to boss you around."
            ri "I won't do that."
        "I will be very happy to help you!":
            ri "Thank you!"
            ri "If anything happens to us, we can count to be there for each other, right?"
            ri "♡"



    compose text s:
        s "Yoo, hi [name] ★_★ !"
        s "I don't think I've messaged you yet."
        s "How r u?? Do you like the app?"
        label reply_howareyous

    return

label reply_howareyous:
    menu:
        "Hi, Seven! I'm great, thank you ^o^":
            s "I'm happy to hear that ^^"
            s "Having a new member is the best!!!"
            s "They can test my app while knowing I'm the one made it <3"
        "This app sucks. Can't you do better?":
            s "?!?!?!"
            s "B-but Rika told me it was amazing... T_T..."

    return
