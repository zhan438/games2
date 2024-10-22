from django.contrib import admin
from .models import Game, Feature

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    # Adding the image field to the admin form
    fields = ('title', 'description', 'trailer_url', 'additional_info', 'development_history', 'community_involvement', 'image')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'game')
    search_fields = ('title',)