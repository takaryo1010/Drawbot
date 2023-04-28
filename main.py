import time
import speech_recognition
import pyaudio
from internal import inputAudio


def main():
    reqAudio = inputAudio.RequestAudio()  # インスタンスを生成

    inputAudio.InputAudio(reqAudio)

    # req.List_inputsの要素をDeeplで翻訳
    # Deeplで翻訳されたリストをChatGPTに投げる


if __name__ == '__main__':
    main()
