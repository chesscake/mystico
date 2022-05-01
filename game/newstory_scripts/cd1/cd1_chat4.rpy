label cd1_chat4():

    scene night

    enter chatroom ja

    ja "Opening up chatroom."
    ja "Done."
    ja "Setting up new status..."

    $ ja.status = "Welcome to the RFA, [name]!"

    ja "Done."
    ja "New status has been added."
    ja "I wanted to greet the newest member and suggest a guest to invite to the party..."
    ja "However, both Rika and [name] are absent."
    ja "No one is here."
    ja "Should I leave?"

    enter chatroom v

    ja "Oh."
    v "Hi? Hello?"
    ja "Welcome to the chatroom, sir."
    ja "I'd like to express my deepest gratitude into choosing me to work for C&R."
    ja "Mr. Han told me how your keen eye selected me among countless candidates."
    ja "Therefore, from the bottom of my heart,"
    ja "thank you."
    ja "I promise I won't let you down."
    v "Ah."
    v "Jaehee Kang, was it?"
    v "For a moment I thought Luciel let one of his bots open a chatroom."
    v "{image=v_well}" (img=True)
    ja "............."
    v "You don't need to be so overly formal."
    v "I'm not your employer"
    v "You can see me as a friend."
    ja "I'm afraid a friend of my superior is my superior too."
    v "Haha..."
    v "Apparently Jumin was so pleased with your performance he wanted you to join us."
    v "That's quite a extraordinary feat."
    v "I can count with the fingers of one hand the people that managed to impress him this much."
    ja "I do not believe I'm that great..."
    ja "And I seldom hear any praise."
    v "Trust me, he might not express it properly and even be rather brusque"
    v "But you're an invaluable asset to him now and for the company."
    v "Ah... Sorry, I have to leave right now."
    v "I dropped by again because I saw the notification."
    ja "Of course. Thank you for your kind words, sir."
    v "You can call me V."
    v "Now if you excuse me."

    exit chatroom v

    ja "I will log off too, I have to get back to work."
    ja "I hope we can talk soon, [name]."

    exit chatroom ja

    return

label cd1_chat4_expired():

    scene night

    enter chatroom ja

    ja "Opening up chatroom."
    ja "Done."
    ja "Setting up new status..."

    $ ja.status = "Welcome to the RFA, [name]!"

    ja "Done."
    ja "New status has been added."
    ja "I wanted to greet the newest member and suggest a guest to invite to the party..."
    ja "However, both Rika and [name] are absent."
    ja "No one is here."
    ja "Should I leave?"

    enter chatroom v

    ja "Oh."
    v "Hi? Hello?"
    ja "Welcome to the chatroom, sir."
    ja "I'd like to express my deepest gratitude in choosing me to work for C&R."
    ja "Mr. Han told me how your keen eye selected me among countless candidates."
    ja "Therefore, from the bottom of my heart,"
    ja "thank you."
    ja "I promise I won't let you down."
    v "Ah."
    v "Jaehee Kang, was it?"
    v "For a moment I thought Luciel let one of his bots open a chatroom."
    v "{image=v_well}" (img=True)
    ja "............."
    v "You don't need to be so overly formal."
    v "I'm not your employer"
    v "You can see me as a friend."
    ja "I'm afraid a friend of my superior is my superior too."
    v "Haha..."
    v "Apparently Jumin was so pleased with your performance he wanted you to join us."
    v "That's quite a extraordinary feat."
    v "I can count with the fingers of one hand the people that managed to impress him this much."
    ja "I do not believe I'm that great..."
    ja "And I seldom hear any praise."
    v "Trust me, he might not express it properly and even be rather brusque"
    v "But you're an invaluable asset to him now and for the company."
    v "Ah... Sorry, I have to leave right now."
    v "I dropped by again because I saw the notification."
    ja "Of course. Thank you for your kind words, sir."
    v "You can call me V."
    v "Now if you excuse me."

    exit chatroom v

    ja "I will log off too, I have to get back to work."
    ja "I hope we can talk soon, [name]."

    return
