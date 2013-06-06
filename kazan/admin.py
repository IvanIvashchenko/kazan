from django.contrib import admin
from kazan.models import Owner, Ad, Sale

class SaleInline(admin.TabularInline):
    model = Sale
    extra = 3

class AdInline(admin.TabularInline):
    model = Ad
    extra = 3

class UserAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['name']}),
    #     ('Information', {'fields': ['email'], 'classes': ['collapse']}),
    # ]
    inlines = [SaleInline, AdInline]

admin.site.register(Owner, UserAdmin)
# admin.site.register(Ad)
# admin.site.register(Sale)
