from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class TimesTamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True        

class Candidate(TimesTamp):
    TYPE_DOCUMENT_CHOICES = (
        ("CNPJ", "CNPJ"),
        ("CPF", "CPF"),
        ("RG", "RG")
    )
    JOB_CHOICES = (
        ("PO", "Programador"),
        ("BD", "DBA"),
        ("GP", "Gerente"),
    )
    name = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    type_document = models.CharField(max_length=50, choices=TYPE_DOCUMENT_CHOICES)
    document = models.CharField(max_length=50, unique=True)
    job = models.CharField(max_length=50, choices=JOB_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'candidate'
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'


class Contact(TimesTamp):
    TYPE_CHOICES = (
        ("comercial", "Comercial"),
        ("residencial", "Residencial"),
    )
    type = models.CharField(max_length=12, choices=TYPE_CHOICES)
    number = models.CharField(max_length=12)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'