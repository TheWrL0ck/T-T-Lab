class IntList():
    def __init__(self,l1):
        self.List=l1
        print("Normal List",self.List)
class SortedIntList(IntList):
    def __init__(self,n):
        super().__init__(n)
    def sort(self,l):
            self.List.append(l)
            self.List.sort()
            print("Sorted List: ",self.List)

            
l=SortedIntList([1,6,5,7,9,3,2,4])
l.sort(8)