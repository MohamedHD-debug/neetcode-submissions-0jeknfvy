class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dictionary = {}

        for word in strs :
            sorted_word = tuple(sorted(word))
            if sorted_word not in my_dictionary:
                my_dictionary[sorted_word] = []
            my_dictionary[sorted_word].append(word)

        result = []
        for row in my_dictionary.values() :
            result.append(row)

        return result