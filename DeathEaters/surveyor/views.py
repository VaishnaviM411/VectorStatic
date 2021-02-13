from django.shortcuts import render
from django.views.generic.base import View
from surveyor.models import HouseHolds 
from surveyor.models import HouseListing

    
SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('O', 'Other',),
    )

CASTE_CHOICES = (
        ('SC', 'Scheduled-Caste',),
        ('ST', 'Scheduled-Tribe',),
        ('NA', 'None',),
    )

MARITAL_STATUS_CHOICES = (
    ('1','Never-Married', ),
    ('2','Currently-Married', ),
    ('3','Widowed', ),
    ('4','Separated',),
    ('5','Divorced', ),
)

RELIGION_CHOICES = (
    ('H', 'Hindu',),
    ('M', 'Muslim',),
    ('C', 'Christian',),
    ('S', 'Sikh',),
    ('B', 'Buddhist',),
    ('J', 'Jain',),
)

DISABILITY_CHOICES = (
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
    ('0','0',),
    ('1', 'School',),
    ('2', 'College',),
    ('3', 'Vocational',),
    ('4', 'Special Institution For Disabled',),
    ('5', 'Literacy-Centre',),
    ('6', 'Other-Institution',),
    ('7', 'None',),
)




CATEGORY_OF_WORKER = (
        ('1', 'Cultivator',),
        ('2', 'Agricultural-Labourer',),
        ('3', 'Work In household industry',),
        ('4', 'Other',),
    )

CLASS_OF_WORKER = (
    ('1', 'Employer',),
    ('2', 'Employee',),
    ('3', 'Single-Worker',),
    ('4', 'Family-Worker',),
)

TYPE_OF_WORKER = (
    ('1', 'Main-Worker',),
    ('2', 'Marginal-Worker',),
    ('3', 'Non-Worker',),
)

TYPE_OF_NON_WORKER = (
    ('1', 'Student',),
    ('2', 'Household-Duties',),
    ('3', 'Dependent',),
    ('4', 'Pensioner',),
    ('5', 'Rentier',),
    ('6', 'Beggar',),
    ('7', 'Other',),
)

MODE_OF_TRAVEL = (
    ('1', 'On Foot',),
    ('2', 'Bicycle',),
    ('3', 'Moped/Scooter/Motor-Cycle',),
    ('4', 'Car/Jeep/VAN  ',),
    ('5', 'Literacy Centre',),
    ('6', 'Other Institution',),
    ('7', 'None',),
)

CAME_FROM = (
    ('1', 'Rural',),
    ('2', 'Urban',),
)



