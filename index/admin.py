from django.contrib import admin
from .models import *
# 高级管理类
class GoodsAdmin(admin.ModelAdmin):

  #指定在列表页中显示的字段们
  list_display = ('title','goodsType','price','spec')
  #指定右侧显示的过滤器
  list_filter = ('goodsType',)
  #指定在上方显示的搜索字段们
  search_fields = ('title',)


class GoodsTypeAdmin(admin.ModelAdmin):
  #指定在列表页中显示的字段们
  list_display = ('title','picture','desc')


class UserAdmin(admin.ModelAdmin):
  # 指定在列表页中显示的字段们
  list_display = ('uname',  'uphone', 'uemail')
  # 指定右侧显示的过滤器
  list_filter = ('isActive',)
  # 指定在上方显示的搜索字段们
  search_fields = ('uname',)
  #   分组显示的字段
  fieldsets = [
    ('基本信息', {'fields': ('uname', 'email', 'uphone',),
              }
     ),
    ("可选信息", {'fields': ( 'isActive', ),
              'classes': ('collapse',)
              }
     )
  ]
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(Goods,GoodsAdmin)