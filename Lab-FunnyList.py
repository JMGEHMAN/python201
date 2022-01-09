"""
# Lab: Inheritance
* create a type called FunnyList which has all the chocolately goodness of a list, but adds the following wrinkle:
 * if two lists have same items but in different orders, they are considered equal
 * e.g., __`[1, 2, 3]`__ == __`[3, 1, 2]`__
"""

class FunnyList(list):
    def __eq__(self, other):
        is_match = True

        if(len(self) == len(other)):
            print("Lists are the same length")
            for item in self:
                if item not in other:

                    is_match = False

            for item in other:
                if item not in self:
                    is_match = False
        else:
            print("Lists are not the same length")
            is_match = False
        
        return is_match

        #just do: return sorted(self) == sorted(other)

list1 = [1,2,3]
list2 = [3,2,1]

flist1 = FunnyList(list1)
flist2 = FunnyList(list2)

print("Lists Equal", list1 == list2)
print("Funny Lists Equal", flist1 == flist2)