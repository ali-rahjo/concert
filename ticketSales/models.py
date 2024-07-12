from django.db import models

# Create your models here.

class concertModel(models.Model):
    Name=models.CharField(max_length=100)
    SingerName=models.CharField(max_length=100)
    lenght=models.IntegerField()
    test=models.CharField(max_length=10, null=True)
    poster=models.ImageField(upload_to="posters/", default='default_poster.jpj')

    def __str__(self):
        return self.SingerName

class locationModel(models.Model):
    IdNumber=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=500, default="Berlin")
    Phone=models.CharField(max_length=11, null=True)
    capacity=models.IntegerField()

    def __str__(self):
        return self.Name

class timeModel(models.Model):
    concertModel=models.ForeignKey("concertModel", on_delete=models.PROTECT)
    locationModel = models.ForeignKey("locationModel", on_delete=models.PROTECT)
    StartDateTime = models.DateTimeField()
    Seats=models.IntegerField
    
    Start=1
    End=2
    Cancel=3
    Sales=4

    status_choices=(("Start","selling is started"),
                   ("End","selling is ended"),
                   ("Concel","selling is cancelled"),
                   ("Sales","selling now"))
    
    status_choices=models.IntegerField(choices=status_choices)

    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(StartDateTime,concertModel.Name,locationModel.Name)
    
class ProfileModel(models.Model):
    Name=models.CharField(max_length=100)
    Family=models.CharField(max_length=100)
    ProfileImage=models.ImageField(upload_to="ProfileImages/")


    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return "FullName:{} {}".format(Name,Family)
    
class ticketModel(models.Model):
    ProfileModel = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='tickets')
    timeModel = models.ForeignKey(timeModel, on_delete=models.CASCADE, related_name='tickets')
    # other fields
    ticketImage=models.ImageField(upload_to="TicketImages/")
    Name=models.CharField(max_length=100)
    Price=models.IntegerField()

    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo: {} ".format(timeModel.__str__())
