# Generated by Django 4.1.3 on 2022-11-07 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('summary', models.TextField(verbose_name='summary')),
                ('isbn', models.CharField(blank=True, help_text='<a href="https://www.isbn-international.org/content/what-isbn" target="_blank">ISBN code</a> consisting of 13 symbols', max_length=13, null=True, verbose_name='ISBN')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.author')),
                ('genre', models.ManyToManyField(help_text='Choose genre(s) for this book', to='library.genre', verbose_name='genre(s)')),
            ],
        ),
    ]
