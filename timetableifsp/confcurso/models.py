from django.db import models

class Restricoes(models.Model):
    """
    CHOICE_PERIOD(
        ("1", "Matutino"),
        ("2", "Vespertino"),
        ("3", "Noturno"),
    )
    """

    #periodo = models.CharField(max_length="1", choices=CHOICE_PERIOD, blank=False)
    dias_semana = models.IntegerField(blank=False)

