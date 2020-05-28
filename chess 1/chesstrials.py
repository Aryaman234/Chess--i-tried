from p5 import * 
from Tiles import *
import py2app

width = 800
height= 800


bRook = None
bPawn = None
bBishop = None
bKingimg = None
bQueenimg = None
bKnight=None
wRook = None
wPawn = None
wBishop = None
wKingimg = None
wQueenimg = None
wKnight=None
chessBoard = None

bPawn1 = 1
bPawn2= 2
bPawn3= 3
bPawn4 = 4
bPawn5 = 5
bPawn6= 6
bPawn7= 7
bPawn8= 8
wKnight1= 9 
wKnight2=10
bKnight1= 11
bKnight2= 12
wQueen = 13
bQueen= 14
wKing = 15
bKing = 16
wBishop1=17
wBishop2=18
bBishop1=19
bBishop2=20
wRook1= 21
wRook2= 22
bRook1= 23
bRook2= 24
wPawn1 = 25
wPawn2= 26
wPawn3= 27
wPawn4 = 28
wPawn5 =29
wPawn6= 31
wPawn7= 32
wPawn8= 33

board = [0]* 64

mouseisreleased = False
mp= False
bRook1display = True
bRook2display = True
bQueendisplay = True
bKingdisplay= True
bBishop1display= True
bBishop2display= True
bKnight1display= True
bKnight2display= True
bPawn1display= True
bPawn2display= True
bPawn3display= True
bPawn4display= True
bPawn5display= True
bPawn6display= True
bPawn7display= True
bPawn8display= True

wRook1display = True
wRook2display = True
wQueendisplay = True
wKingdisplay= True
wBishop1display= True
wBishop2display= True
wKnight1display= True
wKnight2display= True
wPawn1display= True
wPawn2display= True
wPawn3display= True
wPawn4display= True
wPawn5display= True
wPawn6display= True
wPawn7display= True
wPawn8display= True



wTurn = True
bTurn = False

gameboard=[]


def setup():
    global bRook, bPawn, bQueenimg, bKingimg, bBishop, bKnight, wRook, wPawn, wQueenimg , wKingimg , wBishop, wKnight, board, wKing,wQueen,bKing,bQueen, bRook1display, bRook2display ,bQueendisplay,bKingdisplay,bBishop1display, bBishop2display, bKnight1display, bKnight2display,bPawn1display,bPawn2display,bPawn3display,bPawn4display, bPawn5display, bPawn6display, bPawn7display, bPawn8display, wTurn, bTurn,chessBoard, gameboard,tempVal,tempPos, mp, mouseisreleased,pmX, pmY, newarraypos, newval, newpos, mX, mY, arraypos,pieceValue 

    size(800,800)

    
    i=0
    for rows in range(0,9):
        for cols in range(0,9):
            temp=Tile(cols*100,rows*100)
            gameboard.append(temp)
            if((i)%2==0):
                gameboard[i].color=Color(0)
            else:
                gameboard[i].color=Color(255)
        
            
            i=i+1
            

    tempVal=0
    tempPos=65
    pmX = 0
    pmY=0
    newarraypos=65
    newval=0
    newpos=0
    mX=0
    mY=0
    arraypos=65
    pieceValue =0
     

    board[0]=bRook1
    board[1]=bKnight1
    board[2]=bBishop1
    board[3]=bQueen
    board[4]=bKing
    board[5]=bBishop2
    board[6]=bKnight2
    board[7]=bRook2
    board[8]=bPawn1
    board[9]=bPawn2
    board[10]=bPawn3
    board[11]=bPawn4
    board[12]=bPawn5
    board[13]=bPawn6
    board[14]=bPawn7
    board[15]=bPawn8

    board[63]=wRook1
    board[62]=wKnight1
    board[61]=wBishop1
    board[60]=wKing
    board[59]=wQueen
    board[58]=wBishop2
    board[57]=wKnight2
    board[56]=wRook2
    board[55]=wPawn1        
    board[54]=wPawn2
    board[53]=wPawn3
    board[52]=wPawn4
    board[51]=wPawn5
    board[50]=wPawn6
    board[49]=wPawn7
    board[48]= wPawn8

    bRook= load_image("chess 1/pieces/bRook.png")
    bPawn= load_image("chess 1/pieces/bPawn.png")
    bQueenimg= load_image("chess 1/pieces/bQueen.png")
    bKingimg= load_image("chess 1/pieces/bKing.png")
    bBishop= load_image("chess 1/pieces/bBishop.png")
    bKnight= load_image("chess 1/pieces/bKnight.png")
    
    wRook= load_image("chess 1/pieces/wRook.png")
    wPawn= load_image("chess 1/pieces/wPawn.png")
    wQueenimg= load_image("chess 1/pieces/wQueen.png")
    wKingimg= load_image("chess 1/pieces/wKing.png")
    wBishop = load_image("chess 1/pieces/wBishop.png")
    wKnight = load_image("chess 1/pieces/wKnight.png")

    chessBoard = load_image("chess 1/pieces/chessboard.png")    





    





