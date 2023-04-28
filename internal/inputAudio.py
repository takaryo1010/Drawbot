import time
import speech_recognition
import pyaudio
import keyboard as key
from dataclasses import dataclass


@dataclass
class RequestAudio:
    def __init__(self):  # デフォルトの値
        self.SAMPLERATE = 44100
        self.sprec = speech_recognition.Recognizer()
        self.isInput = False
        self.List_inputs = []

    def callback(self, in_data, frame_count, time_info, status):

        if self.isInput != True:
            return (None, pyaudio.paContinue)
        try:
            audiodata = speech_recognition.AudioData(
                in_data, self.SAMPLERATE, 2)
            sprec_text = self.sprec.recognize_google(
                audiodata, language='ja-JP')
            self.List_inputs.append(sprec_text)

            # TODO GUIにするときは、リストを上から表示させたい
            print(self.List_inputs)

        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError as e:
            pass
        finally:
            return (None, pyaudio.paContinue)


def InputAudio(reqAudio):
    audio = pyaudio.PyAudio()     # Audio インスタンス取得
    stream = audio.open(format=pyaudio.paInt16,
                        rate=reqAudio.SAMPLERATE,
                        channels=1,
                        input_device_index=1,
                        input=True,
                        frames_per_buffer=reqAudio.SAMPLERATE*2,  # 2秒周期でコールバック
                        stream_callback=reqAudio.callback)
    stream.start_stream()

    while stream.is_active():
        if key.is_pressed("enter"):  # エンターキーが押されたらbreak
            break
        
        if key.is_pressed("space"):
            reqAudio.isInput = True
        else:
            reqAudio.isInput = False
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return reqAudio.List_inputs
