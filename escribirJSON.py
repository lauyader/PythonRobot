import json

from pprint import pprint

data = json.dumps({
  "Tags":["tag 1","tag 2","tag 3"],
	"Posts":{
		"PostZ":"lalala",
		"PostY":"Leer un JSON",
		"PostX":"Escribir un JSON"
	},
	"Blog":"http://javainutil.blogspot.com",
	"Inicio":2012,
	"Temas":"Informatica"})

with open('prueba2.json', 'w') as outfile:
	json.dump(data, outfile) 
