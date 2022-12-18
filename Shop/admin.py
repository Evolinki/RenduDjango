from django.contrib import admin

from .models import Question
from .models import Product

class QuestionAdmin(admin.ModelAdmin):
    fields =['text']
    
admin.site.register(Question)
    

class ProductAdmin(admin.ModelAdmin):
    fields =['Url_Image','Nom','stock','prix']
    
admin.site.register(Product)
