import praw
import os
import time
import logging
import random

while True:
    try:
        def authenticate():
            # CONFIGS/DEFINITIONS
            localtime = time.asctime(time.localtime(time.time()))
            logging.basicConfig(filename='Activity.log',level=logging.INFO)

            # AUTHENTICATE
            print('Authenticating...')
            reddit = praw.Reddit(
                'korokBot',
                user_agent="dj505gaming's Korok bot")
            print('Authenticated as {}'.format(reddit.user.me()))

            # LOGGING
            logging.info(localtime + ": Authenticated successfully")

            return reddit


        def main():
            # AUTHENTICATE AND RUN BOT
            reddit = authenticate()
            while True:
                run_bot(reddit)


        def run_bot(reddit):
            # CONFIGS/DEFINITIONS
            from random import randint
            num_replies = sum(1 for line in open('replied.txt'))
            hurt = ["Ouch.", "Unngh.", "Gya!"]
            reply = "Yahaha! You found me!\n\n---\n\n^^Koroks ^^found: ^^{} ^^| ^^[Info](https://reddit.com/r/korokbot/) ^^| [^^Suggest ^^a ^^feature](https://www.reddit.com/r/KorokBot/comments/6n35g4/feature_suggestion_and_bux_fix_megathread/) ^^| ^^Twee-hee!".format(num_replies + 1)
            reply2 = "Twee hee!\n\n---\n\n^^Koroks ^^found: ^^{} ^^| ^^[Info](https://reddit.com/r/korokbot/) ^^| [^^Suggest ^^a ^^feature](https://www.reddit.com/r/KorokBot/comments/6n35g4/feature_suggestion_and_bux_fix_megathread/) ^^| ^^Twee-hee!".format(num_replies + 1)
            reply3 = random.choice(hurt) + "\n\n---\n\n^^Koroks ^^found: ^^{} ^^| ^^[Info](https://reddit.com/r/korokbot/) ^^| [^^Suggest ^^a ^^feature](https://www.reddit.com/r/KorokBot/comments/6n35g4/feature_suggestion_and_bux_fix_megathread/) ^^| ^^Twee-hee!".format(num_replies + 1)
            localtime = time.asctime(time.localtime(time.time()))
            logging.basicConfig(filename='Activity.log',level=logging.INFO)

            # MAIN
            print('Searching...')
            
            # OPEN AND READ replied.txt
            if not os.path.isfile("replied.txt"):
                comments_replied = []

            else:
                with open('replied.txt', 'r+') as f:
                    comments_replied = f.read()
                    comments_replied = comments_replied.split("\n")
                    comments_replied = list(filter(None, comments_replied))

            # OPEN AND READ dont_reply.txt
            if not os.path.isfile("dont_reply.txt"):
                dont_reply = []

            else:
                with open('dont_reply.txt', 'r+') as f:
                    dont_reply = f.read()
                    dont_reply = dont_reply.split("\n")
                    dont_reply = list(filter(None, dont_reply))

            # SEARCH FOR COMMENTS IN ZELDA SUBREDDITS (breath_of_the_wild+zelda+botw+legendofzelda+gaming+nintendoswitch)
            for comment in reddit.subreddit('breath_of_the_wild+zelda+botw+legendofzelda+gaming+nintendoswitch').comments(limit=3):

                # LOOKS FOR COMMENTS CONTAINING 'korok'
                if 'korok' in comment.body and comment.id not in comments_replied and comment.id not in dont_reply and randint(0,100) < 30 and comment.parent().author != reddit.user.me() and comment.author != reddit.user.me():
                    # PRINT FOUND CONFIRMATION
                    print("Found Korok (ID: {})".format(comment.id))

                    # REPLY TO COMMENT
                    comment.reply(reply)

                    # ADD COMMENT ID TO replied.txt AND OUTPUT LOG
                    comments_replied.append(comment.id)
                    localtime = time.asctime(time.localtime(time.time()))
                    logging.basicConfig(filename='Activity.log',level=logging.INFO)
                    with open("replied.txt", "w") as f:
                        for comment.id in comments_replied:
                            f.write(comment.id + "\n")
                    logging.info('Found Korok! ID {}'.format(comment.id))

                    # SEND CONFIRMATION
                    print('Replied to ID {}'.format(comment.id))
                    reddit.redditor('dj505Gaming').message('KorokBot', 'Replied to message ID {}'.format(comment.id))
                    print(num_replies)

                if 'korok' in comment.body and comment.id not in comments_replied and comment.id not in dont_reply and randint(0,100) > 30 and comment.parent().author != reddit.user.me():
                    # PRINT FOUND CONFIRMATION
                    print("Didn't reply (below threshold) (ID: {})".format(comment.id))

                    # ADD COMMENT ID TO replied.txt AND OUTPUT LOG
                    dont_reply.append(comment.id)
                    localtime = time.asctime(time.localtime(time.time()))
                    logging.basicConfig(filename='Activity.log',level=logging.DEBUG)
                    with open("dont_reply.txt", "w") as f:
                        for comment.id in dont_reply:
                            f.write(comment.id + "\n")
                    logging.info("Didn't reply (below threshold) (ID {})".format(comment.id))

                elif 'korok' in comment.body and 'rock' not in comment.body and comment.id not in comments_replied and comment.id not in dont_reply and comment.parent().author == reddit.user.me() and comment.author != reddit.user.me():
                    # PRINT FOUND CONFIRMATION
                    print("Found duplicate reply (ID: {})".format(comment.id))

                    # REPLY TO COMMENT
                    comment.reply(reply2)

                    # ADD COMMENT ID TO replied.txt AND OUTPUT LOG
                    dont_reply.append(comment.id)
                    localtime = time.asctime(time.localtime(time.time()))
                    logging.basicConfig(filename='Activity.log',level=logging.INFO)
                    with open("dont_reply.txt", "w") as f:
                        for comment.id in dont_reply:
                            f.write(comment.id + "\n")
                    logging.info('Duplicate reply! ID {}'.format(comment.id))

                    # SEND CONFIRMATION
                    print('Replied to ID {}'.format(comment.id))
                    print(num_replies)

                elif 'drops' in comment.body and comment.id not in dont_reply and comment.parent().author == reddit.user.me() and comment.author != reddit.user.me():
                    # MAKE SURE BOT IS BEING HOT BY ROCK
                    if 'rock' in comment.body:
                        # PRINT FOUND CONFIRMATION
                        print("Hit by rock (ID: {})".format(comment.id))

                        # ADD COMMENT ID TO replied.txt AND OUTPUT LOG
                        dont_reply.append(comment.id)
                        localtime = time.asctime(time.localtime(time.time()))
                        logging.basicConfig(filename='Activity.log',level=logging.INFO)
                        with open("dont_reply.txt", "w") as f:
                            for comment.id in dont_reply:
                                f.write(comment.id + "\n")
                        logging.info('Hit by rock! ID {}'.format(comment.id))

                        # REPLY TO COMMENT
                        comment.reply(reply3)

                        # SEND CONFIRMATION
                        print('Replied to ID {}'.format(comment.id))
                        print(num_replies)

                    elif 'stone' in comment.body:
                        # PRINT FOUND CONFIRMATION
                        print("Hit by rock (ID: {})".format(comment.id))

                        # ADD COMMENT ID TO replied.txt AND OUTPUT LOG
                        dont_reply.append(comment.id)
                        localtime = time.asctime(time.localtime(time.time()))
                        logging.basicConfig(filename='Activity.log',level=logging.INFO)
                        with open("dont_reply.txt", "w") as f:
                            for comment.id in dont_reply:
                                f.write(comment.id + "\n")
                        logging.info('Hit by rock! ID {}'.format(comment.id))

                        # REPLY TO COMMENT
                        comment.reply(reply3)

                        # SEND CONFIRMATION
                        print('Replied to ID {}'.format(comment.id))
                        print(num_replies)

                # IF NO COMMENTS FOUND
                else:
                    # DEFINE COMMENT SEARCH
                    comments = reddit.user.me().comments.new(limit=10)

                    # OUTPUT NUMBER OF TOTAL REPLIES TO CONSOLE
                    num_replies = sum(1 for line in open('replied.txt'))

                    # PRINT CONFIRMATION TO CONSOLE
                    print('Nothing found')
                    print('Replied so far: {}'.format(num_replies))

                    # DELETE COMMENTS WITH A NEGATIVE SCORE
                    for comment in comments:
                        if comment.score < -1:
                            comment.delete()
                            print('Deleted negative comment')
                            logging.info(localtime + ": Deleted negative comment")

            # SLEEP FOR 10s BEFORE NEXT SEARCH
            print('Waiting 10s...')
            time.sleep(10)

        # KEEP THE CODE LOOPING
        if __name__ == '__main__':
            main()

    # HANDLE EXCEPTIONS/ERRORS
    except KeyboardInterrupt:
        raise

    except:
        # DEFINITIONS AND CONFIG
        localtime = time.asctime(time.localtime(time.time()))
        logging.basicConfig(filename='Activity.log',level=logging.INFO)

        # PRINT ERROR MESSAGE AND OUTPUT TO LOG
        print('An error has occured! Restarting...')
        logging.warning(localtime + ": An error has occured! Restarting...")
        pass
        # pass

    # THIS SHOULDN'T HAPPEN
    else:
        break
