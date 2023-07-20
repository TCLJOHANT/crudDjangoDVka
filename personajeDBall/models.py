from django.db import models

# Create your models here.
class Personaje(models.Model):
    id = models.AutoField(primary_key=True ) 
    nombre = models.CharField(max_length=100, verbose_name='titulo')
    imagen =models.ImageField(upload_to='imagenes/',null=True, verbose_name='imagen')
    raza = models.CharField(max_length=100, verbose_name='raza' )
    descripcion =models.TextField(null=True, verbose_name='Descripcion')

    # class Meta: 
    #     db_table = 'personaje' # cambiará el nombre de la tabla en la base de datos a "personaje"
    def __str__(self):
        fila = "nombre: "+ self.nombre+ " raza: "+ self.raza+" Descripcion: "+self.descripcion
        return fila
    def delete(self , using=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
