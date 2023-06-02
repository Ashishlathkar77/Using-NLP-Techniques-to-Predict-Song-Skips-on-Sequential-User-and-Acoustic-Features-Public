# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:54:29 2023

@author: ashish lathkar
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open('C:/Users/admin/Desktop/Spotify-Skip-Prediction/model_dtc.pkl', 'rb')
classifier = pickle.load(pickle_in)

def Welcome():
    return "Welcome All!"

def Spotify_Skip_Predict(hist_user_behavior_reason_end_backbtn, hist_user_behavior_reason_end_fwdbtn, short_pause_before_play, no_pause_before_play, hist_user_behavior_reason_start_fwdbtn, hist_user_behavior_reason_end_clickrow, hist_user_behavior_reason_start_trackerror, bounciness, hist_user_behavior_reason_start_backbtn, hist_user_behavior_reason_end_remote, hist_user_behavior_is_shuffle, context_type_user_collection, hist_user_behavior_reason_start_clickrow, hist_user_behavior_reason_end_endplay, session_length, acoustic_vector_0, us_popularity_estimate, acoustic_vector_3, loudness, acousticness):
    
    prediction = classifier.predict([[hist_user_behavior_reason_end_backbtn, hist_user_behavior_reason_end_fwdbtn, short_pause_before_play, no_pause_before_play, hist_user_behavior_reason_start_fwdbtn, hist_user_behavior_reason_end_clickrow, hist_user_behavior_reason_start_trackerror, bounciness, hist_user_behavior_reason_start_backbtn, hist_user_behavior_reason_end_remote, hist_user_behavior_is_shuffle, context_type_user_collection, hist_user_behavior_reason_start_clickrow, hist_user_behavior_reason_end_endplay, session_length, acoustic_vector_0, us_popularity_estimate, acoustic_vector_3, loudness, acousticness]])
    print(prediction)
    return prediction

def main():
    st.title('Spotify-Skip-Prediction')
    st.image("""https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png""")
    st.header('Enter the Characteristics of the Song:')
    html_temp = """
    <div style="background-color-tomato;padding:10px">
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    hist_user_behavior_reason_end_backbtn = st.text_input("hist_user_behavior_reason_end_backbtn", "Type Here")
    hist_user_behavior_reason_end_fwdbtn = st.text_input("hist_user_behavior_reason_end_fwdbtn", "Type Here")
    short_pause_before_play = st.text_input("short_pause_before_play", "Type Here")
    no_pause_before_play = st.text_input("no_pause_before_play", "Type Here")
    hist_user_behavior_reason_start_fwdbtn = st.text_input("hist_user_behavior_reason_start_fwdbtn", "Type Here")
    hist_user_behavior_reason_end_clickrow = st.text_input("hist_user_behavior_reason_end_clickrow", "Type Here")
    hist_user_behavior_reason_start_trackerror = st.text_input("hist_user_behavior_reason_start_trackerror", "Type Here")
    bounciness = st.text_input("bounciness", "Type Here")
    hist_user_behavior_reason_start_backbtn = st.text_input("hist_user_behavior_reason_start_backbtn", "Type Here")
    hist_user_behavior_reason_end_remote = st.text_input("hist_user_behavior_reason_end_remote", "Type Here")
    hist_user_behavior_is_shuffle = st.text_input("hist_user_behavior_is_shuffle", "Type Here")
    context_type_user_collection = st.text_input("context_type_user_collection", "Type Here")
    hist_user_behavior_reason_start_clickrow = st.text_input("hist_user_behavior_reason_start_clickrow", "Type Here") 
    hist_user_behavior_reason_end_endplay = st.text_input("hist_user_behavior_reason_end_endplay", "Type Here")
    session_length = st.text_input("session_length", "Type Here")
    acoustic_vector_0 = st.text_input("acoustic_vector_0", "Type Here") 
    us_popularity_estimate = st.text_input("us_popularity_estimate", "Type Here") 
    acoustic_vector_3 = st.text_input("acoustic_vector_3", "Type Here")
    loudness = st.text_input("loudness", "Type Here")
    acousticness = st.text_input("acousticness", "Type Here")
    
    result = ""
    if st.button('Predict'):
        result = Spotify_Skip_Predict(hist_user_behavior_reason_end_backbtn, hist_user_behavior_reason_end_fwdbtn, short_pause_before_play, no_pause_before_play, hist_user_behavior_reason_start_fwdbtn, hist_user_behavior_reason_end_clickrow, hist_user_behavior_reason_start_trackerror, bounciness, hist_user_behavior_reason_start_backbtn, hist_user_behavior_reason_end_remote, hist_user_behavior_is_shuffle, context_type_user_collection, hist_user_behavior_reason_start_clickrow, hist_user_behavior_reason_end_endplay, session_length, acoustic_vector_0, us_popularity_estimate, acoustic_vector_3, loudness, acousticness)

    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text("Author: Ashish Lathkar")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()