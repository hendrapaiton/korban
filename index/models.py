from django.db import models

class Pengunjung(models.Model):
	tanggal = models.DateTimeField(auto_now=True)
	address = models.CharField(max_length=64)
