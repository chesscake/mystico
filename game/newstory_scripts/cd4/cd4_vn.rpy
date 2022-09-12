label branches_of_destiny_vn ():

    scene bg mc_room with fade
    pause
    play sound persistent.phone_tone
    "   " "The phone is ringing..."
    menu:
        extend ''

        "*Pick up*":
            stop sound
            "???" "Hello [name]!It's me, Rika."
            ri "I knew you'd answer me, but...I'm so sorry for calling you out of the blue like this. "
            ri "However....I really need you to hear me out"
        "*Don't pick up*":
            play sound persistent.phone_tone
            "   " "The phone keeps ringing.."
            "   " "You feel  a strange urge to pick up."
            "   " "In a flash, you find yourself with your phone to your ear"
            stop sound
            "???" "Hello [name]!It's me, Rika."
            ri "I'm sorry for bothering you..You must have been in the middle of something"
            ri "You can hang up if you're busy, I just..."
            ri "..need you to hear me out"
    "   " "Her voice sounds shaky..."
    play music looking_for_happiness
    ri "I've been doing some thinking and wanted to consult  you about something"
    ri "This might seem like a really strange question but..."
    ri "Imagine there's this amazing goal you're trying to accomplish"
    ri "But the people around you keep telling you that such a thing is impossible."
    ri "Would you listen to them? Or would you persist and keep on trying to achieve your goal?"
    menu:
        extend ''

        "I'd keep on trying, doing everything I can to make my ambitions come to fruition":
            award heart ri 
            ri "Then we agree! I am so glad you said that!"
            ri "Why would you give up on something that means a lot to you.."
            ri "Just because some  people disagree ?"
            ri "I wish everyone would see it like that"
        "If everyone around me thinks it isn't a good idea...I'd probably give up.":
            ri "I see...I'm kind of sad to hear that"
            ri "You know [name], you don't have to give up just because others disagree"
            ri "If you work towards achieving something.."
            ri "Even your wildest dreams could become a reality"
    ri "That question came out of nowhere...Hope I didn't worry you too much"
    ri "I just needed to talk to someone about this."
    ri "I've been having these thoughts a lot these days and needed someone to talk to about them."
    ri "You were the first to come to mind..."
    ri "And....I also wanted to ask you something."
    ri "I need to visit a cathedral that's quite a distance away from here to retrieve some documents."
    ri "Since you're also a coordinator of the R.F.A , you get to accompany me on various RFA-related activities - this trip being one of them."
    ri "Would you be willing to accompany me there?"
    ri "Don't worry about making travel plans! I could call a cab to pick us up or drive you there myself."
    ri "What do you think? I know this is sudden and could possibly interfere with your plans but..."
    ri "I'd really appreciate it if you'd come."
    menu:
        extend ' '


        "Of course I'll come! Count me in!":
            award heart ri
            ri "Thank you so much [name]!" 
            ri "I really appreciate this..more than you could know"
            jump vn_rievent
        "I'm not sure about that...":
            ri "Are you sure you can't make it?"
            ri "I'd really like for you to be there..."
            "   " "Seems like she really wants you there"
            menu:
                extend ' '


                "Sorry, I really don't think I can make it":
                    break heart ri
                    ri "Oh....."
                    ri "I understand..You have a life of your own after all"
                    ri "I'll just...go there myself. Goodbye [name]."
                    play sound call_end_sfx
                    jump vn_mcevent
                "On second thought, I think I'll tag along":
                    ri "I'm so glad you changed your mind.."
                    ri "I'll try to make it worth your time as best I can.."
                    jump vn_rievent


    label vn_rievent ():
    $current_timeline_item.who = 'ri'
    ri "Alright then...since you were gracious enough to accept, I'll be the one driving you there!"
    ri "Give me a minute to get my car started , and I'll be there in a flash!"
    ri "See you soon!!!"
    stop music
    play sound call_end_sfx
    "   " "The call ended"
    scene bg black with fade
    "   " ".  .  ."
    pause
    "   " "Half an hour later..."
    scene bg mc_room with fade
    play sound door_knock_sfx
    ri "Hello [name]! It's me! Hope I didn't startle you"
    play sound door_open_sfx
    show rika smile at vn_center 
    ri "My my, what a beautiful room you have here...Almost makes me want to stay over!"
    ri sad "I guess that'll have to wait though...Are you ready?"
    menu:
        extend ' '
        "Yes I am! You've arrived just in time":
            ri happy "I'm glad to hear that!"
            ri happy "But you don't have to lie, I know I took a while to get here"
            award heart ri
            ri thinking "Stil...I appreciate you saying that!"
        "What took you so long?":
            ri thinking "Ah, I knew it"
            ri "Sorry for making you wait. That wasn't my intention"
    ri neutral "On the way here, I ran into a bit of a traffic jam..."
    ri "Thank you for being patient with me. I know I was the one who roped you into coming in the first place"
    ri happy "Now that that's settled...shall we head out?"
    hide rika
    show bg car with fade
    show rika neutral at vn_center
    ri "I know it isn't the most luxurious of cars, but I think it's good enough for the two of us."
    play music lonesome_practicalism
    ri "I rented it out recently, so I'm still not used to driving it around on my own."
    menu:
        extend ' '
        "You're not alone! I'm here with you":
            award heart ri
            ri happy "That's right! With you here, I'm sure everything will be just fine"
            ri "You know...I have a really good feeling about this trip..."
        "Doesn't V usually drive you around?":
            ri thinking "No, not really. i usually take public transport"
            ri "He's usually busy with one thing or another. I don't mind. Because of that, I get to spend the day with you!"
    ri happy "The place we're heading to is quite special to me!"
    ri "You see, this is where I spent a good chunk of my teenage years volunteering.I know everyone there, as if they're my own family"
    ri "However...I don't want you to feel excluded. So whenever you feel like striking up a conversation with someone, I could help introduce you!"
    ri "I gave them a heads up before coming to pick you up, so they'll be waiting for us at the gate"
    ri "You'll love everyone there! They're all very nice!"
    ri "I can't wait to show you everything that place has to offer....Maybe you could even meet some of the children staying there"
    ri "There's a whole bag of sugar-free candy in the back...We can even hand some out if you want to!"
    ri thinking "Ah, I didn't mean to talk so much...I'm just so excited we're getting to do this together" 
    ri "What do you want to talk about?"
    menu: 
        extend ' '
        "I'm looking forward to meeting everyone you mentioned!":
            award heart ri
            ri "So am I! They're all going to like you, I just know it!"
            ri "I saw just how interesting of a person you are  as soon as I met you..."
            ri sad "Um..I suppose this isn't the time to talk about that though"
        "How long are we going to stay there?":
            ri "Well, I haven't thought about that yet"
            ri "It shouldn't take too long, as I just need to pick some things up from the main building"
            ri "I hope this doesn't disturb your schedule too much..."
    "   " "As the conversation progressed, the scenery changed. Soon, you found yourselves in front of a quaint cathedral in the middle of nowhere"
    ri happy "Oh my..I kind of got lost in our conversation...I can't believe we're already here!"
    ri "Would you look at that? All the children are here...Come on, lets head out"
    stop music
    hide rika
    scene bg cathedral with fade
    pause
    play music same_old_fresh_air
    "Child 1" "Hey, everyone, she's here!! Rika the angel is here!!"
    "Child 2" "Are those sweets?? Can I have some??"
    "Child 3" "Me too! Me too!"
    "Child 2" "No way! You got so many last time. Now its our turn!"
    show rika happy at vn_center
    ri "Calm down everyone! There are enough sweets to go around!"
    hide ri
    pause
    ri worried "I also brought along a dear friend of mine to help me! So please, no more fighting."
    "   " "And with that, Rika managed to stop the fighting."
    "   " "More and more kids kept arriving. At one point, it seemed like they would overwhelm you , but Rika managed to keep the peace."
    "   " "You were both handing out candy for what felt like hours, until the bag was empty,"
    "Child 1" "Thank you so much Rika! Please visit us more often!"
    show rika happy at vn_center
    ri "Are you just saying that because you want more sweets ?"
    "Child 1" "No I'm not!! You're really nice too...and you're always so gentle with us."
    ri "The nuns here are all really nice to you as well! You know how much they care about you."
    "Child 1" "Yeah, but they keep lecturing us! I'm so tired of it. I wish you were here more often"
    ri worried "I'm sure they're just doing what's best for you...I know it might seem harsh sometimes, but it's all for your own good!"
    "Child 1" "I guess! I'm gonna go play with Areum now, goodbye Rika! Goodbye Rika's friend!"
    ri "Look at her go...She's so full of energy. I admire that a lot in these kids"
    ri "You know, they've all been left here because their parents couldn't take care of them"
    ri "So they're being raised by the staff here...It's amazing how they manage to keep a smile on their face despite all that."
    ri "I'm so glad you were here to help me..I think all the kids really liked you."
    ri sad "You looked just like a fairy while you were handing out candy"
    award heart ri
    pause
    ri thinking "Oh my...I'm sorry if I made you uncomfortable with that"
    stop music
    menu:
        extend ' '
        "You didn't make me uncomfortable at all!":
            award heart ri
            ri happy "I'm glad I didn't. I just wanted to compliment you is all"
            ri "You looked like you were having a lot of fun too!"
            menu:
                extend ' '
                "I thought you looked beautiful as well!":
                    award heart ri 
                    award heart ri
                    award heart ri
                    ri sad "Oh my...Thank you [name]."
                    ri "That means a lot , especially from someone as beautiful as .."
                    ri "With a beautiful soul, like you."
                "Hm, I wish we could have handed out some more candy..":
                    ri "That's a great idea! I'll bring some more next time we visit."
                    ri "Along with something a bit more healthy as well, of course."
        "It did make me a bit uncomfortable":
            break heart ri
            ri "I see...I'll keep that in mind in the future"
            ri "Sorry, I think I got a bit too comfortable. I shouldn't have said that...stupid..."
    "???" "Oh my...The children told me you were here and I didn't believe them! How did you arrive so quickly?"
    ri happy "Hello Sister! I'm so glad you're here! [name], meet Sister Agatha! She's the first person I met when I came here"
    "Sister Agatha" "I remember that day like it was yesterday...This girl here came all the way from the city, wanting to help us out"
    play music i_miss_happy_rika
    "Sister Agatha" "Back then, the church was small and in the middle of a very poor neighborhood...But with her help, we raised funds, and look at us now!"
    ri worried "You're too kind, Sister Agatha. I just did what felt right...for you, and all the children here!"
    "Sister Agatha" "Look at her! Still as humble as ever. God, thank you for putting this child among us!"
    show rika thinking
    "Sister Agatha" "You have shown us all what life in Christ is supposed to look like."
    ri "Thank you Sister...."
    "Sister Agatha" "As for those documents you asked about..they're in your old room."
    ri "Yes, I'll go ahead and pick them up then...Do you mind waiting for me here [name]?"
    "Sister Agatha" "Oh, I'm sure it's fine. I'll be here with [them] and keep [them] company."
    ri "All right...I'll be back  very soon!"
    hide rika with easeoutright
    "Sister Agatha" "That child is too good for her own good. I'm worried about her sometimes."
    "Sister Agatha" "Since you two seem pretty close, please make sure she stays out of trouble, alright?"
    show rika neutral at vn_center with ease
    ri "Alright...I think I got everything...Thank you so much for Sister!"
    "Sister Agatha" "Of course child...It's the least I could do for you."
    stop music
    #Possible grieving scene here ?
    ri "I think we're done here for now..."
    ri "Come on, let's head on home..."
    hide rika
    scene bg car wit fade
    "   " "As you were leaving the premises, you could swear you saw a dark, hunched over figure in the cathedrals orchard, disappearing as soon as you tried to get a better look"
    "   " "The rumbling of the motor interrupted your train of thought, as Rika started the trek back home..,"
    return



    label vn_mcevent ():
    pause
    "   " "..."
    menu:
        extend ' '
        "*Call Vanderwood*":
            play sound phone_ring_sfx
            "   " "Dialing..."
            jump vn_venevent
        "*Take a nap*":
            "   " "You feel your eyelids getting heavy and decide to take a rest..."
            "   " "Laying down on your bed, you begin to think about these past few days.."
    "   " "With that, you slowly drift into dreamland.."
    scene bg black with fade
    pause
    scene bg absolute_domain
    play music lost_dream
    "???" "Welcome"
    return


    label vn_venevent ():
    $current_timeline_item.who = 'va'
    va "What is it?"
    return
