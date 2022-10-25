from django.db import models
from django.urls import reverse
import os


class Author(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author', kwargs={'author_id': self.pk})

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Series(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=40, verbose_name='url', unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Серия книг'
        verbose_name_plural = 'Серии книг'


class Tag(models.Model):
    name = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=40, verbose_name='url', unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class File(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    name = models.CharField(max_length=100)

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def file_size(self):
        return round(self.file.size/1024, 2)

    def __str__(self):
        return self.file.name.split('/')[-1]

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Genre(models.Model):
    name = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=40, verbose_name='url', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название книги')
    original_name = models.CharField(max_length=100, verbose_name='Оригинальное название')
    year = models.IntegerField(blank=True, verbose_name='Год')
    description = models.TextField(blank=True, verbose_name='Аннотация')
    rating = models.FloatField(blank=True, verbose_name='Рейтинг')
    cover = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Обложка')
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', blank=True)
    files = models.ManyToManyField(File, verbose_name='Файлы', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    series = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name='Серия книг', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    author_email = models.EmailField()
    author_name = models.CharField(max_length=50, verbose_name='Автор')
    comment_text = models.TextField(verbose_name='Текст комментария', max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} {self.book.title}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
