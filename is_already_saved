import requests


def is_already_saved(url):
    r_url = requests.get(url)
    answer = r_url.json()

    #Remplacer url en check_all par check_one
    #Si idmsg=key renvoie true alors le mail est déja dans la liste

    url = url[0:-3] + "one?idmsg="

    l = []

    for key in (answer["keys"]):
        #print(key)
        r = requests.get(url + key)
        print (r.url)
        #print (r.content)
        #print (type(r.content))

        if (str(r.content) == "b'False'"):
            #print ("Le message n'a pas encore ete sauvegarde = doit etre enregistrer")
            l.append(False)
        elif (str(r.content) == "b'True'"):
            l.append(True)
            #print ("Le messsage a deja ete sauvegarde = pas besoin de l'enregistrer")
        else:
            print ("ERREUR")
    return l


url = "http://192.168.10.86:8000/check_all"
url_2 = "http://192.168.42.205:8000/check_all"
#is_already_saved(url)

print (is_already_saved(url_2))
