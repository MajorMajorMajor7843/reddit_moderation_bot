import praw
import puni

#you need to have registed a personal script in reddit 
reddit = praw.Reddit(client_id = ,client_secret = 
, username = , password = , user_agent = )


r = reddit.subreddit("") #type the name of the subreddit you are moderating, without r/ (so just type in askreddit, not r/askreddit)
un = puni.UserNotes(reddit, r)
redditor = reddit.redditor("")#type in your username, exlcluding u/ (so just type in MajorMajorMajor instead of u/MajorMajorMajor


noted = False

for user in un.get_users():
    try:
        #type the name of the subreddit you are moderating, just like before
        if (any(reddit.subreddit(" ").banned(redditor=user))): #this line checks if the user is banned in the particular subreddit

            for note in un.get_notes(user):
                     #if user has no notes, this does not evaulate, hence, noted reamins false
                    print (note.note + " " + user)
                    noted = True

            if (not noted):
                     #user is banned, it has note, but the note is empty
                    link = 'http://www.reddit.com/message/messages/4vjx3v'   #have no idea what this is for
                    n = puni.Note(user, reason(this is the note), moderator(your username), link, 'permban')
                    un.add_note(n)
                    print ("added")
        else:
            for note in un.get_notes(user):
                     #user is noted, but not banned
                if (len(note.note)) > 1:
                        reddit.redditor(username).message('User noted but not banned', user) #I couldn't figure out how to send a modmail, this sends direct message to you
                    
    except:
        print("{} is shadowbanned/deleted".format(user))
       #To prevent unnecessary API requests, you need to specify remove_user
        #as lazy.
        un.remove_user(user, lazy=True)

#Things to do
#1: send modmail instead of direct message
#2: If the user has no note at all(instead of the note being empty), the script will ignore that as for user in un.get_users() only covers users listed in the moderator note. 
