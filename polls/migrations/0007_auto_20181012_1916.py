# Generated by Django 2.1.1 on 2018-10-12 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20181012_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readnum',
            name='polls',
        ),
        migrations.AlterField(
            model_name='polls',
            name='polls_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.PollsType'),
        ),
        migrations.DeleteModel(
            name='ReadNum',
        ),
    ]