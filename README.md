# Discord Music Bot

A Discord bot that plays music in voice channels. This bot allows users to queue songs, skip tracks, and more.

## Features

- Play music from YouTube
- Queue system
- Skip tracks
- Pause and resume playback
- User-friendly commands

## Prerequisites

Before running the project, make sure you have the following installed:

1. **Python** (>= 3.6):  
    The project is written in Python. You can download it from [here](https://www.python.org/downloads/).

2. **ffmpeg**:  
    This project requires `ffmpeg` for processing audio and video formats. Follow the instructions below to install it on your system:

    - **Windows**:
      1. Download `ffmpeg` from the official website: [FFmpeg Downloads](https://ffmpeg.org/download.html).
      2. Extract the ZIP file and place it in a folder (e.g., `C:\ffmpeg`).
      3. Add the `bin` directory to your system's PATH:
          - Right-click on "This PC" and select "Properties".
          - Click on "Advanced system settings", then "Environment Variables".
          - Under "System variables", find and select `Path`, then click "Edit".
          - Add the path to the `bin` directory of `ffmpeg` (e.g., `C:\ffmpeg\bin`) and click "OK".

    - **macOS**:
      1. Install `Homebrew` if you haven't already: [Homebrew Website](https://brew.sh).
      2. Run the following command in the terminal:
          ```bash
          brew install ffmpeg
          ```

    - **Linux**:
      1. On Debian/Ubuntu-based systems, you can install `ffmpeg` using:
          ```bash
          sudo apt update
          sudo apt install ffmpeg
          ```
      2. For other distributions, use the appropriate package manager for your system.

3. **Discord Bot**:  
    You need to create a Discord bot and get the bot token. Follow the instructions in the [Discord Developer Portal](https://discord.com/developers/docs/intro) to create a bot and obtain the token.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/chrisvobi/discordMusicBot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd discordMusicBot
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `config.json` file in the root directory and add your Discord bot token:
    ```
    {
    "TOKEN": "your_discord_bot_token_here"
    }
    ```

## Usage

1. Start the bot:
    ```bash
    python main.py
    ```

## Commands

Here are some of the commands you can use with the Discord Music Bot:

- `!help`: Displays all available commands
- `!play` or `!p`: Plays a song from YouTube
- `!queue` or `!q`: Displays the current queue
- `!skip` or `!s`: Skips the current song
- `!clear`: Clears the queue
- `!leave` or `!disconnect`: Leaves the voice channel
- `!pause`: Pauses the current song
- `!resume`: Resumes the current song

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

It is illegal to download or use copyrighted content from YouTube without proper authorization. This bot is intended for educational and personal use only. Please ensure you comply with YouTube's terms of service and copyright laws.