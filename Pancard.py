">>>>>! PAN-CARD NUMBER !<<<<<"

import random

import string
def pan() :

   samp_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
   ran_str = "".join((random.choice(samp_str)) for x in range(5)) 

   ran_int  = random.randrange(1000, 10000, 4)

   samp_str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

   ran_str1 = "".join((random.choice(samp_str1)) for x in range(1)) 

   print("YOUR RANDOM PAN NO IS >>" ,ran_str+str(ran_int)+ran_str1)

pan()








