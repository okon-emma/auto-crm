import urllib.request
import time
import pywhatkit
import urllib.request


#Function to check for access
def access(url):
    try:
        urllib.request.urlopen(url, timeout=20)
        return "Okay"
    except urllib.request.URLError as err:
        return "Bad"



def notification():
    number = {"Feranmi": "+2347032366719", "Mercy":"+2348184750832",  "Jennifer":"+2348062970301", "Shogo":"+2347062706840", "Olamide":"+2347086372431"}
    url_list = {"Blue processmaker":"https://processmaker.gtbank.com/sysworkflow/en/gtbank_pro/login/login",
       "BVNPM": "https://bvnpms.gtbank.com/sys/en/neoclassic/login/login",
      "CIS PM": "https://cispm.gtbank.com/sysworkflow/en/neoclassic/login/login",
      "FX PM": "https://fxpms.gtbank.com/syssettlement/en/neolcassic/login/login",
      "Video Banking":"https://vbanking.gtbank.com/videochat",
      "SAP" : "https://sts.gtbank.com/adfs/ls/idpinitiatedsignon.aspx",
      "Ameyo" : 'https://ameyo.gtbank.com:8443/app/',
      "Lead2Loan":"https://leadtoloan.gtbank.com:7002/L2LWeb/LoginRediectServlet"}
   
   
    for name,url in url_list.items():
        if (access(url) == "Bad"):
            for nam_mob,mobile in number.items():
                hour,minute = int(time.strftime("%H")),int(time.strftime("%M")) + 1
                pywhatkit.sendwhatmsg(mobile, 'Hi ' + str(nam_mob)+ ", \n\n" + str(name) + " was down at " + str(hour) + str(minute-1),hour ,minute)
        else:
            pass
while True:
     notification()