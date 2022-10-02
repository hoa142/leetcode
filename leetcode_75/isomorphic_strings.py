class Solution():
    """
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters.
    No two characters may map to the same character, but a character may map to itself.
    """
    @staticmethod
    def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictionary = {}

        if len(s) != len(t):
            return False
        else:
            for index, char in enumerate(s):
                if char not in dictionary:
                    if t[index] in dictionary.values():
                        return False
                    else:
                        dictionary[char] = t[index]
                else:
                    if dictionary[char] != t[index]:
                        return False
            print(dictionary)
            return True
s = 'paper'
t = 'title'
print(Solution.isIsomorphic(s, t))
print(list(enumerate(s)))

