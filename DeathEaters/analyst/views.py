from django.shortcuts import render
from django.views.generic.base import View
from surveyor.views import HouseListing
from surveyor.views import HouseHolds
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
# Create your views here.
def isAnalyst(group_name):
    if group_name == 'analyst_group':
        return 1
    else:
        return 0


class analystPage(View):
    def get(self, request):
        try:
            group = request.user.groups.all()[0].name
            if isAnalyst(group) == 0:
                return render(request, 'login.html')
            return render(request, 'analystPage.html')
        except:
            return render(request, 'login.html')

class houseHoldQueries(View):
    def get(self, request):
        try:
            group = request.user.groups.all()[0].name
            if isAnalyst(group) == 0:
                return render(request, 'login.html')
            return render(request,'houseListQueries.html')
        except:
            return render(request,'login.html')
            
    
    def post(self,request):
        try:
            group = request.user.groups.all()[0].name
            if isAnalyst(group) == 0:
                return render(request, 'login.html')
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

            args = {}
            if fname != 'All': 
                args['fname'] =  fname
            if mname != 'All': 
                args['mname'] = mname  
            if lname != 'All': 
                args['lname'] =   lname
            if state != 'All': 
                args['state'] =  state
            if district  != 'All': 
                args['district'] = district 
            if subDistrict  != 'All': 
                args['subDistrict'] = subDistrict
            if village!= 'All':  
                args['village'] = village  
            if wardNo != 'All': 
                args['wardNo'] =wardNo  
            if adhar != 'All': 
                args['adhar'] =adhar  
            if sex != 'All':
                    args['sex'] =  sex
            if dob  != 'All': 
                args['dob'] =dob  
            if age != 'All': 
                args['age'] = age 
            if religion != 'All':
                args['religion'] =religion   
            if scst != 'All':
                    args['scst'] = scst 
            if scstType != 'All': 
                args['scstType'] =  scstType
            if martialStatus != 'All': 
                args['martialStatus'] =  martialStatus
            if disability!= 'All': 
                args['disability'] =  disability
            if motherTongue != 'All': 
                args['motherTongue'] = motherTongue  
            if literate != 'All': 
                args['literate'] = literate 
            if statusOfAttendance != 'All': 
                args['statusOfAttendance'] =  statusOfAttendance
            if highestEDUAttained != 'All': 
                args['highestEDUAttained'] = highestEDUAttained 
            if workedLike != 'All': 
                args['workedLike'] =  workedLike
            if workedAs != 'All':  
                args['workedAs'] = workedAs  
            if describeWork != 'All':  
                args['describeWork'] = describeWork 
            if industryType!= 'All': 
                args['industryType'] = industryType  
            if workerClass != 'All':  
                args['workerClass'] = workerClass 
            if nonWorkerType != 'All':  
                args['nonWorkerType'] = nonWorkerType 
            if findingWork != 'All': 
                args['findingWork'] =  findingWork 
            if disOfTravelInKm != 'All': 
                args['disOfTravelInKm'] = disOfTravelInKm  
            if modeOfTravel != 'All': 
                args['modeOfTravel'] =  modeOfTravel 
            if birthPlace != 'All': 
                args['birthPlace'] =  birthPlace 
            if birthPlaceBool != 'All': 
                args['birthPlaceBool'] = birthPlaceBool  
            if placeOfLastResidence != 'All': 
                args['placeOfLastResidence'] = placeOfLastResidence  
            if placeOfLastResidenceBool != 'All':
                    args['placeOfLastResidenceBool'] =  placeOfLastResidenceBool
            if lastMigrated != 'All': 
                args['lastMigrated'] =  lastMigrated
            if cameFrom != 'All': 
                args['cameFrom'] =  cameFrom
            if durOfStayAfterMigration != 'All': 
                args['durOfStayAfterMigration'] = durOfStayAfterMigration 
            if curChildren != 'All': 
                args['curChildren'] =  curChildren
            if totChildren!= 'All': 
                args['totChildren'] = totChildren
            queryResult = HouseListing.objects.filter(**args)
            return render(request, 'houseHoldQueries.html')
        except:
            return render(request, 'login.html')

