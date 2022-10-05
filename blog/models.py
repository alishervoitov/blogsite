from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name} {self.user.last_name}'
        elif self.user.first_name:
            return f'{self.user.first_name}'
        elif self.user.last_name:
            return f'{self.user.last_name}'
        else:
            return self.user.username


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='articles', null=True)
    name = models.CharField(max_length=255)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    @property
    def likes(self):
        return self.reactions.filter(react='like').count()

    @property
    def dislikes(self):
        return self.reactions.filter(react='dislike').count()

    def setreaction(self, react, person):
        current_react = self.reactions.filter(person=person)
        current_reaction = current_react[0] if current_react else None
        if not current_reaction:
            reaction = Reaction.objects.create(
                article=self,
                person=person,
                react=react
            )
        elif current_reaction.react == react:
            current_reaction.delete()
        else:
            current_reaction.react=react
            current_reaction.save()

    def setcomment(self,comment,person):
        new_comment = Comment.objects.create(
            article = self,
            person = person,
            comment = comment
        )
    @property
    def get_image(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name


class Reaction(models.Model):
    article = models.ForeignKey(Article, related_name='reactions', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='reacts', on_delete=models.CASCADE)
    react = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f'''{self.person}'s react to {self.article}'''


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f'''{self.person}'s comment to {self.article}:{self.comment}'''
