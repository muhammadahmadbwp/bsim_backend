# Generated by Django 4.0.2 on 2022-03-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0003_alter_influencerschildren_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencerschildren',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
