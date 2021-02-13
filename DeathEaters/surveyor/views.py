from django.shortcuts import render

# Create your views here.
class houselisting(View):
    def get(self, request):
        return render(request, 'houselisting.html')
    




class households(View):
 



# user = models.ForeignKey(User, on_delete=models.CASCADE)
#     fname =
#     mname = 
#     lname = 
#     state =
#     district = models.CharField(default='Pune',max_length=100)
#     subDistrict = models.CharField(default='chincwad',max_length=100)
#     village = models.CharField(default='chincwad',max_length=100)
#     wardNo =
#     adhar = models.BigIntegerField(primary_key=True) 
#     sex = models.CharField(max_length=1,choices=SEX_CHOICES)
#     dob = models.DateField(max_length=30) 
#     age = models.IntegerField() 
#     religion = models.CharField(max_length=1,choices=RELIGION_CHOICES)
#     scst = models.CharField(max_length=2,choices=CASTE_CHOICES)
#     scstType = models.CharField(default = 'KALA', max_length=50)
#     martialStatus = models.CharField(max_length=1,choices=MARITAL_STATUS_CHOICES)
#     disability = models.CharField(max_length=1,choices=DISABILITY_CHOICES)
#     motherTongue =  models.CharField(default = 'Hindi', max_length=50)
#     literate = models.BooleanField(default=True)
#     statusOfAttendance = models.BooleanField(default=False)
#     highestEDUAttained = models.CharField(max_length=1,choices=QUALIFICATION_CHOICES)
#     workedLike = models.CharField(max_length=1,choices= TYPE_OF_WORKER )
#     workedAs =  models.CharField(max_length=1,choices= CLASS_OF_WORKER)
#     describeWork = models.CharField(max_length=250)
#     industryType = models.CharField(max_length=250)
#     workerClass = models.CharField(max_length=1,choices=CLASS_OF_WORKER)
#     nonWorkerType = models.CharField(max_length=1,choices=TYPE_OF_NON_WORKER)
#     findingWork = models.BooleanField(default=False)
#     disOfTravelInKm = models.FloatField(default=0.0)
#     modeOfTravel = models.CharField(max_length=1,choices=MODE_OF_TRAVEL)
#     birthPlace = models.CharField(max_length=500)
#     # True => born in india 
#     birthPlaceBool = models.BooleanField(default=True)
#     placeOfLastResidence = models.CharField(max_length=500)
#     # True => live in india 
#     placeOfLastResidenceBool = models.BooleanField(default=True)
#     lastMigrated = models.BooleanField(default=False)
#     cameFrom = models.CharField(max_length=1,choices=CAME_FROM)
#     durOfStayAfterMigration = models.IntegerField(default=1)
#     curChildren = models.IntegerField(default=0)
#     totChildren = models.IntegerField(default=1)