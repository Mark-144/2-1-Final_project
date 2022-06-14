#프로그램실행에 필요한 내/외부 모듈 선언(L.1~7)
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
import numpy as np
import tkinter as tk
import tkinter.messagebox as msgbox

#d까지의 3D 오비탈의 각도부분 함수(L.9~27)
def s(th,phi):
    return 5
def p_x(th,phi):
    return 5*np.sin(th)**2*np.cos(phi)**2
def p_y(th,phi):
    return 5*np.sin(th)*np.sin(phi)**2
def p_z(th,phi):
    return 5*np.cos(th)**2
def d_z2(th,phi):
    return 5*(3*np.cos(th)**2-1)
def d_xz(th,phi):
    return 10*np.sin(th)*np.cos(th)*np.sin(phi)
def d_yz(th,phi):
    return 10*np.sin(th)*np.cos(th)*np.sin(phi)
def d_xy(th,phi):
    return 10*np.sin(th)**2*np.sin(2*phi)
def d_x2_y2(th,phi):
    return 5*np.sin(th)**2*np.cos(2*phi)

#3D 애니메이션 담당부분(L.29~37)
ax2=0
figg=0
def init(X,Y,Z,fig,ax3): #What is the role
    ax3.plot_surface(X,Y,Z,rstride=5,cstride=5,cmap=cm.RdPu)
    return fig,
def animate(i): #Rotating the orbital_coordinate
    ax2.view_init(elev=20,azim=i*4)
    return figg,

#각도부분 생성함수(L.39~58)
def Y_func(func): #Angular Wave function
    global ax2, figg
    fig=plt.figure(facecolor="Black")
    ax3=plt.axes(projection="3d")
    x=np.arange(0,np.pi*2,0.01)
    y=np.arange(0,np.pi,0.01)
    phi,th=np.meshgrid(x,y)
    f=func(th,phi)
    X=f*np.sin(th)*np.cos(phi)
    Y=f*np.sin(th)*np.sin(phi)
    Z=f*np.cos(th)
    ax3.set_facecolor("#1DD4AF")
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    ax3.set_zlim(-5,5)
    figg=fig
    ax2=ax3
    ani=animation.FuncAnimation(fig,animate,init_func=lambda:init(X,Y,Z,fig,ax3),frames=90,interval=200,blit=False)
    plt.show()