class households(View):
    def get(self, request, template_name='household.html'):
        # group = request.user.groups.all()[0].name
        # if isNotStudent(group):
        #     return render(request, 'login.html')
        # else:
        #     try:
        #         user = request.user
        #         allCourses = Coursera.objects.filter(user=user)
        #         countCourses = len(allCourses)
        #     except:
        #         allCourses = None
        #         countCourses = 0
        #     args = {}
        #     args["allCourses"] = allCourses
        #     args["countCourses"] = countCourses
        return render(request, template_name)

    def post(self, request, template_name='household.html'):        
        user = request.user
        fname = request.POST.get('fname')
        mname  = request.POST.get('mname ')
        lname  = request.POST.get('lname')
        state = request.POST.get('state')
        district  = request.POST.get('district')
        subDistrict  = request.POST.get('subDistrict')
        village  = request.POST.get('village')
        wardNo = request.POST.get('wardNo')
        adhar = request.POST.get('adhar')
        sex = request.POST.get('sex')
        sex = SEX_CHOICES[sex][1]
        dob  = request.POST.get('dob')
        age = request.POST.get('age')
        religion = request.POST.get('religion')
        scst = request.POST.get('scst')
        scstType = request.POST.get('scstType')
        martialStatus = request.POST.get('martialStatus')
        disability = request.POST.get('disability')
        motherTongue = request.POST.get('motherTongue')
        literate = request.POST.get('literate')
        statusOfAttendance = request.POST.get('statusOfAttendance')
        highestEDUAttained = request.POST.get('highestEDUAttained')
        workedLike = request.POST.get('workedLike')
        workedAs = request.POST.get('workedAs')
        describeWork = request.POST.get('describeWork')
        industryType = request.POST.get('industryType')
        workerClass = request.POST.get('workerClass')
        nonWorkerType = request.POST.get('nonWorkerType')
        findingWork = request.POST.get('findingWork')
        disOfTravelInKm = request.POST.get('disOfTravelInKm')
        modeOfTravel = request.POST.get('modeOfTravel')
        birthPlace = request.POST.get('birthPlace')
        # True => born in india 
        birthPlaceBool = request.POST.get('birthPlaceBool')
        placeOfLastResidence = request.POST.get('placeOfLastResidence')
        # True => live in india 
        placeOfLastResidenceBool = request.POST.get('placeOfLastResidenceBool')
        lastMigrated = request.POST.get('lastMigrated')
        cameFrom = request.POST.get('cameFrom')
        durOfStayAfterMigration = request.POST.get('durOfStayAfterMigration ')
        curChildren = request.POST.get('curChildren')
        totChildren = request.POST.get('totChildren')
        householdobj = HouseHolds(
            user =user ,
            mname= fname ,
            lname  =      mname ,
            fname       =      lname,
            state         =    state ,
            district      =        district,  
            subDistrict    =          subDistrict,  
            village     =         village  ,
            wardNo      =       wardNo ,
            adhar   =          adhar ,
            sex       =      sex ,
            dob     =         dob , 
            age        =     age ,
            religion    =         religion, 
            scst            = scst ,
            scstType      =       scstType, 
            martialStatus     =        martialStatus, 
            disability         =   disability,
            motherTongue   =          motherTongue ,
            literate         =    literate ,
            statusOfAttendance    =         statusOfAttendance ,
            highestEDUAttained  =           highestEDUAttained ,
            workedLike       =      workedLike ,
            workedAs           =  workedAs ,
            describeWork          =   describeWork ,
            industryType         =   industryType,
            workerClass       =      workerClass ,
            nonWorkerType     =        nonWorkerType ,
            findingWork        =     findingWork ,
            disOfTravelInKm    =         disOfTravelInKm ,
            modeOfTravel       =      modeOfTravel ,
            birthPlace           =  birthPlace ,
            birthPlaceBool         =    birthPlaceBool, 
            placeOfLastResidence      =       placeOfLastResidence, 
            placeOfLastResidenceBool =            placeOfLastResidenceBool ,
            lastMigrated    =         lastMigrated ,
            cameFrom          =   cameFrom ,
            durOfStayAfterMigration    =         durOfStayAfterMigration ,
            curChildren      =       curChildren ,
            totChildren        =    totChildren,
            )
        householdobj.save()



FLOOR_CHOICES = (
        ('1','Mud'),
        ('2','Wood/bamboo'),
        ('3','Burnt brick'),
        ('4','Stone'),
        ('5','Cement'),
        ('6','Mosaic/floor tiles'),
        ('7','Any other'),
    )

WALL_CHOICES = (
    ('1','Grass/thatch/bamboo'),
    ('2','Plastic/polythene'),
    ('3','Mud/unburnt brick'),
    ('4','Wood'),
    ('5','Stone not packed with mortar'),
    ('6','Stone packed with mortar'),
    ('7','G.I./metal/asbestos sheets'),
    ('8','Burnt brick'),
    ('9','Concrete'),
    ('0','Any other'),
)

ROOF_CHOICES = (
    ('1','Grass/ thatch/ bamboo/ wood/ mud'),
    ('2','Plastic/ polythene'),
    ('3','Hand made tiles'),
    ('4','Machine made tiles'),
    ('5','Burnt brick'),
    ('6','Stone'),
    ('7','Slate'),
    ('8','G.I./metal/asbestos sheets'),
    ('9','Concrete'),
    ('0','Any other'),
)

USE_CHOICES = (

    ('1','Residence'),
    ('2','Residence-cum-other use'),
    ('3','Shop/ office'),
    ('4','School/ college'),
    ('5','Hotel/ lodge/ guest house'),
    ('6','Hospital/ dispensary'),
    ('7','Factory/ workshop/ workshed'),
    ('8','Place of worship'),
    ('9','Other non-residential use'),
    ('0','Any other'),
)

