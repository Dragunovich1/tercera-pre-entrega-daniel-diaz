# Generated by Django 4.1.1 on 2023-09-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLibrary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audiovisual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=10)),
                ('nombre_material', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=40)),
                ('nombre_libro', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameModel(
            old_name='Empresa',
            new_name='Cliente',
        ),
        migrations.DeleteModel(
            name='ConvenioColectivo',
        ),
        migrations.DeleteModel(
            name='Tarea',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='actividadPrincipal',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cuit',
            new_name='dni',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='cuil',
            new_name='dni',
        ),
        migrations.AddField(
            model_name='empleado',
            name='apellido',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
