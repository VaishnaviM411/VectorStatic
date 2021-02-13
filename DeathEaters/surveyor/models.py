from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import MaxValueValidator
from django.db.models import OneToOneField

SEX_CHOICES = (
        ('-1','-1',),
        ('1', 'Female',),
        ('2', 'Male',),
        ('3', 'Other',),
    )

CASTE_CHOICES = (
    ('-1','-1',),
    ('1', 'Scheduled-Caste',),
    ('2', 'Scheduled-Tribe',),
    ('3', 'None',),
)

MARITAL_STATUS_CHOICES = (
    ('-1','-1',),
    ('1','Never-Married', ),
    ('2','Currently-Married', ),
    ('3','Widowed', ),
    ('4','Separated',),
    ('5','Divorced', ),
)

RELIGION_CHOICES = (
    ('-1','-1',),
    ('1', 'Hindu',),
    ('2', 'Muslim',),
    ('3', 'Christian',),
    ('4', 'Sikh',),
    ('5', 'Buddhist',),
    ('6', 'Jain',),
)

DISABILITY_CHOICES = (
    ('-1','-1',),
    ('1', 'Seeing',),
    ('2', 'Hearing',),
    ('3', 'Speech',),
    ('4', 'Movement',),
    ('5', 'Mental-Retardness',),
    ('6', 'Mental-Illness',),
    ('7', 'Multiple-Disability',),
    ('8', 'Other',),
)

QUALIFICATION_CHOICES = (
    ('-1','-1',),
    ('1', 'School',),
    ('2', 'College',),
    ('3', 'Vocational',),
    ('4', 'Special Institution For Disabled',),
    ('5', 'Literacy-Centre',),
    ('6', 'Other-Institution',),
    ('7', 'None',),
)
CATEGORY_OF_WORKER = (
        ('-1','-1',),
        ('1', 'Cultivator',),
        ('2', 'Agricultural-Labourer',),
        ('3', 'Work In household industry',),
        ('4', 'Other',),
    )

CLASS_OF_WORKER = (
    ('-1','-1',),
    ('1', 'Employer',),
    ('2', 'Employee',),
    ('3', 'Single-Worker',),
    ('4', 'Family-Worker',),
)

TYPE_OF_WORKER = (
    ('-1','-1',),
    ('1', 'Main-Worker',),
    ('2', 'Marginal-Worker',),
    ('3', 'Non-Worker',),
)

TYPE_OF_NON_WORKER = (
    ('-1','-1',),
    ('1', 'Student',),
    ('2', 'Household-Duties',),
    ('3', 'Dependent',),
    ('4', 'Pensioner',),
    ('5', 'Rentier',),
    ('6', 'Beggar',),
    ('7', 'Other',),
)

MODE_OF_TRAVEL = (
    ('-1','-1',),
    ('1', 'On Foot',),
    ('2', 'Bicycle',),
    ('3', 'Moped/Scooter/Motor-Cycle',),
    ('4', 'Car/Jeep/VAN  ',),
    ('5', 'Literacy Centre',),
    ('6', 'Other Institution',),
    ('7', 'None',),
)

CAME_FROM = (
    ('-1','-1',),
    ('1', 'Rural',),
    ('2', 'Urban',),
)



FLOOR_CHOICES = (
        ('-1','-1',),
        ('1','Mud'),
        ('2','Wood/bamboo'),
        ('3','Burnt brick'),
        ('4','Stone'),
        ('5','Cement'),
        ('6','Mosaic/floor tiles'),
        ('7','Any other'),
    )

WALL_CHOICES = (
    ('0','Any other'),
    ('1','Grass/thatch/bamboo'),
    ('2','Plastic/polythene'),
    ('3','Mud/unburnt brick'),
    ('4','Wood'),
    ('5','Stone not packed with mortar'),
    ('6','Stone packed with mortar'),
    ('7','G.I./metal/asbestos sheets'),
    ('8','Burnt brick'),
    ('9','Concrete'),
    
)

