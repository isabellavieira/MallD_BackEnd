# Generated by Django 5.0.6 on 2024-06-05 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastramento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem_produto',
            field=models.ImageField(upload_to='img_produtos'),
        ),
    ]
