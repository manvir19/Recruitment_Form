
from django.http import HttpResponse
from django.shortcuts import redirect , render
from .models import Participant
# from django.contrib import messages
import csv
# Create your views here.
import requests
sheetly_header={
    "Authorization": "Bearer gffgfgfggff"
    }
sheetly_endpoint="https://api.sheety.co/78eda28988cc9dbe69ca0a6bb25df255/work/sheets"


all_participants= Participant.objects.all
def home(request):
    return render(request , 'home.html' , {'all':all_participants})

def come(request):
    
    if request.method == "POST" :
        
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        q6 = request.POST['q6']
        q7 = request.POST['q7']
        q8 = request.POST['q8']
        
        
        data=Participant.objects.create(
        q1=q1,
        q2=q2,
        q3=q3,
        q4=q4,
        q5=q5,
        q6=q6,
        q7=q7,
        q8=q8,
        
        
        )
        data.save()
        with open('participants1.csv', 'a', newline='') as csvfile:                 
                    spamwriter= csv.writer(csvfile, delimiter=' ',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    data1=[q1,q2,q3,q4,q5,q6,q7,q8]
    
                    spamwriter.writerow(data1) 



        sheetly_params = {
        "sheet": {
            "name":q1,
            "rollno":q2,
            "phone":q3,
            "email":q4,
            "dayscholarorhosteler":q5,
            "knowvirsa":q6,
            "joinvirsa":q7,
            "contibutevirsa":q8,
            
            
            
             
        }
        }
        
        response = requests.post(url=sheetly_endpoint, json=sheetly_params, headers=sheetly_header)
        return render(request,'thankyou.html')     
    return render(request , 'come.html')





















# data=Participant.objects.create(
        # name=name,
        # branch=branch,
        # email =email,
        # roll= roll,
        # phone=phone,
        # subit=subit
        # )
        # data.save()
        # form.save()



# context={ 'name':name,
        #      'branch':branch,
        #      'email' :email,
        #      'roll': roll,
        #       'phone':phone,
        #       'subit':subit
        #      }




  
        # if form.is_valid():
        #     form.save()
            
        #     with open('participants.csv', 'w', newline='') as csvfile:
        #             spamwriter = csv.writer(csvfile, delimiter=' ',
        #                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
                       
        #             spamwriter.writerow(['name','branch','email','roll','phone','subit'])
        #             m_feilds=all_participants.values_list('name','branch','email','roll','phone','subit')
        #             for Participant in m_feilds:
        #                 spamwriter.writerow(Participant)      
        