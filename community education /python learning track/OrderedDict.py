from collections import OrderedDict
N = int(input())
dic = OrderedDict()
for i in range(N):
    item_name, item_price = input().rsplit(" ", 1)  
    dic[item_name] = dic.get(item_name,0)
    dic[item_name] += int(item_price)
  
for item_name, net_price in dic.items():
    print(f"{item_name} {net_price}")
