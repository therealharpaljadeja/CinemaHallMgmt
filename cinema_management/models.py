from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Movies(models.Model):
    Languages = [('Eng', 'English'),('Hin', 'Hindi'),('Mar', 'Marathi')]
    Certifications = [('U', 'Universal'), ('U/A', 'Universal/Adult'), ('A','Adult')]
    Status = [('U', 'Upcoming'), ('C', 'Currently Airing'), ('A', 'Aired')]
    name = models.CharField(max_length = 100)
    Language = models.CharField(choices = Languages, max_length = 3, blank = True)
    Release_date = models.DateTimeField()
    Runtime = models.CharField(max_length = 10, blank = True)
    Genre = models.CharField(max_length = 15, blank = True)
    Ratings = models.FloatField(default = 0.0)
    Certification = models.CharField(choices = Certifications, max_length = 3, blank = True)
    Poster = models.CharField(max_length = 10000, null = True, blank = True)
    Status = models.CharField(max_length = 1, choices = Status)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name


class Staff(models.Model):
    Shifts = [('M', 'Morning'), ('N', 'Night')]
    name = models.CharField(max_length = 30)
    Address = models.TextField()
    Shift = models.CharField(choices = Shifts, max_length = 1)    
    Designation = models.CharField(max_length = 100, blank = True)
    Salary = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Staff'
    
    def __str__(self):
        return self.name

class FoodStall(models.Model):
    name = models.CharField(max_length = 30)
    Rent = models.IntegerField()   
    Commodity = models.CharField(max_length = 40)
    Commodity_Price = models.IntegerField()
    def __str__(self):
        return self.name

class Screens(models.Model):
    Screen_Type = [('2d', '2D'), ('3D','3D'), ('IMAX', 'Imax')]
    type = models.CharField(choices = Screen_Type,max_length = 4)   

    class Meta:
        verbose_name_plural = 'Screens'

    def __str__(self):
        return self.type
    

class Customer(models.Model):
    name = models.CharField(max_length = 30)     
    Screen_number = models.ForeignKey(Screens, on_delete = models.CASCADE)
    movie_id = models.ForeignKey(Movies, on_delete = models.CASCADE)  
    def __str__(self):
        return self.name


class Contact(models.Model):
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Contact = models.IntegerField(max_length=10) 

    def __str__(self):
        return "{}".format(self.Contact) 
    
class StaffContact(models.Model):
    Staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    Contact = models.IntegerField(max_length=10) 

    def __str__(self):
        return "{}".format(self.Contact) 

class ShowTime(models.Model):
    Screen = models.ForeignKey(Screens, on_delete = models.CASCADE)
    Time = models.TimeField(null = True)
    Movie = models.ForeignKey(Movies, on_delete = models.CASCADE)   

    def __str__(self):
        return "{} - {}".format(self.Movie, self.Time)     

class Seats(models.Model):
           
    Status_Choices = [('A', 'Available'), ('B', 'Booked')]
    Screen = models.ForeignKey(Screens, on_delete = models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE, null = True, blank = True)
    Movies = models.ForeignKey(Movies, on_delete = models.CASCADE)
    price = models.IntegerField(max_length = 3)
    number = models.CharField(max_length = 4)
    location = models.CharField(max_length = 100)
    Status = models.CharField(choices = Status_Choices, max_length = 1, default ='A')
    


    class Meta:
        verbose_name_plural = 'Seats'

    def __str__(self):
        return "{} - {} - {}".format(self.Movies, self.Customer, self.number)  
 

@receiver(post_save, sender = Seats)
def Status_update(sender, instance, **kwargs):
    Seats.objects.filter(Customer__isnull = False).update(Status = 'B')
    Seats.objects.all().order_by('number')
