from django.contrib import admin
from .models import Product, Category
from mptt.admin import MPTTAdminForm, DraggableMPTTAdmin

# Register your models here.
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "category_name"
    list_display = (
        'tree_actions', 'indented_title', 'related_products_count',
        'related_products_cumulative_count'
    )
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(
            qs,
            Product,
            'product_category',
            'products_cumulative_count',
            cumulative = True
        )
        
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'product_category',
            'products_count',
            cumulative = False
        )
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related Posts(for this specific product_category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related posts (in tree)'
        

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "slug"]
    list_filter = ("product_name",)
    readonly_fields =["slug",]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)