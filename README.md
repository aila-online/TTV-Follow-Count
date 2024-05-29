# TTV-Follow-Count
A small script that uses Python and twitchAPI to write your Twitch Channel's current follower count to a text file. Primaryly made as a simple follower counter in OBS.

## Pre-Requisites
- **Python** installed and running on your system.
- [**twitchAPI**](https://pypi.org/project/twitchAPI/) for Python; install online or with pip:
>```pip install twitchAPI```
- Go to [Twitch's Dev Console](https://dev.twitch.tv/console/apps) and register an application.
> Make sure to use ```https://localhost:17563``` as your redirect link. Press **Create Secret** and **Save** as well. Jot down your client ID and secret for the initial setup (see below). THESE ARE PRIVATE, DO NOT SHARE THESE.

## Initial Setup

After aquiring **tracker.py** and moving it to your desired directory, edit the file with any text/code editor of choice. This is where you'll need your Client ID and secret; there a few things to change:
- Replace ```YOUR CLIENT ID``` and ```YOUR CLIENT SECRET``` with the corresponding values given when registering the app with Twitch's Dev Console.

## Usage

Simply run the script in your desired way and presto! The follower count of that channel should be written in the text file **count.txt**, in the same directory as the tracker, every 30 seconds!

## Contributing

If you'd like to update this script, please do feel free. However, make sure to not expose any API keys/secrets, especially in this public repo.

## License

This project uses unlicense, essentially a public works with no warranty or liability attatched to it. Only use this script at your own discretion.
