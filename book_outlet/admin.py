from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin): # Add admin class to fine tune how book is displayed in admin
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating", )
    list_display = ("title", "author", )

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)