def draw():

    global bRook, bPawn, bQueenimg, bKingimg, bBishop, bKnight, wRook, wPawn, wQueenimg , wKingimg , wBishop, wKnight, board, wKing,wQueen,bKing,bQueen, bRook1display,  bRook2display ,bQueendisplay,bKingdisplay,bBishop1display, bBishop2display, bKnight1display, bKnight2display,bPawn1display,bPawn2display,bPawn3display,bPawn4display, bPawn5display, bPawn6display, bPawn7display, bPawn8display, wRook1display, wRook2display ,wQueendisplay,wKingdisplay,wBishop1display, wBishop2display, wKnight1display, wKnight2display,wPawn1display,wPawn2display,wPawn3display,wPawn4display, wPawn5display, wPawn6display, wPawn7display, wPawn8display, wTurn, bTurn, gameBoard,tempVal, tempPos, mp, mouseisreleased, pmX, pmY, newarraypos, newval, newpos, mX, mY, arraypos,pieceValue 



    for tile in gameboard:
        tile.Draw()

    if(bRook1display == True):
        x = 0
        y = 0
        for i in range(0,64):
            if(board[i] == bRook1):
                x=((i%8))* 100
                tempy= (i/8) * 100
                if(tempy > 100):
                    tempy=tempy-100
                    y= ((i/8)*100)-tempy
                y=y+15
                x=x+15
                image(bRook,(x,y),(70,70))

    if(bKnight1display == True):
        a = 0
        b = 0
        for i in range(0,64):
            if(board[i] == bKnight1):
                a=((i%8))* 100
                tempb= (i/8) * 100
                if(tempb > 200):
                    tempb=tempb-100
                    b= ((i/8)*100)-tempb
                a=a+15
                b=b+15
                image(bKnight,(a,b),(70,70))

    if(bBishop1display == True):
        c = 0
        d = 0
        for i in range(0,64):
            if(board[i] == bBishop1):
                c=((i%8))* 100
                tempd= (i/8) * 100
                if(tempd > 200):
                    tempd=tempd-100
                    d = ((i/8)*100)-tempd
                d=d+15
                c=c+15
                image(bBishop,(c,d),(70,70))
    
    if(bQueendisplay == True):
        e = 0
        f = 0
        for i in range(0,64):
            if(board[i] == bQueen):
                e=((i%8))* 100
                tempf= (i/8) * 100
                if(tempf > 200):
                    tempf=tempf-100
                    f= ((i/8)*100)-tempf
                e=e+15
                f=f+15
                image(bQueenimg,(e,f),(70,70))
    
    if(bKingdisplay == True):
        g = 0
        h = 0
        for i in range(0,64):
            if(board[i] == bKing):
                g=((i%8))* 100
                temph= (i/8) * 100
                if(temph > 200):
                    temph=temph-100
                    h= ((i/8)*100)-temph
                g=g+15
                h=h+15
                image(bKingimg,(g,h),(70,70))

    if(bBishop2display == True):
        j = 0
        k = 0
        for i in range(0,64):
            if(board[i] == bBishop2):
                j=((i%8))* 100
                tempk= (i/8) * 100
                if(tempk > 200):
                    tempk=tempk-100
                    k= ((i/8)*100)-tempk
                j=j+15
                k=k+15
                image(bBishop,(j,k),(70,70))

    if(bKnight2display == True):
        l = 0
        m = 0
        for i in range(0,64):
            if(board[i] == bKnight2):
                l=((i%8))* 100
                tempm= (i/8) * 100
                if(tempm > 200):
                    tempm=tempm-100
                    m= ((i/8)*100)-tempm
                l=l+15
                m=m+15
                image(bKnight,(l,m),(70,70))

    if(bRook2display == True):
        n = 0
        o = 0
        for i in range(0,64):
            if(board[i] == bRook2):
                n=((i%8))* 100
                tempo= (i/8) * 100
                if(tempo > 200):
                    tempo=tempo-100
                    o= ((i/8)*100)-tempo
                n=n+15
                o=o+15
                image(bRook,(n,o),(70,70))

    if(bPawn1display == True):
        p = 0
        q = 0
        for i in range(0,64):
            if(board[i] == bPawn1):
                p=((i%8))* 100
                q= ((round((i/8)))*100)
                q=q+15
                p=p+15
                image(bPawn,(p,q),(70,70))
    

    if(bPawn2display == True):
        r = 0
        s = 0
        for i in range(0,64):
            if(board[i] == bPawn2):
                r=((i%8))* 100
                s= ((round((i/8)-0.5))*100)
                s=s+15
                r=r+15
                image(bPawn,(r,s),(70,70))

    if(bPawn3display == True):
        t = 0
        u = 0
        for i in range(0,64):
            if(board[i] == bPawn3):
                t=((i%8))* 100
                u= ((round((i/8)-0.5))*100)
                u=u+15
                t=t+15
                image(bPawn,(t,u),(70,70))
    
    if(bPawn4display == True):
        v = 0
        w = 0
        for i in range(0,64):
            if(board[i] == bPawn4):
                v=((i%8))* 100
                w= ((round((i/8)-0.5))*100)
                w=w+15
                v=v+15
                image(bPawn,(v,w),(70,70))

    if(bPawn5display == True):
        z = 0
        aa = 0
        for i in range(0,64):
            if(board[i] == bPawn5):
                z=((i%8))* 100
                aa= ((round((i/8)-0.5))*100)
                aa=aa+15
                z=z+15
                image(bPawn,(z,aa),(70,70))

    if(bPawn6display == True):
        ab = 0
        ac = 0
        for i in range(0,64):
            if(board[i] == bPawn6):
                ab=((i%8))* 100
                ac= ((round((i/8)-0.5))*100)
                ac=ac+15
                ab=ab+15
                image(bPawn,(ab,ac),(70,70))

    if(bPawn7display == True):
        ad = 0
        ae = 0
        for i in range(0,64):
            if(board[i] == bPawn7):
                ad=((i%8))* 100
                ae= ((round((i/8)-0.5))*100)
                ae=ae+15
                ad=ad+15
                image(bPawn,(ad,ae),(70,70))
    
    if(bPawn8display == True):
        af = 0
        ah = 0
        for i in range(0,64):
            if(board[i] == bPawn8):
                af=((i%8))* 100
                ah= ((round((i/8)-0.5))*100)
                ah=ah+15
                af=af+15
                image(bPawn,(af,ah),(70,70))
    
    if(wRook1display == True):
        ai = 0
        aj = 0
        for i in range(0,64):
            if(board[i] == wRook1):
                ai = ((i%8)) * 100
                aj = ((round((i/8)-0.5))*100)
                ai=ai+15
                aj=aj+15
                image(wRook,(ai,aj),(70,70))


    if(wBishop1display == True):
        ak = 0
        al = 0
        for i in range(0,64):
            if(board[i] == wBishop1):
                ak = ((i%8)) *100
                al = ((round((i/8)-0.5))*100)
                ak=ak+115
                al=al+15
                image(wBishop,(ak,al),(70,70))
    
    if(wKnight1display == True):
        am = 0
        an = 0
        for i in range(0,64):
            if(board[i] == wKnight1):
                am = ((i%8)) *100
                an = ((round((i/8)-0.5))*100)
                am=am-85
                an=an+15
                image(wKnight,(am,an),(70,70))
    
    if(wKingdisplay == True):
        ao = 0
        ap = 0
        for i in range(0,64):
            if(board[i] == wKing):
                ao = ((i%8)) *100
                ap = ((round((i/8)-0.5))*100)
                ao=ao+15
                ap=ap+15
                image(wKingimg,(ao,ap),(70,70))

    if(wQueendisplay == True):
        aq = 0
        ar = 0
        for i in range(0,64):
            if(board[i] == wQueen):
                aq = ((i%8)) *100
                ar = ((round((i/8)-0.5))*100)
                aq=aq+15
                ar=ar+15
                image(wQueenimg,(aq,ar),(70,70))

    if(wBishop2display == True):
        at = 0
        au = 0
        for i in range(0,64):
            if(board[i] == wBishop2):
                at = ((i%8)) *100
                au = ((round((i/8)-0.5))*100)
                at=at+15
                au=au+15
                image(wBishop,(at,au),(70,70))
    
    if(wKnight2display == True):
        av = 0
        aw = 0
        for i in range(0,64):
            if(board[i] == wKnight2):
                av = ((i%8)) *100
                aw = ((round((i/8)-0.5))*100)
                av=av+15
                aw=aw+15
                image(wKnight,(av,aw),(70,70))

    if(wRook2display == True):
        ax = 0
        ay = 0
        for i in range(0,64):
            if(board[i] == wRook2):
                ax = ((i%8)) *100
                ay = ((round((i/8)-0.5))*100)
                ax=ax+15
                ay=ay+115
                image(wRook,(ax,ay),(70,70))

    if(wPawn1display == True):
        az = 0
        ba = 0
        for i in range(0,64):
            if(board[i] == wPawn1):
                az = ((i%8)) *100
                ba = ((round((i/8)-0.5))*100)
                az=az+15
                ba=ba+15
                image(wPawn,(az,ba),(70,70))
    
    if(wPawn2display == True):
        bb = 0
        bc = 0
        for i in range(0,64):
            if(board[i] == wPawn2):
                bb = ((i%8)) *100
                bc = ((round((i/8)-0.5))*100)
                bb=bb+15
                bc=bc+15
                image(wPawn,(bb,bc),(70,70))

    if(wPawn3display == True):
        bd = 0
        be = 0
        for i in range(0,64):
            if(board[i] == wPawn3):
                bd = ((i%8)) *100
                be = ((round((i/8)-0.5))*100)
                bd=bd+15
                be=be+15
                image(wPawn,(bd,be),(70,70))

    if(wPawn4display == True):
        bf = 0
        bg = 0
        for i in range(0,64):
            if(board[i] == wPawn4):
                bf = ((i%8)) *100
                bg = ((round((i/8)-0.5))*100)
                bf=bf+15
                bg=bg+15
                image(wPawn,(bf,bg),(70,70))


    if(wPawn5display == True):
        bh = 0
        bi = 0
        for i in range(0,64):
            if(board[i] == wPawn5):
                bh = ((i%8)) *100
                bi = ((round((i/8)-0.5))*100)
                bh=bh+15
                bi=bi+15
                image(wPawn,(bh,bi),(70,70))
    
    if(wPawn6display == True):
        bj = 0
        bk = 0
        for i in range(0,64):
            if(board[i] == wPawn6):
                bj = ((i%8)) *100
                bk = ((round((i/8)-0.5))*100)
                bj=bj+15
                bk=bk+15
                image(wPawn,(bj,bk),(70,70))

    if(wPawn7display == True):
        bl = 0
        bm = 0
        for i in range(0,64):
            if(board[i] == wPawn7):
                bl = ((i%8)) *100
                bm = ((round((i/8)-0.5))*100)
                bl=bl+15
                bm=bm+15
                image(wPawn,(bl,bm),(70,70))


                
    
    if(wPawn8display == True):
        bn = 0
        bo = 0
        for i in range(0,64):
            if(board[i] == wPawn8):
                bn = ((i%8)) *100
                bo = ((round((i/8)-0.5))*100)
                bn=bn+15
                bo=bo+15
                image(wPawn,(bn,bo),(70,70))

    move()

