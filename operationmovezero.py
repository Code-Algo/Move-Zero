class MoveZero:
    def move_zero(self, x):
        if len(x) == 0:
            return []
        y = 0
        for i in range(len(x)):
            if x[i] != 0:
                x[y] = x[i]
                y+=1
        for z in range(y,len(x)):
            x[z] = 0
        return x

end_zed = MoveZero()
x = [0, 1, 0, 3, 12]
print(end_zed.move_zero(x))

