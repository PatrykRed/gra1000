from django.contrib import admin

# Register your models here.
from accounts.models import uzytkownik


@admin.register(uzytkownik)
class UzytkownikUserAdmin(admin.ModelAdmin):  # noqa D101
    pass
