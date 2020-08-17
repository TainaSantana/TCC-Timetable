from django.db import models

class Disciplina(models.Model):

    STATUS_CHOICES = (
        ("1", "Ativo"),
        ("2", "Inativo"),
    )
    
    nome = models.CharField(max_length=150, blank=False, null=False)
    sigla = models.CharField(max_length=15, blank=False, null=False)
    carga_hor = models.IntegerField(blank=False, null=False)
    semestre = models.IntegerField(blank=False, null=False)
    total_aulas = models.IntegerField(blank=False, null=False)
    aulas_semanais = models.IntegerField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
