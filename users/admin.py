from django.contrib import admin
from users.models import Users, Address, Geo, Company

# Register your models here.
admin.site.register(Users)
admin.site.register(Address)
admin.site.register(Geo)
admin.site.register(Company)
