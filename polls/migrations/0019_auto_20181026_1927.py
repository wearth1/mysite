# Generated by Django 2.1.2 on 2018-10-26 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20181023_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='polls_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.PollsType'),
        ),
    ]
