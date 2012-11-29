from django.db import models
import os
class Fichero(models.Model):
    nombre = models.CharField(max_length=140)
    file = models.FileField(upload_to='ficheros')

    def __unicode__(self):
        #return os.path.join(os.path.dirname(__file__),'/media/')
        return self.file.path

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(Fichero, self).delete(*args, **kwargs)