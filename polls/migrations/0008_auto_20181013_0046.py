# Generated by Django 2.1.1 on 2018-10-12 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20181012_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='polls_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.PollsType'),
        ),
    ]
