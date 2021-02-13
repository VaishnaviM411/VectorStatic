from django.shortcuts import render
from django.views.generic.base import View
from surveyor.models import HouseHolds 
from surveyor.models import HouseListing

def isSurveyor(group_name):
    if group_name == 'surveyor_group':
        return 1
    else:
        return 0

        
class surveyorPage(View):
    def get(self, request):
        try:
            group = request.user.groups.all()[0].name
            if isSurveyor(group) == 0:
                return render(request, 'login.html')
            return render(request, 'surveyorPage.html')
        except:
            return render(request, 'login.html')

        




class households(View):
    def get(self, request, template_name='household.html'):
        try:
            group = request.user.groups.all()[0].name
            if isSurveyor(group) == 0:
                return render(request, 'login.html')
            return render(request, template_name)
        except:
            return render(request, 'login.html')
        

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
        sex = SEX_CHOICES[int(sex)][1]
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




class houselisting(View):

    def get(self, request, template_name='houselisting.html'):
        try:
            group = request.user.groups.all()[0].name
            if isSurveyor(group) == 0:
                return render(request, 'login.html')
            return render(request, template_name)
        except:
            return render(request, 'login.html')

    def post(self, request, template_name='houselisting.html'):
        BuildingNo = request.POST.get('BuildingNo')
        FloorMaterial = request.POST.get('FloorMaterial')
        # print(FloorMaterial)
        # FloorMaterial = FLOOR_CHOICES[int(FloorMaterial)][1],
        CensusHouseNo = request.POST.get('CensusHouseNo')
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