from math import sqrt
class Solution(object):
    def kClosest(self, points, k):
        final = []
        final2 = []
        final3 = []
        for i in range(len(points)):
            cal = sqrt((0 - int(points[i][0]))**2 + (0 - int(points[i][1]))**2)
            final.append(cal)
            final2.append([cal,points[i][0],points[i][1]])
        final2.sort()
        for j in range(k):
            final3.append([final2[j][1],final2[j][2]])
        return final3
           

            
    
        
      


                
        