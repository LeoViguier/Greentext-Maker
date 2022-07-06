# Greentext Maker

A discord bot to make greentext.
Easily make your own greentexts with this tool.
This repo contains a Discord bot that is used to interact with greentext_maker.py, which is responsible for making the greentexts


# Installing

This project has only been tested on Linux.
You will need Python 3.0 or higher and pip3 for this project to work.

To install the basic dependencies, run:
```bash
git clone https://github.com/LeoViguier/Greentext-Maker.git
cd Greentext-Maker/
python3 -m pip install -r requirements.txt
```

You will also need [Chrome WebDriver](https://chromedriver.chromium.org/downloads) and Chromium. Both are necessary to take the screenshot of the greentext.

Using a [GeckoDriver](https://github.com/mozilla/geckodriver) for Mozilla Firefox might work too with some adjustments to the code but I haven't tryed it.


# Run
This section describes how to run the bot.
## Without the Discord bot
If you want to run this without the bot, you can put your text in the `text.txt` file, which is following the same syntax as the discord command, and run:
```bash
cd Greentext-Maker/
python3 greentext_maker.py
```

## With the Discord bot
To run the discord bot, you will have to create one if it is not already done. If you don't know how to, you can read the [official Discord documentation](https://discord.com/developers/docs/tutorials/hosting-on-cloudflare-workers#creating-an-app-on-discord). After generating your token, put it into the file `token.txt`.

Then, run:
```bash
cd Greentext-Maker/
python3 green_bot.py
```


# Usage

Here is a simple way of making a greentext:
![example](https://i.imgur.com/5pTDlVk.png)

The syntax is the following:

`!greentext title of the greentext;url for the picture;text for the greentext`

You can leave the title blank if you don't want to add one but there should always be a link to a picture as no picture is not supported yet.
As for the greentext himself, the syntax is quite simple:

A line starting with `>` will make it appear green.
All the other lines will appear normal.
If you want to go back to the line on Discord, just do Shift + Enter.


# Improvements

There is a lot to improve, starting with the way the screenshots are taken. Each time someone wants to take a screenshot, we have to start a new web browser which is very slow. The goal would be to have some kind of "server" that would take screenshots and send them to the main program, that way, we wouldn't have to create a new instance of Chromium each time.

Another way of improvement that has to be done is regarding the use of the discord bot.
Currently, it is designed for one user to use it, but if several people use it at the same time, it could create collisions when accessing the different files, like the `index.html` file.
