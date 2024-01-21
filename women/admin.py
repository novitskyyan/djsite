from django.contrib import admin, messages

from .models import Women, Category


# Register your models here.

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'brief_info')
    list_display_links = ('id', 'title')
    ordering = ['time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 20
    actions = ('set_published', 'set_draft',)

    @admin.display(description='Краткое описание')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей')

    @admin.action(description='Снять выбранные записи с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(
            request,
            f'{count} записей снято с публикации',
            messages.WARNING
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
