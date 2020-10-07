## ****************************************************
## A TEMPLATE EMAIL GUEST
## ****************************************************

default example_guest = Guest("example",
## The first string, "example", is what will show up in the
## email chain as the guest's 'email' e.g. "longcat" shows up
## as "@longcat" in the email chain. This is also the variable
## you use for reply labels, not the name of the variable
"Email/Thumbnails/guest_unlock_icon.webp",
## The second string is the image to use for the guest's
## thumbnail. It should be 155x155px
## Because the variable is 'example_guest', when you want to
## invite this person, you will write: invite example_guest

## Initial Message
"""Dear [name],

You can write whatever you want in here. It is the first message that is sent
to you after you invite the guest. Note that any new lines you write here will
be new lines in the actual email; you can look to the previous guest for ideas
on formatting. This example simply has breaks in the middle of lines to make
it easier to read when editing code.

From, your example guest""", # don't forget the comma after the quotes

## FIRST MESSAGE - *Question the guest asked here*

## It's a good idea to write down what the answer is to get to this response
## in the comments so you don't forget
## Answer -> CORRECT ANSWER HERE
## First Message (correct)

"""This is what your character will send the guest after selecting the correct
response to the email. You can use their name in the email by typing [name]""",

## Reply to correct message

"""This is what the guest will send you after you replied
to their first email correctly""",

## Answer -> INCORRECT ANSWER HERE
## First Message (incorrect)

"""This is what your character writes to the guest when they
choose the wrong response""",

## Reply to incorrect message

"""And this is the response the guest will write you after you choose
the incorrect response. Usually they say something that indicates they
don't want to go to the party""",

## SECOND MESSAGE - *Question the guest asked here*

## Answer -> CORRECT ANSWER HERE
## Second Message (correct)

"""This is your message to the guest with the correct response""",

## Reply to correct message

"""This is the guest's reply to your message after you choose the
correct response""",

## Answer -> INCORRECT ANSWER HERE
## Second Message (incorrect)

"""This is your message to the guest with the incorrect response""",

## Reply to incorrect message

"""This is the guest's reply to your message after you choose the
wrong response""",

## THIRD MESSAGE - *Question the guest asked here*

## Answer -> CORRECT ANSWER HERE
## Third Message (correct)

"""This is your message to the guest with the correct response""",

## Reply to correct message

"""This is the guest's reply to your message after you chose the
correct response. It usually says something about seeing you at
the party, as this is the final message""",

## Answer -> INCORRECT ANSWER HERE
## Third Message (incorrect)

"""This is your message to the guest with the incorrect response""",

## Reply to incorrect message

"""This is the guest's reply to your message after you choose
the wrong response."""

## These next fields are optional but used for the guestbook
## Large (usually chibi) image for the party, no wider than 315px
"Email/Guest Images/rainbow_unicorn.webp",

## Short description about the guest
"Example Guest, an example guest for this program.",

## Personal Info section on the guest
"Example Guest was made for users to better understand how to create a guest.",

## The ChatCharacter variable of the person who should talk about this
## guest in the long description
s,

## What the previous character says about this guest
"Here, the character from the last variable (Seven) will say this.",

## The expression/displayable name of the character to show
'seven front party happy',

## The name of the guest as it should appear in their
## dialogue box
"Example Guest",

## The dialogue the guest says when they attend the party
"The guest will probably mention something about the party."
) # Don't forget a closing bracket at the end

label example_reply1():
    # The guest is called "example", so the
    # reply labels will be called
    # example_reply1, example_reply2, and example_reply3

    menu:
        "Answer 1":
            # Passing 'True' indicates that this is the correct reply
            # Either answer can be correct, not necessarily the first option
            # The program will randomly shuffle the answers when showing
            # them to the user
            $ current_email.set_reply(True)

        "Answer 2":
            # Similarly, passing 'False' indicates this was the wrong reply
            # and will fail the email chain
            $ current_email.set_reply(False)

    jump email_end # This ensures your response is saved after you reply

label example_reply2():

    menu:
        "Answer 1":
            $ current_email.set_reply(True)

        "Answer 2":
            $ current_email.set_reply(False)

    jump email_end

