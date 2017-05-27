from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField()

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return "Admin: " + self.user.username + ", " + self.user.email


class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField()

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return "Alumno: " + self.user.username + ", " + self.user.email


class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField()

    credito = models.BooleanField(default=False)
    dedito = models.BooleanField(default=False)
    efectivo = models.BooleanField(default=False)
    JUNAEB = models.BooleanField(default=False)

    activo = models.BooleanField()

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return self.user.username + ", " + self.user.email

    def pagos(self):
        cred = "credito, " if self.credito else ""
        deb = "debito, " if self.debito else ""
        efec = "efectivo, " if self.efectivo else ""
        jun = "JUNAEB, " if self.JUNAEB else ""
        return (cred + deb + efec + jun)[:-2]


class VendedorAmbulante(models.Model):
    vendedor = models.OneToOneField(Vendedor, on_delete=models.CASCADE)

    def __str__(self):
        return "Vendedor Ambulante: " + str(self.vendedor)

    def pagos(self):
        return self.vendedor.pagos()


class VendedorFijo(models.Model):
    vendedor = models.OneToOneField(Vendedor, on_delete=models.CASCADE)

    hora_apertura = models.IntegerField()
    hora_clausura = models.IntegerField()
    ubicacion = models.CharField(max_length=60)

    def __str__(self):
        return "Vendedor Ambulante: " + str(self.vendedor)

    def pagos(self):
        return self.vendedor.pagos()


class Producto(models.Model):
    vendedor = models.OneToOneField(Vendedor)

    foto = models.ImageField()

    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    precio = models.IntegerField()
    stock = models.IntegerField()

    categorias = (
        ()
    )
    categoria = models.CharField(choices=categorias, max_length=60, null=True)

    class Meta:
        ordering = ["vendedor", "nombre"]

    def __str__(self):
        return "Producto: " + self.nombre + " $" + self.precio + " q" + self.stock


class Favorito(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["alumno", "vendedor"]
