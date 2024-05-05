# Generated by Django 5.0.4 on 2024-05-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='create',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending'), ('expired', 'Expired')], default='pending', max_length=20),
        ),
    ]