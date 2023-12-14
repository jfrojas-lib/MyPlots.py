# MyPlots.py
---
The module consists of a set of mnemonic functions to quickly build function and data graphs using lists and arrays or explicit functions (library or user-defined).
The user can define whether each plotting action is performed in a separate window or in the same and can change the color, marker, style, and line type each time with explicit functions for each case.
--
---
# General characteristics: 
--
* First argument is Y axis: the function or object to be plotted so that Plot(sin) will make a graph of sin(x) function for the interval [0,10] by default. Plot(sin,[.pi,2*pi]) do it in this interval and Plot(sin,[.pi,2*pi],500) make same plot with 500 points.
* All this with the line style and/or markers defined by user: setLineStyle("-") or setLineStyle(0) are equivalent, same as setPointStyle(0) or setPointStyle(".") (see constants below)
---

# Some functions:
---

def setSameFigure(same=True):   defines if yes or no to use same window on each plot calling

def NextFigure():  create or move to next figure window

def setFixedAxis(same=True):

def setColor(c):  define default color for lines/markers

def Color():  returns actual color

def setPointStyle(ps):

def setPointStyleL(ps):

def setLineStyle(ps):

def setLineWidth(linew):

def setStyle(st):

def resetPointStyles():

def resetLineStyle():

def resetStyle():

def resetLineWidth():

def setTitle(sss):

def PLS():

def PS():

def PSL():

def LS():

def LW():

def TextXY(str,x=1,y=1,ang=0,size=10):

def resetAll():

def Status():

def form(minum,dec=3,len=0):

def Box(x1,x2,y1,y2,z1=None,z2=None):

def ImShow(F,x=[0,1],y=[0,1],tit="ImShow",xlab="x",ylab="y",cbar=True):

def ImShowC(F,x=[0,1],y=[0,1],tit="ImShowC",xlab="x",ylab="y",cbar=True):

def MatShow(x,y,F,cbar=True):

def Plot(F,x=[],tit="Plot",xlab="X",ylab="Y"):

def HorizLine(y):

def VertLine(x):

def PlotLine(F,x=[],tit="PlotLine",xlab="X",ylab="Y"):

def PlotColorPoints(P,tit="Cartesian Points",xlab="A",ylab="B",fm="o"):

def PlotPoints(P,tit="Cartesian Points",xlab="A",ylab="B",fm="o-"):

def Histogram_(Z,bins=10,tit="Plot",xlab="X",ylab="Y"):

def AnimateBox(x1,x2,y1,y2):

def AnimatePlot(x,F,tit="Plot",xlab="X",ylab="Y"):

def AnimatePlotLine(P,tit="PlotLine",xlab="X",ylab="Y"):

def AnimatePlotPoints(P,t=0.1,tit="PlotPoints",xlab="X",ylab="Y"):

def AnimatePP(P,tit="PlotPoints",xlab="X",ylab="Y"):

def status(s):

def Plot3D(x,y,z,tit="Plot3D",xlab="X",ylab="Y",zlab="Z"):

def Plot3D(P,tit="Plot3D",xlab="X",ylab="Y",zlab="Z"):

def Plot3DPoints(x,y,z,tit="Plot3D",xlab="X",ylab="Y",zlab="Z"):

def Plot3DPoints(P,tit="Plot3D",xlab="X",ylab="Y",zlab="Z"):

def Plot3DLine(x,y,z,tit="Plot3DLine",xlab="X",ylab="Y",zlab="Z"):

def Plot3DLine(P,tit="Plot3DLine",xlab="X",ylab="Y",zlab="Z"):

def Plot3DVector(From,To,tit="3D Vectors",xlab="x",ylab="y",zlab="z"):

def WireFrame(F,x=[0,1],y=[0,1],tit="WireFrame",xlab="x",ylab="y",zlab="z"):

def Surface(F,x=[0,1],y=[0,1],tit="Surface",xlab="x",ylab="y",zlab="z"):

def Bar3D(x,y,z,tit="Bar3D",xlab="x",ylab="y",zlab="z"):

def Contour(x,y,F,tit="Contour",xlab="x",ylab="y",zlab="z"):

def SavePlot(MyFig,filename):

def CloseAll():

def AnimateXY(x,y,step,fig=None,iter=None):
   
def AnimateXYZ(x,y,z,step,fig=None):

def Animate(P,step,fig=None):

def AnimateArray(qq,step,fig=None):
   
def AnimateArrayC(qq,step,fig=None):
   
def UpDataArray(qq):

def UpDataXY(x,y):

def UpDataXYZ(x,y,z):

   # from Array4
   export Pareto
   export linspace
   export meshgrid
   export meshgrid2
   export meshgrid3

   # from PyPlot
   export ion
   export ioff
"""

MyFigure = 0
SameFigure = False
FixedAxis = False
Ax,AnimAx,AnimPlot,Fig,LineAnim,Func = 0, 0, 0, 0, 0, 1
TheColors = "0123456789abcdef"
MyColor = "random"
ThePointStyles = ".,o^v<>12345678spPhH*+xXdD|_"
TheLineStyles = ['-', '--', '-.', ':', '',]
TheStyles = ["bmh","classic","fast","grayscale"]
InitPoint = "k."
LineWidth = 1.0
MarkerSize = 5 
IsTheFirst = True
Animate = False
Xle,Xri,Yup,Ydn = 0,0,0,0
AnimateBoxDefined = False
PointStyle = "o"
PointStyleL = ""
LineStyle = "-"
Style = "classic"

ion()
style.use("bmh")
