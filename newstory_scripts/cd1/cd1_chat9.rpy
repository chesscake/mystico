label cd1_chat9():

    scene night

    enter chatroom y

    y "Came out of school and read a couple of chats"
    y "Speaking of which"
    msg y "A, a few days ago Seven called me after class," ser1
    msg y "making these weird cat sounds" ser1
    msg y "saying he no longer wanted to be human." ser1
    y "I don't want to cause alarm but I think"
    y "{size=+15}the meow pox virus is spreading!!{/size}"
    menu:
        "Oh my gosh!! We need to quarantine him!! No party for him!":
            award heart y
            y "Yes!!!"
            y "But if he doesn't go to the party it will disappoint Rika"
            y "and I can't bear to see her sad!!"
            y "Maybe can wrap him up in a giant protective bubble."
            y "He can move it by rolling inside like a hamster!"
            menu:
                "From cat to hamster, Seven's life is already shaping up to be quite a roller coaster.":
                    y "We can't risk the spread of an infectuous disease at the party!"
                    #yoosung defiant emoji
                "Won't he suffocate inside an air tight bubble?":
                    y "Maybe he can go outside to breathe when oxygen is running out..."
        "No no, meow. It's all safe, trust meow!":
            award heart s
            y "NOOO!"
            y "Not YOU TOO, [name]!"
            #yoosung cry
    enter chatroom ja
    msg ja "Let me make something clear" glow
    msg ja "There's no such thing as meow pox virus." blocky
    y "Really?!"
    ja "Yes. There's no such disease and C&R is completely safe."
    ja "We adhere strictly to all safety protocols."
    y "But what if Seven is infected with it?"
    msg ja "{size=+5}That's just how he is.{/size}" blocky
    msg y "Hm... I think I will have to ask Rika about that first." sigh_l
    msg y "I remember meeting Seven at the RFA's very first party," glow
    msg y "before you and Zen joined." glow
    msg y "He was this kind of quiet guy." sser1
    ja "I can't speak much since I wasn't there, however..."
    msg ja "First impressions can be deceiving." bold
    msg ja "Since the group was new and it was the very first party" sser2
    msg ja "it's possible even someone like him was nervous." sser2
    y "You might be right ;;"
    y "I don't know much about him after all..."
    y "despite him being one of the original members when the group was founded."
    ja "Zen, me, [name] all joined after the first party..."
    msg y "Yup!" cloud_s
    msg y "Rika is so amazing! Thanks to her we're all gathered together like this!"
    msg y "Persons from all walks of life I've never thought I could meet" round_m
    msg y "all united for a single cause!!" round_m
    #yoosung smile emoji
    y "I think"
    msg y "{size=+10}Rika is living proof that angels exist!{/size}" sser1 #big emphasis
    msg y "Don't you breathe better whenever she's in chats, Jaehee?!"
    ja "Well, I..."
    ja "I didn't meet her in person yet."
    menu:
        "Seeing Rika makes me so happy...":
            award heart y
            award heart ri
            y "She's so pure, like an angel. A true goddess!"
            ja "Can someone pure like that really exist, though...?"
            y "You only need to open your eyes, Jaehee."
        "Calm down! She's just a normal human girl.":
            award heart ri
            y "She's an inspiration."
            y "You'll understand what I mean..."
            y "Your life will improve with her around. Guarantee!"
            y "My grades improved so much ever since I met her."
        "Should we have a small meetup before the party?":
            award heart ja
            ja "That's actually a good idea."
    ja "Anyway, forgive me for changing subjects..."
    ja "What else do you know about Luciel, Yoosung?"
    ja "I've looked into every member, including [name]"
    ja "but I can't find anything about him."
    ja "I don't even know what he does for a living."
    y "Uh, wasn't he studying something at college?"
    y "And he's now working at some agency."
    y "I haven't been paying much attention, sorry."
    ja "Since you were at the first party you might know more."
    ja "I'm curious about this agency place... could it be an high risk job?"
    menu:
        "His last chat was a bit disconcerting.":
            award heart s
            y "What? No way!"
            y "Rika or V would never let him work on something dangerous!"
            ja "I don't know them well so I will take your word for it."
        "I think it was all genuinely a joke.":
            y "Yeah!!"
        "Agency?? Like a modeling agency?":
            y "maybe lol"
            y "Maybe he's a model and he isn't telling us."
            ja "A model? His red hair is quite striking, just like his golden doed eyes..."
            ja "But it still doesn't compare to Zen's beauty. His long ethereal white hair and"
            y "ethereal white hair, what?? lol"
            y "Jaehee you sound exactly like my girl classmates comparing male idols lolol"
            ja "A, anyway..."
            y "lolol"
        y "I wouldn't take it seriously."
        y "Lately he's been joking like that a lot."
        y "Dark humor goes around a lot these days too."
        y "My classmates make jokes like that too,"
        y "how their parents are going to kill them if they don't get an A"
        y "or they're about to die from all the homework."
        ja "I see..."
        menu:
            "He called Jaehee a robot but she's still worried about him! She's so kind.":
                award heart ja
                ja "Why, thank you..."
                ja "Honestly, I've been hearing that so often I forgot about it."
                ja "It's nice to hear a compliment from someone..."
            "I don't think your classmates jokes should be shrugged off either.":
                award heart ri
                ja "Indeed."
                ja "There's truth in comedy, as the saying goes."
                y "And sometimes jokes are just that, jokes."
                y "I know how demanding the entrance exams are,"
                y "but no one's going to actually die...!"
            "I want to know where this agency is... Maybe I could find my dream guy there.":
                y "?!?!"
                ja "I presume you're assuming it's a modeling agency."
                ja "But we're not sure of that yet, are we?"
                y "what if he's been working on modeling gigs all this time"
                y "secretly plotting to overtake Zen lol"
                y "That's why he's so secretive about his job."
                ja "Impossible."
                ja "There's more to Zen than good looks, he's a fully fledged actor! A master of the performer arts. A model doesn't compare nor will ever replace him. Not only his acting easily bests these of Hollywoob actors, his singing is bar none "
                y "I wasn't serious;;"
                ja "If it's any other kind of talent agency, I'm still certain his singing won't be as good as Zen and what about his acting? Acting is the most important quality of an actor and Zen excels at it! It took years and years to reach that level"
                y "Jaehee, breathe ;;"
                y "No one's going to steal Zen's career."
                y "Rika wouldn't let anyone do that."
        y "Arg, you know..."
        y "I'd love to stay here and talk more"
        y "but I'm about to arrive to cram school."
        y "I really need to leave now, sorry!"

        exit chatroom y

        menu:
            "Aannd off he goes. He's really dedicated, haha":
                award heart y
                ja "Yes, he is."
                ja "I hope his exams go well."
            "I think you should sit out on this one. You don't need to know the private lives of the members.":
                ja "I guess so."
        ja "Anyway, I will leave too."
        ja "Take care, [name]."

        exit chartoom ja

        return

