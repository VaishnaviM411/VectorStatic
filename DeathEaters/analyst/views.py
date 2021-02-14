from django.shortcuts import render
from django.views.generic.base import View
from surveyor.views import HouseListing
from surveyor.views import HouseHolds
from django.http import HttpResponsePermanentRedirect ,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def isAnalyst(group_name):
    if group_name == 'analyst_group':
        return 1
    else:
        return 0

q1 ={}
q2 ={}


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
            # workedAs = request.POST.get('workedAs')
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
            if fname != 'ALL': 
                args['fname'] =  fname
            if mname != 'ALL': 
                args['mname'] = mname  
            if lname != 'ALL': 
                args['lname'] =   lname
            if state != 'ALL': 
                args['state'] =  state
            if district  != 'ALL': 
                args['district'] = district 
            if subDistrict  != 'ALL': 
                args['subDistrict'] = subDistrict
            if village!= 'ALL':  
                args['village'] = village  
            if wardNo != 'ALL': 
                args['wardNo'] =wardNo  
            if adhar != 'ALL': 
                args['adhar'] =adhar  
            if sex != 'ALL':
                args['sex'] =  sex
            if dob  != 'ALL': 
                args['dob'] =dob  
            if age != 'ALL': 
                args['age'] = age 
            if religion != 'ALL':
                args['religion'] =religion   
            if scst != 'ALL':
                args['scst'] = scst 
            if scstType != 'ALL': 
                args['scstType'] =  scstType
            if martialStatus != 'ALL': 
                args['martialStatus'] =  martialStatus
            if disability!= 'ALL': 
                args['disability'] =  disability
            if motherTongue != 'ALL': 
                args['motherTongue'] = motherTongue  
            if literate != 'ALL': 
                args['literate'] = literate 
            if statusOfAttendance != 'ALL': 
                args['statusOfAttendance'] =  statusOfAttendance
            if highestEDUAttained != 'ALL': 
                args['highestEDUAttained'] = highestEDUAttained 
            if workedLike != 'ALL': 
                args['workedLike'] =  workedLike
            # if workedAs != 'ALL':  
            #     args['workedAs'] = workedAs  
            if describeWork != 'ALL':  
                args['describeWork'] = describeWork 
            if industryType!= 'ALL': 
                args['industryType'] = industryType  
            if workerClass != 'ALL':  
                args['workerClass'] = workerClass 
            if nonWorkerType != 'ALL':  
                args['nonWorkerType'] = nonWorkerType 
            if findingWork != 'ALL': 
                args['findingWork'] =  findingWork 
            if disOfTravelInKm != 'ALL': 
                args['disOfTravelInKm'] = disOfTravelInKm  
            if modeOfTravel != 'ALL': 
                args['modeOfTravel'] =  modeOfTravel 
            if birthPlace != 'ALL': 
                args['birthPlace'] =  birthPlace 
            if birthPlaceBool != 'ALL': 
                args['birthPlaceBool'] = birthPlaceBool  
            if placeOfLastResidence != 'ALL': 
                args['placeOfLastResidence'] = placeOfLastResidence  
            if placeOfLastResidenceBool != 'ALL':
                args['placeOfLastResidenceBool'] =  placeOfLastResidenceBool
            if lastMigrated != 'ALL': 
                args['lastMigrated'] =  lastMigrated
            if cameFrom != 'ALL': 
                args['cameFrom'] =  cameFrom
            if durOfStayAfterMigration != 'ALL': 
                args['durOfStayAfterMigration'] = durOfStayAfterMigration 
            if curChildren != 'ALL': 
                args['curChildren'] =  curChildren
            if totChildren!= 'ALL': 
                args['totChildren'] = totChildren

            q1 = args 
            return redirect('analyst:houseHoldQueryResult')
        

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
        
        group = request.user.groups.all()[0].name
        if isAnalyst(group) == 0:
            return render(request, 'login.html')
        state = request.POST.get('state')
        district  = request.POST.get('district')
        subDistrict  = request.POST.get('subDistrict')
        village  = request.POST.get('village')
        wardNo = request.POST.get('wardNo') 
        
        FloorMaterial = request.POST.get('FloorMaterial')
        # 
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
        # print(state)
        # if state != 'ALL':
        #     query['state']=state

        # print(state)
        # print(query['state'])

        # if district != 'ALL':
        #     query['district']=district
        # if village != 'ALL':
        #     query['village']=village
        # if wardNo != 'ALL':
        #     query['wardNo']=wardNo
        # if subDistrict != 'ALL':
        #     query['subDistrict']=subDistrict
        if FloorMaterial != 'ALL':
            query['FloorMaterial']=FloorMaterial
        if WallMaterial != 'ALL':
            query['WallMaterial']=WallMaterial
        if RoofMaterial != 'ALL':
            query['RoofMaterial']=RoofMaterial
        if TotalResidents != '-1':
            query['TotalResidents']=TotalResidents
        if UseOfHouse !='ALL':
            query['UseOfHouse']=UseOfHouse
        if HeadSex != 'ALL':
            query['HeadSex']=HeadSex
        if HeadCaste != 'ALL':
            query['HeadCaste']=HeadCaste
        if Ownership != 'ALL':
            query['Ownership']=Ownership
        if DwellingRooms != '-1':
            query['DwellingRooms']=DwellingRooms
        if MarriedCouples != '-1':
            query['MarriedCouples']=MarriedCouples
        if DrinkingWaterSource != 'ALL':
            query['DrinkingWaterSource']=DrinkingWaterSource
        if LightingSource != 'ALL':
            query['LightingSource']=LightingSource
        if LatrineAccess != 'ALL':
            query['LatrineAccess']=LatrineAccess
        if LatrineType != 'ALL':
            query['LatrineType']=LatrineType
        if WasteWaterOutlet != 'ALL':
            query['WasteWaterOutlet']=WasteWaterOutlet
        if BathingFacility != 'ALL':
            query['BathingFacility']=BathingFacility
        if Kitchen != 'ALL':
            query['Kitchen']=Kitchen
        if KitchenFuel != 'ALL':
            query['KitchenFuel']=KitchenFuel
        if Radio != 'ALL':
            query['Radio']=Radio
        if Television != 'ALL':
            query['Television']=Television
        if Internet != 'ALL':
            query['Internet']=Internet
        if ComputingDevice != 'ALL':
            query['ComputingDevice']=ComputingDevice
        if Phone != 'ALL':
            query['Phone']=Phone
        if TwoWheeler != 'ALL':
            query['TwoWheeler']=TwoWheeler
        if FourWheeler != 'ALL':
            query['FourWheeler']=FourWheeler
        if Cereal != 'ALL':
            query['Cereal']=Cereal
        
        q2 = query 
        # print(query)
        # result = HouseListing.objects.filter(**query)
        # print(result)

        return redirect('analyst:houseListQueryResult')


class houseHoldQueryResult(View):
    def get(self,request, template_name='houseHoldQueryResult.html'):
        group = request.user.groups.all()[0].name
        if isAnalyst(group) == 0:
            return render(request, 'login.html')

        try:
            result = HouseHolds.objects.filter(**q1)
            totalResult = len(result)
        except:
            result = None
            totalResult = 0
        argss = {}

        argss["result"]=result
        argss["totalResult"]=totalResult

        return render(request, 'houseHoldQueryResult.html',argss)




class houseListQueryResult(View):
    def get(self, request, template_name='analyst/houseListQueryResult.html'):
        group = request.user.groups.all()[0].name
        if isAnalyst(group) == 0:
            return render(request, 'login.html')
        
        try:
            result = HouseListing.objects.filter(**q2)
            totalResult = len(result)
        except:
            result = None
            totalResult = 0

        argss = {}
        argss["result"]=result
        argss["totalResult"]=totalResult
        
        return render(request, 'houseListQueryResult.html',argss)



    