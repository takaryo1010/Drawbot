import time
import speech_recognition
import pyaudio
import openai
import deepl
from internal import inputAudio
from internal import MyOpenAI


def main():
    with open("APIKEY.txt") as file:
        keys = file.read()
    keys = keys.split("\n")  # [openAIAPIKEY,openAIorg,DeepLAPIKEY]
    api_key = keys[0]
    organization = keys[1]
    translator = deepl.Translator(keys[2])
    # if len(keys) ==3:

    reqAudio = inputAudio.RequestAudio()  # インスタンスを生成
    inputs = inputAudio.InputAudio(reqAudio)#りんご:海:ばなな...

    # req.List_inputsの要素をDeeplで翻訳
    inputs_translated = translator.translate_text(inputs, target_lang="EN-US")#apple:sea:banana...
    
    # Deeplで翻訳されたリストをChatGPTに投げる
    response_AI = MyOpenAI.organizingAI(api_key,organization,inputs_translated.text)#文章を返す
    
    #ChatGPTから投げられた解答を使ってイラストにする
    MyOpenAI.drawAI(api_key, organization,response_AI)
    
if __name__ == '__main__':
    main()
