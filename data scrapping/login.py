'''# First, we will import the required modules  
from bokeh.plotting import figure as fig  
from bokeh.plotting import output_file as OF  
from bokeh.plotting import show  
    
# Create a file for saving the model   
OF("JTP.html")   
             
# then, we will instantiate the figure object   
graph1 = fig(title = "Pie Chart using Bokeh")   
    
# initiate the center of the pie chart  
x = 0  
y = 0  
    
# then, we will initiate the radius of the glyphs  
radius = 1  
    
# start angle values  
start_angle = [0, 1.2, 2.1,  
               3.3, 5.1]  
    
# end angle values  
end_angle = [1.2, 2.1, 3.3,  
             5.1, 0]  
    
# now, generate the color of the wedges  
color1 = ["brown", "grey", "green",  
          "orange", "red"]  
    
# now, we will plot the graph  
graph1.wedge(x, y, radius,  
            start_angle,  
            end_angle,  
            color = color1)  
    
# At last, we will display the graph  
show(graph1) 
'''
#------------------------------------------------------------------------------
data=[['prat_01234','#prat_69'],['chasma_123','#chasma_123'],['arpit_cs','arpitcs#1']]
def v2():
    def v1():
        global username
        global password
        username=input("enter your username")
        password=input("enter your password")
    v1()
    def v3():
        for i in data:
            if(username==i[0] and password==i[1]):
                print("correct username and password")
                break
            else:
                print("invalid input")
                v1()
    v3()
v2()           
            
