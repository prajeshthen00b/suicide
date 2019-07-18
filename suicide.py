# Data Visualization of Suicide Trends between 1987 and 2014
import pandas as pd
import matplotlib.pyplot as plt
suicide = pd.read_csv(r"C:\Users\user\Desktop\Projects\Py Practice\Suicide\master.csv")
#main code block starts now
def main():
    print("Down below are the list of countries for which details are available.")
    for i in suicide['country'].unique():
        print(i)
    c = input("At first, you can select the county you want to look at the stats for:") #country
    print("Down below are the list of countries for which details are available.")
    for i in suicide['sex'].unique():
        i = i.capitalize()
        print(i)
    g = input("You can now look select the gender you want to look into:")  #gender
    o = stats(c, g)
    o.show()
    
class stats:
    def __init__(self, country, gender):
        self.c = country
        self.g = gender.lower()
        #The function below shows the details of the demography you chose
    def det(self):
        print("In",self.c,",people who had identified themselves as",self.g,"constituted for about", round((sum(suicide[suicide['sex'] == self.g]['suicides_no'][suicide['country'] == self.c])/sum(suicide['suicides_no'][suicide['country'] == self.c]))*100,2),"% of total suicides committed.")
        #Shows the dsitribution of suicides between men and women
    def show(self):
        #We want to create separate graphs for age-groups and their propensity for suicide over the years
        # X: YEAR; Y: SUICIDES
        s1 = suicide[suicide['country'] == self.c][suicide['sex'] == self.g].groupby(['year']).sum()['suicides_no']
        s1.plot(kind = 'bar')
main()
    
