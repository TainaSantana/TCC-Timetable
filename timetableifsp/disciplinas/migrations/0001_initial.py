# Generated by Django 3.1 on 2020-08-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sigla', models.CharField(max_length=15)),
                ('carga_hor', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('total_aulas', models.IntegerField()),
                ('aulas_semanais', models.IntegerField()),
                ('status', models.CharField(choices=[('1', 'Ativo'), ('2', 'Inativo')], max_length=1)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
