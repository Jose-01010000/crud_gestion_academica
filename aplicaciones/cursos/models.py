from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre + ' - ' + self.correo


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo + ' - ' + self.nombre


class Clase(models.Model):
    salon = models.CharField(max_length=3)
    horario = models.CharField(max_length=15)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return self.salon + ' - ' + self.horario
