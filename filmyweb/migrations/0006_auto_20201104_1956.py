# Generated by Django 3.1.2 on 2020-11-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0005_auto_20201104_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Sci-fi'), (4, 'Drama'), (2, 'Komedia'), (1, 'Horror'), (0, 'Inne')], default=0),
        ),
        migrations.CreateModel(
            name='Aktor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=32)),
                ('filmy', models.ManyToManyField(to='filmyweb.Film')),
            ],
        ),
    ]