label cd1_chat9_expired():

    scene night

    enter chatroom y

    y "Came out of school and read a couple of chats"
    y "Speaking of which"
    msg y "A, a few days ago Seven called me after class," ser1
    msg y "making these weird cat sounds" ser1
    msg y "saying he no longer wanted to be human." ser1
    y "I don't want to cause alarm but I think"
    y "{size=+15}the meow pox virus is spreading!!{/size}"

    enter chatroom ja

    msg ja "Let me make something clear" glow
    msg ja "There's no such thing as meow pox virus." blocky
    y "Really?!"
    ja "Yes. There's no such disease and C&R is completely safe."
    ja "We adhere strictly to all safety protocols."
    y "But what if Seven is infected with it?"
    msg ja "{size=+5}That's just how he is.{/size}" blocky
    msg y "Hm... I think I will have to ask Rika about that first." sigh_l
    msg y "I remember meeting Seven at the RFA's very first party," glow
    msg y "before you and Zen joined." glow
    msg y "He was this kind of quiet guy." sser1
    ja "I can't speak much since I wasn't there, however..."
    msg ja "First impressions can be deceiving." bold
    msg ja "Since the group was new and it was the very first party" sser2
    msg ja "it's possible even someone like him was nervous." sser2
    y "You might be right ;;"
    y "I don't know much about him after all..."
    y "despite him being one of the original members when the group was founded."
    ja "Zen, me, [name] all joined after the first party..."
    msg y "Yup!" cloud_s
    msg y "Rika is so amazing! Thanks to her we're all gathered together like this!"
    msg y "Persons from all walks of life I've never thought I could meet." round_m
    msg "All united for a single cause!!"
    #yoosung smile emoji
    y "I think"
    msg y "{size=+10}She is living proof that angels exist!{size}" sser1 #big emphasis
    msg y "Don't you breathe better whenever she's in chats, Jaehee?!"
    ja "Well, I..."
    ja "I didn't meet her yet in person."
    ja "Anyway, forgive me for changing subjects..."
    ja "What else do you know about Luciel, Yoosung?"
    ja "I've looked into every member, including [name]"
    ja "but I can't find anything about him."
    ja "I don't even know what he does for a living."
    y "Uh, wasn't he studying something at college?"
    y "And he's now working at some agency."
    y "I haven't been paying much attention, sorry."
    ja "Since you were at the first party you might know more."
    ja "I'm curious about this agency place... could it be an high risk job?"
    y "No way!"
    y "Rika or V would never let him work on something dangerous!"
    ja "I don't know them well so I will take your word for it."
    y "Lately he's been joking like that a lot."
    y "Dark humor goes around a lot these days too."
    y "My classmates make jokes like that too,"
    y "how their parents are going to kill them if they don't get an A"
    y "or they're about to die from all the homework."
    ja "I see..."
    y "Arg, you know..."
    y "I'd love to stay here and talk more"
    y "but I'm about to arrive to cram school."
    y "I really need to leave now, sorry!"
    ja "No problem, I'm going to leave too."
    y "Alright, see you."

    exit chatroom y
    exit chatroom ja

    return
