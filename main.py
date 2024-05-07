import praw
import random
import os

# Initialize Reddit bot using direct credentials
reddit = praw.Reddit(
    client_id='your_client_id',
    client_secret='your_client_secret',
    user_agent='your_user_agent',
    username='your_reddit_username',
    password='your_reddit_password'
)

# Get subreddit instance
subreddit = reddit.subreddit("SUBREDDIT_TO_REPLY")

# Create a file to store replied posts if it doesn't exist
if not os.path.isfile("posts_replied_to.txt"):
    with open("posts_replied_to.txt", 'w'):
        pass

# Define possible replies
possible_replies = [
    "YOUR_REPLY_1",
    "YOUR_REPLY_2",
    "YOUR_REPLY_3",
    # Add more replies as needed
]

# Define the function to comment on submissions
def docomment():
    print("Bot started - Commenting on new posts")
    
    # Iterate through the newest submissions
    for submission in subreddit.new(limit=None):
        # Load IDs of already replied posts
        with open("posts_replied_to.txt", 'r') as file:
            done = file.read().split(',')
        
        # Check if the submission has not been replied to
        if submission.id not in done:
            # Shuffle the list of possible replies
            random.shuffle(possible_replies)
            # Choose a random reply from the shuffled list
            random_reply = possible_replies[0]
            print("Replying to post:", submission.title)
            # Reply to the submission
            submission.reply(random_reply)
            # Append the ID of the replied post to the file
            with open("posts_replied_to.txt", "a") as posts_replied_to:
                posts_replied_to.write(submission.id + ",")
                # Update the list of replied posts
                done.append(submission.id)
        else:
            print("Skipping the submission (already replied to).")

# Start the bot
while True:
    try:
        docomment()
    except KeyboardInterrupt:
        print("\nOk stopping bot")
        exit(0)
    except Exception as error:
        print("Unknown error:", error)
        continue
