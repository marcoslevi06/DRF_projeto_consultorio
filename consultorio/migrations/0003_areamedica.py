# Generated by Django 4.1.7 on 2023-03-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0002_alter_paciente_cpf_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_area', models.CharField(max_length=25)),
            ],
        ),
    ]
