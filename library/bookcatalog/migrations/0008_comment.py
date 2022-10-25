# Generated by Django 4.1.2 on 2022-10-21 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookcatalog', '0007_alter_file_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Автор')),
                ('comment_text', models.TextField(max_length=1000, verbose_name='Текст комментария')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookcatalog.book', verbose_name='Книга')),
            ],
        ),
    ]