import requests
import xmltodict

r = requests.get("http://meteo2.ftj.agh.edu.pl/meteo/meteo.xml")

print(r.text)

dic = xmltodict.parse(r.text)

print(dic)

'''pip install xmltodict - wczytuje plik xml i zamienia ten plik na strukture slownikowa'''
