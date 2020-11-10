import csv
from matplotlib import pyplot as pp
from datetime import datetime as ti
class Search():
    def __init__(self,f):
        self.f=f
    def process(self,f):
        reader = csv.reader(f)
        r_row = next(reader)
        for i,j in enumerate(r_row):
            print(str(i),j)
        return reader
    def add_list(self):
        mean = []
        date = []
        high = []
        reader=self.process(f)
        for i in reader:
            try:
                yy=ti.strptime(i[0],"%Y-%m-%d")
                ii=int(i[1])
                ib=int(i[3])

            except ValueError:
                print("missing ",yy)
            else:
                mean.append(ii)
                date.append(yy)
                high.append(ib)

        return mean,date,high

    def write_it(self):
        mean=[];date=[];high=[]
        mean,date,high=self.add_list()
        fi=pp.figure(dpi=166,figsize=(10,6))
        pp.plot(date,mean,linewidth=1,c="red",alpha=0.5)
        pp.plot(date,high,linewidth=1,c="gold",alpha=0.5)
        pp.fill_between(date,mean,high,facecolor="blue",alpha=0.5)
        fi.autofmt_xdate()
        pp.xlabel("date",fontsize=12)
        pp.ylabel("the mean temparature",fontsize=1,color="yellow")
        pp.title("temparature of the days")
        pp.tick_params(axis="both",which="major",labelsize=7)
        pp.show()
with open("weather2.csv") as f:
    read=csv.reader(f)

    search=Search(f)
    search.write_it()