ROOF_CHOICES = (
    ('0','Any other'),
    ('1','Grass/ thatch/ bamboo/ wood/ mud'),
    ('2','Plastic/ polythene'),
    ('3','Hand made tiles'),
    ('4','Machine made tiles'),
    ('5','Burnt brick'),
    ('6','Stone'),
    ('7','Slate'),
    ('8','G.I./metal/asbestos sheets'),
    ('9','Concrete'),
    
)

USE_CHOICES = (
    ('0','Any other'),
    ('1','Residence'),
    ('2','Residence-cum-other use'),
    ('3','Shop/ office'),
    ('4','School/ college'),
    ('5','Hotel/ lodge/ guest house'),
    ('6','Hospital/ dispensary'),
    ('7','Factory/ workshop/ workshed'),
    ('8','Place of worship'),
    ('9','Other non-residential use'),
    
)

SEX_CHOICES = (
    ('-1','-1',),
    ('1', 'Female',),
    ('2', 'Male',),
    ('3', 'Other',),
)

CASTE_CHOICES = (
    ('-1','-1',),
    ('1','SC'),
    ('2','ST'),
    ('3','Other'),
)

OWNERSHIP_CHOICES = (
    ('-1','-1',),
    ('1','Owned'),
    ('2','Rented but has own house elsewhere'),
    ('3','Rented and does not own any house'),
    ('4','Any other'),
)

DWATERAVAIL_CHOICES = (
    ('-1','-1',),
    ('1','Within premises'),
    ('2','Near the premises'),
    ('3','Away'),
)

DWATERSOURCE_CHOICES = (
    ('0','Other sources'),
    ('1','Tap water from source'),
    ('2','Tap water from un-treated source'),
    ('3','Well'),
    ('4','Hand Pump'),
    ('5','Tubewell/ borehole'),
    ('6','Spring'),
    ('7','River/canal'),
    ('8','Tank/pond/lake'),
    ('9','Packaged/bottled water'),
    
)

LIGHTING_CHOICES = (
    ('-1','-1',),
    ('1','Electricity'),
    ('2','Kerosene'),
    ('3','Solar'),
    ('4','Other oil'),
    ('5','Any other'),
    ('6','No lighting'),
)

LATRINEACCESS_CHOICES = (
    ('-1','-1',),
    ('1','YES, Exclusively for household use only'),
    ('2','YES, Shared with other household'),
    ('3','YES, Public latrine'),
    ('4','NO, Open'),
)

LATRINETYPE_CHOICES = (
    ('0','Night soil disposed into open drain'),
    ('1','Flush/pour flush latrine connected to Piped sewer system'),
    ('2','Flush/pour flush latrine connected to Septic tack'),
    ('3','Flush/pour flush latrine connected to Other system'),
    ('4','Twin Pit latrine With slab/ventilated improved pit'),
    ('5','Twin Pit latrine Without slab/open pit'),
    ('6','Single Pit latrine With slab/ventilated improved pit'),
    ('7','Single Pit latrine Without slab/open pit'),
    ('8','Service latrine Night soil removed by human'),
    ('9','Service latrine Night soil serviced by animals'),
    
)

KITCHEN_CHOICES = (
    ('-1','-1',),
    ('1','Cooking in kitchen, has LPG/PNG Connection'),
    ('2','Cooking in kitchen, Does not have LPG/PNG Connection'),
    ('3','Cooking inside house, but not in kitchen, Has LPG/PNG Connection'),
    ('4','Cooking inside house, but not in kitchen, does not have LPG/PNG Connection'),
    ('5','Cooking in open/ outside house, Has LPG/PNG Connection'),
    ('6','Cooking in open/ outside house, does not have LPG/PNG Connection'),
    ('7','No cooking'),
)

