import os
import cv2
import mediapipe as mp
import pyttsx3
import speech_recognition as sr
import webbrowser
from datetime import datetime

#setando variaveis
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
quadrado = mp.solutions.drawing_utils
recon = sr.Recognizer()
resposta = ""
parar = False
hora = (str(datetime.today().hour) + ":" + str(datetime.today().minute)) #transformando a hora em string

print("mostre o rosto por favor")
while webcam.isOpened(): #abre a web cam
    verificador, frame = webcam.read()
    if not verificador:
        break

    lista_rostos = reconhecedor_rostos.process(frame) #Seta a lista para cada rosto em cada frame do video

    if lista_rostos.detections: #cria uma condição se o codigo encontrar um rosto
        for rosto in lista_rostos.detections: #Para cada rosto na lista
            quadrado.draw_detection(frame, rosto)#Ele desenha um quadrado
        cv2.imshow("Rostos na webcam", frame) #Abre uma janela para o usuario ver
        if cv2.waitKey(1000) == 27:
            break

        robo = pyttsx3.init() #inicia a voz do robo e setando os parametros de resposta do robo
        robo.say("Olá seja bem vindo, o que deseja?")
        robo.setProperty("voice", b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 1)
        robo.runAndWait() #roda os comandos setados

        with sr.Microphone(1) as source: #Identifica o microfone

            while not parar:

                audio = recon.listen(source, timeout=None) #Abre o microfone do usuario para a resposta, define a configuração de linguagem e devolve o texto falado no print
                res = recon.recognize_google(audio, language='pt-BR')
                resposta = res.lower()  # Setando todas as respostas para minusculo
                print("Texto reconhecido: ", resposta.lower())

                if "youtube" in resposta: #define a condição para entrar no nó
                    robo.say("Abrindo youtube")
                    robo.runAndWait()
                    webbrowser.open('https://www.youtube.com/', autoraise=True) #Inicia um site

                if "notícias" in resposta:
                    robo.say("Abrindo Cnn")
                    robo.runAndWait()
                    webbrowser.open('https://www.cnnbrasil.com.br/', autoraise=True)

                if "ativar protocolo sexta-feira" in resposta:
                    robo.say("Ativando protocolo")
                    robo.runAndWait()
                    os.startfile('C:\Riot Games\Riot Client/RiotClientServices.exe') #inicia um .exe considerando o caminho entregue
                    webbrowser.open('https://music.youtube.com/watch?v=n2qTCfDOysM&list=RDAMVMPwnHHAIi0XQ', autoraise=True)

                if "que horas são" in resposta:
                    robo.say(hora)
                    print(hora)
                    robo.runAndWait()

                if "assuntos do momento" in resposta:
                    robo.say("Mostrando as trendings")
                    robo.runAndWait()   
                    webbrowser.open('https://twitter.com/explore/tabs/trending', autoraise=True)

                elif "saindo" in resposta:
                    robo.say("OK! Até mais tarde senhor!")
                    robo.runAndWait()
                    break

        webcam.release() #desliga a webcam
        cv2.destroyAllWindows() #fecha as janelas








