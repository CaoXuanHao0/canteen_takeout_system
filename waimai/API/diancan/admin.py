from django.contrib import admin
from diancan.models import *
from login.models import student


# Register your models here.
class order_dishes_inline(admin.TabularInline):
    model = dishes


@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('OrderID', 'name', 'canteen_name', 'create_time', 'colored_status')
    list_filter = ['student_id']
    ordering = ('create_time',)
    fk_fields = ('student_id',)
    inlines = [order_dishes_inline]
    fieldsets = (
        ['订单信息', {
            'fields': ('OrderID', 'delivery_time', 'create_time', 'menu', 'canteen_name', 'status'),
        }],
        ['订购人信息', {
            'classes': ('collapse',),  # CSS
            'fields': ('student_id', 'name', 'telephone_num', 'destination'),
        }]
    )
    readonly_fields = ('OrderID', 'student_id', 'create_time', 'telephone_num', 'destination', 'name')


class CanteenAdmin(admin.ModelAdmin):
    list_display = ('menu_ID', 'name', 'windows_name', 'price', 'for_sale')
    list_filter = ['windows_name']
    list_per_page = 20
    fieldsets = (
        ['菜品信息', {
            'fields': ('menu_ID', 'windows_name', 'name', 'price', 'for_sale', 'image', 'last_edit_time'),
        }],
    )
    readonly_fields = ('menu_ID', 'last_edit_time',)

admin.site.register(xinbei, CanteenAdmin)
admin.site.register(heyi, CanteenAdmin)
admin.site.register(xuer, CanteenAdmin)