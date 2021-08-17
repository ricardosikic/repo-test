from django.contrib import admin

# Register your models here.
from .models import Todo
from .models import User

admin.site.register(Todo)
admin.site.register(User)