FUEL_CHOICES = (
    ('0','Any other'),
    ('1','Firewood'),
    ('2','Crop residue'),
    ('3','Cowding cake'),
    ('4','Coal/lignite/charcoal'),
    ('5','Kerosene'),
    ('6','LPG/PNG'),
    ('7','Electricity'),
    ('8','Bio-gas'),
    ('9','Solar'),
    
)

WASTEWATER_CHOICES = (
    ('-1','-1',),
    ('1','Closed drainage'),
    ('2','Open drainage'),
    ('3','No drainage'),
)

BATHINGFACILITY_CHOICES = (
    ('-1','-1',),
    ('1','YES, Bathroom'),
    ('2','YES, Enclosure without roof'),
    ('3','NO'),
)

RADIO_CHOICES = (
    ('-1','-1',),
    ('1','YES, Traditional radio set'),
    ('2','YES, on mobile/smartphone'),
    ('3','YES, On any other device'),
    ('4','NO'),
)

TELEVISION_CHOICES = (
    ('-1','-1',),
    ('1','YES, Doordarshan free dish'),
    ('2','YES, DTH/Dish'),
    ('3','YES, Cable connection'),
    ('4','Any other'),
    ('5','NO'),
)

INTERNET_CHOICES = (
    ('-1','-1',),
    ('1','YES, On laptop/computer'),
    ('2','YES, On mobile/smartphone'),
    ('3','YES, On any other device'),
    ('4','NO'),
)

DEVICE_CHOICES = (
    ('-1','-1',),
    ('1','YES'),
    ('2','NO'),
)

PHONE_CHOICES = (
    ('-1','-1',),
    ('1','YES, Landline only'),
    ('2','YES, Mobile only, Smartphone'),
    ('3','YES, Mobile only, Other basic mobile'),
    ('4','YES, Both'),
    ('5','No'),
)

TWOWHEELER_CHOICES = (
    ('-1','-1',),
    ('1','Bicycle'),
    ('2','Scooter/ Motorcycle/ Moped'),
    ('3','Both'),
    ('4','None'),
)

FOURWHEELER_CHOICES = (
    ('-1','-1',),
    ('1','YES'),
    ('2','NO'),
)

CEREAL_CHOICES = (
    ('-1','-1',),
    ('1','Rice'),
    ('2','Wheat'),
    ('3','Jowar'),
    ('4','Bajra'),
    ('5','Maize'),
    ('6','Any other'),
)




