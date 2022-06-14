from django.contrib import admin
from .models import User, AdminsDetail, ClientsDetail

# Register your models here.

admin.site.register(User)
admin.site.register(AdminsDetail)
admin.site.register(ClientsDetail)