from django.contrib import admin

from ..highlights.models import Search, Highlight

admin.site.register(Search)
admin.site.register(Highlight)