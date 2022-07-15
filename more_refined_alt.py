class IdkMoveZero():
    def __init__(self):
        self.a = [] 
        self.b = []  

    def list_zero(self, x):
        for i in x:
            if i == 0:
                self.a.append(i)
        for e in x:
            if e != 0:
                self.b.append(e)
        #return self.b
    
    def combine_lists(self):
        self.c = self.b + self.a
        return self.c
#x = [0, 1, 0, 3, 12]
idk = IdkMoveZero()
def main():
    idk.list_zero([0, 1, 0, 3, 12])
    #print(idk.other_nums([0, 1, 0, 3, 12]))
    print(idk.combine_lists())
    #return idk.list_zero([1,2,3,4,5,6,0,0,0])
    #return idk.combine_lists([1,2,3,4,5,6,0,0,0])
main()