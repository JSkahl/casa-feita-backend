# Generated by Django 5.1.1 on 2024-09-30 22:11

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('data', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_titular', models.CharField(max_length=255)),
                ('sobrenome_titular', models.CharField(max_length=255)),
                ('numero', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999999999)])),
                ('validade', models.DateField()),
                ('cvv', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('tipo', models.CharField(choices=[('Débito', 'Debito'), ('Crédito', 'Credito')], max_length=10)),
            ],
            options={
                'verbose_name': 'Cartão',
                'verbose_name_plural': 'Cartões',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Cor',
                'verbose_name_plural': 'Cores',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=150)),
                ('complemento', models.CharField(max_length=150)),
                ('numero', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('cep', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999)])),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Carrinho'), (2, 'Concluida'), (3, 'Preparação'), (4, 'Saída'), (5, 'Entregue')], default=1)),
                ('metodo_pagamento', models.IntegerField(choices=[(1, 'Cartão de crédito'), (2, 'Cartão de débito'), (3, 'Pix'), (4, 'Boleto')])),
                ('data', models.DateField(auto_now_add=True)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='casafeita.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nacionalidade', models.CharField(max_length=50)),
                ('capa', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='uploader.image')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categorias', to='casafeita.categoria')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cores', to='casafeita.cor')),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casafeita.fabricante')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='casafeita.compra')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produtos', to='casafeita.produto')),
            ],
            options={
                'verbose_name': 'Item Compra',
                'verbose_name_plural': 'Itens da Compra',
            },
        ),
    ]