SEX_CHOICES = (
    ('F', 'Female',),
    ('M', 'Male',),
    ('O', 'Other',),
)

CASTE_CHOICES = (
    ('1','SC'),
    ('2','ST'),
    ('3','Other'),
)

OWNERSHIP_CHOICES = (
    ('1','Owned'),
    ('2','Rented but has own house elsewhere'),
    ('3','Rented and does not own any house'),
    ('4','Any other'),
)

DWATERAVAIL_CHOICES = (
    ('1','Within premises'),
    ('2','Near the premises'),
    ('3','Away'),
)

DWATERSOURCE_CHOICES = (
    ('1','Tap water from source'),
    ('2','Tap water from un-treated source'),
    ('3','Well'),
    ('4','Hand Pump'),
    ('5','Tubewell/ borehole'),
    ('6','Spring'),
    ('7','River/canal'),
    ('8','Tank/pond/lake'),
    ('9','Packaged/bottled water'),
    ('0','Other sources'),
)

LIGHTING_CHOICES = (
    ('1','Electricity'),
    ('2','Kerosene'),
    ('3','Solar'),
    ('4','Other oil'),
    ('5','Any other'),
    ('6','No lighting'),
)

LATRINEACCESS_CHOICES = (
    ('1','YES, Exclusively for household use only'),
    ('2','YES, Shared with other household'),
    ('3','YES, Public latrine'),
    ('4','NO, Open'),
)

LATRINETYPE_CHOICES = (
    ('1','Flush/pour flush latrine connected to Piped sewer system'),
    ('2','Flush/pour flush latrine connected to Septic tack'),
    ('3','Flush/pour flush latrine connected to Other system'),
    ('4','Twin Pit latrine With slab/ventilated improved pit'),
    ('5','Twin Pit latrine Without slab/open pit'),
    ('6','Single Pit latrine With slab/ventilated improved pit'),
    ('7','Single Pit latrine Without slab/open pit'),
    ('8','Service latrine Night soil removed by human'),
    ('9','Service latrine Night soil serviced by animals'),
    ('0','Night soil disposed into open drain'),
)

KITCHEN_CHOICES = (
    ('1','Cooking in kitchen, has LPG/PNG Connection'),
    ('2','Cooking in kitchen, Does not have LPG/PNG Connection'),
    ('3','Cooking inside house, but not in kitchen, Has LPG/PNG Connection'),
    ('4','Cooking inside house, but not in kitchen, does not have LPG/PNG Connection'),
    ('5','Cooking in open/ outside house, Has LPG/PNG Connection'),
    ('6','Cooking in open/ outside house, does not have LPG/PNG Connection'),
    ('7','No cooking'),
)

FUEL_CHOICES = (
    ('1','Firewood'),
    ('2','Crop residue'),
    ('3','Cowding cake'),
    ('4','Coal/lignite/charcoal'),
    ('5','Kerosene'),
    ('6','LPG/PNG'),
    ('7','Electricity'),
    ('8','Bio-gas'),
    ('9','Solar'),
    ('0','Any other'),
)

WASTEWATER_CHOICES = (
    ('1','Closed drainage'),
    ('2','Open drainage'),
    ('3','No drainage'),
)

BATHINGFACILITY_CHOICES = (
    ('1','YES, Bathroom'),
    ('2','YES, Enclosure without roof'),
    ('3','NO'),
)

RADIO_CHOICES = (
    ('1','YES, Traditional radio set'),
    ('2','YES, on mobile/smartphone'),
    ('3','YES, On any other device'),
    ('4','NO'),
)

TELEVISION_CHOICES = (
    ('1','YES, Doordarshan free dish'),
    ('2','YES, DTH/Dish'),
    ('3','YES, Cable connection'),
    ('4','Any other'),
    ('5','NO'),
)

INTERNET_CHOICES = (
    ('1','YES, On laptop/computer'),
    ('2','YES, On mobile/smartphone'),
    ('3','YES, On any other device'),
    ('4','NO'),
)

