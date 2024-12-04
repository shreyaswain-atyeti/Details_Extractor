import json
import re
import os

# print(os.system('dir'))
# exit()
with open('data.json','r') as json_data_ob:
    json_data=json.load(json_data_ob)




def json_processor():
    global json_data
    #print(type(json_data))
    #print(list(set(json_data)))
    unique_list=[]
    for i in json_data:
        if i not in unique_list:
            unique_list.append(i)
    
##################################################################

    new_data=[]
    for i in unique_list:
        phone=re.sub(r'[^\d]','',i['phone_number'])
        i['phone_number']=(f"({phone[:3]}) {phone[3:6]}-{phone[6:]}")
        new_data.append(i)
        #new_data.append()
    #print(new_data)
    
#####################################################################

    new_data1=[]
    for i in new_data:
        i['email']=i['email'].lower()
        new_data1.append(i)
    #print(new_data1)

######################################################################

    new_data2=[]
    for i in new_data1:
        st=''
        full_name=i['name'].split(' ')
        for j in full_name:
            j=j.capitalize()
            st=st+' '+j
        i['name']=st.strip()
        new_data2.append(i)
    #print(new_data2)

#######################################################################

    new_data3=[]
    for i in new_data2:
        nested_add=i['address'].split(',')
        i['address']={'street':nested_add[0],'city':nested_add[1],'state':nested_add[2],'zip':nested_add[3]}
        new_data3.append(i)
    #print(new_data3)
    
#######################################################################

    state_abr=[]
    for i in new_data3:
        state_abr.append(i['address']['state'])
#########################################################################
    new_data3.append({'state_abbreviation':state_abr})
    with open('cleaned_data.json','w') as json_write:
        json.dump(new_data3,json_write,indent=4)
    
    

json_processor()



    





