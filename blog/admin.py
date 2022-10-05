from django.contrib import admin
from .models import Author,Article,Person,Reaction,Comment


admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Person)
admin.site.register(Reaction)
admin.site.register(Comment )
