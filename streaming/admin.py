from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.html import format_html
from .models import Movie, Series, Season, Episode, Genre
from django import forms


# Register your models here.
class MovieAdminForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        }
def make_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)
make_featured.short_description = "Mark selected as featured"

class FeaturedFilter(SimpleListFilter):
    title = 'featured'  # A label for your filter
    parameter_name = 'featured'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Featured'),
            ('No', 'Not Featured'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Yes':
            return queryset.filter(is_featured=True)
        if self.value() == 'No':
            return queryset.filter(is_featured=False)

class SeasonInline(admin.TabularInline):
    model = Season
    extra = 1  # Number of empty forms to display

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    form = MovieAdminForm
    actions = [make_featured]
    list_filter = (FeaturedFilter, 'is_featured', 'release_date', 'genres')
    list_display = ('title', 'release_date', 'is_featured', 'thumbnail', 'trailer_iframe')
    search_fields = ('title', 'description', 'trailer_url')
    filter_horizontal = ('genres',)  # This provides a user-friendly interface for managing many-to-many relationships
    ordering = ('-release_date',)  # Orders by release_date in descending order

    def thumbnail(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="100" height="50" />', obj.image_url)
        return "-"
    thumbnail.short_description = 'Thumbnail'

    def trailer_iframe(self, obj):
        if obj.trailer_url:
            return format_html('<iframe src="{}" width="100" height="50" frameborder="0" allowfullscreen></iframe>',
                               obj.trailer_url)
        return 'No Trailer'

    trailer_iframe.short_description = 'Trailer'


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title','number_of_seasons', 'release_date', 'is_featured', 'trailer_url', 'thumbnail')
    list_filter = ('is_featured', 'release_date', 'genres')
    search_fields = ('title', 'description', 'trailer_url')
    ordering = ('-release_date',)  # Orders by release_date in descending order

    def thumbnail(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image_url)
        return "-"
    thumbnail.short_description = 'Thumbnail'

    def number_of_seasons(self, obj):
        return obj.seasons.count()
    number_of_seasons.short_description = 'Number of Seasons'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('series', 'season_number', 'title', 'release_date')
    list_filter = ('series', 'release_date')
    search_fields = ('title', 'description')
    ordering = ('series', 'season_number')


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('season', 'episode_number', 'title', 'release_date', 'duration')
    list_filter = ('season__series', 'season', 'release_date')
    search_fields = ('title', 'description')
    ordering = ('season', 'episode_number')
