import os
import time as t
import pywhatkit as messenger
import pyautogui as cur



def start_approval(schedule_time,phonenumber,message):
    while True:
        time=t.localtime()
        if time.tm_hour == schedule_time[0] and time.tm_min == schedule_time[1] :
            return True
        else:
            os.system('clear')
            print("====================================================================================")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-𝕎𝕙𝕒𝕥𝕤𝕒𝕡𝕡 𝕄𝕖𝕤𝕤𝕒𝕘𝕖 𝕊𝕔𝕙𝕖𝕕𝕦𝕝𝕖𝕣*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("====================================================================================")
            print("\n\t\t\tLocal Time : ",time.tm_hour," : ",time.tm_min," : ",time.tm_sec)
            print("\n\t\t\tLocal Date : ",time.tm_mday," - ",time.tm_mon," - ",time.tm_year)
            print("\n\t\t\tPhone Number : ",phonenumber)
            print("\n\t\t\tMessage : ",message)
            print("\n\t\t\tScheduled Time : ",schedule_time[0]," : ",schedule_time[1]," : 00")
            # if(schedule_time[0]==time.tm_hour):
            #     print("\n\t\t\tTime remaining : ",abs(schedule_time[0]-time.tm_hour)," : ",abs(schedule_time[1]-time.tm_min-1)," : ",abs(59-time.tm_sec))
            # else:
            #     if(schedule_time[0]>time.tm_hour): 

            #         print("\n\t\t\tTime remaining : ",abs(schedule_time[0]-time.tm_hour-1)," : ",abs(60-schedule_time[1]-time.tm_min)," : ",abs(59-time.tm_sec))
            #     else:
            #         print("\n\t\t\tTime remaining : ",abs(schedule_time[0]-time.tm_hour-1)," : ",abs(schedule_time[1]-time.tm_min)," : ",abs(59-time.tm_sec))

            difftime=((schedule_time[0]*60*60)+(schedule_time[1]*60))-((time.tm_hour*60*60)+(time.tm_min*60)+time.tm_sec)
            
            if(difftime<0):
                 print("====================================================================================")
                 print("\n\t\t\tCan't send a message to past : (\n")
                 print("====================================================================================")
                 exit()

            print("\n\t\t\t\t",difftime ," Seconds left for task")
            print("====================================================================================")

            t.sleep(1)

def sleep_sequence():
    with cur.hold("win"):
            cur.press("d")

    t.sleep(1)
    
    with cur.hold("alt"):
            with cur.hold("fn"):
                cur.press("f4")

    t.sleep(0.3)

    cur.press('up', presses=2)
    cur.press("enter")


     
print("\n\n")
print("====================================================================================")
print("-*-*-*-*-*-*-*-*-*-*-*-*-𝕎𝕙𝕒𝕥𝕤𝕒𝕡𝕡 𝕄𝕖𝕤𝕤𝕒𝕘𝕖 𝕊𝕔𝕙𝕖𝕕𝕦𝕝𝕖𝕣*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("====================================================================================")

print("\t\t",end="")
phone_num=input("Enter phone number (with country code): ")
print("\t\t",end="")
msg=input("Enter message : ")
print("\t\t",end="")
schedule_time=list(map(int,input("Enter schedule time (HH MM -- 24Hrs Format) : ").split()))
res=input("Do you want to sleep the device after completing the task (y/n): ")
res=res.upper()

print("====================================================================================")



if start_approval(schedule_time,phone_num,msg)==True:

        messenger.sendwhatmsg_instantly(phone_num,msg)

        cur.press("enter")
        t.sleep(3.5)

        with cur.hold("ctrl"):
            cur.press("w")

        t.sleep(0.3)

        print("====================================================================================")
        print("Message Sent....✅")
        print("====================================================================================")
        t.sleep(2)

        if res=="Y":
            for sec in range(10,-1,-1):
                print("Sleeping in ",sec,"Seconds")
                t.sleep(1)
            print("====================================================================================")

            sleep_sequence()