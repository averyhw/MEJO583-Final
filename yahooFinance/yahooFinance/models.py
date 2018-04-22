from django.db import models

class Company(models.Model):
    name = models.CharField(unique=True, max_length=50)
    openning = models.DecimalField(unique=False, max_digits=5, decimal_places=2)
    previous_close = models.DecimalField(unique=False, max_digits=5, decimal_places=2)
    volume = models.IntegerField(unique=False, default=0.00)
    pe_ratio = models.DecimalField(unique=False, max_digits=6, decimal_places=2, default=0.00)
    eps = models.DecimalField(unique=False, max_digits=6, decimal_places=4, default=0.00)
    one_year = models.DecimalField(unique=False, max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
            return U'%s' %(self.name)
    def save(self):
        self.name = self.name.upper()
