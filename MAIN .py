p_dict = {
            "LOL": "una respuesta a algo gracioso"
            "CRINGE": "algo raro o embarazoso"
            "ROFL" - "una respuesta a una broma"
            "SHEESH" - "ligera desaprobación"
            "CREEPY" - "aterrador, siniestro"
            "AGGRO" - "ponerse agresivo/enojado"
        }
word = input("escribe algo EN MEYUSCULAS")
if wrd in p_dict.keys():
    print(p_dict[word])
else:
    print("ERRR")
