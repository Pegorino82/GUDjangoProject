from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)

    def __str__(self):
        return '{} {}'.format(self.name, self.lastname)

    def __repr__(self):
        return '{} {}'.format(self.name, self.lastname)


class MainPageContent(models.Model):
    chapter = models.CharField(max_length=150)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField()
    author = models.ForeignKey(
        'main.Author',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} {} (author {})'.format(self.chapter[:10],
                                          self.content[:10],
                                          self.author)
