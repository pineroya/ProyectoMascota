# Generated by Django 4.0.3 on 2022-05-09 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotasapp', '0002_rename_raza_conejos_color_rename_raza_gatos_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('creted', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.AddField(
            model_name='perros',
            name='categorias',
            field=models.ManyToManyField(to='mascotasapp.categoria'),
        ),
    ]