
list = ['lesslesser', 'form', 'slave', 'mount', 'trouble']


for iter_num in range(len(list)-1,0,-1):
  for idx in range(iter_num):
     if len(list[idx])>len(list[idx+1]):
        temp = list[idx]
        list[idx] = list[idx+1]
        list[idx+1] = temp
print(list)

