class Solution:

    # in the same loop!! no need to set two map
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for s in strs:
            count=[0]*26 #an array to store the num of each char eg: a==1 b==4
            for char in s: #each char in s
                count[ord(char)-ord('a')]+=1 # eg: count[3]+=1
            key= tuple(count) #change to tuple
            if key not in map:
                map[key] = [] #first give a space!!!!!!
            map[key].append(s) #no matter key in map or not
        return list(map.values()) 