DEVICE_CHOICES = (
    ('1','YES'),
    ('2','NO'),
)

PHONE_CHOICES = (
    ('1','YES, Landline only'),
    ('2','YES, Mobile only, Smartphone'),
    ('3','YES, Mobile only, Other basic mobile'),
    ('4','YES, Both'),
    ('5','No'),
)

TWOWHEELER_CHOICES = (
    ('1','Bicycle'),
    ('2','Scooter/ Motorcycle/ Moped'),
    ('3','Both'),
    ('4','None'),
)

FOURWHEELER_CHOICES = (
    ('1','YES'),
    ('2','NO'),
)

CEREAL_CHOICES = (
    ('1','Rice'),
    ('2','Wheat'),
    ('3','Jowar'),
    ('4','Bajra'),
    ('5','Maize'),
    ('6','Any other'),
)

class houselisting(View):

    def get(self, request, template_name='houselisting.html'):
        return render(request, 'houselisting.html')

    def post(self, request, template_name='houselisting.html'):
        BuildingNo = request.POST.get('BuildingNo')
        CensusHouseNo = request.POST.get('CensusHouseNo')
        FloorMaterial = request.POST.get('FloorMaterial')
        WallMaterial = request.POST.get('WallMaterial')
        RoofMaterial = request.POST.get('RoofMaterial')
        UseOfHouse =request.POST.get('UseOfHouse')
        TotalResidents = request.POST.get('TotalResidents')
        HeadName = request.POST.get('HeadName')
        HeadSex = request.POST.get('HeadSex')
        HeadCaste = request.POST.get('HeadCaste')
        Ownership = request.POST.get('Ownership')
        DwellingRooms = request.POST.get('DwellingRooms')
        MarriedCouples = request.POST.get('MarriedCouples')
        DrinkingWaterSource = request.POST.get('DrinkingWaterSource')
        DrinkingWaterAvail = request.POST.get('DrinkingWaterAvail')
        LightingSource = request.POST.get('LightingSource')
        LatrineAccess = request.POST.get('LatrineAccess')
        LatrineType = request.POST.get('LatrineType')
        WasteWaterOutlet = request.POST.get('WasteWaterOutlet')
        BathingFacility = request.POST.get('BathingFacility')
        Kitchen = request.POST.get('Kitchen')
        KitchenFuel = request.POST.get('KitchenFuel')
        Radio = request.POST.get('Radio')
        Television = request.POST.get('Television')
        Internet = request.POST.get('Internet')
        ComputingDevice = request.POST.get('ComputingDevice')
        Phone = request.POST.get('Phone')
        TwoWheeler = request.POST.get('TwoWheeler')
        FourWheeler = request.POST.get('FourWheeler')
        Cereal = request.POST.get('Cereal')
        ContactNo = request.POST.get('ContactNo')

        house = HouseListing(
        BuildingNo = BuildingNo,
        CensusHouseNo = CensusHouseNo,
        FloorMaterial = FloorMaterial,
        WallMaterial = WallMaterial,
        RoofMaterial = RoofMaterial,
        UseOfHouse = UseOfHouse,
        TotalResidents = TotalResidents,
        HeadName = HeadName,
        HeadSex = HeadSex,
        HeadCaste = HeadCaste,
        Ownership = Ownership,
        DwellingRooms = DwellingRooms,
        MarriedCouples = MarriedCouples,
        DrinkingWaterSource = DrinkingWaterSource,
        DrinkingWaterAvail = DrinkingWaterAvail,
        LightingSource = LightingSource,
        LatrineAccess = LatrineAccess,
        LatrineType = LatrineType,
        WasteWaterOutlet = WasteWaterOutlet,
        BathingFacility = BathingFacility,
        Kitchen = Kitchen,
        KitchenFuel = KitchenFuel, 
        Radio = Radio,
        Television = Television,
        Internet = Internet,
        ComputingDevice = ComputingDevice,
        Phone = Phone,
        TwoWheeler = TwoWheeler,
        FourWheeler = FourWheeler,
        Cereal = Cereal,
        ContactNo = ContactNo,
        )
        house.save()

        return render(request, 'houselisting.html')