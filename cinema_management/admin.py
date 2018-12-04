from django.contrib import admin

from .models import Customer
from .models import Movies
from .models import Staff
from .models import Screens
from .models import FoodStall
from .models import Contact
from .models import StaffContact, ShowTime, Seats
from django.db.models import Avg, Max, Min, Sum, Subquery



class SeatsAdmin(admin.TabularInline):
    model = Seats

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['number', 'price', 'Movies', 'Screen', 'location','Customer', 'Status']
        else:
            return []
    extra = 0
    can_delete  = False

    


class ShowTimeAdmin(admin.TabularInline):
    model = ShowTime
    extra = 0

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['Time']
        else:
            return []
class StaffContactAdmin(admin.TabularInline):
    model = StaffContact
    extra = 0
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["Contact"]
        else:
            return []

class ContactAdmin(admin.TabularInline):
    model = Contact
    extra = 0
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["Contact"]
        else:
            return []
    can_delete = False

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['name', 'Language', 'Release_date', 'Runtime', 'Ratings', 'Genre', 'Certification']
    inlines = [ShowTimeAdmin,]
    list_filter = ['Language', 'Release_date', 'Certification']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'Address', 'Shift', 'Designation', 'Salary']
    inlines = [StaffContactAdmin,]
    list_filter = ['Shift', 'Designation']
    search_fields = ['name']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'Screen_number', 'movie_id']
    list_filter = ['Screen_number', 'movie_id']
    inlines = [ContactAdmin,SeatsAdmin,]
    search_fields = ['name']
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["name", "Screen_number", "movie_id",'seats_price']
        else:
            return []

    def has_delete_permission(self, request, obj=None):
        return False  

    def has_add_permission(self, request):
        return False      

    def seats_price(self, request):
        seats_amounts = Seats.objects.filter(Customer_id = request.id).values_list('price', flat = True)
        total = sum(seats_amounts)
        return total 
    seats_price.short_description = 'Total Price'    
@admin.register(FoodStall)
class FoodStallAdmin(admin.ModelAdmin):
    pass

@admin.register(Screens)
class ScreensAdmin(admin.ModelAdmin):
    inlines = [SeatsAdmin,]


