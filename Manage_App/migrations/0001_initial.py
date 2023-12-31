# Generated by Django 4.2.3 on 2023-07-27 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
                ('option5', models.TextField()),
                ('answer', models.IntegerField()),
                ('explain', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idname', models.CharField(max_length=250, unique=True)),
                ('display_name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ReadQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manage_App.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manage_App.user')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manage_App.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manage_App.user')),
            ],
        ),
    ]