class HouseHolds(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(default = 'AMAR', max_length=50)
    mname = models.CharField(default = 'AKBAR', max_length=50)
    lname = models.CharField(default = 'ANTHONY', max_length=50)
    state = models.CharField(default= 'UP',max_length=100)
    district = models.CharField(default='Pune',max_length=100)
    subDistrict = models.CharField(default='chincwad',max_length=100)
    village = models.CharField(default='chincwad',max_length=100)
    wardNo = models.IntegerField(default=0)
    adhar = models.BigIntegerField(primary_key=True) 
    sex = models.CharField(max_length=1000,choices=SEX_CHOICES)
    dob = models.DateField(max_length=1000) 
    age = models.IntegerField() 
    religion = models.CharField(max_length=1000,choices=RELIGION_CHOICES)
    scst = models.CharField(max_length=1001000,choices=CASTE_CHOICES)
    scstType = models.CharField(default = 'KALA', max_length=50)
    martialStatus = models.CharField(max_length=1000,choices=MARITAL_STATUS_CHOICES)
    disability = models.CharField(max_length=1000,choices=DISABILITY_CHOICES)
    motherTongue =  models.CharField(default = 'Hindi', max_length=1000)
    literate = models.BooleanField(default=True)
    statusOfAttendance = models.BooleanField(default=False)
    highestEDUAttained = models.CharField(max_length=1000,choices=QUALIFICATION_CHOICES)

    
    workedLike = models.CharField(max_length=1000,choices= TYPE_OF_WORKER )
    workedAs =  models.CharField(max_length=1000,choices= CLASS_OF_WORKER)
    describeWork = models.CharField(max_length=250)
    industryType = models.CharField(max_length=250)
    workerClass = models.CharField(max_length=1000,choices=CLASS_OF_WORKER)
    nonWorkerType = models.CharField(max_length=1000,choices=TYPE_OF_NON_WORKER)
    findingWork = models.BooleanField(default=False)
    disOfTravelInKm = models.FloatField(default=0.0)
    modeOfTravel = models.CharField(max_length=1000,choices=MODE_OF_TRAVEL)
    birthPlace = models.CharField(max_length=500)
    # True => born in india 
    birthPlaceBool = models.BooleanField(default=True)
    placeOfLastResidence = models.CharField(max_length=500)
    # True => live in india 
    placeOfLastResidenceBool = models.BooleanField(default=True)
    lastMigrated = models.BooleanField(default=False)
    cameFrom = models.CharField(max_length=1000,choices=CAME_FROM)
    durOfStayAfterMigration = models.IntegerField(default=1)
    curChildren = models.IntegerField(default=0)
    totChildren = models.IntegerField(default=1)
    



class HouseListing(models.Model):

    
    BuildingNo = models.CharField(max_length=10)
    CensusHouseNo = models.CharField(max_length=1000,null=True)
    FloorMaterial = models.CharField(max_length=1000, choices=FLOOR_CHOICES)
    WallMaterial = models.CharField(max_length=1000,choices=WALL_CHOICES)
    RoofMaterial = models.CharField(max_length=1000,choices=ROOF_CHOICES)
    UseOfHouse = models.CharField(max_length=1000,choices=USE_CHOICES)
    TotalResidents = models.IntegerField()
    HeadName = models.CharField(max_length=200)
    HeadSex = models.CharField(max_length=1000,choices=SEX_CHOICES)
    HeadCaste = models.CharField(max_length=1000,choices=CASTE_CHOICES)
    Ownership = models.CharField(max_length=1000,choices=OWNERSHIP_CHOICES)
    DwellingRooms = models.IntegerField()
    MarriedCouples = models.IntegerField()
    DrinkingWaterSource = models.CharField(max_length=1000,choices=DWATERSOURCE_CHOICES)
    DrinkingWaterAvail = models.CharField(max_length=1000,choices=DWATERAVAIL_CHOICES)
    LightingSource = models.CharField(max_length=1000,choices=LIGHTING_CHOICES)
    LatrineAccess = models.CharField(max_length=1000,choices=LATRINEACCESS_CHOICES)
    LatrineType = models.CharField(max_length=1000,choices=LATRINETYPE_CHOICES)
    WasteWaterOutlet = models.CharField(max_length=1000,choices=WASTEWATER_CHOICES)
    BathingFacility = models.CharField(max_length=1000,choices=BATHINGFACILITY_CHOICES)
    Kitchen = models.CharField(max_length=1000,choices=KITCHEN_CHOICES)
    KitchenFuel = models.CharField(max_length=1000,choices=FUEL_CHOICES)
    Radio = models.CharField(max_length=1000,choices=RADIO_CHOICES)
    Television = models.CharField(max_length=1000,choices=TELEVISION_CHOICES)
    Internet = models.CharField(max_length=1000,choices=INTERNET_CHOICES)
    ComputingDevice = models.CharField(max_length=1000,choices=DEVICE_CHOICES)
    Phone = models.CharField(max_length=1000,choices=PHONE_CHOICES)
    TwoWheeler = models.CharField(max_length=1000,choices=TWOWHEELER_CHOICES)
    FourWheeler = models.CharField(max_length=1000,choices=FOURWHEELER_CHOICES)
    Cereal = models.CharField(max_length=1000,choices=CEREAL_CHOICES)
    ContactNo = models.CharField(max_length=1000)