label day_1_chatroom_5():

    $ ri.status = "So many things for [name] to learn! Please help [them] everyone"

    scene noon
    play music the_way_home

    enter chatroom ri

    ri "My my, what nice day this is turning out to be"
    ri "The sky is clear, birds are chirping...it feels like a paradise"
    msg ri "I'm so glad you were introduced to the R.F.A on  a day like this one  [name]! ^^" glow 
    $ is_idiot = False 
    menu:
        "I'm so excited to begin working with you guys!":
            $ is_idiot = False 
            award heart ri
            ri "That's the spirit!"
            msg ri "I'm glad you're so eager to begin" curly
        "It just feels like any other day to me": 
            $ is_idiot = False 
            ri "I see....That's alright."
            ri "I guess that means you're adjusting to us faster than I expected"
        "You again? I was kind of hoping to meet someone new": 
            $ is_idiot = True
            break heart ri
            ri "Oh my, am I being overbearing?"
            ri "That wasn't my intention...I'm sorry"
    ri "I'll try to make this experience the best it can possibly be "
    msg ri "Seeing the chatroom filled with buzz, as per usual, fills me with so much joy" bold
    if is_idiot:
        ri "I'm sorry if my presence caused you uneccesary stress "
        ri "I promise I'll do better.."
    msg ri "I try to do my best for the R.F.A" glow
    ri "I thought I'd come in for a bit and explain the basics to you"
    msg ri "You see, while this chatroom may provide a way for members to communicate" ser1
    ri "That isn't its main purpose"
    ri "Discussing the parties, and the noble deeds they lead to is the actual objective!"
    ri "We've had so much success in the past, so now isn't the time to stop!"
    msg ri "Let's try to make an amazing party everyone will remember [name]!"
    menu:
        "I'll do my best for the sake of the R.F.A!":
            award heart ri
            ri "And that's exactly the thing we need!"
            ri "I'm sure you'll rise to the ocassion"
            msg ri "You seem so passionate about this! I'm glad to hear that!^^" glow
        "Sure...Hope it won't be too difficult":
            ri "Oh no, it won't be difficult at all!"
            ri "I'll be there to help you every step of the way"
            msg ri "Have no doubts about that!" bold
        "Not really interested in stuff like that, sorry":
            ri "Oh...Why is that?"
            ri "Have any specific reasons?"
            menu:
                "I feel like parties aren't enough to truly help people":
                    msg ri "Though you may have a point..." ser1
                    award heart ri
                    ri "Doing anyting is better than doing nothing at all"
                "I don't really care about helping lazy people who accept charity":
                    ri "..."
                    break heart ri
                    ri "I'm a bit shocked to hear that...Especially coming from you"
                    ri "I hope being a member of the R.F.A changes your mind..."
    ri "Back to the task at hand.."
    ri "You see, our main purpose is to bring smiles to peoples faces!"
    ri "That means inviting as many different kinds of people as possible to our parties and making sure they all feel comfortable being there"
    ri "Without good will, you can't create an environment that everyone can enjoy"
    ri "That's why we strive to keep our heads high and mind clear when doing the work we do"
    msg ri "Being a good host to the guests is integral to making the experience fun for them, as well as the other members" glow
    ri "Party planning can often take months to complete.."
    ri "Luckily, a lot of that work has already been done!"
    ri "We've booked our venue and made arrangements with our sponsors"
    ri "However...I realized we don't have many guests that reflect the people we see all around us.."
    ri "Small business owners, entrepeneurs who want to do good for the world, people who want to feel like they finally belong..."
    ri "In fact.."
    msg ri "You're the one wo made me realise that, back when we had our first conversation!" glow
    ri "Since then, I've been encouraging the members to discuss any potential guest opportunities with you"
    ri "The party will hopefully be a success, regardless of how many people we manage to invite during this time"
    ri "However..."
    msg ri "I'd really appreciate if if you could invite as many people as possible!" bold
    menu:
        "Sounds like a lot of fun! I'm in!":
            award heart ri
            ri "So happy to hear that!!"
            ri "The R.F.A will only continue to grow if you're the one helping us out!"
        "If that's a part of the job...alright.":
            ri "I suppose it is, yeah!"
            ri "Glad you're in! Hope to see the fruits of our labour soon"
    ri "Reading over what the others have said..."
    ri "I've noticed a couple of them already started suggesting possible guests to invite"
    msg ri "That's just what I wanted! So excited to meet some of the people the members mentioned" ser2
    ri "Occasionaly I'll be the one suggesting what guests we could invite"
    msg ri "I know it might seem a bit silly, since I could just invite them myself" ser1
    msg ri "But I really want to see you at play on your own!" glow
    ri "How fun that will be!"
    ri "Is there something I'm forgetting?"
    ri "I feel like I'm leaving something important out..."
    pause 1.0*5
    ri "Oh yes! Of course!"
    ri "Another duty you'll have as a coordinator is doing field work with me!"
    ri "That means going to various places and seeing what people are in need"
    ri "This way, we'll know exactly who the people we are helping are!"
    msg ri "Isn't that amazing?" glow
    menu:
        "I hope we can bring a smile to the faces of those people":
            award heart ri
            ri "I hope so too!!!"
            msg ri "There are so many unhappy people in this world.."
            ri "Bringing happiness to them is of the utmost importance"
        "Let's hope we won't have to do that all that often":
            ri "I'll try not to bother you with it too much"
            ri "I know you might have a lot of responsibillities outside the R.F.A"
            ri "But...it'd be great if you showed up, even if its only once"
    ri "Speaking to people like that is very important, as it allows us to connect to them even more"
    ri "I hope I made everything about the party clear!"
    msg ri "If you have any other questions...feel free to text or call me!" glow
    ri "Stay safe! I heard there's a new plague making its way around the world ^^"
    ri "See you soon!!!"
    
    exit chatroom ri
    
    return

