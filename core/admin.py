from django.contrib import admin

from .models import Manufacturer, Order, Product

admin.site.site_header = "NTEC Shop — администрирование"
admin.site.site_title = "NTEC Shop Admin"
admin.site.index_title = "Управление данными магазина"


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country", "phone")
    search_fields = ("name", "country")
    list_filter = ("country",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "discount", "manufacturer")
    list_filter = ("manufacturer",)
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "status")
    list_filter = ("status",)
    search_fields = ("product__name",)