label example_reply3():

    menu:
        "Answer 1":
            $ current_email.set_reply(True)

        "Answer 2":
            $ current_email.set_reply(False)

    jump email_end


default example_guest_new = Guest(
## Because the variable is 'example_guest_new', when you want to
## invite this person, you will write: invite example_guest_new

## The first string, "example", is what will show up in the
## email chain as the guest's 'email' e.g. "longcat" shows up
## as "@longcat" in the email chain.
"example",

## The next string is the name of the guest as it should show up in the
## guestbook when they arrive at the party e.g. "Long Cat"
"Example Guest",

## This string is the image to use for the guest's
## thumbnail. It should be 155x155px
"Email/Thumbnails/guest_unlock_icon.webp",

## This string is the file path to the full-body image of this guest. It will
## be shown when they attend the party. It is a larger (usually chibi) image
## for the party, no wider than 315px.
"Email/Guest Images/rainbow_unicorn.webp",

## This next string is a short description of the guest, shown in the
## guestbook when they have been invited.
"Example Guest, an example guest for this program.",

## Personal Info section on the guest, shown in the guestbook after the
## guest has attended the party.
"Example Guest was made for users to better understand how to create a guest.",

## This is the beginning email that will be sent to the player after the guest
## is invited. It is usually easier to write this with triple quotes so you
## can incorporate line breaks.
"""Dear [name],

You can write whatever you want in here. It is the first message that is sent
to you after you invite the guest. Note that any new lines you write here will
be new lines in the actual email; you can look to tutorial_2_emails for ideas
on formatting. This example simply has breaks in the middle of lines to make
it easier to read when editing code.

From, Example Guest""", # don't forget the comma after the quotes

## This differs from the previous way to define guests. Here, you will define
## the sequence of choices the player has to answer the guest.
[ EmailReply(
    ## An EmailReply object holds the information needed for an email message.
    ## The first argument is the text that will appear on the choice box when
    ## the player opts to answer the email.
    "There will be food at the party",

    ## The next argument is the message that the player will send to the guest
    """Dear Example Guest,

    Yes, we are planning to have an entire banquet at the party, with plenty
    of food.

    Sincerely, [name]""", # Don't forget the comma

    ## And this is the reply the guest will send the player.
    """Dear [name],

    That sounds wonderful. Do you like soup?

    From, Example Guest""", # Don't forget the comma

    ## Now, since this choice continues the chain, you will add another
    ## EmailReply object
    [EmailReply(
        "I love soup",

        """Dear Example Guest,

        Yes I love soup!

        Sincerely, [name]""",

        """Dear [name],

        Oh, that is excellent news. What soup is your favourite?

        From, Example Guest""",

        ## Once again, this is the good reply, so the chain continues
        [EmailReply(
            "I love potato soup",

            """Dear Example Guest,

            I love potato soup the most. Will I see you at the party?

            Sincerely, [name]""",

            """Dear [name],

            An excellent choice. I hope you are serving potato soup at the
            party. I will see you there!

            From, Example Guest""",
            ## This is the end of this particular chain, so no more EmailReply.
            ## However, you need to indicate whether getting to this reply
            ## resulted in a successful email chain or a failed one.
            email_success=True
        ), # Don't forget a comma here if you want to add more choices
        ## This is another choice for the menu
        EmailReply(
            "I love stew",

            """Dear Example Guest,

            I'd have to say I love stew best! Hope to see you at the party~

            Sincerely, [name]""",

            """Dear [name],

            I believe we may have misunderstood each other. Stew is not soup!
            I may be at the party... I will have to think about it.

            From, Example Guest""",
            ## This is the end of the email chain, but this was the incorrect
            ## reply, so indicate that
            email_success=False
        )   # If you like, you can add a comma here and add another EmailReply
            # object to the list. However, this menu has two choices, so it
            # ends with a square bracket here to finish the list.
        ]
    ),
    ## This is a choice that will show up alongside the "I love soup" choice.
    ## Note the indentation and list elements.
    EmailReply(
        "I like cereal better",

        """Dear Example Guest,

        Soup is nice, but you know what's better? A nice bowl of cereal. I hope
        you'll agree.

        Sincerely, [name].""",

        """Dear [name],

        Cereal??? At a party??? I must say I question your food choices.
        I may not attend this party after all.

        From, Example Guest""",

        ## This email also ends the chain, so it is set to False here
        email_success=False
    )]
),
## And this choice shows up alongside the "There will be food at the party"
## choice.
EmailReply(
    "We will have a DJ at the party",

    """Dear Example Guest,

    Thank you for your interest! We are planning to hire a DJ for the party.

    Hope to see you there,
    [name]""",

    """Dear [name],

    Ah, I was really hoping there might be some food at the party... I am
    quite the food lover. I don't know if I'll be attending this party after
    all.

    From, Example Guest""",

    email_success=False
)], # There's a comma here to continue adding information to the guest; the
# remaining fields are optional but recommended. They appear when the guest
# attends the party and when the player clicks on the guest's entry in the
# guestbook.

## The dialogue the guest says when they attend the party
"Thank you for inviting me! I wonder if they're serving any potato soup...",

## The ChatCharacter variable of the person who should talk about this
## guest in the long description in the guestbook.
s,

## What the previous character says about this guest.
"Here, the character from the last variable (Seven) will say this.",

## The expression/displayable name of the character to show
"seven front party happy",

## This indicates how many emails the player needs to successfully exchange
## with this guest to guarantee their presence at the party.
## By default this is 3 but you may change it here like so.
num_emails=3

) # Don't forget a closing bracket at the end