#2차원 파동함수의 그래프를 만드는 부분(그래프 크기 조정을 위한 적절한 크기를 만들었다.)(L.62~349)
def s1(choose,se,ga,i):
    xaxis = np.arange(-100, 100)
    yaxis = xaxis*0
    plt.plot(xaxis, yaxis, 'k')
    xs11 = np.arange(-2,30,0.1)
    ys11 = np.exp(-1*xs11)
    xs12 = np.arange(-2,30,0.1)
    ys12 = ys11**2
    ys1 = ys11*xs12
    xs13 = np.arange(-2,30,0.1)
    ys13 = ys1**2

    if choose == 1:
        plt.subplot(se,ga,i)
        plt.xlim(0, 7)
        plt.ylim(-0.4, 1.2)
        plt.plot(xs11,ys11,'b', label='1s(R(r))')
        plt.xlabel('distance')
        plt.ylabel('R(r)')
        
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 2:
        plt.subplot(se,ga,i)
        plt.xlim(0, 10)
        plt.ylim(-0.1, 1)
        plt.plot(xs12,ys12,'r', label='1s(R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('R(r)2')
        
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 3:
        plt.subplot(se,ga,i)
        plt.xlim(0, 4)
        plt.ylim(0, 0.2)
        plt.plot(xs13,ys13,'g', label='1s(r2R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('r2R(r)2')
        
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

def s2(choose,se,ga,i):
    xaxis = np.arange(-100, 100)
    yaxis = xaxis*0
    plt.plot(xaxis, yaxis, 'k')
    xs21 = np.arange(-2,30,0.1)
    ys21 = np.exp(-1*xs21/2)*(2-xs21)
    xs22 = np.arange(-2,30,0.1)
    ys22 = ys21**2
    ys2 = ys21*xs22
    xs23 = np.arange(-2,30,0.1)
    ys23 = ys2**2

    if choose == 1:
        plt.subplot(se,ga,i)
        plt.xlim(0, 15)
        plt.ylim(-0.4, 2)
        plt.plot(xs21,ys21,'b', label='2s(R(r))')
        plt.xlabel('distance')
        plt.ylabel('R(r)')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 2:
        plt.subplot(se,ga,i)
        plt.xlim(0, 15)
        plt.ylim(0, 1)
        plt.plot(xs22,ys22,'r', label='2s(R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('R(r)2')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 3:
        plt.subplot(se,ga,i)
        plt.xlim(0, 20)
        plt.ylim(0, 1.8)
        plt.plot(xs23,ys23,'g', label='2s(r2R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('r2R(r)2')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

def s3(choose,se,ga,i):
    xaxis = np.arange(-100, 100)
    yaxis = xaxis*0
    plt.plot(xaxis, yaxis, 'k')
    xs31 = np.arange(-2,40,0.1)
    ys31 = np.exp(-1*xs31/3)*(1-2/3*xs31+2/27*(xs31**2))
    xs32 = np.arange(-2,40,0.1)
    ys32 = ys31**2
    ys3 = ys31*xs32
    xs33 = np.arange(-2,40,0.1)
    ys33 = ys3**2

    if choose == 1:
        plt.subplot(se,ga,i)
        plt.xlim(0, 25)
        plt.ylim(-0.4, 1)
        plt.plot(xs31,ys31,'b', label='3s(R(r))')
        plt.xlabel('distance')
        plt.ylabel('R(r)')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 2:
        plt.subplot(se,ga,i)
        plt.xlim(0, 20)
        plt.ylim(-0.02, 0.2)
        plt.plot(xs32,ys32,'r', label='3s(R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('R(r)2')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 3:
        plt.subplot(se,ga,i)
        plt.xlim(0, 30)
        plt.ylim(0, 1)
        plt.plot(xs33,ys33,'g', label='3s(r2R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('r2R(r)2')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

def p2(choose,se,ga,i):
    xaxis = np.arange(-100, 100)
    yaxis = xaxis*0
    plt.plot(xaxis, yaxis, 'k')
    xp21 = np.arange(-2,30,0.1)
    yp21 = np.exp(-1*xp21/2)*(xp21)
    xp22 = np.arange(-2,30,0.1)
    yp22 = yp21**2
    yp2 = yp21*xp22
    xp23 = np.arange(-2,30,0.1)
    yp23 = yp2**2

    if choose == 1:
        plt.subplot(se,ga,i)
        plt.xlim(0, 25)
        plt.ylim(-0.4, 1)
        plt.plot(xp21,yp21,'b', label='2p(R(r))')
        plt.xlabel('distance')
        plt.ylabel('R(r)')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 2:
        plt.subplot(se,ga,i)
        plt.xlim(0, 12)
        plt.ylim(-0.2, 0.8)
        plt.plot(xp22,yp22,'r', label='2p(R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('R(r)2')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 3:
        plt.subplot(se,ga,i)
        plt.xlim(0, 30)
        plt.ylim(0, 6)
        plt.plot(xp23,yp23,'g', label='2p(r2R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('r2R(r)2')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

def p3(choose,se,ga,i):
    xaxis = np.arange(-100, 100)
    yaxis = xaxis*0
    plt.plot(xaxis, yaxis, 'k')
    xp31 = np.arange(-2,30,0.1)
    yp31 = np.exp(-1*xp31/3)*(xp31-1/6*(xp31**2))
    xp32 = np.arange(-2,30,0.1)
    yp32 = yp31**2
    yp3 = yp31*xp32
    xp33 = np.arange(-2,30,0.1)
    yp33 = yp3**2

    if choose == 1:
        plt.subplot(se,ga,i)
        plt.xlim(0, 25)
        plt.ylim(-0.4, 1)
        plt.plot(xp31,yp31,'b', label='3p(R(r))')
        plt.xlabel('distance')
        plt.ylabel('R(r)')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 2:
        plt.subplot(se,ga,i)
        plt.xlim(0, 30)
        plt.ylim(-0.1, 0.6)
        plt.plot(xp32,yp32,'r', label='3p(R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('R(r)2')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 3:
        plt.subplot(se,ga,i)
        plt.xlim(0, 30)
        plt.ylim(0, 10)
        plt.plot(xp33,yp33,'g', label='3p(r2R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('r2R(r)')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

def d3(choose,se,ga,i):
    xd31 = np.arange(0,30,0.1)
    yd31 = np.exp(-1*xd31/3)*(xd31**2)
    xd32 = np.arange(0,30,0.1)
    yd32 = yd31**2
    yd3 = yd31*xd32
    xd33 = np.arange(0,30,0.1)
    yd33 = yd3**2
    
    if choose == 1:
        plt.subplot(se,ga,i)
        plt.xlim(0, 30)
        plt.ylim(0, 7)
        plt.plot(xd31,yd31,'b', label='3d(R(r))')
        plt.xlabel('distance')
        plt.ylabel('R(r)')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    if choose == 2:
        plt.subplot(se,ga,i)
        plt.xlim(0, 30)
        plt.ylim(0, 25)
        plt.plot(xd32,yd32,'r', label='3d(R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('R(r)2')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])
        
    if choose == 3:
        plt.subplot(se,ga,i)
        plt.xlim(0, 30)
        plt.ylim(0, 2000)
        plt.plot(xd33,yd33,'g', label='3d(r2R(r)2)')
        plt.xlabel('distance')
        plt.ylabel('r2R(r)2')
        plt.legend(loc='upper right')
        ax = plt.gca()
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

#2D 함수를 부르는 부분(L.351~431)
def show():
    global chkvar1s, chkvar2s, chkvar3s, chkvar2p, chkvar3p, chkvar3d, chkvar1s1, chkvar1s2, chkvar1s3, chkvar2s1, chkvar2s2, chkvar2s3, chkvar3s1, chkvar3s2, chkvar3s3, chkvar2p1, chkvar2p2, chkvar2p3, chkvar3p1, chkvar3p2, chkvar3p3, chkvar3d1, chkvar3d2, chkvar3d3
    chkvar = str(chkvar1s1.get()) + str(chkvar1s2.get()) + str(chkvar1s3.get()) + str(chkvar2s1.get()) + str(chkvar2s2.get()) + str(chkvar2s3.get()) + str(chkvar3s1.get()) + str(chkvar3s2.get()) + str(chkvar3s3.get()) + str(chkvar2p1.get()) + str(chkvar2p2.get()) + str(chkvar2p3.get()) + str(chkvar3p1.get()) + str(chkvar3p2.get()) + str(chkvar3p3.get()) + str(chkvar3d1.get()) + str(chkvar3d2.get()) + str(chkvar3d3.get()) 
    n=chkvar.count('1')
    ga= (n>=3)*3+(n<3)*n
    se= (n-1)//3+1
    ts11 = chkvar[0]
    ts12 = chkvar[1]
    ts13 = chkvar[2]
    ts21 = chkvar[3]
    ts22 = chkvar[4]
    ts23 = chkvar[5]
    ts31 = chkvar[6]
    ts32 = chkvar[7]
    ts33 = chkvar[8]
    tp21 = chkvar[9]
    tp22 = chkvar[10]
    tp23 = chkvar[11]
    tp31 = chkvar[12]
    tp32 = chkvar[13]
    tp33 = chkvar[14]
    td31 = chkvar[15]
    td32 = chkvar[16]
    td33 = chkvar[17]
    i=1
    if ts11 == '1':
        s1(1,se,ga,i)
        i+=1
    if ts12 == '1':
        s2(2,se,ga,i)
        i+=1
    if ts13 == '1':
        s3(3,se,ga,i)
        i+=1
    if ts21 == '1':
        s2(1,se,ga,i)
        i+=1
    if ts22 == '1':
        s2(2,se,ga,i)
        i+=1
    if ts23 == '1':
        s2(3,se,ga,i)
        i+=1
    if ts31 == '1':
        s3(1,se,ga,i)
        i+=1
    if ts32 == '1':
        s3(2,se,ga,i)
        i+=1
    if ts33 == '1':
        s3(3,se,ga,i)
        i+=1
    if tp21 == '1':
        p2(1,se,ga,i)
        i+=1
    if tp22 == '1':
        p2(2,se,ga,i)
        i+=1
    if tp23 == '1':
        p2(3,se,ga,i)
        i+=1
    if tp31 == '1':
        p3(1,se,ga,i)
        i+=1
    if tp32 == '1':
        p3(2,se,ga,i)
        i+=1
    if tp33 == '1':
        p3(3,se,ga,i)
        i+=1
    if td31 == '1':
        d3(1,se,ga,i)
        i+=1
    if td32 == '1':
        d3(2,se,ga,i)
        i+=1
    if td33 == '1':
        d3(3,se,ga,i)
        i+=1
    plt.show()

#종료알림 메시지 박스
def okcancel2():
    global window
    response = msgbox.askokcancel("알림", "종료하시겠습니까?")
    if response == 1:
        window.destroy()

def d_2():#2차원 함수 보여주는 곳
    global window
    window = tk.Toplevel()
    window.title("2Dimntion H atomic orbital Wave function")
    window.geometry("640x500+600+200")
    window['bg']='skyblue'
    frm=tk.Frame(window, bg='skyblue')
    frm.pack()
    global chkvar1s, chkvar2s, chkvar3s, chkvar2p, chkvar3p, chkvar3d, chkvar1s1, chkvar1s2, chkvar1s3, chkvar2s1, chkvar2s2, chkvar2s3, chkvar3s1, chkvar3s2, chkvar3s3, chkvar2p1, chkvar2p2, chkvar2p3, chkvar3p1, chkvar3p2, chkvar3p3, chkvar3d1, chkvar3d2, chkvar3d3
    
    chkbox1s = tk.Label(frm, text="1s", font=('Consolas', 30), bg='#60E000')
    chkbox1s.grid(row=0, column=0, padx=3, pady=3)
    chkvar1s1 = tk.IntVar()
    chkbox1s1 = tk.Checkbutton(frm, text="R(r)", font=('Consolas', 15), variable=chkvar1s1, bg='#E080E0')
    chkbox1s1.grid(row=0, column=1, padx=3, pady=3)
    chkvar1s2 = tk.IntVar()
    chkbox1s2 = tk.Checkbutton(frm, text="R(r)2", font=('Consolas', 15), variable=chkvar1s2, bg='#E080E0')
    chkbox1s2.grid(row=0, column=2, padx=3, pady=3)
    chkvar1s3 = tk.IntVar()
    chkbox1s3 = tk.Checkbutton(frm, text="r2R(r)2", font=('Consolas', 15), variable=chkvar1s3, bg='#E080E0')
    chkbox1s3.grid(row=0, column=3, padx=3, pady=3)
    
    chkbox2s = tk.Label(frm, text="2s", font=('Consolas', 30), bg='#60E000')
    chkbox2s.grid(row=1, column=0, padx=3, pady=3)
    chkvar2s1 = tk.IntVar()
    chkbox2s1 = tk.Checkbutton(frm, text="R(r)", font=('Consolas', 15), variable=chkvar2s1, bg='#E080E0')
    chkbox2s1.grid(row=1, column=1, padx=3, pady=3)
    chkvar2s2 = tk.IntVar()
    chkbox2s2 = tk.Checkbutton(frm, text="R(r)2", font=('Consolas', 15), variable=chkvar2s2, bg='#E080E0')
    chkbox2s2.grid(row=1, column=2, padx=3, pady=3)
    chkvar2s3 = tk.IntVar()
    chkbox2s3 = tk.Checkbutton(frm, text="r2R(r)2", font=('Consolas', 15), variable=chkvar2s3, bg='#E080E0')
    chkbox2s3.grid(row=1, column=3, padx=3, pady=3)
    
    
    chkbox3s = tk.Label(frm, text="3s", font=('Consolas', 30), bg='#60E000')
    chkbox3s.grid(row=2, column=0, padx=3, pady=3)
    chkvar3s1 = tk.IntVar()
    chkbox3s1 = tk.Checkbutton(frm, text="R(r)", font=('Consolas', 15), variable=chkvar3s1, bg='#E080E0')
    chkbox3s1.grid(row=2, column=1, padx=3, pady=3)
    chkvar3s2 = tk.IntVar()
    chkbox3s2 = tk.Checkbutton(frm, text="R(r)2", font=('Consolas', 15), variable=chkvar3s2, bg='#E080E0')
    chkbox3s2.grid(row=2, column=2, padx=3, pady=3)
    chkvar3s3 = tk.IntVar()
    chkbox3s3 = tk.Checkbutton(frm, text="r2R(r)2", font=('Consolas', 15), variable=chkvar3s3, bg='#E080E0')
    chkbox3s3.grid(row=2, column=3, padx=3, pady=3)
    
    
    chkbox2p = tk.Label(frm, text="2p", font=('Consolas', 30), bg='#60E000')
    chkbox2p.grid(row=3, column=0, padx=3, pady=3)
    chkvar2p1 = tk.IntVar()
    chkbox2p1 = tk.Checkbutton(frm, text="R(r)", font=('Consolas', 15), variable=chkvar2p1, bg='#E080E0')
    chkbox2p1.grid(row=3, column=1, padx=3, pady=3)
    chkvar2p2 = tk.IntVar()
    chkbox2p2 = tk.Checkbutton(frm, text="R(r)2", font=('Consolas', 15), variable=chkvar2p2, bg='#E080E0')
    chkbox2p2.grid(row=3, column=2, padx=3, pady=3)
    chkvar2p3 = tk.IntVar()
    chkbox2p3 = tk.Checkbutton(frm, text="r2R(r)2", font=('Consolas', 15), variable=chkvar2p3, bg='#E080E0')
    chkbox2p3.grid(row=3, column=3, padx=3, pady=3)
    
    
    chkbox3p = tk.Label(frm, text="3p", font=('Consolas', 30), bg='#60E000')
    chkbox3p.grid(row=4, column=0, padx=3, pady=3)
    chkvar3p1 = tk.IntVar()
    chkbox3p1 = tk.Checkbutton(frm, text="R(r)", font=('Consolas', 15), variable=chkvar3p1, bg='#E080E0')
    chkbox3p1.grid(row=4, column=1, padx=3, pady=3)
    chkvar3p2 = tk.IntVar()
    chkbox3p2 = tk.Checkbutton(frm, text="R(r)2", font=('Consolas', 15), variable=chkvar3p2, bg='#E080E0')
    chkbox3p2.grid(row=4, column=2, padx=3, pady=3)
    chkvar3p3 = tk.IntVar()
    chkbox3p3 = tk.Checkbutton(frm, text="r2R(r)2", font=('Consolas', 15), variable=chkvar3p3, bg='#E080E0')
    chkbox3p3.grid(row=4, column=3, padx=3, pady=3)
    
    
    chkbox3d = tk.Label(frm, text="3d", font=('Consolas', 30), bg='#60E000')
    chkbox3d.grid(row=5, column=0, padx=3, pady=3)
    chkvar3d1 = tk.IntVar()
    chkbox3d1 = tk.Checkbutton(frm, text="R(r)", font=('Consolas', 15), variable=chkvar3d1, bg='#E080E0')
    chkbox3d1.grid(row=5, column=1, padx=3, pady=3)
    chkvar3d2 = tk.IntVar()
    chkbox3d2 = tk.Checkbutton(frm, text="R(r)2", font=('Consolas', 15), variable=chkvar3d2, bg='#E080E0')
    chkbox3d2.grid(row=5, column=2, padx=3, pady=3)
    chkvar3d3 = tk.IntVar()
    chkbox3d3 = tk.Checkbutton(frm, text="r2R(r)2", font=('Consolas', 15), variable=chkvar3d3, bg='#E080E0')
    chkbox3d3.grid(row=5, column=3, padx=3, pady=3)
    
    button = tk.Button(frm, overrelief="solid", width=15, text="클릭!", command=show, bg='yellow')
    button.grid(row=6, column=2)
    tk.Button(frm,text="QUIT", command=okcancel2, bg='red').grid(row=7, column=2)

def okcancel():
    global window2
    response = msgbox.askokcancel("알림", "종료하시겠습니까?")
    if response == 1:
        window2.destroy()

def d_3():#3차원 함수 보여주는 곳
    global window2
    window2 = tk.Tk()
    window2.title("3Dimantion H atomic orbital")
    window2.geometry("800x380+600+300")
    frm=tk.Frame(window2,pady=10)
    frm.pack()
    obit=['s','p_x','p_y','p_z','d_z2','d_xz','d_yz','d_xy','d_x2_y2']
    f_obit=[s,p_x,p_y,p_z,d_z2,d_xz,d_yz,d_xy,d_x2_y2]
    for i in range(len(obit)):
        tk.Button(frm, overrelief="solid", width=15, height=2, relief='solid', font=('Consolas', 15, 'bold'), bg="#E0A0D0", command= lambda f=f_obit[i]:Y_func(f), text=obit[i]).grid(row=i//4, column=i%4)
    frm2=tk.Frame(window2,pady=10)
    frm2.pack()
    tk.Button(frm2, text="QUIT", width=10, height=2, font=('Consolas', 15, 'bold'), bg="red", command=okcancel).grid(column=1,row=0)

from PIL import ImageTk
main=tk.Tk()
main.geometry('800x600+500+200')
main.title("보어야 보아라")
frm1=tk.Frame(main,pady=20)
frm1.pack(padx=10,pady=10,fill='both')
tk.Label(frm1,text='Orbital of H atom', font=('Consolas', 30, 'bold'),).pack(ipadx=20, ipady=10)
frm2=tk.Frame(main,pady=200,bg='yellow')
frm2.pack(padx=5,pady=5,fill='both')


frameCnt = 3
frames = [ImageTk.PhotoImage(file='QM_orbital_evolution.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    frm2.after(100, update, ind)

positionRight = frm2.winfo_screenwidth()/2 
positionDown = frm2.winfo_screenheight()/5

label = tk.Label(frm2, bg='black')
label.place(x=positionRight,y=positionDown,anchor='center')
frm2.after(0, update, 0)

tk.Button(frm2,text='2D', font=('Consolas', 25), command=d_2, bg='skyblue').pack(padx=20,ipadx=60, ipady=100,side='left')
tk.Button(frm2, text='3D',font=('Consolas', 25), command=d_3, bg='orange').pack(padx=20,ipadx=60, ipady=100,side='right')
main.mainloop()
