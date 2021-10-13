import speech_recognition as sr; import webbrowser;
reconocimiento = True

# Reconoce el audio del microfono
r = sr.Recognizer()  



while reconocimiento == True:
    with sr.Microphone() as source: 

        print("Se esta calibrando el microfono...")  

    # 5 segundos para calibrar el microfono
        rec = r.adjust_for_ambient_noise(source, duration=0)  
        print("¿Necesitas algo? - Escuchando...\n")

        audio = r.listen(source)  
    
    # Reconoce el texto usando sphinx

        palabra = r.recognize_sphinx(audio, language = "es-ES")
        print("\nSphinx piensa que dijiste '" + palabra + "'\n")  
        abrir = palabra.find("abrir")
        cerrar = palabra.find("cerrar")
        buscar = palabra.find("buscar")
        #print(abrir, cerrar)

        if abrir >= 0:
            print("Abriendo...")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0)

        if cerrar >= 0:
            print("Cerrando...")
            reconocimiento = False

        if buscar >= 0 and reconocimiento == True:
                with sr.Microphone() as source: 
                    print("¿Que queres buscar en youtube?")
                    rec2 = r.adjust_for_ambient_noise(source, duration=0)  
                    print("Escuchando...\n")
                    audio2 = r.listen(source)  
                    busqueda = r.recognize_sphinx(audio2, language = "es-ES")

                    if busqueda and reconocimiento == True:
                        print("¿Queres buscar " + busqueda + " en youtube?")
                        print("Si \nNo\n")

                        rec3 = r.adjust_for_ambient_noise(source, duration=0)  
                        print("Escuchando...\n")
                        audio3 = r.listen(source)  
                        resp = r.recognize_sphinx(audio3, language = "es-ES")
                        si = resp.find("si")
                        no = resp.find("no")

                        if si >= 0:
                            webbrowser.open("https://www.youtube.com/results?search_query="+ busqueda, new=1)
                        if no >= 0:
                            reconocimiento == False
                            print("Ok :(")




