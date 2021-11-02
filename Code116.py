import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
import random

# 함수 선언
def connectMYSQL() :
    
    global conn, curr, window, canvas
    
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='kingHotDB', charset='utf8')
    curr = conn.cursor()

def closeMYSQL() :
    global conn, curr, window, canvas
    curr.close()
    conn.close()
    curr, conn = None, None

def randomColor() :
    COLORS = ["red", "green", "blue", "magenta", "orange", "brown", "maroon", "coral"]
    return random.choice(COLORS)


def clearMap() :
    global conn, curr, window, canvas
    canvas.destroy()
    canvas = Canvas(window, height=SCR_HEIGHT, width=SCR_WIDTH)
    canvas.pack()

def displayRestarunt() :
    global conn, curr, window, canvas
    connectMYSQL()

    sql = "select restName, ST_AsText((ST_Buffer(restLocation, 3))) from restaurant"
    curr.execute(sql)

    while True:
        row = curr.fetchone()
        if not row:
            break;
        restName, gisStr = row
        start = gisStr.index('(') + 2
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        gisList = gisStr.split(',')
        
        newGisList = []

        for xyStr in gisList :
            x, y = xyStr.split(' ') # x, y 를 분리
            x, y = float(x), float(y)
            xyList = [ (x+90)*2, SCR_HEIGHT-(y+90)*2] #맨 위가 0, 아래가 360이기 때문에 y는 기준값에서 -형식
            newGisList.append(xyList)

        myColor = randomColor()
        canvas.create_line(newGisList, fill=myColor, width=3)
        tx, ty = xyList[0], xyList[1]+15
        canvas.create_text([tx, ty], fill=myColor, text=restName.split(' ')[2])
        # 왕매워 짬뽕 1호점을 스페이스 단위로 나눈뒤 [2]인덱스인 호점을 반환

    closeMYSQL()

def displayManger() :
    global conn, curr, window, canvas
    connectMYSQL()
    color = ["white", "yello"]

    sql = "select managername, ST_AsText(Area) from manager order by managername"    
    curr.execute(sql)

    while True:
        row = curr.fetchone()
        if not row:
            break;
        managerName, gisStr = row
        start = gisStr.index('(') + 2
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        gisList = gisStr.split(',')
        newGisList = []
        for xyStr in gisList :
            x, y = xyStr.split(' ')
            x, y = float(x), float(y)
            xyList = [ (x+90)*2, SCR_HEIGHT-(y+90)*2]
            newGisList.append(xyList)

        if managerName == "존밴이" :
            canvas.create_polygon(newGisList, fill="gray")
        else :
            canvas.create_polygon(newGisList, fill="yellow")
    
    closeMYSQL()

def displayRoad() :
    global conn, curr, window, canvas
    connectMYSQL()

    sql = "select roadname, ST_AsText(ST_BUFFER(RoadLine, 2)) from road"    
    curr.execute(sql)

    while True:
        row = curr.fetchone()
        if not row:
            break;
        managerName, gisStr = row
        start = gisStr.index('(')+2
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        gisList = gisStr.split(',')
        newGisList = []
        for xyStr in gisList :
            x, y = xyStr.split(' ')
            x, y = float(x), float(y)
            xyList = [ (x+90)*2, SCR_HEIGHT-(y+90)*2]
            newGisList.append(xyList)

        canvas.create_polygon(newGisList, fill=randomColor())

    closeMYSQL()

def showResMan() :
    global conn, curr, window, canvas

    displayRestarunt()

    connectMYSQL()
    sql = "select M.managername, R.restname, ST_AsText((ST_Buffer(R.restlocation, 3))) from restaurant R, manager M where ST_Contains(M.area, R.restLocation) = 1 order by R.restname"

    curr.execute(sql)

    saveRest = ''
    i = 1
    while True:
        
        row = curr.fetchone()
        if not row:
            break;
        managerName, restName, gisStr = row
        print(i)
        print("saveRest"+saveRest)
        start = gisStr.index('(')+2
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        gisList = gisStr.split(',')
        newGisList = []
        for xyStr in gisList :
            x, y = xyStr.split(' ')
            x, y = float(x), float(y)
            xyList = [ (x+90)*2, SCR_HEIGHT-(y+90)*2]
            newGisList.append(xyList)
        print(saveRest)
        myColor = randomColor()
        if saveRest == restName :
            canvas.create_polygon(newGisList, fill=myColor)

        if saveRest == restName:
            tx, ty = xyList[0], xyList[1]+45
        else :
            tx, ty = xyList[0], xyList[1]+30
        
        canvas.create_text([tx, ty], fill=myColor, text=managerName)
        saveRest = restName
        i += 1
    
    closeMYSQL()

def showNearest() :
    global conn, curr, window, canvas

    baseRest = '왕매워 짬뽕 ' + askstring('기준 체인점', '체인점 번호를 입력하세요') + '호점'

    connectMYSQL()
    sql = "select ST_AsText(R2.restlocation), ST_Distance(R1.restlocation, R2.restlocation) from restaurant R1, restaurant R2 where R1.restname = '"+baseRest+"' order by ST_Distance(R1.restlocation, r2.restlocation)"
    curr.execute(sql)

    row = curr.fetchone()
    gisStr, distance = row
    start = gisStr.index('(')
    start += 1
    end = gisStr.index(')')
    gisStr = gisStr[start:end]
    x, y = list(map(float, gisStr.split(' ')))
    baseXY = [ (x+90)*2, SCR_HEIGHT-(y+90)*2]

    lineWidth = 20
    while True :
        row = curr.fetchone()
        if not row:
            break;
        gisStr, distance = row
        start = gisStr.index('(')
        start += 1
        end = gisStr.index(')')
        gisStr = gisStr[start:end]
        x, y = list(map(float, gisStr.split(' ')))
        targetXY = [ (x+90)*2, SCR_HEIGHT-(y+90)*2]

        myColor = randomColor()
        if lineWidth < 0 :
            lineWidth = 0
        canvas.create_line([baseXY, targetXY], fill=myColor, width=lineWidth)
        lineWidth -= 5

    closeMYSQL()

    displayRestarunt()

conn, curr = None, None
window, canvas = None, None

SCR_WIDTH, SCR_HEIGHT = 360, 360

window = Tk()
window.title("왕매워 짬뽕 ver 0.1")
canvas = Canvas(window, height=SCR_HEIGHT, width=SCR_WIDTH)
canvas.pack()

mainMenu = Menu(window)
window.config(menu=mainMenu)

gis1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="GIS 데이터 보기", menu=gis1Menu)
gis1Menu.add_command(label="체인점 보기", command=displayRestarunt)
gis1Menu.add_command(label="관리자 보기", command=displayManger)
gis1Menu.add_command(label="도로 보기", command=displayRoad)
gis1Menu.add_separator()
gis1Menu.add_command(label="화면 지우기", command=clearMap)
gis1Menu.add_separator()

gis2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="GIS 데이터 분석", menu=gis2Menu)
gis2Menu.add_command(label="관리자별 담당 체인점", command=showResMan)
gis2Menu.add_command(label="가장 가까운 체인점", command=showNearest)

window.mainloop()