default rainbow = Guest(
## Because the variable is 'example_guest_new', when you want to
## invite this person, you will write: invite example_guest_new

## The first string, "example", is what will show up in the
## email chain as the guest's 'email' e.g. "longcat" shows up
## as "@longcat" in the email chain.
"rainbow",

## The next string is the name of the guest as it should show up in the
## guestbook when they arrive at the party e.g. "Long Cat"
"Rainbow",

## This string is the image to use for the guest's
## thumbnail. It should be 155x155px
"Email/Thumbnails/rainbow_unicorn_guest_icon.webp",

## This string is the file path to the full-body image of this guest. It will
## be shown when they attend the party. It is a larger (usually chibi) image
## for the party, no wider than 315px.
"Email/Guest Images/rainbow_unicorn.webp",

## This next string is a short description of the guest, shown in the
## guestbook when they have been invited.
"Rainbow Unicorn, the creator of this program.",

## Personal Info section on the guest, shown in the guestbook after the
## guest has attended the party.
"Rainbow started working on this project back in 2018 and she's excited to share it with the world!",

## This is the beginning email that will be sent to the player after the guest
## is invited. It is usually easier to write this with triple quotes so you
## can incorporate line breaks. Note that double line breaks will be preserved,
## but singular line breaks are replaced with a space, so you can split up
## lines for ease of reading the code.
"""Hi [name]!

Really excited to hear about this party you're holding! Can't wait to see
how things will turn out for you. Zen told me to make sure your inbox is
working, and well, if you're reading this, I guess it is! So that's good.

I did have one quick question though -- will the party be held inside or
outside? Please let me know as soon as possible!

Thanks,

Rainbow Unicorn""", # don't forget the comma after the quotes

## This differs from the previous way to define guests. Here, you will define
## the sequence of choices the player has to answer the guest.
[ EmailReply(
    ## An EmailReply object holds the information needed for an email message.
    ## The first argument is the text that will appear on the choice box when
    ## the player opts to answer the email.
    "Indoor Party",

    ## The next argument is the message that the player will send to the guest
    """Dear Rainbow,

    I'm pleased to inform you that the party will be indoors. No need for
    umbrellas or sunscreen!

    Hope to see you there,

    [name], the party coordinator""", # Don't forget the comma

    ## And this is the reply the guest will send the player.
    """Hi again,

    Oh, how wonderful! I was worried about what the weather would be like
    on the day of the party. I thought of another question: what kind of
    music will there be at the party?

    Hope to hear from you soon,

    Rainbow Unicorn""", # Don't forget the comma

    ## Now, since this choice continues the chain, you will add another
    ## EmailReply object
    [EmailReply(
        "Smooth Jazz",

        """Dear Rainbow,

        We've got a wonderful playlist full of smooth jazz songs to
        play at the party. We're also looking into the possibility of
        a live band!

        Hope that answers your question.

        Sincerely,

        [name]""",

        """Dear [name],

        Oh, that's just fantastic news. Jazz is such a lovely music genre,
        isn't it? Just between the two of us, I'm also quite partial to video
        game soundtrack music. But I don't expect you to play that at the party!

        You've been so kind with your answers, and if you don't mind, I had
        one last question -- what sort of food will there be at the party?
        Please let me know when you can!

        From, Rainbow""",

        ## Once again, this is the good reply, so the chain continues
        [EmailReply(
            "Spicy food",

            """To the lovely Rainbow,

            There will be a delicious selection of spicy food at the party!
            In particular there will be experienced chefs from places such as
            India and Mexico who will be catering. I hope your taste buds
            are ready!

            Sincerely,

            [name]""",

            """To [name],

            Wow! I adore spicy foods; it's almost as though you read my mind!
            I will most certainly have to come and sample the dishes you've
            described.

            Thank you very much for taking the time to answer my questions.
            I'll see you at the party!

            Best,

            Rainbow""",
            ## This is the end of this particular chain, so no more EmailReply.
            ## However, you need to indicate whether getting to this reply
            ## resulted in a successful email chain or a failed one.
            email_success=True
        ), # Don't forget a comma here if you want to add more choices
        ## This is another choice for the menu
        EmailReply(
            "Seafood",

            """To the lovely Rainbow,

            We're planning to serve a variety of seafood at the party! There
            will be plenty of dishes to try, like fried octopus, shrimp
            tempura, and caviar. Hope you come with an appetite!

            From,

            [name]""",

            """To [name],

            That certainly sounds... interesting! I can't really consider
            myself a fan of seafood, however, so you'll have to excuse me
            for my lack of enthusiasm.

            That said, I do appreciate you taking the time to answer me. I'm
            a bit undecided on whether or not to attend, but wish you the
            best of luck with the preparations!

            Sincerely,

            Rainbow Unicorn""",
            ## This is the end of the email chain, but this was the incorrect
            ## reply, so indicate that
            email_success=False
        )   # If you like, you can add a comma here and add another EmailReply
            # object to the list. However, this menu has two choices, so it
            # ends with a square bracket here to finish the list.
        ]
    ),
    ## This is a choice that will show up alongside the "I love soup" choice.
    ## Note the indentation and list elements.
    EmailReply(
        "Heavy Metal",

        """Hi Rainbow,

        I've found some wonderful heavy metal music to play at the party!
        Screaming vocals really set the mood, don't you think? I hope you'll
        enjoy the music!

        Sincerely,

        [name], the party coordinator""",

        """Hi again,

        Oh dear, heavy metal? I can't say I enjoy that sort of music. I
        appreciate the invitation, but now that I know you'll be playing
        heavy metal music... I'll have to think more on it.

        Thank you for your help.

        Rainbow""",

        ## This email also ends the chain, so it is set to False here
        email_success=False
    )]
),
## And this choice shows up alongside the "There will be food at the party"
## choice.
EmailReply(
    "Outdoor party",

    """Dear Rainbow,

    We're planning for an outdoor party! There are gardens at the venue that will be perfect for an elegant party.
    Hope to see you there!

    Sincerely,

    [name], the party coordinator""",

    """Hi again,

    Oh dear, I'm afraid I have terrible allergies and that may not work out well for me. I appreciate the time you've taken to email me but I may have to decline.

    Thank you for the invitation, and best of luck to you and the party.

    Rainbow Unicorn""",

    email_success=False
)], # There's a comma here to continue adding information to the guest; the
# remaining fields are optional but recommended. They appear when the guest
# attends the party and when the player clicks on the guest's entry in the
# guestbook.

## The dialogue the guest says when they attend the party
"Oh, it's so exciting to be at the party! I can't wait to see everyone.",

## The ChatCharacter variable of the person who should talk about this
## guest in the long description in the guestbook.
z,

## What the previous character says about this guest.
"Is Rainbow's name a reference to me? Haha, well, I am quite a rainbow unicorn if I do say so myself~",

## The expression/displayable name of the character to show
"zen front party happy",

## This indicates how many emails the player needs to successfully exchange
## with this guest to guarantee their presence at the party.
## By default this is 3 but you may change it here like so.
num_emails=3

) # Don't forget a closing bracket at the end

