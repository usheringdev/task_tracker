# Generated by Django 4.0.4 on 2022-04-28 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_name_alter_team_name'),
        ('users', '0002_taskuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='team',
        ),
        migrations.CreateModel(
            name='TeamUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_users', to='tasks.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('team', 'user')},
            },
        ),
    ]
