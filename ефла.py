#target = 9
#nums = [2, 7, 11, 15]
#d = {}
#for i in range(len(nums)):
    #if target - nums[i] in d:
        #print(i, d[target - nums[i]])


    #d[nums[i]] = i
#s = 'anagram'
#t = 'naagram'
#print(sorted(s) == sorted(t))
#if len(s) != len(t):
    #print(False)
#d1 = {}
#d2 = {}
#for i in s:
    #if i in d1:
        #d1[i] += 1
    #else:
        #d1[i] = 1
#for i in t:
    #if i in d2:
        #d2[i] += 1
    #else:
        #d2[i] = 1
#for i in d1.keys():
    #if i not in d2.keys():
        #print(False)
    #if d2[i] != d1[i]:
        #print(False)
#print(True)
#nums1 = [1,2,2,1]
#nums2 = [2, 2]
#d1 = {}
#for i in nums1:
    #if i not in d1:
        #d1[i] = 1
    #else:
        #d1[i] += 1
#d2 = {}
#for i in nums2:
    #if i not in d2:
        #d2[i] = 1
    #else:
        #d2[i] += 1
#ans = []
#for i in d1.keys():
    #if i in d2:
        #occurens = min(d1[i], d2[i])
        #while occurens > 0:
            #ans.append(i)
            #occurens -= 1
#print(ans)
#a = [2, 3, 4, 6, 6, 7, 8, 6]
#d = {}
#for i in a:
    #if i in d:
        #d[i] += 1
    #else:
        #d[i] = 1

#ans = (-1, -1)
#for key, values in d.items():
    #if values > ans[1]:
        #ans = (key, values)
#print(ans[0])
#битовые операции = [|] & ~ << >>
#                    or
#                    1 | 1 = 1, 1 | 0 = 1, 0 | 0 = 0
#                        and
#                        0 | 0 = 0, 1 | 1 = 1, 0 | 1 = 0
#                            no[10101] =     01010
#                               ->*2
#                               0101  = 1010 -> >>1 = 1011 =
#a = [2, 3, 4, 5, 6, 6]
#import  numpy
#zerod = numpy.array([1, 1])
#random = numpy.random.random((3, 3))
#const = numpy.full((3, 3), 3)
#print(const)
#print(random)
#print(zerod.ndim)
class Node:
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self, head):
        self.head = head

    def add(self):
        new = Node(data=None)
        if (self.head):
            temp = self.head
            while (temp != None):
                temp = temp.next
            temp.next = new
        else:
            self.head = new
    def List(self, first=None):
        self.first = first
        first = self.head
        while first:
            print(first.data)
            first = first.next
