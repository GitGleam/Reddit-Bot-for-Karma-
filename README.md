# PRAW Reddit Bot for Karma Accumulation with Direct Credentials and Shuffled Replies

This Python script serves as a Reddit bot designed to accumulate karma by engaging with Reddit communities. Built using the PRAW (Python Reddit API Wrapper) library, the bot integrates Reddit API credentials directly into the script for seamless authentication. In addition to its primary function of karma accumulation, the bot also features shuffled replies to provide diverse and engaging interactions.
<br/><br/>
## Key Features:

**Karma Accumulation:** The bot actively engages with Reddit communities by commenting on new submissions, thereby accruing karma for the associated Reddit account. By strategically participating in discussions and providing valuable contributions, the bot aims to enhance the user's Reddit karma score over time.<br/><br/>
**Direct Credentials Integration:** Unlike conventional bot setups that rely on external configuration files, this bot allows users to input their Reddit API credentials directly into the script. This approach simplifies deployment and ensures secure authentication with the Reddit API.<br/><br/>
**Shuffled Replies:** To maintain engagement and avoid repetitive interactions, the bot shuffles the list of possible replies before selecting one. This randomized approach ensures that the bot's responses remain varied and unpredictable, contributing to a more natural and dynamic interaction experience.<br/><br/>
**Automatic Post Tracking:** The bot automatically tracks the posts it has replied to, preventing duplicate interactions with the same submissions. By maintaining a record of replied posts, the bot ensures respectful engagement within Reddit communities and minimizes unnecessary repetition.<br/><br/>
**Customizable Responses:** Users can easily customize the list of possible replies within the script to align with subreddit contexts or engagement strategies. By adding, removing, or modifying responses, users can tailor the bot's behavior to suit specific community dynamics and preferences.

## Popular Subreddits for Karma Exchange:
r/FreeKarma4U
r/KarmaFarming4Pros
r/KarmaStore
r/KarmaWhores
r/UpvoteExchange
r/KarmaCourt
r/FreeKarmaEverywhere

## Usage:

**Requirements:** Ensure you have Python installed on your system. Install the necessary Python package by running:
```pip install praw```

**Configuration:** Replace placeholder values for Reddit ```API credentials (client_id, client_secret, user_agent, username, password)``` with actual credentials obtained from Reddit's developer portal.

**Customization:** Modify the possible_replies ```(YOUR_REPLY_1, YOUR_REPLY_2, YOUR_REPLY_3)``` list within the script to include desired responses, you can add how many you want. Add insightful comments, witty remarks, or relevant contributions to enhance engagement and karma accumulation.

**Subreddit Selection:** Specify the subreddit(s) to target for engagement by setting the ```SUBREDDIT_TO_REPLY``` variable in the script. Choose subreddits aligned with the user's interests or areas of expertise for optimal participation.

**Execution:** Run the Python script (main.py) to start the bot. It will continuously monitor specified subreddits for new submissions and comment with shuffled replies, contributing to karma accumulation.
```python main.py```

## Contributions and Feedback:
Contributions, suggestions, and feedback are welcome! If you encounter any issues, have ideas for improvements, or want to contribute to the project, feel free to submit pull requests or open issues on GitHub.
