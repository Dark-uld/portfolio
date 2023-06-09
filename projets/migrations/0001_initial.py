# Generated by Django 4.1.7 on 2023-03-05 19:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('origines', models.CharField(choices=[('Formation', 'Formation'), ('Perso', 'Personnel'), ('Pro', 'Professionnel')], max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('alter_text', models.CharField(max_length=200)),
                ('url_image', models.CharField(blank=True, max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projets.projet')),
            ],
        ),
    ]
