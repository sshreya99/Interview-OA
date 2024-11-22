# https://leetcode.com/discuss/interview-question/6068670/Amazon-OA-Questions-with-explainations
#0(n)
package_weight = [2,4,6,6,4,2,4]

def countTrips(package_weight):
    dic = {}
    total = 0
    
    for i in package_weight:
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] = 1
    
    for i in dic:
        if dic[i] % 3 == 0:
            total = total + dic[i] // 3
        elif dic[i] % 2 == 0:
            total = total + dic[i] // 2
            
    return total    
    
    
package_weight = [2,4,6,6,4,2,4,4,4]  
print(countTrips(package_weight))
