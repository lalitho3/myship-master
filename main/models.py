from django.db import models

class Post(models.Model):
    titulo = models.CharField('Titulo',max_length=100, blank=False)
    mensaje = models.TextField('Mensaje', blank=False)
    foto = models.ImageField('Foto', upload_to='fotos/', blank=False)
    fecha = models.DateTimeField('Fecha', auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo
