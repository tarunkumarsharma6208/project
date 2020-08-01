from django.contrib import admin
from .models import Products, Order

admin.site.site_header = "ABC site"
admin.site.site_title = "ABC shop"
admin.site.index_title = "Manage ABC shop"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description = 'Default Category'
    search_fields = ('title','category',)
    list_display = ("title", 'price', 'discount_price', 'category', 'description')
    actions = ('change_category_to_default',)
    list_editable = ("price",'category')
    slice = ("description",)


admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