class houseListQueries(View):

    def get(self, request):
        try:
            group = request.user.groups.all()[0].name
            if isAnalyst(group) == 0:
                return render(request, 'login.html')
            return render(request,'houseListQueries.html')
        except:
            return render(request,'login.html')


    def post(self, request):
        try:
            group = request.user.groups.all()[0].name
            if isAnalyst(group) == 0:
                return render(request, 'login.html')
            state = request.POST.get('state')
            district  = request.POST.get('district')
            subDistrict  = request.POST.get('subDistrict')
            village  = request.POST.get('village')
            wardNo = request.POST.get('wardNo') 
            
            FloorMaterial = request.POST.get('FloorMaterial')
            # print(FloorMaterial)
            # FloorMaterial = FLOOR_CHOICES[int(FloorMaterial)][1],
            
            WallMaterial = request.POST.get('WallMaterial')
            RoofMaterial = request.POST.get('RoofMaterial')
            UseOfHouse =request.POST.get('UseOfHouse')
            TotalResidents = request.POST.get('TotalResidents')
            
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
            query = {}
            if state != 'All':
                query['state']=state
            if district != 'All':
                query['district']=district
            if village != 'All':
                query['village']=village
            if wardNo != 'All':
                query['wardNo']=wardNo
            if subDistrict != 'All':
                query['subDistrict']=subDistrict
            if FloorMaterial != 'All':
                query['FloorMaterial']=FloorMaterial
            if WallMaterial != 'All':
                query['WallMaterial']=WallMaterial
            if RoofMaterial != 'All':
                query['RoofMaterial']=RoofMaterial
            if TotalResidents != 'All':
                query['TotalResidents']=TotalResidents
            if UseOfHouse !='All':
                query['UseOfHouse']=UseOfHouse
            if HeadSex != 'All':
                query['HeadSex']=HeadSex
            if HeadCaste != 'All':
                query['HeadCaste']=HeadCaste
            if Ownership != 'All':
                query['Ownership']=Ownership
            if DwellingRooms != 'All':
                query['Dwelling']=Dwelling
            if MarriedCouples != 'All':
                query['MarriedCouples']=MarriedCouples
            if DrinkingWaterSource != 'All':
                query['DrinkingWaterSource']=DrinkingWaterSource
            if LightingSource != 'All':
                query['LightingSource']=LightingSource
            if LatrineAccess != 'All':
                query['LatrineAccess']=LatrineAccess
            if LatrineType != 'All':
                query['LatrineType']=LatrineType
            if WasteWaterOutlet != 'All':
                query['WasteWaterOutlet']=WasteWaterOutlet
            if BathingFacility != 'All':
                query['BathingFacility']=BathingFacility
            if Kitchen != 'All':
                query['Kitchen']=Kitchen
            if KitchenFuel != 'All':
                query['KitchenFuel']=KitchenFuel
            if Radio != 'All':
                query['Radio']=Radio
            if Television != 'All':
                query['Television']=Television
            if Internet != 'All':
                query['Internet']=Internet
            if ComputingDevice != 'All':
                query['ComputingDevice']=ComputingDevice
            if Phone != 'All':
                query['Phone']=Phone
            if TwoWheeler != 'All':
                query['TwoWheeler']=TwoWheeler
            if FourWheeler != 'All':
                query['FourWheeler']=FourWheeler
            if Cereal != 'All':
                query['Cereal']=Cereal
            
            return HttpResponsePermanentRedirect(reverse('houseListQueryResult', args=(query,)))

        except:
            return render(request, 'login.html')

class houseHoldQueriesResult(View):
    def get(self, request,args, template_name='analyst/houseHoldQueriesResult.html'):
        print(args)
        try:
            group = request.user.groups.all()[0].name
            if isAnalyst(group) == 0:
                return render(request, 'login.html')
            result = HouseListing.objects.filter(**args)
            argss = {}
            argss["result"]=result

            return render(request, 'analyst/houseHoldQueriesResult.html',args)
        except:
            return render(request,'login.html')