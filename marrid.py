import random 

girl = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
boy = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']

random.shuffle(girl) 
random.shuffle(boy) 

for i in range(len(boy)):
    
    print(girl[i] , "&" , boy[i])        


    