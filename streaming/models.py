from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    release_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    image_url = models.URLField(blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)  # Field to store the trailer URL
    iframe_url = models.URLField(blank=True, null=True)  # URL for embedding content

    def __str__(self):
        return self.title

class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='series')
    release_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    image_url = models.URLField(blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)  # Field to store the trailer URL

    def __str__(self):
        return self.title

class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='seasons')
    season_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    release_date = models.DateField()

    class Meta:
        unique_together = ('series', 'season_number')
        ordering = ['season_number']

    def __str__(self):
        return f"{self.series.title} - Season {self.season_number}"

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    episode_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.DurationField()  # Duration of the episode
    iframe_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['season', 'episode_number']

    def __str__(self):
        return f"{self.season.series.title} - S{self.season.season_number}E{self.episode_number}: {self.title}"

