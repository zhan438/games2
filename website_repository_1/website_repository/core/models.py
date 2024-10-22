from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    trailer_url = models.URLField()
    additional_info = models.TextField(blank=True, null=True)
    development_history = models.TextField(blank=True, null=True)
    community_involvement = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='game_images/')  # Add an image field for the game cover or main image

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    game = models.ForeignKey(Game, related_name='features', on_delete=models.CASCADE)

    def __str__(self):
        return self.title