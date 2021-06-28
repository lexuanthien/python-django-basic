from django.contrib import admin

# Register your models here.
from .models import user, post, comment, Car

# Khi muon tuy chinh, hien thi hoac an cac truong
# class userAdmin(admin.ModelAdmin):
#     # fields = ['age', 'phone', 'name']
#     fieldsets = [
#         (None,               {'fields': ['name']}),
#         ('Date information', {'fields': ['age', 'phone']}),
#     ]

# admin.site.register(user, userAdmin)

admin.site.register(user)
admin.site.register(post)
admin.site.register(comment)
admin.site.register(Car)