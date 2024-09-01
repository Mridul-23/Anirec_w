from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GeneralData(models.Model):
    unique_id = models.IntegerField(unique=True, default=-1)
    name = models.CharField(max_length=255)
    name_english = models.CharField(max_length=255)
    score = models.FloatField()
    ranked = models.IntegerField()
    popularity = models.IntegerField()
    members = models.IntegerField()
    synopsis = models.TextField()
    total_episodes = models.FloatField()
    premiered = models.CharField(max_length=100)
    duration_per_ep = models.CharField(max_length=100)
    scored_by = models.FloatField()
    favorites = models.IntegerField()
    aired = models.CharField(max_length=100)
    imagelink = models.CharField(max_length=255, default='un-available', null=True)

    studio = models.ForeignKey(to='Studio', null=True, on_delete=models.CASCADE )
    demographic = models.ForeignKey(to='Demographic', null=True, on_delete=models.CASCADE)
    genre = models.ManyToManyField(to='Genre', related_name='animes')
    rating = models.ForeignKey(to='Rating', null=True, on_delete=models.CASCADE)
    source = models.ForeignKey(to='Source', null=True, on_delete=models.CASCADE)
    typeof = models.ForeignKey(to='Typeof', null=True, on_delete=models.CASCADE)


    watching = models.IntegerField()
    completed = models.IntegerField()
    on_hold = models.IntegerField()
    dropped = models.IntegerField()
    plan_to_watch = models.IntegerField()
    total = models.IntegerField()
    scored_10_by = models.FloatField()
    scored_9_by = models.FloatField()
    scored_8_by = models.FloatField()
    scored_7_by = models.FloatField()
    scored_6_by = models.FloatField()
    scored_5_by = models.FloatField()
    scored_4_by = models.FloatField()
    scored_3_by = models.FloatField()
    scored_2_by = models.FloatField()
    scored_1_by = models.FloatField()

class Studio(models.Model):
    name = models.CharField(max_length=255, unique=True, default='Unknown Studio')

class Demographic(models.Model):
    name = models.CharField(max_length=255, unique=True, default='Unknown Demographic')

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True, default='Unknown Genre')

class Rating(models.Model):
    name = models.CharField(max_length=255, unique=True, default='Unknown Rating')

class Source(models.Model):
    name = models.CharField(max_length=255, unique=True, default='Unknown Source')

class TypeOf(models.Model):
    name = models.CharField(max_length=255, unique=True, default='Unknown Type')

class AdminChoices(models.Model):
    index = models.IntegerField()

class Saved_anime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(GeneralData, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'anime')
    
    def __str__(self):
        return f'{self.user.username} - {self.anime.name}'