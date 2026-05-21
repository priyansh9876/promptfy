from django.contrib import admin
from .models import Category, Prompt


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'approved',
        'upvotes',
        'views',
        'created_at'
    )

    list_filter = (
        'approved',
        'category',
        'created_at'
    )

    search_fields = (
        'title',
        'description',
        'tags'
    )

    prepopulated_fields = {'slug': ('title',)}

    list_editable = ('approved',)