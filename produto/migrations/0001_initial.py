# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompraProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd', models.IntegerField()),
                ('preco', models.FloatField()),
                ('processado', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('qtd', models.IntegerField(default=0)),
                ('precoMedio', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='compraproduto',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto'),
        ),
    ]