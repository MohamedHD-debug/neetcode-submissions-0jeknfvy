class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        for string in s :
            if string in s_dic:
                s_dic[string] += 1
            else:
                s_dic[string] = 1

        for string in t :
            if string in s_dic:
                s_dic[string] -= 1
            else :
                return False

        return (all(v == 0 for v in s_dic.values()))

        
        