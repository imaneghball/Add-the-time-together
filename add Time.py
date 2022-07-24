class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
        self.H=3600*self.h
        self.M=self.m*60
        self.res=self.H+self.M+self.s
    def __add__(self, other):
        result=self.res+other.res
        H=int(result/3600)
        M=int((result%3600)/60)
        S=result-((H*3600)+M*60)
        return f"{H}:{M}:{S}"
    def __sub__(self, other):
        if self.res<other.res:
            return 0.0
        result=self.res-other.res
        H = int(result / 3600)
        M = int((result % 3600) / 60)
        S = result - ((H * 3600) + M * 60)
        return f"{H}:{M}:{S}"


t1=Time(13,40,50)
t2=Time(17,30,40)
t3=Time(10,50,55)
print(t1.__add__(t2))
print(t1.__sub__(t2))
print(t1.__sub__(t3))