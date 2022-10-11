# YouTube Video Transcription with Whisper 🤫
Demo developed by [Marcos Fernández Carbonell](https://www.linkedin.com/in/marferca/?locale=en_US)

## Summary
This Streamlit app showcases the power of [Whisper](https://github.com/openai/whisper), a general-purpose speech recognition model developed by [OpenAI](https://openai.com/).

Note: This demo utilizes the tiny version of the model.

[Streamlit App](https://marferca-yt-whisper-demo-streamlit-app-luptcq.streamlitapp.com/)
<img src="media/streamlit_app.gif" />

## Setup
I used Python 3.9.13 to develop the app.

To run the app on your local machine you will need to install some Python packages. 
```bash
pip install -r requirements.txt
```

You will also need to install the command-line tool [`ffmpeg`](https://ffmpeg.org/) on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

Lastly, run the following command to launch the Streamlit app.
```bash
streamlit run streamlit_app.py

## Useful links
* [Whisper paper](https://cdn.openai.com/papers/whisper.pdf)
* [OpenAI Whisper: Robust Speech Recognition via Large-Scale Weak Supervision | Paper and Code by Aleksa Gordić - The AI Epiphany [YouTube Video]](https://www.youtube.com/watch?v=AwJf8aQfChE)
* [Streamlit](https://streamlit.io/)