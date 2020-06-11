from pydub import AudioSegment

#wav_audio = AudioSegment.from_file("example.wav", format="wav")
#wav_audio.export("example.mp3", format="mp3")
#AudioSegment.from_file("example.wav").export("example.mp3", format="mp3")


song_wav = AudioSegment.from_wav("example.wav")
song_wav.export("example.mp3", format="mp3")
