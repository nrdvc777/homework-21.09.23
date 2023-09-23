from django.contrib import admin
from .models import NewsModel
# Register your models here.
from .models import NewsModel
from .forms import NewsForm

class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ("name", 'body', 'status')
    search_fields = ('name',)

admin.site.register(NewsModel, NewsAdmin)