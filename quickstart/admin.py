from django.contrib import admin
from .models import Customer, Account, Background
# Register your models here.



class CustomerAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
    pass

class BackgroundAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Background, BackgroundAdmin)