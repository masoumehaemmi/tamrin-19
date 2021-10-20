array = []
leng= int(input("enter your lenght array : "))
for i in range(leng):
    count = int(input("Enter your number: "))
    array.append(count)

tagharon = len(array)//2

if len(array) % 2 == 0:
    first = array[:tagharon]
    second = array[tagharon:]
else:
    first = array[:tagharon]
    second = array[tagharon +1:]

second.reverse()
if first == second:
    
    print("This is tagharon array")
else:
    print("This is not tagharon array")