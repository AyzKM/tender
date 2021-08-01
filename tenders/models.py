from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.

class ProcuringOrganization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Procuring Organization"
        verbose_name_plural = "Procuring Organizations"

class Participants(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"

    def __str__(self):
        return self.name

class RedFlags(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Red Flag"
        verbose_name_plural = "Red Flags"

class Tender(models.Model):
    tender_id = models.IntegerField()
    name = models.CharField(max_length=255)
    date_published = models.DateField()
    price = models.FloatField()
    procuring_organ = models.ForeignKey(
        to=ProcuringOrganization, 
        on_delete=CASCADE,
        related_name='tender')
    winner = models.OneToOneField(
        to=Participants, 
        on_delete=CASCADE,
        null=True, blank=True,
        )
    red_flag = models.ManyToManyField(to=RedFlags)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tender"
        verbose_name_plural = "Tenders"



    


