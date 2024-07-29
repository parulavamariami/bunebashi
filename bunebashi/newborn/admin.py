from django.contrib import admin
from . models import Service, Username, User, Type


admin.site.register(Service)
admin.site.register(Username)
admin.site.register(User)
admin.site.register(Type)