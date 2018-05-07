from 	models import Cartolas 
import cartolafc

def cartolafc():
	api = cartolafc.Api()
	times = Cartolas.objects.all()

	for nomeTime in times:
		time = api.time(nome=nomeTime.cartolaTime)
		print(time.info.nome, '-', time.ultima_pontuacao)