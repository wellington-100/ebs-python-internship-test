from django.contrib import admin

from apps.blog.models import Blog, Category, Comments


# Milestone 1, task 2
class CustomBlogAdmin(admin.ModelAdmin):
    list_display = ("title", "enabled")
    list_filter = ("enabled",)


admin.site.register(Blog, CustomBlogAdmin)
admin.site.register(Category)

# Milestone 1, task 5
admin.site.register(Comments)
