from django.contrib import admin
from .models import Query,Category,Blogs,Contact
from django.utils.translation import gettext, gettext_lazy as _
from .utils import unique_slug_generator

# Register your models here.

@admin.register(Query)
class Query(admin.ModelAdmin):
   
    list_display = ('id','email','query',)

    fieldsets = (
        (_('Query'), {'fields': ('email', 'query',)}),
        
        )

    def save_model(self, request, obj, form, change):
        obj.save()


@admin.register(Contact)
class Contact(admin.ModelAdmin):
   
    list_display = ('id','email','sub',)

    fieldsets = (
        (_('Query'), {'fields': ('fname','lname','phone','email', 'sub','msg')}),
        
        )

    def save_model(self, request, obj, form, change):
        obj.save()



@admin.register(Category)
class CategoryManager(admin.ModelAdmin):
    list_display = ('id','content','slug')
    search_fields = ('content',)
    readonly_fields = ('slug',)

    def save_model(self, request, obj, form, change):
        obj.save()


@admin.register(Blogs)
class Blogs(admin.ModelAdmin):
   
    search_fields = ('question','tags',)
    list_filter = ('question','tags')
    list_display = ('id','question','slug',)
    filter_horizontal = ['tags']
    readonly_fields = ('slug','published_on')

    fieldsets = (
        (_('Question'), {'fields': ('question',)}),
        (_('Answer'), {'fields': ('answer', 'code',)}),
        (_('Social'), {'fields': ('name', 'college_name','facebook','twitter','linkedin','instagram')}),
        (_('tags'), {'fields': ('tags',)}),
        
    )

    def save_model(self, request, obj, form, change):
        obj.save()