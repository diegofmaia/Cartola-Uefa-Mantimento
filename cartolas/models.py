from django.db import models

class ListarCartolas(models.Manager):
	def search(self):
		return self.get_queryset()

class ListarRodadas(models.Manager):
	def search(self):
		return self.get_queryset()		


class Cartolas(models.Model):

	cartolaNome = models.CharField('cartolaNome', max_length=50)
	cartolaTime = models.CharField('cartolaTime', max_length=50)
	
	cartolaImagem = models.ImageField(
		upload_to='cartolas/images', verbose_name="Imagem",
		null=True, blank=True)

	objects = ListarCartolas()

	def __str__(self):
		return self.cartolaTime

	class Meta:
		verbose_name = "Cartola"
		verbose_name_plural = "Cartolas"
		ordering = ['id']


class Rodadas(models.Model):

	rodadaId   = models.AutoField('rodadaId', primary_key=True)
	rodadaNome = models.CharField('rodadaNome', max_length=50)
	rodadaRealizada = models.CharField('rodadaRealizada', max_length=1, null=True)

	objects = ListarRodadas()

	def __str__(self):
		return self.rodadaNome

	class Meta:
		verbose_name = "Rodada"
		verbose_name_plural = "Rodadas"
		ordering = ['rodadaId']


class Pontuacao(models.Model):

	rodadaId = models.ForeignKey(Rodadas, on_delete=models.CASCADE)
	cartolaId = models.ForeignKey(Cartolas, on_delete=models.CASCADE)
	pontuacao = models.DecimalField(max_digits=2, decimal_places=2, default="")

	