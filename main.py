import time
import speech_recognition
import pyaudio
from internal import inputAudio as iA





def main(): 
    reqAudio=iA.RequestAudio() # インスタンスを生成
    # Audio インスタンス取得
    iA.InputAudio(reqAudio)
    # req.List_inputsの要素をDeeplで翻訳
    # Deeplで翻訳されたリストをChatGPTに投げる

    
if __name__ == '__main__':
    main()