from django.contrib import admin
from find.models import UserProfile, Discount, Review, Rating

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('id',)}

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Discount)
admin.site.register(Review)
admin.site.register(Rating)
