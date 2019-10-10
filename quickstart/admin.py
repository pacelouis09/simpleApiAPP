from django.contrib import admin
from .models import Customer, Account, Background #, Organization, OrganizationAPIKey
# Register your models here.


admin.site.header = "Leads App"
admin.site.site_title = "Leads App Admin Portal"
admin.site.index_title = "Welcome to Leads App"


class CustomerAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'phone')

class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'street_address', 'address2', 'city', 'state', 'zip_code')

# class OrganizationAdmin(admin.ModelAdmin):
#     pass

# class OrganizationAPIKeyAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Background, BackgroundAdmin)
# admin.site.register(Organization, OrganizationAdmin)
# admin.site.register(OrganizationAPIKey, OrganizationAPIKeyAdmin)