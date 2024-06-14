# pip install pyzmq cbor keyboard
from zmqRemoteApi import RemoteAPIClient
from zmqRemoteApi_IPv6 import RemoteAPIClient
import keyboard
import random
import math

client = RemoteAPIClient('120.113.99.21', 23000)
# client = RemoteAPIClient('2001:288:6004:17:2023:cda:4:6', 23000)

print('Program started')
sim = client.getObject('sim')
# sim.startSimulation()
print('Simulation started')

v = 8
a = 40

# 選擇控制的球員
# player = '/a_player1'
# player = '/a_player2'
# player = '/a_player3'
# player = '/a_player4'
player = '/b_player1'
# player = '/b_player2'
# player = '/b_player3'
# player = '/b_player4'


def setVelocity(lfwV, rfwV, lbwV, rbwV):
    leftMotor1 = sim.getObject(player + '/joint_lf')
    rightMotor1 = sim.getObject(player + '/joint_rf')
    leftMotor2 = sim.getObject(player + '/joint_lb')
    rightMotor2 = sim.getObject(player + '/joint_rb')
    sim.setJointTargetVelocity(leftMotor1, lfwV)
    sim.setJointTargetVelocity(rightMotor1, rfwV)
    sim.setJointTargetVelocity(leftMotor2, lbwV)
    sim.setJointTargetVelocity(rightMotor2, rbwV)
    # 輸入四個變數分別給四個軸速度


def setAngel(y):
    ontology = sim.getObject(player)
    angel = [-90 * math.pi / 180, y * math.pi / 180, 0 * math.pi / 180]
    leftMotor = sim.getObject(player + '/joint_lf')
    rightMotor = sim.getObject(player + '/joint_rf')
    sim.setObjectOrientation(leftMotor, ontology, angel)
    sim.setObjectOrientation(rightMotor, ontology, angel)
    # 輸入一個變數改變前輪方向


def controlAngel(y):
    if keyboard.is_pressed('a'):
        setAngel(-y)
    elif keyboard.is_pressed('d'):
        setAngel(y)
    else:
        setAngel(0)


def turnover():
    floor = sim.getObject('/Floor')
    player1 = sim.getObject(player)
    a = sim.getObjectOrientation(player1, floor)
    b = sim.getObjectPosition(player1, floor)
    a[0] = 0
    a[1] = 0
    b[2] = 0.3
    sim.setObjectPosition(player1, floor, b)
    sim.setObjectOrientation(player1, floor, a)


def playerControl(x, y):
    if keyboard.is_pressed('w'):
        setVelocity(x, x, x, x)
        controlAngel(y)
    elif keyboard.is_pressed('s'):
        setVelocity(-x, -x, -x, -x)
        controlAngel(y)
    elif keyboard.is_pressed('a'):
        setVelocity(-x, x, -x, x)
    elif keyboard.is_pressed('d'):
        setVelocity(x, -x, x, -x)
    elif keyboard.is_pressed('space'):
        turnover()
    elif keyboard.is_pressed('q'):
        # stop simulation
        sim.stopSimulation()
    else:
        setVelocity(0, 0, 0, 0)
        setAngel(0)


while True:
    if keyboard.is_pressed('shift'):
        playerControl(v + 4, a - 20)
    else:
        playerControl(v, a)
