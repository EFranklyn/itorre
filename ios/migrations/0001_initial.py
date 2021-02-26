# Generated by Django 3.1.7 on 2021-02-24 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Os',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('servico', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=50)),
                ('detalhes', models.CharField(max_length=255)),
                ('prioridade', models.CharField(choices=[('1', 'Baixa'), ('2', 'Média'), ('3', 'Alta')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
