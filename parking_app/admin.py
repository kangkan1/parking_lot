from django.contrib import admin
from parking_app.models import Account, Registration, PageViewsCounter
# Register your models here.

admin.site.register(Account)
admin.site.register(Registration)
admin.site.register(PageViewsCounter)
