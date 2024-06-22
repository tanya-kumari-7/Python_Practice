# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:47:40 2024

@author: user
"""

# =============================================================================
'''
Sample_list=[2,5,df,good,great,awesome,hero,006,007,wonderful,ff]
	1.iterate over a list change the 4th and 6th index value.
	done
    2.remove 10th index value(write in try and except and print msg as if 10th index value is not there and print e too.)
	3.append new value
	4.check the new value index
	5.loop over all the data in the list and concat gaurav in every 3rd elements.
	6.Remove all the elements which has any numerical value(09_xx)
	7.append 4th elements  with string as tanya
	8.count number of elements which keyword as tanya and as gaurav and return the value as dict
	for all the above steps return the value as dict for example
	dic{
		step1:output of step 1
		step2:output od step 2
	}
 
'''
# =============================================================================
sample_list=[2,5,'df','good','great','awesome','hero',6,7,'wonderful','ff']

step1_output=sample_list.copy()

# =============================================================================
# Iterate over a list change the 4th and 6th index value.
# =============================================================================
for index,value in enumerate(step1_output):
    if index == 4:
        # print(value)
        value2=f'{value}_changed'
        # print(value2)
        step1_output[index]=value2
    if index==6:
        # print(value)
        value2==f'{value}_changed'
        # print(value2)
        step1_output[index]=value2
        
print(step1_output)

# =============================================================================
#  2.Remove 10th index value(write in try and except and print 
# msg as if 10th index value is not there and print e too.)
# =============================================================================
step2_output=step1_output.copy()
try:
    for index, value in enumerate(step2_output):
        if index==10:
            print(f'remove {value}')
            step2_output.remove(value)
            
except Exception as e:
    print(f'index value error {e}')
            

print(step2_output)
    
    

# =============================================================================
# 3.append new value
# =============================================================================
step3_output=step2_output.copy()
step3_output.append('GauravTanya')

print(step3_output)

# =============================================================================
# 4.check the new value index
# =============================================================================
for index,value in enumerate(step3_output):
    if value == 'GauravTanya':
        # print(index)
        step4_output=index
    
print(step4_output)

# =============================================================================
# 5.loop over all the data in the list and concat gaurav in every
 # 3rd elements.
# =============================================================================
step5_output=step3_output.copy()

for index,value in enumerate(step5_output):
    if index % 3==0:
        print (index)
        step5_output[index]=f'{value}_Gaurav'


# =============================================================================

# 6.Remove all the elements which has any numerical value(09_xx)

# =============================================================================
step6_output=step5_output.copy()


for x in step6_output:
    x1=str(x)
    if type(x)==int:
        step6_output.remove(x)
    if x1[0].isdigit():
        print(x1)
        step6_output.remove(x)
    
        
# =============================================================================
# 7.append 4th elements  with string as tanya   
# =============================================================================

step7_output=step6_output.copy()

for index,value in enumerate(step7_output):
    if index==4:
        step7_output[index]=f'{value}_Tanya'
print(step7_output)

# =============================================================================
# 8.count number of elements which keyword as tanya and as gaurav 
# and return the value as dict
# =============================================================================

dict_of_count={}
count_of_tanya=0
count_of_gaurav=0

for x in step7_output:
    if 'tanya' in x.lower():
        count_of_tanya+=1
    if 'gaurav' in x.lower():
        count_of_gaurav+=1
dict_of_count['Tanya']=count_of_tanya
dict_of_count['Gaurav']=count_of_gaurav
    



steps_dic={
    "Output of step1" :step1_output,
    "Output of step2": step2_output,
    "Output of step3": step3_output,
    "Output of step4": step4_output,
    "Output of step5": step5_output,
    "Output of step6": step6_output,
    "Output of step7": step7_output,
    "Output of step8":dict_of_count
    }

#for index,value in enumerate(sample_list):
#   print(index,value)