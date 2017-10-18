from django.contrib import admin
from .models import Important, Solutions, Products, Example, News, Aboutus, UserProfile, SolutionCate, ProductCate, NewsCate

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Important)
admin.site.register(Solutions)
admin.site.register(Products)
admin.site.register(Example)
admin.site.register(News)
admin.site.register(Aboutus)

admin.site.register(SolutionCate)
admin.site.register(ProductCate)
admin.site.register(NewsCate)
