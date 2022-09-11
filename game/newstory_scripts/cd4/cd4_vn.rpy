label branches_of_destiny_vn ():

    scene bg hallway with fade
    #scene bg MC_room
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
                    #play sound call_end
                    jump vn_mcevent
                "On second thought, I think I'll tag along":
                    ri "I'm so glad you changed your mind.."
                    ri "I'll try to make it worth your time as best I can.."
                    jump vn_rievent


    label vn_rievent ():
    $current_timeline_item.who = 'ri'
    ri "I'm on my way to your dimension *-;"
    return



    label vn_mcevent ():
    pause
    "   " "..."
    menu:
        extend ' '
        "*Call Vanderwood*":
            #play sound dialing
            "   " "Dialing..."
            jump vn_venevent
        "*Take a nap*":
            "   " "You feel your eyelids getting heavy and decide to take a rest..."
            "   " "Laying down on your bed, you begin to think about these past few days.."
    "   " "With that, you slowly drift into dreamland.."
    scene bg black with fade
    pause
    #scene bg absolute_domain
    #play in_a_frozen_dream
    "???" "Welcome"
    return


    label vn_venenet ():
    $current_timeline_item.who = 'va'
    va "What is it?"
    return