def move():
    
    global bRook, bPawn, bQueenimg, bKingimg, bBishop, bKnight, wRook, wPawn, wQueenimg , wKingimg , wBishop, wKnight, board, wKing,wQueen,bKing,bQueen, bRook1display,  bRook2display ,bQueendisplay,bKingdisplay,bBishop1display, bBishop2display, bKnight1display, bKnight2display,bPawn1display,bPawn2display,bPawn3display,bPawn4display, bPawn5display, bPawn6display, bPawn7display, bPawn8display, wRook1display, wRook2display ,wQueendisplay,wKingdisplay,wBishop1display, wBishop2display, wKnight1display, wKnight2display,wPawn1display,wPawn2display,wPawn3display,wPawn4display, wPawn5display, wPawn6display, wPawn7display, wPawn8display, wTurn,bTurn, tempVal, tempPos, mp, mouseisreleased, pmX, pmY, newarraypos, newval, newpos, mX, mY, arraypos,pieceValue 

    if(wTurn==True):
        bTurn = False
    elif(wTurn==False):
        bTurn = True

    if(bTurn==True):
        wTurn = False
    elif(bTurn==False):
        wTurn = True


    if mouse_is_pressed:
        mp=True
        pmX=(round((mouse_x/100)+0.5))
        pmY=(round((mouse_y/100+0.5)))
        arraypos = int((8*(pmY-1))+(pmX-1))
        pieceValue = board[arraypos] 
        if(pieceValue == 0):
            print()            
        else:
            tempVal = board[arraypos]
            tempPos= arraypos
            #print(tempVal)       #val assigned above
            #print(tempPos)       #0-64  
       
    if (mp==True) and (mouse_is_pressed == False): 
        mp=False
        mX=(round((mouse_x/100)+0.5))
        mY=(round((mouse_y/100+0.5)))
        newarraypos = int((8*(mY-1))+(mX-1))
        board[newarraypos] = pieceValue
        board[arraypos] = 0

             





   
if __name__ == '__main__':
    run()