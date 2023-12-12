

from matplotlib.pyplot import plot,imshow,\
                              contour,\
                              scatter,xticks,yticks,\
                              figure,title,xlabel,ylabel,\
                              cm,show,matshow,colorbar,axes,\
                              close,ion,ioff,legend,subplots,\
                              savefig,hist,rcParams,xlim,ylim,\
                              style,text,axhline,axvline,plot
from matplotlib.animation import FuncAnimation
import matplotlib.animation as anim
#from matplotlib import use
#use("Agg")
from mpl_toolkits.mplot3d import Axes3D
from numpy import ndarray,arange,ndim,zeros,ones,sin,exp,sqrt,\
                  pi,cos,linspace,meshgrid,linspace,transpose,\
                  array,sign
from numpy.random import randint,random,uniform
from Array4 import Pareto,Lap_5,Lap_9
from time import sleep

"""
def setSameFigure(same=True):
def NextFigure():
def setFixedAxis(same=True):
def setColor(c):
def Color():
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

def setSameFigure(same=True):
   global SameFigure,IsTheFirst,Ax,MyFigure
   SameFigure = same
   IsTheFirst, Ax = True, 0

def NextFigure(m=1):
   global SameFigure,MyFigure
   MyFigure += m
   figure(MyFigure)
   print("Figure",MyFigure)

def PrevFigure(m=1):
   global SameFigure,MyFigure
   MyFigure -= m
   figure(MyFigure)

def Figure(k=1):
   global MyFigure
   MyFigure = k
   figure(MyFigure)

def setFixedAxis(same=True):
   global FixedAxis
   FixedAxis = same

def setColor(c):
   global MyColor
   MyColor = c

def Color():
   global MyColor,TheColors
   if MyColor == "random":
      ic = TheColors[randint(0,16)] + TheColors[randint(0,16)] + TheColors[randint(0,16)]
      ic += TheColors[randint(0,16)] + TheColors[randint(0,16)] + TheColors[randint(0,16)]
      return "#" + ic
   return MyColor

def setPointStyle(ps):
   global PointStyle,PointStyleL,ThePointStyles
   if type(ps) == int: PointStyle = ThePointStyles[ps % 28]
   else: PointStyle = ps

def setPointStyleL(ps):
   global PointStyle,PointStyleL,ThePointStyles
   if type(ps) == int: PointStyleL = ThePointStyles[ps & 28]
   else: PointStyleL = ps

def setLineStyle(ps):
   global LineStyle,TheLineStyles
   if type(ps) == int: LineStyle = TheLineStyles[ps % 5]
   else: LineStyle = ps

def setLineWidth(linew):
   global LineWidth
   LineWidth = linew

def setMarkerSize(msize):
   global MarkerSize
   MarkerSize = msize

def setStyle(st):
   global Style,TheStyles
   if type(st) == int: Style = TheStyles[st % 4]
   else: Style = st
   style.use(Style)

def resetPointStyles():
   global PointStyle,PointStyleL
   PointStyle = "o"
   PointStyleL = ""

def resetLineStyle():
   global LineStyle
   LineStyle = "-"

def resetStyle():
   global Style
   Style = "classic"

def setinitPoint(s):
   global InitPoint
   InitPoint = s

def resetLineWidth():
   global LineWidth
   LineWidth = 1

def resetMarkerSize():
   global MarkerSize
   MarkerSize = 5

def PLS():
   global PointStyleL,LineStyle
   return PointStyleL+LineStyle

def PS():
   global PointStyle,LineStyle
   return PointStyle

def PSL():
   global PointStyleL,LineStyle
   return PointStyleL

def LS():
   global PointStyle,LineStyle
   return LineStyle

def LW():
   global LineWidth
   return LineWidth

def MS():
   global MarkerSize
   return MarkerSize

def TextXY(str,x=1,y=1,ang=0,size=10):
   text(x,y,str,rotation=ang,fontsize=size)

def resetAll():
   global MyFigure,SameFigure,FixedAxis,Ax,AnimAx,AnimPlot,Fig, \
          MyColor,LineWidth,IsTheFirst,Animate,Xle,Xri,Yup,Ydn, \
          AnimateBoxDefined,PointStyle,PointStyleL,LineStyle,Style
MyFigure = 0
SameFigure = False
FixedAxis = False
Ax,AnimAx,AnimPlot,Fig = 0, 0, 0, 0
MyColor = "random"
LineWidth = 1.0
IsTheFirst = True
Animate = False
Xle,Xri,Yup,Ydn = 0,0,0,0
AnimateBoxDefined  = False
PointStyle = "o"
PointStyleL = ""
LineStyle = "-"
Style = "classic"

def Status():
   global MyFigure,SameFigure,FixedAxis,Ax,AnimAx,AnimPlot,Fig, \
          MyColor,LineWidth,IsTheFirst,Animate,Xle,Xri,Yup,Ydn, \
          AnimateBoxDefined,PointStyle,PointStyleL,LineStyle,Style, \
          ThePointStyles,TheLineStyles,TheStyles   
   print("\nMyFigure: ",MyFigure, \
         "\nSameFigure: ",SameFigure,\
         "\nFixedAxis: ",FixedAxis,\
         "\nAx,AnimAx,AnimPlot,Fig: ",Ax,AnimAx,AnimPlot,Fig,\
         "\nMyColor: ",MyColor,\
         "\nLineWidth: ",LineWidth,\
         "\nIsTheFirst: ",IsTheFirst,\
         "\nAnimate: ",Animate,\
         "\nXle,Xri,Yup,Ydn (box): ",Xle,Xri,Yup,Ydn,\
         "\nAnimateBoxDefined: ",AnimateBoxDefined,\
         "\nPointStyle: ",PointStyle," of ",ThePointStyles, \
         "\nPointStyleL(ine): ",PointStyleL,\
         "\nLineStyle: ",LineStyle," of ",TheLineStyles, \
         "\nStyle: ",Style," of ",TheStyles, \
         "\nThePointStyles = ',o^v<>12345678spPhH*+xXdD|_'",\
         "\nTheLineStyles = ['-', '--', '-.', ':', '',]",\
         '\nTheStyles = ["bmh","classic","fast","grayscale"]')

def form(minum,dec=3,len=0):
   minum *= 10**dec
   minum = round(minum)
   minum /= 10**dec
   return str(minum)

def Box(x1,x2,y1,y2,z1=None,z2=None):
    global MyColor,SameFigure,MyFigure,IsTheFirst,Ax
    if MyFigure == 0:
        MyFigure += 1
    figure(MyFigure)
    col = Color()
    if z1 == None:
        plot([x1,x2],[y1,y1],PLS(),color=col,lw=LW())
        plot([x1,x2],[y2,y2],PLS(),color=col,lw=LW())
        plot([x1,x1],[y1,y2],PLS(),color=col,lw=LW())
        plot([x2,x2],[y1,y2],PLS(),color=col,lw=LW())
    else:
        if IsTheFirst:
            Ax = axes(projection="3d")
            if IsTheFirst: IsTheFirst = False
        tit = ""
        #Ax = axes(projection="3d")
        PUp = array([[x1,y1,z1],[x2,y1,z1],[x2,y2,z1],[x1,y2,z1],[x1,y1,z1]])
        x,y,z = PUp[:,0],PUp[:,1],PUp[:,2]
        Ax.plot3D(x,y,z,PLS(),label=tit,color=col,lw=LW())
        PDn = array([[x1,y1,z2],[x2,y1,z2],[x2,y2,z2],[x1,y2,z2],[x1,y1,z2]])
        x,y,z = PDn[:,0],PDn[:,1],PDn[:,2]
        Ax.plot3D(x,y,z,PLS(),label=tit,color=col,lw=LW())
        P = array([[x1,y1,z1],[x1,y1,z2]])
        x,y,z = P[:,0],P[:,1],P[:,2]
        Ax.plot3D(x,y,z,PLS(),label=tit,color=col,lw=LW())
        P = array([[x1,y2,z1],[x1,y2,z2]])
        x,y,z = P[:,0],P[:,1],P[:,2]
        Ax.plot3D(x,y,z,PLS(),label=tit,color=col,lw=LW())
        P = array([[x2,y2,z1],[x2,y2,z2]])
        x,y,z = P[:,0],P[:,1],P[:,2]
        Ax.plot3D(x,y,z,PLS(),label=tit,color=col,lw=LW())
        P = array([[x2,y1,z1],[x2,y1,z2]])
        x,y,z = P[:,0],P[:,1],P[:,2]
        Ax.plot3D(x,y,z,PLS(),label=tit,color=col,lw=LW())
        show()

def setTitle(sss):
   title(r"$"+sss+"$")
   show()

def ImShow(F,x=[0,1],y=[0,1],tit="ImShow",xlab="x",ylab="y",cbar=True):
   global MyFigure,SameFigure
   if not SameFigure:
      MyFigure += 1
   figure(MyFigure)
   if type(F) == ndarray:
      qq = F
   else:
      xx, yy = meshgrid(x,y)
      qq = F(xx,yy)
   x,y = list(x), list(y)
   if x == [0]: xticks([],[])
   else:
      if x == [1]: x = [0,qq.shape[1]]
      xinit = x[0]
      xstop = x[-1]
      xlen = xstop-xinit
      xstepsize = xlen/(5)
      xticpos = [ xt for xt in arange(0,qq.shape[1],qq.shape[1]/6) ]
      xticlab = [ form(xinit+xstepsize*i,2) for i in range(6) ]
      xticks(xticpos,xticlab)
   if y == [0]: yticks([],[])
   else:
      if y == [1]: y = [0,qq.shape[0]]
      yinit = y[0]
      ystop = y[-1]
      ylen = ystop-yinit
      ystepsize = ylen/(5)
      yticpos = [ xt for xt in arange(0,qq.shape[0],qq.shape[0]/6) ]
      yticlab = [ form(yinit+ystepsize*i,2) for i in range(6) ]
      yticks(yticpos,yticlab)
   if SameFigure: imshow(qq, cmap=cm.bone, origin="lower",alpha=0.4)
   else: imshow(qq, cmap=cm.bone, origin="lower",alpha=1)
   #plot([xinit,xstop],[yinit,ystop])
   xlabel(xlab)
   ylabel(ylab)
   title(tit)
   if cbar and not SameFigure:
      colorbar()
   show()

def ImShowC(F,x=[0,1],y=[0,1],tit="ImShowC",xlab="x",ylab="y",cbar=True):
   #x,y,F,cbar=True,tit="ImShowC",xlab="x",ylab="y"):
   global MyFigure,SameFigure
   if not SameFigure or MyFigure == 0:
      MyFigure += 1
   figure(MyFigure)
   if type(F) == ndarray:
      qq = F
   else:
      xx, yy = meshgrid(x,y)
      qq = F(xx,yy)
   if x == [0]: xticks([],[])
   else:
      if x == [1]: x = [0,qq.shape[1]]
      xinit = x[0]
      xstop = x[-1]
      xlen = xstop-xinit
      xstepsize = xlen/(5)
      xticpos = [ xt for xt in arange(0,qq.shape[1],qq.shape[1]/5) ]
      xticlab = [ form(xinit+xstepsize*i,2) for i in range(6) ]
      xticks(xticpos,xticlab)
   if y == [0]: yticks([],[])
   else:
      if y == [1]: y = [0,qq.shape[0]]
      yinit = y[0]
      ystop = y[-1]
      ylen = ystop-yinit
      ystepsize = ylen/(5)
      yticpos = [ xt for xt in arange(0,qq.shape[0],qq.shape[0]/5) ]
      yticlab = [ form(yinit+ystepsize*i,2) for i in range(6) ]
      yticks(yticpos,yticlab)
   if SameFigure: imshow(qq, origin="lower",alpha=0.4)
   else: imshow(qq, origin="lower",alpha=1.0)
   title(tit)
   xlabel(xlab)
   ylabel(ylab)
   if cbar and not SameFigure:
      colorbar()
   show()

def MatShow(x,y,F,cbar=True):
   global MyFigure,SameFigure
   if not SameFigure or MyFigure == 0:
      MyFigure += 1
   figure(MyFigure)
   if type(F) == ndarray:
      qq = F
   else:
      xx, yy = meshgrid(x,y)
      qq = F(xx,yy)
   if x == [0]: xticks([],[])
   else:
      if x == [1]: x = [0,qq.shape[1]]
      xinit = x[0]
      xstop = x[-1]
      xlen = xstop-xinit
      xstepsize = xlen/(5)
      xticpos = [ xt for xt in arange(0,qq.shape[1],qq.shape[1]/5) ]
      xticlab = [ form(xinit+xstepsize*i,2) for i in range(6) ]
      xticks(xticpos,xticlab)
   if y == [0]: yticks([],[])
   else:
      if y == [1]: y = [0,qq.shape[0]]
      yinit = y[0]
      ystop = y[-1]
      ylen = ystop-yinit
      ystepsize = ylen/(5)
      yticpos = [ xt for xt in arange(0,qq.shape[0],qq.shape[0]/5) ]
      yticlab = [ form(yinit+ystepsize*i,2) for i in range(6) ]
      yticks(yticpos,yticlab)
   if SameFigure:
      matshow(qq, cmap=cm.bone,alpha=0.4)
   else:
      matshow(qq, cmap=cm.bone,alpha=1.0)
   if cbar and not SameFigure:
      colorbar()
   show()

def Plot(F,x=[],tit="Plot",xlab="X",ylab="Y"):
      global MyFigure,SameFigure
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)

      if type(F) == ndarray: y = F        ### first check for 'Y'
      elif type(F) == list: y = array(F)
      else: 
         if len(x) == 0: x = linspace(0,10,50)
         elif len(x) == 2: x = linspace(x[0],x[1],50)
         elif len(x) == 3: x = linspace(x[0],x[1],x[2])
         else: 
            x = array(x)
         y = F(x)
      
      scatter(x,y,marker=PS(),color=Color(),label=r"$"+tit+"$")
      xlab = r"$"+xlab+"$"
      ylab = r"$"+ylab+"$"
      xlabel(xlab)
      ylabel(ylab)
      if len(tit): legend()
      show()

def HorizLine(y):
   axhline(y, color=Color(),linewidth=LW(),linestyle=LS())

def VertLine(x):
   axvline(x, color=Color(),linewidth=LW(),linestyle=LS())

def PlotLine(F,x=[],tit="PlotLine",xlab="X",ylab="Y"):
      """
      Gráfica de una sola línea:
      F puede ser una función y único argumento
      F array construye una curva por columna
      """
      global MyFigure,SameFigure
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      y,yisa = F,False
      if type(y) == ndarray: y = F.copy()        ### first check for 'Y'
      elif type(y) == list: y = array(F)
      if type(y) == ndarray: 
         np = len(y)
         yisa = True
      else: np = 50
      if type(x) == list: 
         if len(x) > 3 and yisa:
            if len(x) == len(y): x = array(x)
         if yisa and len(x) != len(y) or not yisa:
            if len(x) == 0: x = linspace(0,10,np)
            elif len(x) == 2: x = linspace(x[0],x[1],np)
            elif len(x) == 3: x = linspace(x[0],x[1],int(x[2]))
            #else: x = array(x)
      #print(x.shape,x)
      if not yisa: y = F(x)
      tit = r"$"+tit+"$"
      plot(x,y,marker=PSL(),linestyle=LS(),color=Color(),label=tit)
      #xlim(min(x),max(x))
      xlabel(r"$"+xlab+"$")
      ylabel(r"$"+ylab+"$")
      if len(tit): legend()
      show()

def PlotLines(F,x=[],tit=["PlotLines"],xlab="X",ylab="Y"):
      global MyFigure,SameFigure,MyColor
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      
      locsamefigure = SameFigure
      setSameFigure(True)
      locolor = MyColor
      setColor("random")
      if len(tit) == 1: tit_ = [tit[0]+"_"+str(i) for i in range(len(F))]
      else: tit_ = tit  ##[tit[i]+"_"+str(i) for i in range(len(F))]
      if type(F) == list: F = array(F)
      if F.shape[1] > F.shape[0]: F = transpose(F)
      #print("F",F, type(F),F.shape)
      for i in range(F.shape[1]):
         PlotLine(F=F[:,i],x=x,tit=tit_[i],xlab=xlab,ylab=ylab)
      #if len(tit): legend()
      show()
      setSameFigure(locsamefigure)
      setColor(locolor)

def PlotColorPoints(P,tit="Cartesian Points",xlab="A",ylab="B"):
      global MyFigure,SameFigure
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      P = array(list(P))
      localcolor = Color()
      Color("random")
      for i in range(len(P)):
         scatter(P[i,0],P[i,1],marker=PS(),color=Color())
      title(tit)
      xlabel(xlab)
      ylabel(ylab)
      show()
      Color(localcolor)

def PlotPoints(P,tit="Cartesian Points",xlab="A",ylab="B"):
      global MyFigure,SameFigure
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      miP = []
      for i in range(len(P)):
         miP.append(P[i])
      P = array(P)
      if len(P.shape) > 1:
         scatter(P[:,0],P[:,1],marker=PS(),color=Color())
      else:
         scatter(P[0],P[1],marker=PS(),color=Color())
      title(tit)
      xlabel(xlab)
      ylabel(ylab)
      show()

def Histogram_(Z,bins=10,tit="Plot",xlab="X",ylab="Y"):
      global MyFigure,SameFigure
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      #x = range(len(y))
      histogram(Z,bins=bins,label=tit,alpha=0.4)
      #title(tit)
      xlabel(xlab)
      ylabel(ylab)
      if len(tit): legend()
      show()

def AnimateBox(x1,x2,y1,y2):
    global Xle,Xri,Yup,Ydn,AnimateBoxDefined
    lasX = [x1,x2]
    lasY = [y1,y2]
    Xle, Xri = min(lasX), max(LasX)
    Ydn, Yup = min(lasY), max(lasY)
    AnimateBoxDefined = True

def AnimatePlot(x,F,tit="Plot",xlab="X",ylab="Y"):
      global MyFigure,SameFigure,Animate,AnimAx
      if type(F) == ndarray:
         y = F
      else:
         y = F(x)

      if not Animate:
         Fig = figure(MyFigure)
         AnimAx = Fig.add_subplot(111)
         AnimAx.set_xlim(min(x),max(x))
         AnimAx.set_ylim(min(y),max(y))
         title(tit)
         xlabel(xlab)
         ylabel(ylab)
         Animate = True
      else:
         AnimAx.set_data(x,y)
      Fig.canvas.draw()
      Fig.canvas.flush_events()
      #time.sleep(0.01)
      show()

def AnimatePlotLine(P,tit="PlotLine",xlab="X",ylab="Y"):
      global MyFigure,SameFigure,Animate,AnimAx,Fig,AnimPlot
      P = array(list(P))
      x,y = P[:,0],P[:,1]
      #LocalSameFigure = SameFigure
      #setSameFigure()
      #if not SameFigure or MyFigure == 0:
      #   MyFigure += 1
      #figure(MyFigure)
      if not Animate:
         #figure, ax = plt.subplots(figsize=(8,6))
         #line1, = ax.plot(x, y)
         Fig,AnimAx = subplots()
         #AnimAx = Fig.add_subplot(111)
         AnimAx.set_xlim(min(x),max(x))
         AnimAx.set_ylim(min(y),max(y))
         title(tit)
         xlabel(xlab)
         ylabel(ylab)
         Animate = True
         AnimPlot, = AnimAx.plot(x,y,color=Color())
      else:
         if not FixedAxis:
            AnimAx.set_xlim(min(x),max(x))
            AnimAx.set_ylim(min(y),max(y))
         AnimPlot.set_data(x,y)
      Fig.canvas.draw()
      Fig.canvas.flush_events()
      #time.sleep(0.1)
      show()

def AnimatePlotPoints(P,t=0.1,tit="PlotPoints",xlab="X",ylab="Y"):
      global MyFigure,SameFigure,Animate,Ax,Fig,AnimPlot,FixedAxis,LineAnim
      P = array(list(P))

      def UpDateLine(num):
         x,y = P[:,0],P[:,1]
         print("UpDate...",x,y)
         AnimPlot.set_data(x,y)
      
      x,y = P[:,0],P[:,1]
      if not Animate:
         #figure, ax = plt.subplots(figsize=(8,6))
         #line1, = ax.plot(x, y)
         #Fig,Ax = subplots()
         #AnimAx = Fig.add_subplot(111)
         #Ax.set_xlim(min(x),max(x))
         #Ax.set_ylim(min(y),max(y))
         Fig = figure()
         AnimPlot, = plot(P[:,0],P[:,1],"o",color=Color())
         title(tit)
         xlabel(xlab)
         ylabel(ylab)
         Animate = True
         print("animate ",Animate)
         
         LineAnim = FuncAnimation(Fig, UpDateLine, fargs=(AnimPlot,P), blit=False)
         show()
      else:
         pass
         """
         if not FixedAxis:
            AnimPlot.set_xlim(min(x),max(x))
            AnimPlot.set_ylim(min(y),max(y))
         #AnimPlot.set_data(x,y)
         """
      #show()
      #Fig.canvas.draw()
      #Fig.canvas.flush_events()
      #sleep(t)
      show()

def AnimatePP(P,tit="PlotPoints",xlab="X",ylab="Y"):
      global MyFigure,SameFigure,Animate,AnimAx,Fig,AnimPlot,IsTheFirst
      P = array(list(P))
      x,y,z = P[:,0],P[:,1],P[:,2]
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Fig = figure(MyFigure)
         AnimAx = axes(projection="3d")
         IsTheFirst = False

         AnimAx.set_xlim(min(x),max(x))
         AnimAx.set_ylim(min(y),max(y))
         title(tit)
         xlabel(xlab)
         ylabel(ylab)
         #zlabel(ylab)
         Animate = True
         AnimPlot, = AnimAx.plot3D(x,y,z,"o",color=Color())
      else:
         AnimPlot.set_data(x,y,z)
      Fig.canvas.draw()
      Fig.canvas.flush_events()
      #time.sleep(0.1)
      show()

def status(s):
   global MyFigure,SameFigure,Ax,IsTheFirst
   print(s,SameFigure,MyFigure,IsTheFirst)

def PlotXYZ(x,y,z,tit="Plot3D",xlab="X",ylab="Y",zlab="Z"):
      global MyFigure,SameFigure,Ax,IsTheFirst
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Ax = axes(projection="3d")
         IsTheFirst = False
      Ax.scatter3D(x,y,z,marker=PS(),c=z,label=tit)
      Ax.set_xlabel(xlab)
      Ax.set_ylabel(ylab)
      Ax.set_zlabel(zlab)
      legend()
      show()

def Plot3D(P,tit="Plot3D",xlab="X",ylab="Y",zlab="Z"):
   #global MyFigure,SameFigure,Ax,IsTheFirst
   #if not SameFigure or IsTheFirst:
   #   Ax = axes(projection="3d")
   #   IsTheFirst = False
   if type(P) == list: #P = array(P)
      x,y,z = P[:][0],P[:][1],P[:][2]
   else:
      x,y,z = P[:,0],P[:,1],P[:,2]
   PlotXYZ(x,y,z,tit,xlab,ylab,zlab)

def Plot3DPoints(P,tit="Plot3DPoints",xlab="X",ylab="Y",zlab="Z"):
      global MyFigure,SameFigure,Ax,IsTheFirst
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Ax = axes(projection="3d")
         IsTheFirst = False
      if type(P) == list: #P = array(P)
         x,y,z = P[:][0],P[:][1],P[:][2]
      else:
         x,y,z = P[:,0],P[:,1],P[:,2]
      Ax.scatter3D(x,y,z,marker=PS(),c=z,label=tit)
      Ax.set_xlabel(xlab)
      Ax.set_ylabel(ylab)
      Ax.set_zlabel(zlab)
      if len(tit): legend()
      show()

def PlotXYZLine(x,y,z,tit="Plot3DLine",xlab="X",ylab="Y",zlab="Z"):
      global MyFigure,SameFigure,Ax,IsTheFirst
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Ax = axes(projection="3d")
         IsTheFirst = False
      Ax.plot3D(x,y,z,ls=LS(),lw=LW(),c=Color(),label=tit)
      Ax.set_xlabel(xlab)
      Ax.set_ylabel(ylab)
      Ax.set_zlabel(zlab)
      if len(tit): legend()
      show()

def Plot3DLine(P,tit="Plot3DLine",xlab="X",ylab="Y",zlab="Z"):
      #global MyFigure,SameFigure,Ax,IsTheFirst
      #if not SameFigure or MyFigure == 0:
      #   MyFigure += 1
      #figure(MyFigure)
      #if not SameFigure or IsTheFirst:
      #   Ax = axes(projection="3d")
      #   IsTheFirst = False
      if type(P) == list: #P = array(P)
         x,y,z = P[:][0],P[:][1],P[:][2]
      else:
         x,y,z = P[:,0],P[:,1],P[:,2]
      PlotXYZLine(x,y,z,tit,xlab,ylab,zlab)

def Plot3DVectorField(From,To,tit="3D Vectors",xlab="x",ylab="y",zlab="z"):
      global MyFigure,SameFigure,Ax,IsTheFirst
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Ax = axes(projection="3d")
         if IsTheFirst: IsTheFirst = False
      P,Q = transpose(array(From)),transpose(array(To))
      if len(P.shape)>1:
          x,y,z = P[:,0],P[:,1],P[:,2]
          u,v,w = Q[:,0],Q[:,1],Q[:,2]
      else:
          x,y,z = P[0],P[1],P[2]
          u,v,w = Q[0],Q[1],Q[2]
      Ax.quiver(x, y, z, u, v, w, color=Color(),length=0.1, normalize=True,label=tit)
      Ax.set_xlabel(xlab)
      Ax.set_ylabel(ylab)
      Ax.set_zlabel(zlab)
      if len(tit): legend()
      show()

def Plot3DVector(From,To,tit="3D Vectors",xlab="x",ylab="y",zlab="z"):
      global MyFigure,SameFigure,Ax,IsTheFirst
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Ax = axes(projection="3d")
         if IsTheFirst: IsTheFirst = False
      P,Q = transpose(array(From)),transpose(array(To))
      if len(P.shape)>1:
          x,y,z = P[:,0],P[:,1],P[:,2]
          u,v,w = Q[:,0],Q[:,1],Q[:,2]
      else:
          x,y,z = P[0],P[1],P[2]
          u,v,w = Q[0],Q[1],Q[2]
      Ax.quiver(x, y, z, u, v, w, color=Color(),label=tit)
      Ax.set_xlabel(xlab)
      Ax.set_ylabel(ylab)
      Ax.set_zlabel(zlab)
      if len(tit): legend()
      show()

def WireFrame(F,x=[0,1],y=[0,1],tit="WireFrame",xlab="x",ylab="y",zlab="z"):
      global MyFigure,SameFigure,Ax,IsTheFirst
      if type(F) == ndarray:
         qq = F
         x = linspace(x[0],x[-1],qq.shape[1])
         y = linspace(y[0],y[-1],qq.shape[0])
         x, y = meshgrid(x,y)
      else:
         if len(x) == 2:
            x = linspace(x[0],x[1],50)
            y = linspace(y[0],y[1],50)
         elif len(x) == 3:
            x = linspace(x[0],x[1],x[2])
            y = linspace(y[0],y[1],y[2])
         x, y = meshgrid(x,y)
         qq = F(x,y)
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Ax = axes(projection="3d")
         IsTheFirst = False
      Ax.plot_wireframe(x,y,qq,color=Color(),label=tit)
      Ax.set_xlabel(xlab)
      Ax.set_ylabel(ylab)
      Ax.set_zlabel(zlab)
      if len(tit): Ax.legend()
      show()

def Surface(F,x=[0,1],y=[0,1],tit="Surface",xlab="x",ylab="y",zlab="z"):
      global MyFigure,SameFigure,Ax,IsTheFirst
      if not (type(F) == ndarray):
         x, y = meshgrid(x,y)
         qq = F(x,y)
      else:
         qq = F
         if ndim(x)*ndim(y) == 1:
            x = linspace(x[0],x[-1],qq.shape[1])
            y = linspace(y[0],y[-1],qq.shape[0])
            x,y = meshgrid(x,y)
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Ax = axes(projection="3d")
         isTheFirst = False
      Ax.plot_surface(x,y,qq,color=Color(),label=tit)
      Ax.set_xlabel(xlab)
      Ax.set_ylabel(ylab)
      Ax.set_zlabel(zlab)
      #if len(tit): legend()
      show()

def Bar3D(x,y,z,tit="Bar3D",xlab="x",ylab="y",zlab="z"):
      global MyFigure,SameFigure,Ax,IsTheFirst
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Ax = axes(projection="3d")
         IsTheFirst = False
      MyPlot = Ax.bar3d(x,y,zeros(len(z)),ones(len(x)),ones(len(y)),z,color=Color(),label=tit)
      Ax.set_title(tit)
      Ax.set_xlabel(xlab)
      Ax.set_ylabel(ylab)
      Ax.set_zlabel(zlab)
      handles, labels = Ax.get_legend_handles_labels()
      #Ax.legend(handles, labels)
      #Ax.legend(handles=[MyPlot],labels=[tit])
      show()

def Contour(x,y,F,tit="Contour",xlab="x",ylab="y",zlab="z"):
      global MyFigure,SameFigure
      if not (type(F) == ndarray):
         x, y = meshgrid(x,y)
         qq = F(x,y)
      else:
         qq = F
         if ndim(x)*ndim(y) == 1:
            x = linspace(x[0],x[-1],qq.shape[1])
            y = linspace(y[0],y[-1],qq.shape[0])
            x,y = meshgrid(x,y)
      if not SameFigure or MyFigure == 0:
         MyFigure += 1
      figure(MyFigure)
      contour(x,y,qq)
      title(tit)
      xlabel(xlab)
      ylabel(ylab)
      zlabel(zlab)
      show()

def PlotPhase(F,cols=[0,1],labels=["PlotPhase"]):
      global MyFigure,SameFigure,MyColor
      if not SameFigure or MyFigure == 0: MyFigure += 1
      figure(MyFigure)
      
      #locsamefigure = SameFigure
      #setSameFigure(True)
      locolor = MyColor
      setColor("random")
      #if len(tit) == 1: tit = [tit for i in range(len(F))]
      if type(F) == list: F = array(F)
      if F.shape[1] > F.shape[0]: F = transpose(F)
      if len(labels) == 1: tit_ = [labels[0]+"_"+str(i) for i in range(len(F))]
      else: tit_ = labels
      lc = len(cols)
      for i in range(lc-1):
         for j in range(i+1,lc):
            ttit = r"$"+tit_[cols[i]]+","+tit_[cols[j]]+"$" 
            plot(F[:,cols[i]],F[:,cols[j]],marker=PSL(),linestyle=LS(),color=Color(),label=ttit)
            plot(F[0,cols[i]],F[0,cols[j]],InitPoint)
            if len(ttit): legend()
            """
            if not SameFigure: 
               title("PHASE PORTRAIT")
               if i<lc-2 and j<lc-1: NextFigure()
            """
      if SameFigure:
         """
         xl = r"$"+xlab+"_"+str(cols[0])+"$"
         yl = r"$"+ylab+"_"+str(cols[1])+"$"
         xlabel(xl)
         ylabel(yl)
         """
         if len(labels): legend()
      show()
      #setSameFigure(locsamefigure)
      setColor(locolor)

def PlotPhase3D(F,cols=[0,1,2],labels=["PlotPhase"]):
      global MyFigure,SameFigure,MyColor
      #if not SameFigure or MyFigure == 0:
      MyFigure += 1
      figure(MyFigure)
      if not SameFigure or IsTheFirst:
         Ax = axes(projection="3d")
         IsTheFirst = False
      locolor = MyColor
      setColor("random")

      if type(F) == list: F = array(F)
      if F.shape[1] > F.shape[0]: F = transpose(F)
      if len(labels) == 1: tit_ = [labels[0]+"_"+str(i) for i in range(len(F))]
      else: tit_ = labels
      lc = len(cols)
      for i in range(lc-2):
         for j in range(i+1,lc-1):
            for k in range(j+1,lc):
               ttit = r"$"+tit_[cols[i]]+","+tit_[cols[j]]+","+tit_[cols[k]]+"$" 
               Ax.plot3D(F[:,cols[i]],F[:,cols[j]],F[:,cols[k]],ls=LS(),lw=LW(),c=Color(),label=ttit)
               Ax.plot3D(F[0,cols[i]],F[0,cols[j]],F[0,cols[k]],InitPoint)
               if len(ttit): legend()
               if not SameFigure: 
                  title("PHASE SPACE")
                  if i<lc-3 and j<lc-2 and k<lc-1: NextFigure()
      #if len(tit_) > 1:  #SameFigure:
      xl = r"$"+tit_[cols[0]]+"$"
      yl = r"$"+tit_[cols[1]]+"$"
      zl = r"$"+tit_[cols[2]]+"$"
      Ax.set_xlabel(xl)
      Ax.set_ylabel(yl)
      Ax.set_zlabel(zl)
      if len(tit_): legend()
      show()
      #setSameFigure(locsamefigure)
      setColor(locolor)

def SavePlot(MyFig,filename):
   global MyFigure,Samefigure
   FrameOn = True
   savefig(filename+".svg",
            format="svg",
            dpi=300,
            orientation="landscape",
            papertype="A6",
            transparent=True),
            #facecolor=FrameOn)
   savefig(filename+".png",
            format="png",
            dpi=300,
            orientation="landscape",
            papertype="A6",
            transparent=True),
            #facecolor=FrameOn)
   savefig(filename+".eps",
            format="eps",
            dpi=300,
            orientation="landscape",
            papertype="A6",
            transparent=True),
            #facecolor=FrameOn)

def CloseAll():
   global MyFigure,Samefigure,IsTheFirst
   close("all")
   MyFigure = 0
   SameFigure = False
   IsTheFirst = True

def AnimateXY(x,y,step,fig=None,iter=None):
   global Fig,AnimPlot,Func
   if fig: globals()['Fig'] = figure(fig,figsize(6,6))
   else: globals()['Fig'] = figure(figsize=(6,6))
   globals()['AnimPlot'] = plot(x,y,marker=PS(),ls=LS(),lw=LW(),c=Color(),markersize=MS())[0]
   globals()['Func'] = anim.FuncAnimation(Fig, step, frames=iter) #, fargs=(AL,R))
   show()
   
def AnimateXYZ(x,y,z,step,fig=None):
   global Fig,AnimPlot,Func,Ax
   if fig: Fig = figure(fig,figsize(6,6))
   else: Fig = figure(figsize=(6,6))
   Ax = Fig.add_subplot(projection='3d')
   AnimPlot = plot(x,y,z,marker=PS(),ls=LS(),lw=LW(),c=Color(),markersize=MS())[0]
   Func = anim.FuncAnimation(Fig, step, cache_frame_data=False)
   show()

def Animate(P,step,fig=None):
   global Fig,AnimPlot,LineAnim,Func
   x,y = P[0], P[1]
   AnimateXY(x,y,step,fig=None)

def AnimateArray(qq,step,fig=None):
   global Fig,AnimPlot,LineAnim,Func
   if fig: Fig = figure(fig,figsize(6,6))
   else: Fig = figure(figsize=(6,6))
   #AnimPlot = plot(x,y,"ko")[0]
   AnimPlot = imshow(qq,cmap=cm.bone, origin="lower",alpha=1)
   Func = anim.FuncAnimation(Fig, step) #, fargs=(AL,R))
   colorbar()
   show()
   
def AnimateArrayC(qq,step,fig=None):
   global Fig,AnimPlot,LineAnim,Func
   if fig: Fig = figure(fig,figsize(6,6))
   else: Fig = figure(figsize=(6,6))
   #AnimPlot = plot(x,y,"ko")[0]
   AnimPlot = imshow(qq,origin="lower",alpha=1)
   Func = anim.FuncAnimation(Fig, step) #, fargs=(AL,R))
   colorbar()
   show()
   
def UpDataArray(qq):
   global AnimPlot
   AnimPlot.set_data(qq)

def UpDataXY(x,y):
   global AnimPlot
   AnimPlot.set_data(x,y)

def UpDataXYZ(x,y,z):
   global AnimPlot
   AnimPlot.set_data(x,y)

if __name__ == "__main__":
   ### Animation..!
   def Step(i): 
      global R, V
      R[:] = R + dt*V 
      pout = (abs(R) > L)*1
      sgn = sign(R)
      R[:] = R + 2*pout*(sgn*L-R)
      V[:] = V - 2*pout*V
      V[:] = V + dt*g
      UpDataXYZ(R[0],R[1],R[2])

   dt = 0.01
   L = 10
   N = 100
   Vm = 50.
   dim = 3
   R = uniform(-L,L,(dim,N))
   V = uniform(-Vm,Vm,(dim,N))
   g = zeros((dim,N))  
   g[1] = -9.8

   #AnimateXYZ(R[0],R[1],R[2],Step)
   print("...",AnimPlot,Func)

   # animaciones independientes? AL,Func = AnimaXY(R[0],R[1],Step)
   
   a = random((50,50))
   def StepA(i):
      global a
      a[:] = a + 0.01*Lap_5(a)
      UpDataArray(a)

   AnimateArray(a,StepA)
   print("...",AnimPlot,Func)


   #show()

   """
   xa = linspace(-5,5,200)
   ya = linspace(-5,5,200)
   xxa,yya = meshgrid(xa,ya)
   qqa = sin(xxa+yya) * exp(-yya)
   qqs = sin(sqrt(xxa**2 + yya**2))

   xr = randint(0,30,(20))
   yr = randint(0,300,(20))

   zc = linspace(0,12*pi,200)
   xc = cos(zc)
   yc = sin(zc)

   def F(x,y):
      return cos(x**2 + y**2) * exp(-y)

   def G(x):
      return sin(x)*x*cos(x**2/10.0)

   ion()

   ImShow(qqa,xa,ya,r"$\sum_{n=1}^{\infty} x_n^3 $ example",cbar=True)
   ImShow(F,xa,ya)
   #NextFigure()
   WireFrame(F,xa,ya)
   Surface(F,xa,ya)
   
   NextFigure()
   setSameFigure()
   setColor("red")
   Plot3D([xc,yc,zc + random((200))],"spiral")
   setSameFigure(False)

   Plot3D([xc,yc,zc + random((200))],"espiral 2")

   setSameFigure(True)
   setColor("random")
   Plot3DLine([xc,yc,zc*2],"z-scaled")
   Plot3DLine([xc,yc,zc+13],"z-shifted")
   NextFigure()
   Plot3DLine([xc,yc,zc],"spiral")
   
   setSameFigure(False)

   setColor("random")
   for i in range(4):
     r = randint(1,6)
     Plot3D([r*xc,r*yc,r*zc],"POLLOS 2 "+str(i))
   Plot3DLine([xc,yc,zc],"3dline 2")
   Plot3DLine([xc,yc,zc],"again 2")
   setSameFigure(False)

   def feo(x,y):
      return sin(x*y)

   print(type(feo))
   NextFigure()
   setSameFigure()
   WireFrame(qqs,tit="gorro")
   WireFrame(F=feo,x=linspace(0,1,20),y=linspace(0,1,20))
   setSameFigure(False)
   WireFrame(qqs,tit="gorro solo")
   WireFrame(F=feo,x=linspace(0,1,20),y=linspace(0,1,20),tit="feo solo")
   setLineWidth(3)
   Box(0,1,0,1,0,1)
   resetLineWidth()
   Surface(qqs,tit="SURFACE VIL")

   #print Pareto(3,1,20)
   setSameFigure()
   setColor("yellow")
   Bar3D(xr,yr,Pareto(3,1,20))
   setColor("black")
   Bar3D(xr,yr,Pareto(2.5,1,20))
   #Contour
   setColor("orange")
   NextFigure()
   setPointStyle("*")
   Plot(sin)
   setColor("black")
   Plot(G,[0,2*pi,20],tit="G")
   setColor("green")
   Plot([1,2],[3,5])
   NextFigure()
   setStyle(3)
   title("Harmonic..."+Style)
   PlotLine(sin,tit="sin")
   setPointStyleL("D")
   setLineStyle("")
   PlotLine(G,[0,2*pi,10],tit="G <- [0,2*pi,10]")
   resetPointStyles()
   resetLineStyle()
   PlotLine(G,[0,2*pi,50],tit="G <- [0,2*pi,50]")
   setPointStyleL("D")
   setLineStyle(":")
   setColor("random")
   PlotLines([[1,2],[3,5],[4,4]],[0,1,2],tit=["[1,2]","[3,5] and [4,4] <- [0,1,2]"])
   NextFigure()
   PlotLines([[1,2],[3,5]],[0,1],tit=["[1,2] <- [0,1]","[3,5] <- [0,1]"])
   setColor("blue")
   PlotLine([7,8],[0,1],tit="[7,8] <- [0,1]")
   NextFigure()
   PlotLines([xc,yc,zc],x=[]) #,tit=["xc,xc","yc,xc","yc,zc"])
   TextXY("hola pellitos",4,4,size=23)
   setLineStyle("-.")
   HorizLine(4)
   """
   input("enter...")
