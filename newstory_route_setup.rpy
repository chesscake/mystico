#This is the setup page of New Story's common days from prologue (as of yet, not completed)
#to the 4th day before it branches off to the potential routes.
#since it's still in the demo phase, there's no character routes yet,
#it includes several endings instead based on heart points

label newstory_start():
    $ new_route_setup(route=newstory_route)
    $ character_list = [ju, z, s, y, ja, v, ri, r]
    $ heart_point_chars = [ju, z, s, y, ja, v, ri, r]
    # Typically you would put an introductory chatroom of some kind here.
    # For convenience, this simply jumps to the home screen.
    jump skip_intro_setup

default newstory_route_good_end = ["Good End",
    RouteDay('1st',
        [ChatRoom("Welcome [name]", "cd1_chat1", "00:01", [ri]),
        ChatRoom("Happily Ever After?", "cd1_chat2", "01:11", [z]),
        ChatRoom("Wine and Chocolates", "cd1_chat3", "03:38", [ju, v]),
        ChatRoom("Assistant Jaehee Kang here", "cd1_chat4", "06:00", [ja]),
        ChatRoom("I want a robot assistant too!", "cd1_chat5", "08:05", [s]),
        ChatRoom("Extracurricularly Attacked", "cd1_chat6", "10:46", [y]),
        ChatRoom("Yoosung's determination", "cd1_chat7", "12:18", [ri]),
        ChatRoom("Out of Touch", "cd1_chat8", "14:25", [ju]),
        ChatRoom("Cause for alarm?!", "cd1_chat9", "18:41", [y]),
        ChatRoom("Heart Man", "cd1_chat10", "21:44", [ju]),
        ChatRoom("Narcissistic Chatter", "cd1_chat11", "22:56", [z]),
        ]),
    RouteDay('2nd',
        [ChatRoom("-", "cd2_chat1", "00:01"),
        ChatRoom("-", "cd2_chat2", "01:11", [z]),
        ChatRoom("-", "cd2_chat3", "03:38", [ju, v]),
        ChatRoom("-", "cd2_chat4", "06:00", [ja]),
        ChatRoom("-", "cd2_chat5", "08:05", [s]),
        ChatRoom("-", "cd2_chat6", "10:46", [y]),
        ChatRoom("-", "cd2_chat7", "12:18", [ri]),
        ChatRoom("-", "cd2_chat8", "14:25", [ju]),
        ChatRoom("-", "cd2_chat9", "18:41", [y]),
        ChatRoom("-", "cd2_chat10", "21:44", [z]),
        ChatRoom("-", "cd2_chat11", "22:56", [ri]),
        ]),
    RouteDay('3rd',
        [ChatRoom("-", "cd3_chat1", "00:01"),
        ChatRoom("-", "cd3_chat2", "01:11", [z]),
        ChatRoom("-", "cd3_chat3", "03:38", [ju, v]),
        ChatRoom("-", "cd3_chat4", "06:00", [ja]),
        ChatRoom("To work or to live?", "cd3_chat5", "08:05", [ja]),
        ChatRoom("-", "cd3_chat6", "10:46", [y]),
        ChatRoom("-", "cd3_chat7", "12:18", [ri]),
        ChatRoom("-", "cd3_chat8", "14:25", [ju]),
        ChatRoom("-", "cd3_chat9", "18:41", [y]),
        ChatRoom("-", "cd3_chat10", "21:44", [z]),
        ChatRoom("-", "cd3_chat11", "22:56", [ri]),
        ]),
    RouteDay('4th',
        [ChatRoom("-", "cd4_chat1", "00:01"),
        ChatRoom("-", "cd4_chat2", "01:11", [z]),
        ChatRoom("-", "cd4_chat3", "03:38", [ju, v]),
        ChatRoom("-", "cd4_chat4", "06:00", [ja]),
        ChatRoom("-", "cd4_chat5", "08:05", [s]),
        ChatRoom("-", "cd4_chat6", "10:46", [y]),
        ChatRoom("-", "cd4_chat7", "12:18", [ri]),
        ChatRoom("-", "cd4_chat8", "14:25", [ju]),
        ChatRoom("-", "cd4_chat9", "18:41", [y]),
        ChatRoom("-", "cd4_chat10", "21:44", [z]),
        ChatRoom("End of the Common Days", "cd4_chat11", "22:56", [ri], plot_branch=PlotBranch(False)),
        ]),
    RouteDay('5th'),
    RouteDay('6th'),
    RouteDay('7th'),
    RouteDay('8th'),
    RouteDay('9th'),
    RouteDay('10th'),
    RouteDay('Final')]

default newstory_route_bad_end = ["Bad Story End",
    RouteDay('5th',
        [ChatRoom('An Unfinished Task', 'bad_end', '23:26', [v])] )]
default newstory_route_bre = ["Bad Relationship End",
    RouteDay('5th',
            branch_vn=BranchStoryMode('plot_branch_bre'))]
default newstory_route_normal_end = ["Normal End",
    RouteDay('5th',
        [TheParty('plot_branch_normal_end', '23:54')])] #this plot branch should be replaced by the diff. routes

default newstory_route = Route(
    default_branch=newstory_route_good_end,
    branch_list=[newstory_route_normal_end,
                    newstory_route_bad_end,
                    newstory_route_bre],
    route_history_title='New Story Common Days',
    history_background="Menu Screens/Main Menu/tutorial_day_route_bg.webp")
