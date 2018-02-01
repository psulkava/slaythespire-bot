# slaythespire-bot
Modified version of [d-schmidt's hearthscan-bot](https://github.com/d-schmidt/hearthscan-bot) credit goes to him for the majority of the code
To see the bot in action send a PM containing `[[Strike]]` to [/u/slaythespire-bot](https://www.reddit.com/message/compose/?to=slaythespire-bot)

## Requirements
- tested on Python 3.4+
- Python libraries: `requests`, `praw`, `lxml`
- [Reddit API](https://www.reddit.com/prefs/apps/) id, secret and refresh token

## Tests
Not currently set up.

## Running the bot
Use `start.sh` to run in background.  
If you want to start it without, no parameters are required (`python3 slaythespire-bot.py`).  
The script pipes startup errors to `std.txt` and `err.txt`. The bot logs to `bot.log` once it is running.

You will require json-data for the bot to work. Start the `scrape.py` and wait or create the data file yourself.
Create a `items.json` and add a card or relic in the format:
``` JSON
{
  "Accuracy": {
      "Name": "Accuracy",
      "Energy": "1",
      "Type": "Silent Power",
      "Rarity": "Uncommon",
      "Description": "Shivs deal 3 (5) additional damage."
  },
  ...
}
```
Cards are not required in the files, but the file has to exist and contain valid json: `{}`.  
While the bot is running, you can teach it new cards or relics without stopping. Create or edit `tempinfo.json` following the same format.

Delete the `lockfile.lock` or kill it to stop the bot gracefully.

## Learning from this bot
This project is based off of [d-schmidt's hearthscan-bot](https://github.com/d-schmidt/hearthscan-bot)
so I reccomend going there if you want to make a bot similar to this
There are nice people out there answering questions ([/r/learnpython](https://www.reddit.com/r/learnpython), [/r/redditdev](https://www.reddit.com/r/redditdev)) and the [PRAW documentation](http://praw.readthedocs.io/en/latest/getting_started/quick_start.html) is decent.

## License
All code contained here is licensed by [MIT](https://github.com/psulkava/slaythespire-bot/blob/master/LICENSE).
