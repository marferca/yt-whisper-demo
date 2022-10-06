import os

import numpy as np
from pytube import YouTube
import streamlit as st
import whisper


SAMPLES = {
    "DALL·E 2 Explained by OpenAI": "https://www.youtube.com/watch?v=qTgPSKKjfVg",
    "Streamlit Shorts: How to make a select box by Streamlit": "https://www.youtube.com/watch?v=8-GavXeFlEA"
    }


def sample_to_url(option):
    return SAMPLES.get(option)


@st.experimental_singleton(show_spinner=False)
def load_whisper_model():
    model = whisper.load_model('tiny')
    return model


def _get_audio_from_youtube_url(url):
    yt = YouTube(url)
    if not os.path.exists('data'):
        os.makedirs('data')
    yt.streams.filter(only_audio=True).first().download(filename=os.path.join('data','audio.mp3'))
    #return yt


def _whisper_result_to_srt(result):
    text = []
    for i,s in enumerate(result['segments']):
        text.append(str(i+1))

        time_start = s['start']
        hours, minutes, seconds = int(time_start/3600), (time_start/60) % 60, (time_start) % 60
        timestamp_start = "%02d:%02d:%06.3f" % (hours, minutes, seconds)
        timestamp_start = timestamp_start.replace('.',',')     
        time_end = s['end']
        hours, minutes, seconds = int(time_end/3600), (time_end/60) % 60, (time_end) % 60
        timestamp_end = "%02d:%02d:%06.3f" % (hours, minutes, seconds)
        timestamp_end = timestamp_end.replace('.',',')        
        text.append(timestamp_start + " --> " + timestamp_end)

        text.append(s['text'].strip() + "\n")
            
    return "\n".join(text)


@st.cache(show_spinner=False, max_entries=1)
def transcribe_youtube_video(model, url):
    _get_audio_from_youtube_url(url)
    result = model.transcribe(os.path.join('data','audio.mp3'))
    result['srt'] = _whisper_result_to_srt(result)
    return result
