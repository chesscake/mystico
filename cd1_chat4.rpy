label cd1_chat6():

    $ y.status = "Busy with school..."

    scene noon
    play music silly_smile_again


    enter chatroom y

    y " Teacher gave us a 10 minute break in class"
    msg y "Finally, he rambled on for so long ;;" sigh_m
    y "It wasn't even related to the material for the exam!!"
    y "It was like"
    msg y "~Kids these days don't know how good they have it~" ser2
    msg y "~Back when I was young we didn't have those fancy calculators~" ser2
    msg y "Argh" spike_s
    msg y "Of course it wasn't just 5 minutes of complaining" blocky
    msg y "He began to throw his entire life story at us." blocky
    y "Mr. Lee, it's not our fault"
    y "you didn't have any electricity growing up"
    y "with 6 other siblings!!"
    msg y "Just do your job, we have an exam in 4 days!!" sigh_m
    menu:
        "Stop whinning, this app is to organize parties.":
            break heart y
            y "Rika told us we can use this app to chat like friends too..."
        "Who's Mr. Lee?":
            y "My math teacher."
            y "Please don't tell me..."
            y "That you are thinking of inviting him to the party?!"
        "An exam in 4 days? Good luck!!":
            award heart y
            y "Thank you!"
    y "I went through"
    y "every math assignment already,"
    y "every math problem in the book!!"
    y "But I still don't think it's good enough..."
    y "I need more!"
    y "I can't afford to screw up."
    msg y "{size=+5}I have to make Rika happy.{/size}" glow
    msg y "I can't let her down." ser1
    menu:
        "That's a noble goal!":
            award heart ri
            award heart y
            y "Thank you, [name]!!"
            y "Praise makes me feel good ^_^"
        "It's ok to take a break.":
            y "No time for breaks!!"
            y "The more I study the less room for mistakes there is."
    #add shake and delay
    y "Ugh!"
    y "My classmates are calling me."
    msg y "I wonder what it is this time?" curly
    y "I already told them I don't have time to hang out."
    y "After the exams are over I will be busy again"
    y "helping Rika with the party..."
    menu:
        "Run along and take a good rest after your exams! I will help Rika out!":
            award heart ri
            award heart y
            y "You're so kind"
            y "No wonder you and Rika are friends."
            y "But I want to help too!"
            y "This party is so important to her..."
        "You're such a nerd lol":
            y "I have to in order to get into a good university!"
        "That's right, this is no time to mess around.":
            award heart y
            y "You got it!"
    y "Well then,"
    y "See you later, [name]!"
    exit chatroom y

    return

label cd1_chat6_expired():


    $ y.status = "Busy with school..."

    scene noon
    play music silly_smile_again


    enter chatroom y

    y " Teacher gave us a 10 minute break in class"
    msg y "Finally, he rambled on for so long ;;" sigh_m
    y "It wasn't even related to the material for the exam!!"
    y "It was like"
    msg y "~Kids these days don't know how good they have it~" ser2
    msg y "~Back when I was young we didn't have those fancy calculators~" ser2
    msg y "Argh" spike_s
    msg y "Of course it wasn't just 5 minutes of complaining" blocky
    msg y "He began to throw his entire life story at us." blocky
    y "Mr. Lee, it's not our fault"
    y "you didn't have any electricity growing up"
    y "with 6 other siblings!!"
    msg y "Just do your job, we have an exam in 4 days!!" sigh_m
    y "I went through"
    y "every math assignment already,"
    y "every math problem in the book!!"
    y "But I still don't think it's good enough..."
    y "I need more!"
    y "I can't afford to screw up."
    msg y "{size=+5}I have to make Rika happy.{/size}" glow
    msg y "I can't let her down." ser1
    y "Anyway, my classmates are calling me."
    msg y "I wonder what it is this time?" curly
    y "I already told them I don't have time to hang out."
    y "After the exams are over I will be busy"
    y "helping Rika with the party..."
    y "Well then,"
    y "I hope everyone is keeping up to date with their responsibillities."
    y "See you all later."
    exit chatroom y

    return