label day_1_chatroom_5_expired():

    $ ri.status = "So many things for [name] to learn! Please help [them] everyone"

    scene noon
    play music the_way_home

    enter chatroom ri

    ri "My my, what nice day this is turning out to be"
    ri "The sky is clear, birds are chirping...it feels like a paradise"
    msg ri "I'm so glad [name] was introduced to the R.F.A today!" glow
    ri "I wish [they] were here.."
    ri "I wanted to explain a couple of things about the party to [them]"
    ri "I'll try to make this experience the best it can possibly be "
    ri "Seeing the chatroom filled with buzz, as per usual, fills me with so much joy"
    ri "I try to do my best for the R.F.A"
    ri "I thought I'd come in for a bit and explain the basics to you"
    ri "You see, while this chatroom may provide a way for members to communicate"
    ri "That isn't its main purpose"
    ri "Discussing the parties, and the noble deeds they lead to is the actual objective!"
    ri "We've had so much success in the past, so now isn't the time to stop!"
    msg ri "Let's try to make an amazing party everyone will remember !"
    ri "It shouldn't be difficult at all!"
    ri "I'll be there to help [name] every step of the way, and so will everyone else"
    ri "Back to the task at hand.."
    ri "Our main purpose is to bring smiles to peoples faces!"
    ri "That means inviting as many different kinds of people as possible to our parties and making sure they all feel comfortable being there"
    ri "Without good will, you can't create an environment that everyone can enjoy"
    ri "That's why we strive to keep our heads high and mind clear when doing the work we do"
    msg ri "Being a good host to the guests is integral to making the experience fun for them, as well as the other members" glow
    ri "Party planning can often take months to complete.."
    ri "Luckily, a lot of that work has already been done!"
    ri "We've booked our venue and made arrangements with our sponsors"
    ri "However...I realized we don't have many guests that reflect the people we see all around us.."
    ri "Small business owners, entrepeneurs who want to do good for the world, people who want to feel like they finally belong..."
    ri "In fact.."
    msg ri "[name] is the  one who made me realise that, back when we had our first conversation!" glow
    ri "Since then, I've been encouraging the members to discuss any potential guest opportunities with you"
    ri "The party will hopefully be a success, regardless of how many people we manage to invite during this time"
    ri "However..."
    msg ri "I'd really appreciate it if [name] could invite as many people as possible!" bold
    ri "Reading over what the others have said..."
    ri "I've noticed a couple of them already started suggesting possible guests to invite"
    msg ri "That's just what I wanted! So excited to meet some of the people the members mentioned" ser2
    ri "Occasionaly I'll be the one suggesting what guests we could invite"
    msg ri "I know it might seem a bit silly, since I could just invite them myself" ser1
    msg ri "But I really want to see [name] at play on [their] own!" glow
    ri "How fun that will be!"
    ri "Is there something I'm forgetting?"
    ri "I feel like I'm leaving something important out..."
    pause 1.0*5
    ri "Oh yes! Of course!"
    ri "Another duty [they] will have as a coordinator is doing field work with me!"
    ri "That means going to various places and seeing what people are in need"
    ri "This way, we'll know exactly who the people we are helping are!"
    msg ri "Isn't that amazing?" glow
    msg ri "There are so many unhappy people in this world.." glow
    ri "Bringing happiness to them is of the utmost importance"
    ri "I'll try not to bother [them] with it too much"
    ri "I know [they] might have a lot of responsibillities outside the R.F.A"
    ri "But...it'd be great if [name] showed up, even if its only once"
    ri "Speaking to people like that is very important, as it allows us to connect to them even more"
    ri "I hope I made everything about the party clear!"
    msg ri "If you have any other questions...feel free to text or call me!" glow
    ri "Stay safe everyone! I heard there's a new plague making its way around the world ^^"
    
    exit chatroom ri
    
    return

    label after_day_1_chatroom_5:

    compose text ri:
        ri "I hope I made everything a little more clear for you!"
        ri "I hope this text feature will be of use whenever you need to contact me!"
        label reply_explanation

    return

label reply_explanation:
    menu:
        "I got it! Thank you for helping me": 
            award heart ri
            ri "Of course! I'm so glad I could be of use" 
            ri "I was getting worried you were getting bored! Glad that wasn't the case "
        "I already knew most of what you said":
            ri "That's great ! Sorry I was a bit of a bore then"
            ri "We could discuss something you like next time!"
    ri "I won't be on the chatroom much today..Hope you have fun with the members!"
    ri "I'll come back to chat soon!"

    return