  #Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
  #Type "copyright", "credits" or "license()" for more information.
  #>>>



import math
import time
from math import pi as M_PI
from Global_Variables_Only_Class import Global_Variables_Only_Class
GV = Global_Variables_Only_Class



#=======for servo stuff========================================
import time
#from adafruit_servokit import ServoKit
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
#kit = ServoKit(channels=16)
#GV.MAX_NUMBER_SERVOS = len(kit.servo)
GV.MAX_NUMBER_SERVOS = 12#12
#==============================================================




#for check cpu temperature
#from gpiozero import CPUTemperature
#CPU_Rep = CPUTemperature()



#^^^^^^^^^^^^^^^^^^^^^^^^^^IMPORTANT MATH GEOMETRY FUNCTIONS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def GetAngle(AX, AY, Bx, By, Cx, Cy):

  # Get the lengths of the triangle#s sides.
  side_a = math.sqrt(math.pow((float)((Bx - Cx)), 2) + math.pow((float)((By - Cy)), 2))
  side_b = math.sqrt(math.pow((float)((AX - Cx)), 2) + math.pow((float)((AY - Cy)), 2))
  side_c = math.sqrt(math.pow((float)((AX - Bx)), 2) + math.pow((float)((AY - By)), 2))

  #Calculate angle B between sides ab and bc.
  DDER = (math.pow(side_b, 2) - math.pow(side_a, 2) - math.pow(side_c, 2))
  DWE = (-2 * side_a * side_c)
  if DWE == 0:
    DWE = 0.00001
    #ENDEX================

  DDER = DDER / DWE
  if DDER == 0:
    DDER = 0.0001
  if DDER < -1:
    DDER = -1
  if DDER > 1:
    DDER = 1

  return (int)(math.acos(DDER) / M_PI * 180)
#ENDEX================


#calculate like 50%of100=50 and 50%of2=1 and so on #output
def PercentOF(Thispercent, OfThisNumIS):
  perhol = 0
  temp = Thispercent
  if Thispercent > 0 and OfThisNumIS > 0: 
    #perhol = Thispercent / 100
    perhol = temp / 100
  #ENDEX================
  return (int)(perhol * OfThisNumIS)
#ENDEX================



#calculate like 50%of100=50 and 50%of2=1 and so on #output
def PercentOFDecimal(Thispercent, OfThisNumIS):
  perhol = 0
  temp = Thispercent
  if Thispercent > 0 and OfThisNumIS > 0: 
    #perhol = Thispercent / 100
    perhol = temp / 100
  #ENDEX================
  return (perhol * OfThisNumIS)
#ENDEX================



#calculate 28%of140=20 %output
def WhatPercentOF(WhatPerOfThisNuM, isThis):
  perhol = 0
  temp = isThis
  if isThis > 0 and WhatPerOfThisNuM > 0: 
    #If isThis = 0 Then Exit Function
    perhol = temp / WhatPerOfThisNuM
  #ENDEX================
  return (int)(perhol * 100)
#ENDEX================


def Distance(AX, AY, BX, BY):
  #Calculates the distance between 2 points.
  return (int)(math.sqrt(math.pow(BX - AX, 2) + math.pow(BY - AY, 2)))
#ENDEX================
#==


#thetha calc Get angle between two points
def DeriveTheta(x, y, DestX, DestY):

  TempX = (float)(DestX - x)
  TempY = (float)(DestY - y)
  DeriveTheta_AngleOUT = 0

  if TempX == 0:
    TempX = 0.01
  if TempY == 0:
    TempY = 0.01
  if TempX >= 0:
    DeriveTheta_AngleOUT = round((math.atan(TempY / TempX) * 57.2957795130824 + 90))
  if TempX <= 0:
    DeriveTheta_AngleOUT = round((math.atan(TempY / TempX) * 57.2957795130824 + 270))

  return (int)(DeriveTheta_AngleOUT)
#ENDEX================
#========

#old
#float DegreesToRadians(float dDegrees)
#
#  return dDegrees * (M_PI / 180)
##ENDEX================

def DegreesToRadians(dDegrees):

  DegreesOUT = (float)(dDegrees * (M_PI / 180))
  return DegreesOUT
#ENDEX================

#new
def RadiansToDegrees(Radians):

  RadiansOUT = (Radians * 180) / M_PI
  return (int)(RadiansOUT)
#ENDEX================



#====360 star ref===================================
def Gqx(Ang, rad):

  Ang_Combine = 270 + Ang
  Degr = DegreesToRadians(Ang_Combine)
  x = (int)(rad * math.cos(Degr) + 0)
  GV.Gqy = (int)(rad * math.sin(Degr) + 0)
  return x
#ENDEX================
#============================================
#====360 star ref===================================
##def Gqy(Ang, rad):
##  Ang_Combine = 270 + Ang
##  Degr = DegreesToRadians(Ang_Combine)
##  #x = (int)(rad * math.cos(Degr) + 0)
##  y = (int)(rad * math.sin(Degr) + 0)
##  return y
###ENDEX================
#============================================

#get oposite 360 (but 180 = 0) and (0 = 180)
def O360(Ang_IN):
  Ang_Combine = 180 + Ang_IN
  Degr = DegreesToRadians(Ang_Combine)
  return RadiansToDegrees(Degr)
#ENDEX================

#360 revers
def Reverse_Angle(Ang_IN):

  temp_Result = 360 - Ang_IN
  if temp_Result < 0:
      temp_Result = 0 #ENDEX================
  if temp_Result > 360:
      temp_Result = 360 #ENDEX================
  return temp_Result
#ENDEX================

def Cn360(Ang_IN):

  Ang_Combine = 0 + Ang_IN
  Degr = DegreesToRadians(Ang_Combine)
  return RadiansToDegrees(Degr)
#ENDEX================


#function to invert servo data eg 0 = 180 and 180 back to 0 (handy for parts on the other side of the body)
def Reverse_Servo_Values_Func(Ang_IN):

  temp_Result = 180 - Ang_IN
  if temp_Result < 0:
      temp_Result = 0 #ENDEX================
  if temp_Result > 180:
      temp_Result = 180 #ENDEX================
  return temp_Result
#ENDEX================
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^END IMPORTANT MATH GEOMETRY FUNCTIONS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def Define_Acivity_Names_And_Numbers(Activity_Names_IN):
  GV.Total_Possible_Activities = GV.Total_Possible_Activities + 1
  #GV.Total_Possible_Activities += 1
  GV.Activity_Names_Collection[GV.Total_Possible_Activities] = Activity_Names_IN
  return GV.Total_Possible_Activities
#ENDEX================


def Add_Draw_Points(X_1_IN, Y_1_IN, X_2_IN, Y_2_IN, Default_Color_Select_IN):
  #defualt this is a point to be drawn 
  GV.Num_Point_To_Draw = GV.Num_Point_To_Draw + 1

  GV.Drawer_X[GV.Num_Point_To_Draw] = X_1_IN
  GV.Drawer_Y[GV.Num_Point_To_Draw] = Y_1_IN
  GV.This_is_a_Line[GV.Num_Point_To_Draw] = False
  GV.DrawMatrix_NUM[GV.Num_Point_To_Draw] = GV.DrawMatrix_NUM_IN
  GV.Default_Color_Select[GV.Num_Point_To_Draw] = Default_Color_Select_IN
  #if it is a line then include second point 
  if X_2_IN > 0 or Y_2_IN > 0:
    GV.Num_Point_To_Draw = GV.Num_Point_To_Draw + 1
    GV.Drawer_X[GV.Num_Point_To_Draw] = X_2_IN
    GV.Drawer_Y[GV.Num_Point_To_Draw] = Y_2_IN
    GV.This_is_a_Line[GV.Num_Point_To_Draw] = True#mark line end array num
    GV.DrawMatrix_NUM[GV.Num_Point_To_Draw] = GV.DrawMatrix_NUM_IN
    GV.Default_Color_Select[GV.Num_Point_To_Draw] = Default_Color_Select_IN
#===============================================================================================================


def Add_Limb_Joints_To_Draw(FOOT_ID_NUM_IN, upperArm_X, upperArm_Y, forearm_X, forearm_Y, foot_X, foot_Y, foot_IK_Target_X, foot_IK_Target_Y, forearmLength):
    GV.DrawMatrix_NUM_IN = 3

    #get the angle to and from
    Ang = DeriveTheta(forearm_X, forearm_Y, foot_IK_Target_X, foot_IK_Target_Y)
    if Ang > 360:
        Ang = 360 #ENDEX================
    if Ang < 0:
        Ang = 0 #ENDEX================
    #place and rotate Point_To_Foot_joint from elbow position
    Point_To_Foot_joint_X = forearm_X + Gqx(Ang, forearmLength)
    Point_To_Foot_joint_Y = forearm_Y + GV.Gqy#(Ang, forearmLength)
    #===========================================================




    #show me stuff
    Add_Draw_Points(upperArm_X, upperArm_Y, forearm_X, forearm_Y, 0)
    Add_Draw_Points(forearm_X, forearm_Y, Point_To_Foot_joint_X, Point_To_Foot_joint_Y, 0)
    Add_Draw_Points(foot_X, foot_Y, foot_IK_Target_X, foot_IK_Target_Y, 0)																					  #draw conecting lines
    Add_Draw_Points(GV.Uper_Arm_Angle_Help_X, GV.Uper_Arm_Angle_Help_Y, 0, 0, 0)
    #draw conecting joints
    select_Defalt_color = 0
    if FOOT_ID_NUM_IN == GV.RIGHT_FRONT_FOOT_ID_NUM or FOOT_ID_NUM_IN == GV.RIGHT_REAR_FOOT_ID_NUM:
       select_Defalt_color = 1#draw right side joints in red 
    #ENDEX================
    Add_Draw_Points(upperArm_X, upperArm_Y, 0, 0, select_Defalt_color)
    Add_Draw_Points(forearm_X, forearm_Y, 0, 0, select_Defalt_color)
    Add_Draw_Points(foot_X, foot_Y, 0, 0, select_Defalt_color)
    Add_Draw_Points(foot_IK_Target_X, foot_IK_Target_Y, 0, 0, select_Defalt_color)
    Add_Draw_Points(Point_To_Foot_joint_X, Point_To_Foot_joint_Y, 0, 0, select_Defalt_color)
    Add_Draw_Points(GV.Uper_Arm_Angle_HelpARR_X[FOOT_ID_NUM_IN], GV.Uper_Arm_Angle_HelpARR_Y[FOOT_ID_NUM_IN], 0, 0, select_Defalt_color)
    #----------------------


#ENDEX================
#=========================================================================






def Do_IK_And_Get_Limb_Angles_Front(FOOT_ID_NUM_IN, Add_Front_View_Foot_Y_lift_Value, upperArmLength, forearmLength, footLength):

  #combine front and side leg lifts to lift foot from both actions
  foot_Y = GV.Foot_Current_Pos_Y[FOOT_ID_NUM_IN] - Add_Front_View_Foot_Y_lift_Value
  foot_X = GV.Foot_Current_Pos_X[FOOT_ID_NUM_IN]

  upperArm_X = GV.Main_Joint_SideV_X[FOOT_ID_NUM_IN]
  upperArm_Y = GV.Main_Joint_SideV_Y[FOOT_ID_NUM_IN]
  TweekMe = 270#265,255


  i = 0

  foot_IK_Target_X = 0
  foot_IK_Target_Y = 0

  forearm_X = 0
  forearm_Y = 0

  Angle_Ajust = 0
  Angle_Ajust_INC = 0

  DistDif = 0
  Ang_First = 0

                                                           #get the angle to and from
  
  #place and rotate the foot_IK_Target to look at the main joint (upperarm joint)
  Ang = DeriveTheta(foot_X, foot_Y, upperArm_X, upperArm_Y)
  foot_IK_Target_X = foot_X + Gqx(Ang, footLength)
  foot_IK_Target_Y = foot_Y + GV.Gqy#(Ang, footLength)
  #===========================================================

  #\/they look at each other at the begining

  #place and rotate forearm_X from uparm position to look at the foot position
  Ang_First = DeriveTheta(upperArm_X, upperArm_Y, foot_X, foot_Y)
  forearm_X = upperArm_X + Gqx(Ang_First, upperArmLength)
  forearm_Y = upperArm_Y + GV.Gqy#(Ang_First, upperArmLength)
  #===========================================================


  #create IK of whole limb including foot=========================================
  for i in range(14):
  

    #place and rotate forearm_X from uparm position
    Ang = (Ang_First + Angle_Ajust)#200
    forearm_X = upperArm_X + Gqx(Ang, upperArmLength)
    forearm_Y = upperArm_Y + GV.Gqy#(Ang, upperArmLength)
    #===========================================================


    #get distance from point 1 to 2 to detect if there is a gap `
    Dstc = Distance(forearm_X, forearm_Y, foot_IK_Target_X, foot_IK_Target_Y)
    #
    DistDif = Dstc - forearmLength
    if forearmLength > Dstc:
      DistDif = forearmLength - Dstc
      #ENDEX================
    
    #leave if 
    if Dstc >= forearmLength:
      break
    #ENDEX================
    #------------------


    #see if the IK is close enough 
    if DistDif < 2: 
      break
    #ENDEX================
    else:
    
      #if distance is great then move a bit faster
      Angle_Ajust_INC = 1
      if DistDif > 4:
        Angle_Ajust_INC = 2
      #ENDEX================
      if DistDif >= 8:
        Angle_Ajust_INC = DistDif / 2
      #ENDEX================

      #bring the joints together to close the gap
      Angle_Ajust = Angle_Ajust + Angle_Ajust_INC
      #============================================ 
    #ENDEX================


  #ENDEX================
  #=============================================================



  #Use to extend GV.Uper_Arm_Angle_Help_X properly
  GV.Uper_Arm_Angle_HelpARR_X[FOOT_ID_NUM_IN] = upperArm_X + Gqx(GV.Hip_X_Tilt_Angle, 40)
  GV.Uper_Arm_Angle_HelpARR_Y[FOOT_ID_NUM_IN] = upperArm_Y + GV.Gqy#(GV.Hip_X_Tilt_Angle, 40)
  #===========================================================
  #get the angles
  GV.Uper_Arm_X_Angle_OUT = GetAngle(GV.Uper_Arm_Angle_HelpARR_X[FOOT_ID_NUM_IN], GV.Uper_Arm_Angle_HelpARR_Y[FOOT_ID_NUM_IN], upperArm_X, upperArm_Y, forearm_X, forearm_Y) #(point 3)
  if GV.Uper_Arm_X_Angle_OUT > 165:
    GV.Uper_Arm_X_Angle_OUT = 165
  GV.Fore_Arm_Angle_OUT = GetAngle(upperArm_X, upperArm_Y, forearm_X, forearm_Y, foot_IK_Target_X, foot_IK_Target_Y) #(point 3)
  if GV.Fore_Arm_Angle_OUT > 165:
    GV.Fore_Arm_Angle_OUT = 165
  #===========================================================

  #for drawing only (coment out in arduino IDE)
  if GV.Select_View_To_Draw_NUM == 3:
    Add_Limb_Joints_To_Draw(FOOT_ID_NUM_IN, upperArm_X, upperArm_Y, forearm_X, forearm_Y, foot_X, foot_Y, foot_IK_Target_X, foot_IK_Target_Y, forearmLength)


#ENDEX================



def Do_IK_And_Get_Limb_Angles(FOOT_ID_NUM_IN, upperArmLength, forearmLength, footLength):


  foot_Y = GV.Foot_Current_Pos_Y[FOOT_ID_NUM_IN]
  foot_X = GV.Foot_Current_Pos_X[FOOT_ID_NUM_IN]

  upperArm_X = GV.Main_Joint_SideV_X[FOOT_ID_NUM_IN]
  upperArm_Y = GV.Main_Joint_SideV_Y[FOOT_ID_NUM_IN]


  TweekMe = 255#255

  i = 0


  foot_IK_Target_X = 0
  foot_IK_Target_Y = 0

  Point_To_Foot_joint_X = 0
  Point_To_Foot_joint_Y = 0

  forearm_X = 0
  forearm_Y = 0

  #------For to rotate lowerfoot---------------------------------------------
  Hip_X_Independent_Angle_0_to_180 = 0
  #==========================================================
  Angle_Ajust = 0
  Angle_Ajust_INC = 0
  DistDif = 0

  #get hip to foot angle
  Hip_X_Independent_Angle_0_to_180 = GetAngle(GV.Uper_Arm_Angle_Help_X, GV.Uper_Arm_Angle_Help_Y, upperArm_X, upperArm_Y, foot_X, foot_Y) #(point 3)
    

  #create IK of whole limb including foot=========================================
  for i in range(20):
  


    #place and rotate the foot_IK_Target
    Ang = Cn360(Hip_X_Independent_Angle_0_to_180 + TweekMe + Angle_Ajust)
    foot_IK_Target_X = foot_X + Gqx(Ang, footLength)
    foot_IK_Target_Y = foot_Y + GV.Gqy#(Ang, footLength)
    #===========================================================


    #place and rotate elbow from hip position
    Ang = O360(Ang)
    forearm_X = upperArm_X + Gqx(Ang, upperArmLength)
    forearm_Y = upperArm_Y + GV.Gqy#(Ang, upperArmLength)
    #===========================================================




    #get distance from point 1 to 2 to detect if there is a gap 
    #Dstc = Distance(Point_To_Foot_joint_X, Point_To_Foot_joint_Y, foot_IK_Target_X, foot_IK_Target_Y)
    Dstc = Distance(forearm_X, forearm_Y, foot_IK_Target_X, foot_IK_Target_Y)
    #
    DistDif = Dstc - forearmLength
    if forearmLength > Dstc:
      DistDif = forearmLength - Dstc
    #ENDEX================

    #leave if 
    if Dstc > forearmLength:
      Ang = GetAngle(upperArm_X, upperArm_Y, forearm_X, forearm_Y, foot_IK_Target_X, foot_IK_Target_Y) #(point 3)
      if Ang > 165:#175 good
        break
      #ENDEX================
    #ENDEX================


    #see if the IK is close enough 
    if DistDif < 2:
    
      break
    #ENDEX================
    else:
    
      #if distance is great then move a bit faster
      Angle_Ajust_INC = 1
      if DistDif > 4:
        Angle_Ajust_INC = 2
      #ENDEX================
      if DistDif > 8:
        Angle_Ajust_INC = 3
      #ENDEX================

      #if angle is more close to 0 then seperate the angles to bring the joints together to close the gap
      if Dstc > forearmLength:
        Angle_Ajust = Angle_Ajust + Angle_Ajust_INC
      #ENDEX================
      else:#bring angles together to close the gap
        Angle_Ajust = Angle_Ajust - Angle_Ajust_INC
      #ENDEX================

      #============================================ 
    #ENDEX================
  #ENDEX================
  #=============================================================




  #Use to extend GV.Uper_Arm_Angle_Help_X properly
  GV.Uper_Arm_Angle_HelpARR_X[FOOT_ID_NUM_IN] = upperArm_X + Gqx(GV.Shoulder_X_Tilt_Angle, 40)
  GV.Uper_Arm_Angle_HelpARR_Y[FOOT_ID_NUM_IN] = upperArm_Y + GV.Gqy#(GV.Shoulder_X_Tilt_Angle, 40)
  #===========================================================
  #get the angles
  GV.Uper_Arm_X_Angle_OUT = GetAngle(GV.Uper_Arm_Angle_HelpARR_X[FOOT_ID_NUM_IN], GV.Uper_Arm_Angle_HelpARR_Y[FOOT_ID_NUM_IN], upperArm_X, upperArm_Y, forearm_X, forearm_Y) #(point 3)
  GV.Fore_Arm_Angle_OUT = GetAngle(upperArm_X, upperArm_Y, forearm_X, forearm_Y, foot_IK_Target_X, foot_IK_Target_Y) #(point 3)
  #===========================================================

  #for drawing only (coment out in arduino IDE)
  if GV.Select_View_To_Draw_NUM == 3:
    Add_Limb_Joints_To_Draw(FOOT_ID_NUM_IN, upperArm_X, upperArm_Y, forearm_X, forearm_Y, foot_X, foot_Y, foot_IK_Target_X, foot_IK_Target_Y, forearmLength)

#ENDEX================













def DriveServos():


  servonumber = 0




  #----colect the angles to servo data array

  #Head (NEWLY moved to the front of servo output pins cause Head X cable is short)
  GV.ServoAnglePos[0] = Reverse_Servo_Values_Func(GV.Head_X_Rotation_Angle)
  GV.ServoAnglePos[1] = Reverse_Servo_Values_Func(GV.Head_Y_Rotation_Angle)
  
  GV.ServoAnglePos[2] = GV.Left_Rear_Uper_Arm_X_Angle
  GV.ServoAnglePos[3] = GV.Left_Rear_Fore_Arm_Angle
  #
  GV.ServoAnglePos[4] = Reverse_Servo_Values_Func(GV.Left_Front_Uper_Arm_X_Angle)
  GV.ServoAnglePos[5] = Reverse_Servo_Values_Func(GV.Left_Front_Fore_Arm_Angle)
  #
  GV.ServoAnglePos[6] = Reverse_Servo_Values_Func(GV.Right_Rear_Uper_Arm_X_Angle)
  GV.ServoAnglePos[7] = Reverse_Servo_Values_Func(GV.Right_Rear_Fore_Arm_Angle)
  #
  GV.ServoAnglePos[8] = GV.Right_Front_Uper_Arm_X_Angle
  GV.ServoAnglePos[9] = GV.Right_Front_Fore_Arm_Angle
  #
  GV.ServoAnglePos[10] = GV.Left_Front_Uper_Arm_Z_Angle
  GV.ServoAnglePos[11] = Reverse_Servo_Values_Func(GV.Right_Front_Uper_Arm_Z_Angle)
  #------------------------------------------------------------



  #-Drive the servos using the angles data colected above)---------------------------------------------------------
  #for servonumber in range(GV.MAX_NUMBER_SERVOS):
  # kit.servo[servonumber].angle = GV.ServoAnglePos[servonumber]
  #-----------------------------------------------------------
  
  #give a little time for servos
  time.sleep(0.0004)#0.0004
  
#ENDEX================#def loop
#--------------------end loop---------------------------------------------------------------------------------------------------------------------------------------





def Get_HalfWay_Point(Point_1_X, Point_1_Y, Point_2_X, Point_2_Y):
  #For center Point 1 get distance from point 1 to 2
  Dist = Distance(Point_1_X, Point_1_Y, Point_2_X, Point_2_Y)
  #get the angle from point 1 to 2
  Ang = DeriveTheta(Point_1_X, Point_1_Y, Point_2_X, Point_2_Y)
  #get half way distance between 1 and 2
  HalfDist = Dist / 2
  #now get the half way point
  GV.Half_Point_Out_X = Point_1_X + Gqx(Ang, HalfDist)
  GV.Half_Point_Out_Y = Point_1_Y + GV.Gqy#(Ang, HalfDist)
#------------------------------------------------------------------------------------------------



#==detect foot grounded using feet Y positions cleaner for walking
def Detect_Virtual_Foot_grounded(Foot_ID_NUM_IN):
  
  #do
  if GV.Foot_Current_Pos_Y[Foot_ID_NUM_IN] > GV.Ground_Level_Y:
    GV.Foot_Current_Pos_Y[Foot_ID_NUM_IN] = GV.Ground_Level_Y
    GV.Foot_Grounded[Foot_ID_NUM_IN] = 1
  #ENDEX================
  if GV.Foot_Current_Pos_Y[Foot_ID_NUM_IN] < GV.Ground_Level_Y:
    GV.Foot_Grounded[Foot_ID_NUM_IN] = 0
#ENDEX================








def Get_Feet_Positions_IDS():

  #get feet positioning sumary ID number
  GV.Front_Feet_Positions_ID = 0
  #Feet are at reset position
  if GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM] == GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM]:
    GV.Front_Feet_Positions_ID = 1
  #ENDEX================
  #Feet are at reset position
  if GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM] > GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM]:
    GV.Front_Feet_Positions_ID = 2
  #ENDEX================
      #Feet are at reset position
  if GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM] > GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM]:
    GV.Front_Feet_Positions_ID = 3
  #ENDEX================
  #==================================================================
    #get feet positioning sumary ID number
  GV.Rear_Feet_Positions_ID = 0
  #Feet are at reset position
  if GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM] == GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM]:
    GV.Rear_Feet_Positions_ID = 1
  #ENDEX================
  #Feet are at reset position
  if GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM] > GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM]:
    GV.Rear_Feet_Positions_ID = 2
  #ENDEX================
      #Feet are at reset position
  if GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM] > GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM]:
    GV.Rear_Feet_Positions_ID = 3
  #ENDEX================
  #==================================================================




#will only ancount for a few of the posible feet positions which are used in walk cycles (walk will be interupted only at certain points to allow few needed feet posibilities)
def Feet_Move_Sequence_Selector(Walk_Type_IN):


  #decide which foot move sequence to use in the walk based on the wheater we are walking forward or backward 
  if Walk_Type_IN == GV.WALK_TYPE_01:#WALK FORWARD

    #if we turned to the right then switch the feet sequence
    if GV.Sholder_Rotate_Angle > 90:
      GV.Feet_Move_Sequence[1] = GV.RIGHT_REAR_FOOT_ID_NUM
      GV.Feet_Move_Sequence[2] = GV.RIGHT_FRONT_FOOT_ID_NUM
      GV.Feet_Move_Sequence[3] = GV.LEFT_REAR_FOOT_ID_NUM
      GV.Feet_Move_Sequence[4] = GV.LEFT_FRONT_FOOT_ID_NUM
      GV.Selected_Feet_Sequence = 1
    else:
       #If all feet are all at defualt position then use normal walk sequence
      GV.Feet_Move_Sequence[1] = GV.LEFT_REAR_FOOT_ID_NUM
      GV.Feet_Move_Sequence[2] = GV.LEFT_FRONT_FOOT_ID_NUM
      GV.Feet_Move_Sequence[3] = GV.RIGHT_REAR_FOOT_ID_NUM
      GV.Feet_Move_Sequence[4] = GV.RIGHT_FRONT_FOOT_ID_NUM
      GV.Selected_Feet_Sequence = 2
      #-------------------------------------------------------------------
    
    
    #If right feet are in front of left feet
    if GV.Rear_Feet_Positions_ID == 2 and GV.Front_Feet_Positions_ID == 2:
      GV.Feet_Move_Sequence[1] = GV.LEFT_REAR_FOOT_ID_NUM
      GV.Feet_Move_Sequence[2] = GV.LEFT_FRONT_FOOT_ID_NUM
      GV.Feet_Move_Sequence[3] = GV.RIGHT_REAR_FOOT_ID_NUM
      GV.Feet_Move_Sequence[4] = GV.RIGHT_FRONT_FOOT_ID_NUM
      GV.Selected_Feet_Sequence = 3
    #If left feet are in front of right feet
    if GV.Rear_Feet_Positions_ID == 3 and GV.Front_Feet_Positions_ID == 3:
      GV.Feet_Move_Sequence[1] = GV.RIGHT_REAR_FOOT_ID_NUM
      GV.Feet_Move_Sequence[2] = GV.RIGHT_FRONT_FOOT_ID_NUM
      GV.Feet_Move_Sequence[3] = GV.LEFT_REAR_FOOT_ID_NUM
      GV.Feet_Move_Sequence[4] = GV.LEFT_FRONT_FOOT_ID_NUM
      GV.Selected_Feet_Sequence = 4
  #-----------------------------------------------------------


  #RETURN TO IDLE
  if Walk_Type_IN == GV.WALK_TO_IDLE:
    #SET DEFAULT (this feet see quence will
    GV.Feet_Move_Sequence[1] = GV.LEFT_REAR_FOOT_ID_NUM
    GV.Feet_Move_Sequence[2] = GV.RIGHT_REAR_FOOT_ID_NUM
    GV.Feet_Move_Sequence[3] = GV.LEFT_FRONT_FOOT_ID_NUM
    GV.Feet_Move_Sequence[4] = GV.RIGHT_FRONT_FOOT_ID_NUM
    GV.Selected_Feet_Sequence = 5


#-end decide feet sequence---------------------------------------------------------------------------------------------




#function to set feet targets Side view (target are set in front or behind the initial foot positions (default feet positions)
def Set_Feet_Trajectory_Targets_SideV(Left_Feet_Target, Right_Feet_Target):

  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Hip_Position_X + GV.Inital_Rear_Foot_SideV_Position_X + Left_Feet_Target
  GV.Foot_Traje_Target_Y[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Ground_Level_Y
  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_X + GV.Inital_Front_Foot_SideV_Position_X + Left_Feet_Target
  GV.Foot_Traje_Target_Y[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Ground_Level_Y
  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Hip_Position_X + GV.Inital_Rear_Foot_SideV_Position_X + Right_Feet_Target
  GV.Foot_Traje_Target_Y[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Ground_Level_Y
  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_X + GV.Inital_Front_Foot_SideV_Position_X + Right_Feet_Target
  GV.Foot_Traje_Target_Y[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Ground_Level_Y
  #====================================================================
#ENDEX================

#function to set feet targets Side view (this one sets one target for front feet and one target for rear feet instead of one for left and one for right feet
def Set_Feet_Trajectory_Targets_SideV2(Front_Feet_Target, Rear_Feet_Target):

  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Hip_Position_X + GV.Inital_Rear_Foot_SideV_Position_X + Rear_Feet_Target
  GV.Foot_Traje_Target_Y[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Ground_Level_Y
  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_X + GV.Inital_Front_Foot_SideV_Position_X + Front_Feet_Target
  GV.Foot_Traje_Target_Y[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Ground_Level_Y
  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Hip_Position_X + GV.Inital_Rear_Foot_SideV_Position_X + Rear_Feet_Target
  GV.Foot_Traje_Target_Y[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Ground_Level_Y
  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_X + GV.Inital_Front_Foot_SideV_Position_X + Front_Feet_Target
  GV.Foot_Traje_Target_Y[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Ground_Level_Y
  #====================================================================
#ENDEX================

def Set_Feet_Trajectory_Targets_FrontV(Stride_FrontV_Left_Target, Stride_FrontV_Right_Target):


  #create the feet target group for Front View and move it with the GV.Hip_Position_X value
  #Stride_FrontV_Left_Target = -40
  #Stride_FrontV_Right_Target = 40
  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM] = GV.Uper_Body_Front_Side_Turn_Mover + GV.Inital_Left_Foot_FrontV_Position_X + Stride_FrontV_Left_Target
  GV.Foot_Traje_Target_Y[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM] = GV.Ground_Level_Y
  #place the feet default positions============================================================
  GV.Foot_Traje_Target_X[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM] = GV.Uper_Body_Front_Side_Turn_Mover + GV.Inital_Right_Foot_FrontV_Position_X + Stride_FrontV_Right_Target
  GV.Foot_Traje_Target_Y[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM] = GV.Ground_Level_Y
  #====================================================================================================
#ENDEX================







#takes in from and to points (values) and chops increament to reach destination in 100 ticks (helps syncronize two or more seperate movements)
def Move_To_Destination_In_100_Ticks(Fromt_Value, To_Value, Output_Array_IN):

  i = 0
  
  #get the distance between distination point and current point
  destDist = Fromt_Value - To_Value
  if destDist < 0:
    destDist = To_Value - Fromt_Value
  #Get the 1 percent increment percent to use to increment to destination
  Decimal_1_Percent_INC = PercentOFDecimal(1, destDist)
  if Decimal_1_Percent_INC < 0.0001:
    Decimal_1_Percent_INC = 0.0001
  #--------------------------------------------------------------

  #Get the start position
  From_Start_Point_INC = Fromt_Value


  #increment in +ev direction
  if Fromt_Value < To_Value:
    for i in range(101):
      From_Start_Point_INC = From_Start_Point_INC + Decimal_1_Percent_INC
      if From_Start_Point_INC > To_Value:
        From_Start_Point_INC = To_Value
      #==
      Output_Array_IN[i] = (int) (From_Start_Point_INC)
  #------------------------------------------------
  
  #increment in -ev direction
  if Fromt_Value > To_Value:
    for i in range(101):
      From_Start_Point_INC = From_Start_Point_INC - Decimal_1_Percent_INC
      if From_Start_Point_INC < To_Value:
        From_Start_Point_INC = To_Value
      #==
      Output_Array_IN[i] = (int) (From_Start_Point_INC)
  #------------------------------------------------
  
#=======================================================================================================





#returns the ID num of the foot oposite balance of the input foot
def Get_Oposite_Foot(Foot_ID_NUM):
  Oposite_Foot_ID_NUM = 0
  
  #if this is Left Rear foot
  if Foot_ID_NUM == GV.LEFT_REAR_FOOT_ID_NUM:
    Oposite_Foot_ID_NUM = GV.RIGHT_FRONT_FOOT_ID_NUM
  #ENDEX================
    #if this is Left Rear foot
  if Foot_ID_NUM == GV.RIGHT_FRONT_FOOT_ID_NUM:
    Oposite_Foot_ID_NUM = GV.LEFT_REAR_FOOT_ID_NUM
  #ENDEX================
  #if this is Rith Rear foot
  if Foot_ID_NUM == GV.RIGHT_REAR_FOOT_ID_NUM:
    Oposite_Foot_ID_NUM = GV.LEFT_FRONT_FOOT_ID_NUM
  #ENDEX================
    #if this is Right front foot
  if Foot_ID_NUM == GV.LEFT_FRONT_FOOT_ID_NUM:
    Oposite_Foot_ID_NUM = GV.RIGHT_REAR_FOOT_ID_NUM
  #ENDEX================
  return Oposite_Foot_ID_NUM
#------------------------------------------------------------------------------------------








class Global_Essentials_Class():

  
  def GVO(in_GV):
    in_GV = GV



  #using sensors to make sure at feet are still on the ground (robot is not lifted off ground)
  def Get_Body_Feet_Grounded():
    Feet_Adjust_Done = False
      
    GV.SensorS_Values[GV.Left_Front_Sensor_VAL] = GPIO.input(Left_Front_Foot_Force_Sensor_Pin)
    GV.SensorS_Values[GV.Right_Front_Sensor_VAL] = GPIO.input(Right_Front_Foot_Force_Sensor_Pin)
    
    #make sure the body has tilted enough by detecting the oposite balance foot sensor has recieved body weight
    if GV.SensorS_Values[GV.LEFT_FRONT_FOOT_ID_NUM] >= GV.Ground_Presure_Sensivity or GV.SensorS_Values[GV.RIGHT_FRONT_FOOT_ID_NUM] >= GV.Ground_Presure_Sensivity:
      Feet_Adjust_Done = True
    #ENDEX================
    return Feet_Adjust_Done
  #------------------------------------------------------------------------------------------







  #Initialize feet positions
  def Initialize_Positions():



    i = 0
    Grouping_Num = 12#10
    #create angles grouping ref for head accel values grouping
    for i in range(190):
      if i > (Grouping_Num + 11):#9
        Grouping_Num = Grouping_Num + 12#10
        if Grouping_Num > 165:
          Grouping_Num = 165
      #-----
      #colect the grouping angle
      GV.Group_Angles_180[i] = Grouping_Num
    #====================================


    

    #==============================
    GV.Rear_upperArmLength = 59#58
    GV.Rear_forearmLength = 59#58
    GV.Rear_footLength = 50

    GV.Front_upperArmLength = 60#56
    GV.Front_forearmLength = 60#60
    GV.Front_footLength = 38#36
    #==============================
    #GV.TempWidth = 640#Cannyout.cols
    #GV.TempHeight = 480#Cannyout.rows
    GV.TempWidth = 660#Cannyout.cols
    GV.TempHeight = 660#Cannyout.rows
    GV.screen_Center = GV.TempWidth / 2


    GV.Ground_Level_Y = 300#320


    #for side view body center and x rotation center
    GV.Body_X_Tilt_Angle = 90#90
    GV.Body_Torso_Radius = 90
    GV.Uper_Body_Front_Back_Mover = 10000#320#move it far into the world away from zero (incase we have to walk backward) so we dont produce -ev vals
    GV.Body_Height = 140#135 170
    GV.BodyHeight_Total = GV.Ground_Level_Y - GV.Body_Height#170


    #get the body center 
    GV.Body_Center_X = GV.Uper_Body_Front_Back_Mover
    GV.Body_Center_Y = GV.BodyHeight_Total
    #place the hip
    GV.Hip_X_Tilt_Angle = Cn360(GV.Body_X_Tilt_Angle + 180)
    GV.Hip_Position_X = GV.Body_Center_X + Gqx(GV.Hip_X_Tilt_Angle, GV.Body_Torso_Radius)
    GV.Hip_Position_Y = GV.Body_Center_Y + GV.Gqy#(GV.Hip_X_Tilt_Angle, GV.Body_Torso_Radius)
    #place the Shoulder
    GV.Shoulder_X_Tilt_Angle = Cn360(GV.Body_X_Tilt_Angle)
    GV.Shoulder_Position_X = GV.Body_Center_X + Gqx(GV.Shoulder_X_Tilt_Angle, GV.Body_Torso_Radius)
    GV.Shoulder_Position_Y = GV.Body_Center_Y + GV.Gqy#(GV.Shoulder_X_Tilt_Angle, GV.Body_Torso_Radius)
    #place the uper arm angle helpers
    GV.Uper_Arm_Angle_Help_X = GV.Body_Center_X
    GV.Uper_Arm_Angle_Help_Y = GV.Body_Center_Y
    #======================================================================




    GV.Inital_Front_Foot_SideV_Position_X = 0#0
    GV.Inital_Rear_Foot_SideV_Position_X = -55

    #place the feet default positions============================================================
    GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Hip_Position_X + GV.Inital_Rear_Foot_SideV_Position_X
    GV.Foot_Current_Pos_Y[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Ground_Level_Y
    #place the feet default positions============================================================
    GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_X + GV.Inital_Front_Foot_SideV_Position_X# +Move_Foot_INC
    GV.Foot_Current_Pos_Y[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Ground_Level_Y
    #place the feet default positions============================================================
    GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Hip_Position_X + GV.Inital_Rear_Foot_SideV_Position_X
    GV.Foot_Current_Pos_Y[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Ground_Level_Y
    #place the feet default positions============================================================
    GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_X + GV.Inital_Front_Foot_SideV_Position_X# +Move_Foot_INC
    GV.Foot_Current_Pos_Y[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Ground_Level_Y
    #====================================================================





    #place shoulder for front view
    GV.Uper_Body_Front_Side_Turn_Mover = 10000
    GV.Inital_Left_Foot_FrontV_Position_X = 35
    GV.Inital_Right_Foot_FrontV_Position_X = -35


    #place left and right feet
    GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM] = GV.Uper_Body_Front_Side_Turn_Mover + GV.Inital_Left_Foot_FrontV_Position_X
    GV.Foot_Current_Pos_Y[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM] = GV.Ground_Level_Y
    GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM] = GV.Uper_Body_Front_Side_Turn_Mover + GV.Inital_Right_Foot_FrontV_Position_X
    GV.Foot_Current_Pos_Y[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM] = GV.Ground_Level_Y




    GV.Shoulder_Top_View_X = GV.Uper_Body_Front_Side_Turn_Mover
    GV.Shoulder_Top_View_Y = GV.screen_Center
    GV.Shoulder_TopV_Raduis = 30
    GV.Neck_Length = 30
    GV.Head_Lenght = 20


    GV.Head_X_Rotation_Angle = 90
    GV.Head_Y_Rotation_Angle = 90
    GV.Sholder_Rotate_Angle = 90#90


    GV.Left_Front_Uper_Arm_Z_Angle = 90
    GV.Right_Front_Uper_Arm_Z_Angle = 90





    



    #get activity names and numbers
    GV.WALK_TYPE_01 = Define_Acivity_Names_And_Numbers("WALK_TYPE_01")
    GV.WALK_TO_IDLE = Define_Acivity_Names_And_Numbers("WALK_TO_IDLE")
    GV.IDLE_STAND_01 = Define_Acivity_Names_And_Numbers("IDLE_STAND_01")

  #ENDEX================





  #this is to rotate on X the body torso using shoulder or Hip as pivots (clockwise angle input will low shoulder and keep hip in place)
  def X_Tilt_Body_From_Shoulder_Or_Hip_Point(Wanted_Tilt_IN, Tilt_Speed_IN):

    Tilt_Adjust_Done = False

    #rotate +ev
    if Wanted_Tilt_IN > GV.Body_X_Tilt_Angle:
      GV.Body_X_Tilt_Angle = GV.Body_X_Tilt_Angle + Tilt_Speed_IN
      if GV.Body_X_Tilt_Angle > Wanted_Tilt_IN:
        GV.Body_X_Tilt_Angle = Wanted_Tilt_IN
    #-----------------------------------------
    #rotate -ev
    if Wanted_Tilt_IN < GV.Body_X_Tilt_Angle:
      GV.Body_X_Tilt_Angle = GV.Body_X_Tilt_Angle - Tilt_Speed_IN
      if GV.Body_X_Tilt_Angle < Wanted_Tilt_IN:
        GV.Body_X_Tilt_Angle = Wanted_Tilt_IN
    #-----------------------------------------


    #do the rotation and lower body height if front end goes heigher than normal body height
    for i in range(150):
      GV.Body_Center_X = GV.Uper_Body_Front_Back_Mover
      GV.Body_Center_Y = GV.BodyHeight_Total + GV.Over_Stretch_Height_Manager

      #rotate the hip
      GV.Hip_X_Tilt_Angle = Cn360(GV.Body_X_Tilt_Angle + 180)
      GV.Hip_Position_X = GV.Body_Center_X + Gqx(GV.Hip_X_Tilt_Angle, GV.Body_Torso_Radius)
      GV.Hip_Position_Y = GV.Body_Center_Y + GV.Gqy#(GV.Hip_X_Tilt_Angle, GV.Body_Torso_Radius)
      #rotate the Shoulder
      GV.Shoulder_X_Tilt_Angle = Cn360(GV.Body_X_Tilt_Angle)
      GV.Shoulder_Position_X = GV.Body_Center_X + Gqx(GV.Shoulder_X_Tilt_Angle, GV.Body_Torso_Radius)
      GV.Shoulder_Position_Y = GV.Body_Center_Y + GV.Gqy#(GV.Shoulder_X_Tilt_Angle, GV.Body_Torso_Radius)

      #see if the shouder or hip has gone higher than body height
      if GV.Shoulder_Position_Y < GV.BodyHeight_Total or GV.Hip_Position_Y < GV.BodyHeight_Total:
        #lower body center if so
        GV.Over_Stretch_Height_Manager = GV.Over_Stretch_Height_Manager + 1
      else:
        break
    #----------------------------------------------------------------------


    
    #if angle reached then say done
    if GV.Body_X_Tilt_Angle == Wanted_Tilt_IN:
      Tilt_Adjust_Done = True
    #----------------------------------
      
    return Tilt_Adjust_Done
  #==================================================================================================









  #this is to raise or lower body height but also returns torso rotation to 90degrees (level with ground horizontaly)
  def Raise_Or_Lower_Body_Height_Reset_XTilt(Wanted_Body_Height_IN, Raise_Lower_Speed_IN):

    Tilt_Adjust_Done = False


    #Wanted_Body_Height_IN = 0 means reset body to max height (GV.BodyHeight_Total)

    #raise +ev
    if Wanted_Body_Height_IN > GV.Over_Stretch_Height_Manager:
      GV.Over_Stretch_Height_Manager = GV.Over_Stretch_Height_Manager + Raise_Lower_Speed_IN
      if GV.Over_Stretch_Height_Manager > Wanted_Body_Height_IN:
        GV.Over_Stretch_Height_Manager = Wanted_Body_Height_IN
    #-----------------------------------------
    #lower -ev
    if Wanted_Body_Height_IN < GV.Over_Stretch_Height_Manager:
      GV.Over_Stretch_Height_Manager = GV.Over_Stretch_Height_Manager - Raise_Lower_Speed_IN
      if GV.Over_Stretch_Height_Manager < Wanted_Body_Height_IN:
        GV.Over_Stretch_Height_Manager = Wanted_Body_Height_IN
    #-----------------------------------------


    #do the rotate body if shoulder or hip points raise above wanted height

    GV.Body_Center_X = GV.Uper_Body_Front_Back_Mover
    GV.Body_Center_Y = GV.BodyHeight_Total + GV.Over_Stretch_Height_Manager

    #rotate the hip
    GV.Hip_X_Tilt_Angle = Cn360(GV.Body_X_Tilt_Angle + 180)
    GV.Hip_Position_X = GV.Body_Center_X + Gqx(GV.Hip_X_Tilt_Angle, GV.Body_Torso_Radius)
    GV.Hip_Position_Y = GV.Body_Center_Y + GV.Gqy#(GV.Hip_X_Tilt_Angle, GV.Body_Torso_Radius)
    #rotate the Shoulder
    GV.Shoulder_X_Tilt_Angle = Cn360(GV.Body_X_Tilt_Angle)
    GV.Shoulder_Position_X = GV.Body_Center_X + Gqx(GV.Shoulder_X_Tilt_Angle, GV.Body_Torso_Radius)
    GV.Shoulder_Position_Y = GV.Body_Center_Y + GV.Gqy#(GV.Shoulder_X_Tilt_Angle, GV.Body_Torso_Radius)


    #rotate +ev to return to 90 (horizontal)
    if GV.Shoulder_Position_Y < (GV.BodyHeight_Total + Wanted_Body_Height_IN):
      GV.Body_X_Tilt_Angle = GV.Body_X_Tilt_Angle + 1
      if GV.Body_X_Tilt_Angle > 90:
        GV.Body_X_Tilt_Angle = 90
    #-----------------------------------------
    #rotate -ev to return to 90 (horizontal)
    if GV.Shoulder_Position_Y > (GV.BodyHeight_Total + Wanted_Body_Height_IN):
      GV.Body_X_Tilt_Angle = GV.Body_X_Tilt_Angle - 1
      if GV.Body_X_Tilt_Angle < 90:
        GV.Body_X_Tilt_Angle = 90
    #-----------------------------------------
    

    
    #if angle reached then say done
    if GV.Over_Stretch_Height_Manager == Wanted_Body_Height_IN and GV.Body_X_Tilt_Angle == 90:
      Tilt_Adjust_Done = True
    #-------------------------------------------------

    return Tilt_Adjust_Done
  #==================================================================================================










  #$$FOOT_TRAJECTORY_MOVE$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  def Move_Foot_To_Target(Foot_ID_NuM, Step_Height_Y):

    Done_Foot_Move_ops = False
    Done_Done = 0
    Foot_Target_Half_Dist = 0
    i = 0
    Hiest_Y_UP_Pos = 0
    GV.Foot_To_Ground_Dist = 0
    The_Foot_Target_Pos_X = GV.Foot_Traje_Target_X[Foot_ID_NuM]
    StepA_Height_Y_COMP = Step_Height_Y



    This_Is_A_Front_Foot = False
    if GV.RIGHT_FRONT_FOOT_ID_NUM == Foot_ID_NuM or GV.LEFT_FRONT_FOOT_ID_NUM == Foot_ID_NuM:
      This_Is_A_Front_Foot = True


    #if foot starts moving then set target
    if GV.Foot_Anim_Position[Foot_ID_NuM] == 0:


      #get oposite foot id num
      GV.Get_Oposite_MoveFoot_ID_NUM = Get_Oposite_Foot(Foot_ID_NuM)


      #reset foot move situation
      GV.Move_Foot_Situation = 0
      GV.Foot_Lifted_Off_Ground_Count = 0

      GV.Foot_Coming_Down_Tracker = 0

      #set foot move incrementer to positive direction
      GV.Foot_Anim_Direction = 1

      
      #get the foots current position
      GV.The_Foot_Pos_X = GV.Foot_Current_Pos_X[Foot_ID_NuM]
      GV.The_Foot_Pos_Y = GV.Foot_Current_Pos_Y[Foot_ID_NuM]


      #GV.Foot_Anim_Position[Foot_ID_NuM] = 1
      GV.Total_Trajectory_Dots = -1#0 so to start with array zero




      #get the distance between the foot and foot trajectory target destination
      GV.Foot_Target_Dist = GV.The_Foot_Pos_X - The_Foot_Target_Pos_X
      if GV.Foot_Target_Dist < 0:
        GV.Foot_Target_Dist = The_Foot_Target_Pos_X - GV.The_Foot_Pos_X
      #ENDEX===================================================



      #if the distance between foot and target are too small then increase the foot lift height to make sure the foot lifts off the ground
      if GV.Foot_Target_Dist < 30 and Step_Height_Y < 30:
        StepA_Height_Y_COMP = 30
      #just incase step height was set to zero increase it
      if Step_Height_Y < 5:
        StepA_Height_Y_COMP = 5
      #===========================================================================================

      

      #collect the leg lift part of the trajectory
      for i in range(0, StepA_Height_Y_COMP, 1):#for i in range(StepA_Height_Y_COMP):
        GV.Total_Trajectory_Dots = GV.Total_Trajectory_Dots + 1
        GV.Traj_Calc_X[GV.Total_Trajectory_Dots] = GV.The_Foot_Pos_X
        GV.Traj_Calc_Y[GV.Total_Trajectory_Dots] = GV.The_Foot_Pos_Y - i
      #ENDEX================
      Hiest_Y_UP_Pos = GV.Traj_Calc_Y[GV.Total_Trajectory_Dots]
      #===========================================





      #only use arc if the foot and target trajectory destinations are far enough appart
      if GV.Foot_Target_Dist > 2:
        #get the half way point between foot and target
        Foot_Target_Half_Dist = GV.Foot_Target_Dist / 2


        
        #collect the arc from foot to target clockwise direction
        if GV.The_Foot_Pos_X > The_Foot_Target_Pos_X: 
          #place the trajectory mover Half way between the foot and the foot target
          GV.Foot_Trajectory_PosX = The_Foot_Target_Pos_X + Foot_Target_Half_Dist
          #collect the leg arc circular part of the trajectory
          for i in range(449, 271, -3):#-2
            GV.Total_Trajectory_Dots = GV.Total_Trajectory_Dots + 1
            Ang = Cn360(i)
            GV.Traj_Calc_X[GV.Total_Trajectory_Dots] = GV.Foot_Trajectory_PosX + Gqx(Ang, Foot_Target_Half_Dist)
            GV.Traj_Calc_Y[GV.Total_Trajectory_Dots] = Hiest_Y_UP_Pos + GV.Gqy#(Ang, Foot_Target_Half_Dist)
          #ENDEX================
          Hiest_Y_UP_Pos = GV.Traj_Calc_Y[GV.Total_Trajectory_Dots]
          #===========================================
        #ENDEX================
          
        else:  #collect the arc from foot to target Anticlockwise direction
        
         
          #place the trajectory mover Half way between the foot and the foot target
          GV.Foot_Trajectory_PosX = GV.The_Foot_Pos_X + Foot_Target_Half_Dist
          #collect the leg arc circular part of the trajectory
          for i in range(271, 449, 3):#2
            GV.Total_Trajectory_Dots = GV.Total_Trajectory_Dots + 1
            Ang = Cn360(i)
            GV.Traj_Calc_X[GV.Total_Trajectory_Dots] = GV.Foot_Trajectory_PosX + Gqx(Ang, Foot_Target_Half_Dist)
            GV.Traj_Calc_Y[GV.Total_Trajectory_Dots] = Hiest_Y_UP_Pos + GV.Gqy#(Ang, Foot_Target_Half_Dist)
          #ENDEX================
          Hiest_Y_UP_Pos = GV.Traj_Calc_Y[GV.Total_Trajectory_Dots]
          #===========================================  
      #ENDEX================
      #============================================


      #collect the bring down part of the trajectory
      for i in range(1, StepA_Height_Y_COMP + 10, 1):#10
        GV.Total_Trajectory_Dots = GV.Total_Trajectory_Dots + 1
        GV.Traj_Calc_X[GV.Total_Trajectory_Dots] = The_Foot_Target_Pos_X
        GV.Traj_Calc_Y[GV.Total_Trajectory_Dots] = Hiest_Y_UP_Pos + i
      #ENDEX================
      Hiest_Y_UP_Pos = GV.Traj_Calc_Y[GV.Total_Trajectory_Dots]
      #===========================================


      #get the hiest Y point of the trajectory to use do decelerate foot when it reaches
      GV.Foot_Trajectory_Hiest_Point = 1
      for i in range(1, GV.Total_Trajectory_Dots, 1):
        if GV.Traj_Calc_Y[i] < GV.Traj_Calc_Y[GV.Foot_Trajectory_Hiest_Point]:
          GV.Foot_Trajectory_Hiest_Point = i
      #---------------------------------------------------------------------------------
      #print(GV.Foot_Trajectory_Hiest_Point)


    #ENDEX=================================================================================================








    #make sure there is a trajectory planed before starting to move foot
    if GV.Total_Trajectory_Dots > 1:
      
      #check virtual world fool hit ground when moving foot in (+ev) direction
      if GV.Foot_Anim_Direction == 1:
        if GV.Foot_Grounded[Foot_ID_NuM] == 1 and GV.Foot_Anim_Position[Foot_ID_NuM] > (GV.Total_Trajectory_Dots / 3):
          # got to next step
          Done_Done = 1
        else:
        

          #Current_Moving_Foot = Foot_Names[Foot_ID_NuM]

          #Move the foot
          GV.The_Foot_Pos_X = GV.Traj_Calc_X[GV.Foot_Anim_Position[Foot_ID_NuM]]
          GV.The_Foot_Pos_Y = GV.Traj_Calc_Y[GV.Foot_Anim_Position[Foot_ID_NuM]]
          #Get the moved foot position
          GV.Foot_Current_Pos_X[Foot_ID_NuM] = GV.The_Foot_Pos_X
          GV.Foot_Current_Pos_Y[Foot_ID_NuM] = GV.The_Foot_Pos_Y
          #Draw_Mat[3].at<Vec3b>(GV.The_Foot_Pos_Y, GV.The_Foot_Pos_X)[2] = 255


          #get distance of foot to ground
          GV.Foot_To_Ground_Dist = GV.Ground_Level_Y - GV.Foot_Current_Pos_Y[Foot_ID_NuM]
          
          


          #ENDEX================
          #advance to next foot trajectory point (0 to 100)
          if GV.Foot_Anim_Position[Foot_ID_NuM] < GV.Foot_Trajectory_Hiest_Point:#(GV.Total_Trajectory_Dots / 2):#
          
            GV.Foot_Speed_INC[Foot_ID_NuM] = GV.Foot_Speed_INC[Foot_ID_NuM] + GV.Leg_INC_Speed
            if GV.Foot_Speed_INC[Foot_ID_NuM] > GV.Leg_Speeds:
              GV.Foot_Speed_INC[Foot_ID_NuM] = GV.Leg_Speeds
            #ENDEX================
          #ENDEX================





              
          #start slowing down when the foot is comming down
          else:          


            #+++++NEW_ADD_QUICKLY drop the shoulder main joint of THE FOOT additive when it the foot reaches a certain height off the ground
            #if This_Is_A_Front_Foot == True:
            if GV.Foot_To_Ground_Dist > 10:#15
              #print("Foot Height reached")
              GV.Main_Joint_SideVADJUST_Y[Foot_ID_NuM] = GV.Main_Joint_SideVADJUST_Y[Foot_ID_NuM] + 4#2
              if GV.Main_Joint_SideVADJUST_Y[Foot_ID_NuM] > 14:
                GV.Main_Joint_SideVADJUST_Y[Foot_ID_NuM] = 14
            #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




                  

            #start slowing down if foot is close to ground so we dont hit too hard
            if GV.Foot_To_Ground_Dist < 15:#25     
              GV.Foot_Speed_INC[Foot_ID_NuM] = GV.Foot_Speed_INC[Foot_ID_NuM] - GV.Leg_Deccelaration_INC_Speed
              #dont slow down too much
              if GV.Foot_Speed_INC[Foot_ID_NuM] < 2:
                GV.Foot_Speed_INC[Foot_ID_NuM] = 2
              #ENDEX================
            #ENDEX================  
          #ENDEX================
        #===================================================
      
        #advance the foot move increment in (+ev) direction
        GV.Foot_Anim_Position[Foot_ID_NuM] = GV.Foot_Anim_Position[Foot_ID_NuM] + GV.Foot_Speed_INC[Foot_ID_NuM]
        #Limit foot move advaner to GV.Total_Trajectory_Dots
        if GV.Foot_Anim_Position[Foot_ID_NuM] > GV.Total_Trajectory_Dots:
          GV.Foot_Anim_Position[Foot_ID_NuM] = GV.Total_Trajectory_Dots
      #END-if GV.Foot_Anim_Direction == 1------------------------------------------------------------------------------------------------------------------------------------


        
      #advance the foot move increment in reverse (-ev) direction
      if GV.Foot_Anim_Direction == 2:
        GV.Foot_Anim_Position[Foot_ID_NuM] = GV.Foot_Anim_Position[Foot_ID_NuM] - 3
        #Limit foot move advaner to zero incase the foot is reversing
        if GV.Foot_Anim_Position[Foot_ID_NuM] <= 0:
          GV.Foot_Anim_Position[Foot_ID_NuM] = 0
          #say done
          Done_Done = 1
        #ADVANCE FEET IN REVERSE
        GV.The_Foot_Pos_X = GV.Traj_Calc_X[GV.Foot_Anim_Position[Foot_ID_NuM]]
        GV.The_Foot_Pos_Y = GV.Traj_Calc_Y[GV.Foot_Anim_Position[Foot_ID_NuM]] + Done_Done#this will place foot sligtly below ground so virtual grounded funtion works
        #Get the moved foot position
        GV.Foot_Current_Pos_X[Foot_ID_NuM] = GV.The_Foot_Pos_X
        GV.Foot_Current_Pos_Y[Foot_ID_NuM] = GV.The_Foot_Pos_Y
      #---------------****************************END Foot_Movement_Steps***********


    return Done_Done
  #ENDEX================














  #z tilt is done by lifting or droping shoulder and hip sides of left and right
  def Body_To_Center_Mass_Move_Func(Body_Move_Speed_IN):


    done_Tilt = False
    #get the complete target destination value
    GV.Center_Plus_FrontBackOffset = GV.Center_BODY_Feet_X + GV.Center_BODY_Feet_X_Offset


    
    #only do movement stuff if destination changes
    if GV.Uper_Body_Front_Back_Mover != GV.Center_Plus_FrontBackOffset:
      
      #to do this only once at start of part move
      if GV.Calc_Body_To_Center_Mass_Dist_Done == False:

        #get the movement increments into array
        Move_To_Destination_In_100_Ticks(GV.Uper_Body_Front_Back_Mover, GV.Center_Plus_FrontBackOffset, GV.Body_To_CMass_Chop)

        GV.Body_To_CentMass_Advance = 0
        #say calc done
        GV.Calc_Body_To_Center_Mass_Dist_Done = True

        GV.Body_Center_Accel_Deccel_INC = 0
    #----------------------------------------------------------------------------


      
      

      #Advance to the destination in 100 clicks or less
      if GV.Body_To_CentMass_Advance < 100:



        #slow accelerate
        if GV.Body_To_CentMass_Advance < 20:
         GV.Body_Center_Accel_Deccel_INC = GV.Body_Center_Accel_Deccel_INC + Body_Move_Speed_IN#4
         if GV.Body_Center_Accel_Deccel_INC > 20:
           GV.Body_Center_Accel_Deccel_INC = 20
        #slow deccelerate
        if GV.Body_To_CentMass_Advance > 80:
         GV.Body_Center_Accel_Deccel_INC = GV.Body_Center_Accel_Deccel_INC - Body_Move_Speed_IN#4
         if GV.Body_Center_Accel_Deccel_INC < 5:
           GV.Body_Center_Accel_Deccel_INC = 5
        #---------------------------------------------------------------------------
        intme_INC = (int) (GV.Body_Center_Accel_Deccel_INC)
        #---------------------------------------------------------------------------



        
        #advance the percents
        GV.Body_To_CentMass_Advance = GV.Body_To_CentMass_Advance + GV.Body_Center_Accel_Deccel_INC# Body_Move_Speed_IN
        if GV.Body_To_CentMass_Advance >= 100:
          GV.Body_To_CentMass_Advance = 100
          #print(GV.Body_To_CMass_Chop[GV.Body_To_CentMass_Advance])
          #print(GV.Center_Plus_FrontBackOffset)
          
        GV.Uper_Body_Front_Back_Mover = GV.Body_To_CMass_Chop[GV.Body_To_CentMass_Advance]
        #ENDEX================
      #ENDEX================



    #See if destination reached
    if GV.Uper_Body_Front_Back_Mover == GV.Center_Plus_FrontBackOffset:
      GV.Calc_Body_To_Center_Mass_Dist_Done = False
      done_Tilt = True
    #ENDEX================
    return done_Tilt

  #ENDEX================






  #old body to center mass mover (still used for stading up
  def Body_To_Center_Mass_Move_FuncOLD(Body_Move_Speed_IN):


    done_Tilt = False

    Center_Plus_FrontBackOffset = GV.Center_BODY_Feet_X + GV.Center_BODY_Feet_X_Offset


    #get the distance between distination poin and current point
    destDist = GV.Uper_Body_Front_Back_Mover - Center_Plus_FrontBackOffset
    if destDist < 0:
      destDist = Center_Plus_FrontBackOffset - GV.Uper_Body_Front_Back_Mover
    #----------------------------------------------------------------------------
    
    #slow accelerate if far from destination
    if destDist > 10:
      GV.Body_Center_Accel_Deccel_INC = GV.Body_Center_Accel_Deccel_INC + 0.6
      if GV.Body_Center_Accel_Deccel_INC > Body_Move_Speed_IN:
        GV.Body_Center_Accel_Deccel_INC = Body_Move_Speed_IN
    else:
      GV.Body_Center_Accel_Deccel_INC = GV.Body_Center_Accel_Deccel_INC - 1
      if GV.Body_Center_Accel_Deccel_INC < 1:
        GV.Body_Center_Accel_Deccel_INC = 1
    #---------------------------------------------------------------------------

    intme_INC = (int) (GV.Body_Center_Accel_Deccel_INC)
    

    #Z tilt the body to the Right till it reaches
    if GV.Uper_Body_Front_Back_Mover < Center_Plus_FrontBackOffset:
    
      #move the local X to create body tilt
      GV.Uper_Body_Front_Back_Mover = GV.Uper_Body_Front_Back_Mover + intme_INC
      if GV.Uper_Body_Front_Back_Mover >= Center_Plus_FrontBackOffset:
      
        GV.Uper_Body_Front_Back_Mover = Center_Plus_FrontBackOffset
      #ENDEX================
    #ENDEX================
    #Z tilt the body to the left till it reaches
    if GV.Uper_Body_Front_Back_Mover > Center_Plus_FrontBackOffset:
    
      #move the local X to create body tilt
      GV.Uper_Body_Front_Back_Mover = GV.Uper_Body_Front_Back_Mover - intme_INC
      if GV.Uper_Body_Front_Back_Mover <= Center_Plus_FrontBackOffset:
      
        GV.Uper_Body_Front_Back_Mover = Center_Plus_FrontBackOffset
      #ENDEX================
    #ENDEX================
    #=============================================================================================

    if GV.Uper_Body_Front_Back_Mover == Center_Plus_FrontBackOffset:
      GV.Body_Center_Accel_Deccel_INC = 0
      done_Tilt = True
    #ENDEX================
    return done_Tilt

  #ENDEX================
















  #z tilt is done by lifting or droping shoulder and hip sides of left and right
  def Do_Z_TILT_Func(Wanted_Z_Tilt_IN, Z_Tilt_Speed_IN):


    done_Tilt = False
    #get the positive difference
    Diff = GV.Z_Tilt_Mover_Value - Wanted_Z_Tilt_IN
    if Diff < 0:
      Diff = Wanted_Z_Tilt_IN - GV.Z_Tilt_Mover_Value
    #-------------------------------------------------
    
    #slowly accelerate toward target value
    if Diff > 1:#
      GV.Z_Tilt_Speed_INC = GV.Z_Tilt_Speed_INC + GV.Z_Tilt_INC_Accel_Deccel#0.2
      if GV.Z_Tilt_Speed_INC >= Z_Tilt_Speed_IN:
        GV.Z_Tilt_Speed_INC = Z_Tilt_Speed_IN
    else:#slowly decelerate when close to end
      GV.Z_Tilt_Speed_INC = GV.Z_Tilt_Speed_INC - GV.Z_Tilt_INC_Accel_Deccel
      if GV.Z_Tilt_Speed_INC <= GV.Z_Tilt_INC_Accel_Deccel:
        GV.Z_Tilt_Speed_INC = GV.Z_Tilt_INC_Accel_Deccel
    #-----------------------------------------------------------
    

    #Z tilt the body to the Right till it reaches
    if GV.Z_Tilt_Mover_Value < Wanted_Z_Tilt_IN:
      #move the local X to create body tilt
      GV.Z_Tilt_Mover_Value = GV.Z_Tilt_Mover_Value + GV.Z_Tilt_Speed_INC
      if GV.Z_Tilt_Mover_Value >= Wanted_Z_Tilt_IN:
      
        GV.Z_Tilt_Mover_Value = Wanted_Z_Tilt_IN
      #ENDEX================
    #ENDEX================
    #Z tilt the body to the left till it reaches
    if GV.Z_Tilt_Mover_Value > Wanted_Z_Tilt_IN:
    
      #move the local X to create body tilt
      GV.Z_Tilt_Mover_Value = GV.Z_Tilt_Mover_Value - GV.Z_Tilt_Speed_INC
      if GV.Z_Tilt_Mover_Value <= Wanted_Z_Tilt_IN:
      
        GV.Z_Tilt_Mover_Value = Wanted_Z_Tilt_IN
      #ENDEX================
    #ENDEX================
    #=============================================================================================






    if GV.Z_Tilt_Mover_Value == Wanted_Z_Tilt_IN:
      GV.Z_Tilt_Speed_INC = 0
      done_Tilt = True
    #ENDEX================
    return done_Tilt

  #ENDEX================










  #this is also used to move shoulder left or right by moving Z angles of both Z angle servos in front uper body shoulders
  def Body_To_Center_Mass_Move_Func_FRONT_V(Shoulder_Left_Right_Offset, Body_Move_Speed_IN):


    done_Tilt = False
    #use Shoulder_Left_Right_Offset to move sholders left or right (Shoulder_Left_Right_Offset = 0 = return body to center of front feet)
    Combine_With_Offset = GV.Center_BODY_Feet_Side_X + Shoulder_Left_Right_Offset


    #Z tilt the body to the Right till it reaches
    if GV.Uper_Body_Front_Side_Turn_Mover < Combine_With_Offset:
    
      #move the local X to create body tilt
      GV.Uper_Body_Front_Side_Turn_Mover = GV.Uper_Body_Front_Side_Turn_Mover + Body_Move_Speed_IN
      if GV.Uper_Body_Front_Side_Turn_Mover >= Combine_With_Offset:
      
        GV.Uper_Body_Front_Side_Turn_Mover = Combine_With_Offset
      #ENDEX================
      #just toget a representation of the amount of turning we are doing in degrees
      GV.Y_Body_Rotate = GV.Y_Body_Rotate + Body_Move_Speed_IN
      if GV.Y_Body_Rotate > 359:
        GV.Y_Body_Rotate = 0
        #ENDEX================
    #ENDEX================
    #Z tilt the body to the left till it reaches
    if GV.Uper_Body_Front_Side_Turn_Mover > Combine_With_Offset:
    
      #move the local X to create body tilt
      GV.Uper_Body_Front_Side_Turn_Mover = GV.Uper_Body_Front_Side_Turn_Mover - Body_Move_Speed_IN
      if GV.Uper_Body_Front_Side_Turn_Mover <= Combine_With_Offset:
      
        GV.Uper_Body_Front_Side_Turn_Mover = Combine_With_Offset
      #ENDEX================
      #just toget a representation of the amount of turning we are doing in degrees
      GV.Y_Body_Rotate = GV.Y_Body_Rotate - Body_Move_Speed_IN
      if GV.Y_Body_Rotate < 0:
        GV.Y_Body_Rotate = 359
        #ENDEX================
    #ENDEX================
    #=============================================================================================

    if GV.Uper_Body_Front_Side_Turn_Mover == Combine_With_Offset:
    
      done_Tilt = True
    #ENDEX================
    return done_Tilt

  #ENDEX================








  #head up down using acceleration and deceleration
  def Do_Head_X_Rotate_UP_DOWN_Accel(Wanted_Tilt_IN, Tilt_Speed_IN):


    done_Tilt = False


    #get distance between
    dist = (GV.Head_X_Rotation_Angle - Wanted_Tilt_IN) 
    if dist < 0:
      dist = (Wanted_Tilt_IN - GV.Head_X_Rotation_Angle)
    #----------------------------------------------------

    #use slow speed if close to target
    if dist < 8:
      GV.Head_X_UPDOWN_INC = 2
    else:
      #accelerate to target speed----------------------------
      if GV.Head_X_UPDOWN_INC < Tilt_Speed_IN:
        GV.Head_X_UPDOWN_INC = GV.Head_X_UPDOWN_INC + 1
      #------------------------------------------------------
      if GV.Head_X_UPDOWN_INC > Tilt_Speed_IN:
        GV.Head_X_UPDOWN_INC = Tilt_Speed_IN
      #------------------------------------------------------
    #------------------------------------------------------
    


    
    
    #Z tilt the body to the Right till it reaches
    if GV.Head_X_Rotation_Angle < Wanted_Tilt_IN:
    
      #move the local X to create body tilt
      GV.Head_X_Rotation_Angle = GV.Head_X_Rotation_Angle + GV.Head_X_UPDOWN_INC
      if GV.Head_X_Rotation_Angle >= Wanted_Tilt_IN:
      
        GV.Head_X_Rotation_Angle = Wanted_Tilt_IN
      #ENDEX================
    #ENDEX================
    
    #Z tilt the body to the left till it reaches
    if GV.Head_X_Rotation_Angle > Wanted_Tilt_IN:
    
      #move the local X to create body tilt
      GV.Head_X_Rotation_Angle = GV.Head_X_Rotation_Angle - GV.Head_X_UPDOWN_INC
      if GV.Head_X_Rotation_Angle <= Wanted_Tilt_IN:
      
        GV.Head_X_Rotation_Angle = Wanted_Tilt_IN
      #ENDEX================
    #ENDEX================
    #=============================================================================================

    if GV.Head_X_Rotation_Angle == Wanted_Tilt_IN:
      GV.Head_X_UPDOWN_INC = 0
      done_Tilt = True
    #ENDEX================
    return done_Tilt

  #ENDEX================










  #head up down (using a fixed speed)
  def Do_Head_X_Rotate_UP_DOWN(Wanted_Tilt_IN, Tilt_Speed_IN):


    done_Tilt = False
    
    #Z tilt the body to the Right till it reaches
    if GV.Head_X_Rotation_Angle < Wanted_Tilt_IN:
    
      #move the local X to create body tilt
      GV.Head_X_Rotation_Angle = GV.Head_X_Rotation_Angle + Tilt_Speed_IN
      if GV.Head_X_Rotation_Angle >= Wanted_Tilt_IN:
      
        GV.Head_X_Rotation_Angle = Wanted_Tilt_IN
      #ENDEX================
    #ENDEX================
    #Z tilt the body to the left till it reaches
    if GV.Head_X_Rotation_Angle > Wanted_Tilt_IN:
    
      #move the local X to create body tilt
      GV.Head_X_Rotation_Angle = GV.Head_X_Rotation_Angle - Tilt_Speed_IN
      if GV.Head_X_Rotation_Angle <= Wanted_Tilt_IN:
      
        GV.Head_X_Rotation_Angle = Wanted_Tilt_IN
      #ENDEX================
    #ENDEX================
    #=============================================================================================

    if GV.Head_X_Rotation_Angle == Wanted_Tilt_IN:
    
      done_Tilt = True
    #ENDEX================
    return done_Tilt

  #ENDEX================




  
  #head left and right
  def Do_Head_Y_Rotate_Left_Right(Wanted_Tilt_IN, Tilt_Speed_IN):


    done_Tilt = False

    #Z tilt the body to the Right till it reaches
    if GV.Head_Y_Rotation_Angle < Wanted_Tilt_IN:
    
      #move the local X to create body tilt
      GV.Head_Y_Rotation_Angle = GV.Head_Y_Rotation_Angle + Tilt_Speed_IN
      if GV.Head_Y_Rotation_Angle >= Wanted_Tilt_IN:
      
        GV.Head_Y_Rotation_Angle = Wanted_Tilt_IN
      #ENDEX================
    #ENDEX================
    #Z tilt the body to the left till it reaches
    if GV.Head_Y_Rotation_Angle > Wanted_Tilt_IN:
    
      #move the local X to create body tilt
      GV.Head_Y_Rotation_Angle = GV.Head_Y_Rotation_Angle - Tilt_Speed_IN
      if GV.Head_Y_Rotation_Angle <= Wanted_Tilt_IN:
      
        GV.Head_Y_Rotation_Angle = Wanted_Tilt_IN
      #ENDEX================
    #ENDEX================
    #=============================================================================================

    if GV.Head_Y_Rotation_Angle == Wanted_Tilt_IN:
      done_Tilt = True
      #disable servo to move
      GV.Driving_Head_Y_Rotate = False
    else:
      #enable servo movement
      GV.Driving_Head_Y_Rotate = True
    #ENDEX================
    return done_Tilt

  #ENDEX================






  def ACTIVITY_CHANGE(New_Activity, Number_Of_Times_To_Do_Act_IN):


    #reset when animation changes
    GV.Number_Of_Times_Act_Done = 0
    GV.Activity_Start_Steps = 0
    #---ACTIVITY CHANGE,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    #set the activity number
    
    GV.Activity_Select = New_Activity
    #set the activity duration
    GV.Number_Of_Times_To_Do_Act = Number_Of_Times_To_Do_Act_IN#(seconds)

    #set the first ever animation to be played only once at ini
    GV.New_Act_Name = GV.Activity_Names_Collection[New_Activity]
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    GV.Move_Steps = 0


  #ENDEX================









  def Set_Walk_Values(Walk_Type_IN):
    
    #set feet stride height
    GV.Ground_Presure_Sensivity = 1#3
    #get feet positioning sumary ID number
    Get_Feet_Positions_IDS()
    #decide feet move sequence 
    Feet_Move_Sequence_Selector(Walk_Type_IN)
    #--------------------------------------------

    #set limit to not exceed z tilt max
    GV.Max_Z_Tilt = 8

    #GV.Wanted_Z_Tilt = 6#6 5,8
    GV.Z_Tilt_SPeed = 4#3
    GV.Z_TILT_Reset_Speed = 2
    GV.Z_Tilt_INC_Accel_Deccel = 0.2#0.2
    #===========

    #----normal walk settings
    GV.Leg_Speeds = 6#5
    GV.Leg_INC_Speed = 2#3 0.25f
    GV.Leg_Deccelaration_INC_Speed = 1
    #====


    

    #Set stride length and direction for forward walk
    if Walk_Type_IN == GV.WALK_TYPE_01:
      #================================
      GV.Wanted_Z_Tilt = 6#6 5,8
      #================================
      GV.Body_To_Center_Mass_Speed = 4#4
      GV.Leg_Lift_Height = 5
      #for normal staight walk use small additive amount
      GV.Z_Tilt_Add_Amount = 2#1
      #-------------------------
      GV.Z_Tilt_Add_Speed = 1
      GV.Z_Tilt_Add_RESET_Speed = 2#1
      #======================================
      #If this is first step after feet reset position==========================================
      if GV.Rear_Feet_Positions_ID == 1:
        #set feet targets if first moving foot is left rear
        if GV.Feet_Move_Sequence[1] == GV.LEFT_REAR_FOOT_ID_NUM:
          Set_Feet_Trajectory_Targets_SideV(40, 80)
        #set feet targets if first moving foot is right rear
        if GV.Feet_Move_Sequence[1] == GV.RIGHT_REAR_FOOT_ID_NUM:
          Set_Feet_Trajectory_Targets_SideV(80, 40)
      #ENDEX================

        
      #resume normal walking settings
      #===Left legs behind need double forward=========================================
      if GV.Rear_Feet_Positions_ID == 2: 
        #set feet targets
        Set_Feet_Trajectory_Targets_SideV(63, 105)#Set_Feet_Trajectory_Targets_SideV(68, 110)
      #ENDEX================
        #===Right legs behind need double forward=========================================
      if GV.Rear_Feet_Positions_ID == 3:    
        #set feet targets
        Set_Feet_Trajectory_Targets_SideV(105, 63)#Set_Feet_Trajectory_Targets_SideV(110, 68)
      #ENDEX================
    #=END if Walk_Type_IN == WALK_TYPE_01:=================================================================


    #Set stride length and direction for return to idle
    if Walk_Type_IN == GV.WALK_TO_IDLE:
      #----walk settings
      GV.Leg_Speeds = 7#5
      GV.Leg_INC_Speed = 2#3 0.25f
      GV.Leg_Deccelaration_INC_Speed = 1
      #====
      #================================
      GV.Wanted_Z_Tilt = 6#6 5,8
      #================================
      GV.Body_To_Center_Mass_Speed = 2#3
      GV.Leg_Lift_Height = 18
      #Z tilt oposite foot push lift settings
      GV.Z_Tilt_Add_Amount = 6#5
      GV.Z_Tilt_Add_Speed = 1
      GV.Z_Tilt_Add_RESET_Speed = 1
      #=========================================
      Set_Feet_Trajectory_Targets_SideV(0, 0)
      #ENDEX================
    #=END if Walk_Type_IN == WALK_TYPE_01:=================================================================









    #GV.Body_To_Center_Mass_Speed = 2
    GV.Body_To_Center_Mass_Speed_Front = 2


    #reset feet stuff
    GV.Foot_Anim_Position[1] = 0
    GV.Foot_Anim_Position[2] = 0
    GV.Foot_Anim_Position[3] = 0
    GV.Foot_Anim_Position[4] = 0
    GV.Foot_Anim_Position[5] = 0
    GV.Foot_Anim_Position[6] = 0

    #reset the feet speed incrementers
    GV.Foot_Speed_INC[1] = 1
    GV.Foot_Speed_INC[2] = 1
    GV.Foot_Speed_INC[3] = 1
    GV.Foot_Speed_INC[4] = 1
    GV.Foot_Speed_INC[5] = 1
    GV.Foot_Speed_INC[6] = 1


    
    #got to first step
    GV.Move_Steps = 1
    GV.Foot_Move_Steps = 0

  #ENDEX================







  #z tilt is done by lifting or droping shoulder and hip sides of left and right
  def Foot_Y_Pos_ADJUST_Func(Foot_ID_NUM_IN, Wanted_Z_Tilt_IN, Z_Tilt_Speed_IN):


    done_Tilt = False

    #Z tilt the body to the Right till it reaches
    if GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] < Wanted_Z_Tilt_IN:
    
      #move the local X to create body tilt
      GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] = GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] + Z_Tilt_Speed_IN
      if GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] >= Wanted_Z_Tilt_IN:
      
        GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] = Wanted_Z_Tilt_IN
      #ENDEX================
    #ENDEX================
    #Z tilt the body to the left till it reaches
    if GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] > Wanted_Z_Tilt_IN:
    
      #move the local X to create body tilt
      GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] = GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] - Z_Tilt_Speed_IN
      if GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] <= Wanted_Z_Tilt_IN:
      
        GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] = Wanted_Z_Tilt_IN
      #ENDEX================
    #ENDEX================
    #=============================================================================================

    if GV.Main_Joint_SideVADJUST_Y[Foot_ID_NUM_IN] == Wanted_Z_Tilt_IN:
    
      done_Tilt = True
    #ENDEX================
    return done_Tilt

  #ENDEX================






  def Do_IK_And_Generate_Joint_Angles():


    #just to show loop is going on
    GV.TestVarME = GV.TestVarME + 1;
    if GV.TestVarME > 88:
      GV.TestVarME = 0
    

    x = 0
    y = 0
    d = 0
    i = 0
    Feet_Distance = 0
    GV.Center_Front_X = 0
    GV.Center_Rear_X = 0
    Center_Div = 0

    GV.BodyHeight_Total = GV.Ground_Level_Y - GV.Body_Height


    
    #==detect foot grounded using feet Y positions cleaner for walking
    Detect_Virtual_Foot_grounded(GV.LEFT_REAR_FOOT_ID_NUM)
    Detect_Virtual_Foot_grounded(GV.LEFT_FRONT_FOOT_ID_NUM)
    Detect_Virtual_Foot_grounded(GV.RIGHT_REAR_FOOT_ID_NUM)
    Detect_Virtual_Foot_grounded(GV.RIGHT_FRONT_FOOT_ID_NUM)
    Detect_Virtual_Foot_grounded(GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM)
    Detect_Virtual_Foot_grounded(GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM)
    #================================================================
    




    #-----------Top view for sore dog world and head Y left right rotation, for Y rotate representation and placing objects and mapping environment
    #place and rotate shoulder
    Ang = GV.Y_Body_Rotate
    #place hip and body and rotate hip to rotate shoulder z agles from front view
    Ang = Cn360(GV.Y_Body_Rotate + 135)
    GV.Left_Front_Main_Joint_TopV_X = GV.Shoulder_Top_View_X + Gqx(Ang, GV.Shoulder_TopV_Raduis)
    GV.Left_Front_Main_Joint_TopV_Y = GV.Shoulder_Top_View_Y + GV.Gqy#(Ang, GV.Shoulder_TopV_Raduis)
    #place hip and body and rotate hip to rotate shoulder z agles from front view
    Ang = Cn360(GV.Y_Body_Rotate + 225)
    GV.Right_Front_Main_Joint_X = GV.Shoulder_Top_View_X + Gqx(Ang, GV.Shoulder_TopV_Raduis)
    GV.Right_Front_Main_Joint_Y = GV.Shoulder_Top_View_Y + GV.Gqy#(Ang, GV.Shoulder_TopV_Raduis)

    #place the neck
    Ang = Cn360(GV.Y_Body_Rotate)
    GV.Neck_Top_Pos_X = GV.Shoulder_Top_View_X + Gqx(Ang, GV.Neck_Length)
    GV.Neck_Top_Pos_Y = GV.Shoulder_Top_View_Y + GV.Gqy#(Ang, GV.Neck_Length)
    #place and rotate the head Y rotate
    Ang = Cn360(GV.Y_Body_Rotate + 270 + GV.Head_Y_Rotation_Angle)
    GV.Head_Top_Pos_X = GV.Neck_Top_Pos_X + Gqx(Ang, GV.Head_Lenght)
    GV.Head_Top_Pos_Y = GV.Neck_Top_Pos_Y + GV.Gqy#(Ang, GV.Head_Lenght)
    #--------------------------------------------------------------------------------------------------









    
    #-----------Front view only for Front Legs Z rotation value generation

    #GV.Uper_Body_Front_Side_Turn_Mover = 300

    #place Left and right shoulder main joints
    GV.Left_Front_Joint_Front_View_X = GV.Uper_Body_Front_Side_Turn_Mover + GV.Inital_Left_Foot_FrontV_Position_X
    GV.Left_Front_Joint_Front_View_Y = GV.Shoulder_Position_Y
    GV.Right_Front_Joint_Front_View_X = GV.Uper_Body_Front_Side_Turn_Mover + GV.Inital_Right_Foot_FrontV_Position_X
    GV.Right_Front_Joint_Front_View_Y = GV.Shoulder_Position_Y

    #colect joint angles for Z rotation
    GV.Left_Front_Uper_Arm_Z_Angle = GetAngle(GV.Uper_Body_Front_Side_Turn_Mover, GV.Shoulder_Position_Y, GV.Left_Front_Joint_Front_View_X, GV.Left_Front_Joint_Front_View_Y, GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM], GV.Foot_Current_Pos_Y[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM])
    GV.Right_Front_Uper_Arm_Z_Angle = GetAngle(GV.Uper_Body_Front_Side_Turn_Mover, GV.Shoulder_Position_Y, GV.Right_Front_Joint_Front_View_X, GV.Right_Front_Joint_Front_View_Y, GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM], GV.Foot_Current_Pos_Y[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM])
    #==============


    #--------------get center point of FRONT feet--------------------------
    Feet_Distance = GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM] - GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM]
    if Feet_Distance < 0:
    
      Feet_Distance = Feet_Distance * -1
      Center_Div = Feet_Distance / 2
      #place the FRONT center point half distance----------------------------
      GV.Center_BODY_Feet_Side_X = GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM] + Center_Div
    #ENDEX================
    else:
    
      Center_Div = Feet_Distance / 2
      #place the FRONT center point half distance----------------------------
      GV.Center_BODY_Feet_Side_X = GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM] + Center_Div
    #ENDEX================
    #==============================================================================================







    #-------side view for walking forward backward, sitting and head X rotation up down
    #get the body center 
    GV.Body_Center_X = GV.Uper_Body_Front_Back_Mover
    GV.Body_Center_Y = GV.BodyHeight_Total + GV.Over_Stretch_Height_Manager
    #place the hip
    Ang = Cn360(GV.Body_X_Tilt_Angle + 180)
    GV.Hip_Position_X = GV.Body_Center_X + Gqx(Ang, GV.Body_Torso_Radius)
    GV.Hip_Position_Y = GV.Body_Center_Y + GV.Gqy#(Ang, GV.Body_Torso_Radius)
    #place the hip
    Ang = Cn360(GV.Body_X_Tilt_Angle)
    GV.Shoulder_Position_X = GV.Body_Center_X + Gqx(Ang, GV.Body_Torso_Radius)
    GV.Shoulder_Position_Y = GV.Body_Center_Y + GV.Gqy#(Ang, GV.Body_Torso_Radius)
    #place the uper arm angle helpers
    GV.Uper_Arm_Angle_Help_X = GV.Body_Center_X
    GV.Uper_Arm_Angle_Help_Y = GV.Body_Center_Y
    #======================================================================


    #for hip twist when shoulders rotate hip Y
    Hip_Twist_Y_Rotate = (int) (GV.Uper_Body_Front_Side_Turn_Mover - GV.Center_BODY_Feet_Side_X) * 0.21#0.5

    #place top joints (of each arm and leg) to allow for raising and lowering each shoulder or hip joint individualy or together
    GV.Main_Joint_SideV_X[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_X
    GV.Main_Joint_SideV_Y[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_Y + GV.Z_Tilt_Mover_Value + GV.Main_Joint_SideVADJUST_Y[GV.LEFT_FRONT_FOOT_ID_NUM]
    #==
    GV.Main_Joint_SideV_X[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Hip_Position_X + (-Hip_Twist_Y_Rotate)
    GV.Main_Joint_SideV_Y[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Hip_Position_Y + GV.Z_Tilt_Mover_Value + GV.Main_Joint_SideVADJUST_Y[GV.LEFT_REAR_FOOT_ID_NUM]
    #==
    GV.Main_Joint_SideV_X[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_X
    GV.Main_Joint_SideV_Y[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Shoulder_Position_Y + (GV.Z_Tilt_Mover_Value * -1) + GV.Main_Joint_SideVADJUST_Y[GV.RIGHT_FRONT_FOOT_ID_NUM]
    #==
    GV.Main_Joint_SideV_X[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Hip_Position_X + Hip_Twist_Y_Rotate
    GV.Main_Joint_SideV_Y[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Hip_Position_Y + (GV.Z_Tilt_Mover_Value * -1) + GV.Main_Joint_SideVADJUST_Y[GV.RIGHT_REAR_FOOT_ID_NUM]
    #===================================================================


    #place the main joints default positions============================================================
    Do_IK_And_Get_Limb_Angles(GV.LEFT_REAR_FOOT_ID_NUM, GV.Rear_upperArmLength, GV.Rear_forearmLength, GV.Rear_footLength)
    #colect joint angles 
    GV.Left_Rear_Uper_Arm_X_Angle = GV.Uper_Arm_X_Angle_OUT
    GV.Left_Rear_Fore_Arm_Angle = GV.Fore_Arm_Angle_OUT
    #==========================================================================================================

    #place the main joints default positions============================================================
    add_Ys1 = GV.Ground_Level_Y - GV.Foot_Current_Pos_Y[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM]
    if add_Ys1 < 0:
      add_Ys1 = 0
    #ENDEX================
    Do_IK_And_Get_Limb_Angles_Front(GV.LEFT_FRONT_FOOT_ID_NUM, add_Ys1, GV.Front_upperArmLength, GV.Front_forearmLength, GV.Front_footLength)
    #colect joint angles
    GV.Left_Front_Uper_Arm_X_Angle = GV.Uper_Arm_X_Angle_OUT
    GV.Left_Front_Fore_Arm_Angle = GV.Fore_Arm_Angle_OUT
    #==========================================================================================================

    #place the main joints default positions============================================================
    Do_IK_And_Get_Limb_Angles(GV.RIGHT_REAR_FOOT_ID_NUM, GV.Rear_upperArmLength, GV.Rear_forearmLength, GV.Rear_footLength)
    #colect joint angles 
    GV.Right_Rear_Uper_Arm_X_Angle = GV.Uper_Arm_X_Angle_OUT
    GV.Right_Rear_Fore_Arm_Angle = GV.Fore_Arm_Angle_OUT
    #==========================================================================================================

    #place the main joints default positions============================================================
    add_Ys1 = GV.Ground_Level_Y - GV.Foot_Current_Pos_Y[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM]
    if add_Ys1 < 0:
      add_Ys1 = 0
    #ENDEX================
    Do_IK_And_Get_Limb_Angles_Front(GV.RIGHT_FRONT_FOOT_ID_NUM, add_Ys1, GV.Front_upperArmLength, GV.Front_forearmLength, GV.Front_footLength)
    #colect joint angles
    GV.Right_Front_Uper_Arm_X_Angle = GV.Uper_Arm_X_Angle_OUT
    GV.Right_Front_Fore_Arm_Angle = GV.Fore_Arm_Angle_OUT
    #==========================================================================================================




    #place and rotate the head position (x rotate UP Down)
    Ang = GV.Head_X_Rotation_Angle
    GV.Head_Pos_X = GV.Shoulder_Position_X + Gqx(Ang, GV.Neck_Length)
    GV.Head_Pos_Y = GV.Shoulder_Position_Y + GV.Gqy#(Ang, GV.Neck_Length)
    #--------------------------------------------------------------------------------------------------




















    #-----------to make top view representation of whole body including live movement parts positions and trangle weight shift sector represetation

    Body_Torso_Raduis_TOPV = 80#GV.Body_Torso_Radius
    
    
    GV.Body_Center_Of_Mass_X = GV.screen_Center
    GV.Body_Center_Of_Mass_Y = GV.screen_Center + 50#(+50 is to bring body down screen a bit more
    
    GV.Shoulder_Top_REP_X = GV.Body_Center_Of_Mass_X + Gqx(0, Body_Torso_Raduis_TOPV)
    GV.Shoulder_Top_REP_Y = GV.Body_Center_Of_Mass_Y + GV.Gqy#(0, Body_Torso_Raduis_TOPV)
    GV.Shoulder_Top_REP_Raduis = 50#60


    GV.Hip_Top_REP_X = GV.Body_Center_Of_Mass_X + Gqx(180, Body_Torso_Raduis_TOPV)
    GV.Hip_Top_REP_Y = GV.Body_Center_Of_Mass_Y + GV.Gqy#(180, Body_Torso_Raduis_TOPV)
    GV.Hip_Top_REP_Raduis = 50#60





    #for twisting shoulders joints when turning shoulders in Y axis to
    Shoulder_Y_Rotate_Include = (int) (90 - GV.Sholder_Rotate_Angle) * -1
    Left_Shoulder_Y_Rotate = 270 + Shoulder_Y_Rotate_Include
    Right_Shoulder_Y_Rotate = 90 + Shoulder_Y_Rotate_Include
    
    Neck_Y_Rotate = 360 + Shoulder_Y_Rotate_Include
    Head_Y_Rotate = 270 + Shoulder_Y_Rotate_Include + GV.Head_Y_Rotation_Angle#+neck_angle_rotate


    GV.Head_Lenght_Top_REP = 10
    GV.Neck_Length_Top_REP = 30
    
    GV.Neck_Top_REP_Pos_X = GV.Shoulder_Top_REP_X + Gqx(Neck_Y_Rotate, GV.Neck_Length_Top_REP)
    GV.Neck_Top_REP_Pos_Y = GV.Shoulder_Top_REP_Y + GV.Gqy#(Neck_Y_Rotate, GV.Neck_Length_Top_REP)


    GV.Head_Top_REP_Pos_X = GV.Neck_Top_REP_Pos_X + Gqx(Head_Y_Rotate, GV.Head_Lenght_Top_REP)
    GV.Head_Top_REP_Pos_Y = GV.Neck_Top_REP_Pos_Y + GV.Gqy#(Head_Y_Rotate, GV.Head_Lenght_Top_REP)


    GV.Left_Front_Main_Joint_Top_REP_X = GV.Shoulder_Top_REP_X + Gqx(Left_Shoulder_Y_Rotate, GV.Shoulder_Top_REP_Raduis)
    GV.Left_Front_Main_Joint_Top_REP_Y = GV.Shoulder_Top_REP_Y + GV.Gqy#(Left_Shoulder_Y_Rotate, GV.Shoulder_Top_REP_Raduis)
    
    GV.Right_Front_Main_Joint_Top_REP_X = GV.Shoulder_Top_REP_X + Gqx(Right_Shoulder_Y_Rotate, GV.Shoulder_Top_REP_Raduis)
    GV.Right_Front_Main_Joint_Top_REP_Y = GV.Shoulder_Top_REP_Y + GV.Gqy#(Right_Shoulder_Y_Rotate, GV.Shoulder_Top_REP_Raduis)
    

    GV.Left_Rear_Main_Joint_Top_REP_X = GV.Hip_Top_REP_X + Gqx(270, GV.Hip_Top_REP_Raduis)
    GV.Left_Rear_Main_Joint_Top_REP_Y = GV.Hip_Top_REP_Y + GV.Gqy#(270, GV.Hip_Top_REP_Raduis)
    
    GV.Right_Rear_Main_Joint_Top_REP_X = GV.Hip_Top_REP_X + Gqx(90, GV.Hip_Top_REP_Raduis)
    GV.Right_Rear_Main_Joint_Top_REP_Y = GV.Hip_Top_REP_Y + GV.Gqy#(90, GV.Hip_Top_REP_Raduis)

    #---
    Foot_Front_Back_Angle = 0
    Foot_Distance_To_Joint = 0
    #---

    #Place foot live top view
    if GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM] >= GV.Main_Joint_SideV_X[GV.LEFT_FRONT_FOOT_ID_NUM]:
      Foot_Distance_To_Joint = (GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM] - GV.Main_Joint_SideV_X[GV.LEFT_FRONT_FOOT_ID_NUM])
      Foot_Front_Back_Angle = Left_Shoulder_Y_Rotate + 90#this places the foot in front of shoulder (sort of)
    #====
    if GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM] < GV.Main_Joint_SideV_X[GV.LEFT_FRONT_FOOT_ID_NUM]:
      Foot_Distance_To_Joint = (GV.Main_Joint_SideV_X[GV.LEFT_FRONT_FOOT_ID_NUM] - GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM])
      Foot_Front_Back_Angle = Left_Shoulder_Y_Rotate - 90#this places the foot in front of shoulder (sort of)
    #-------------------------------------------------------------------------------------------------------------------------
    GV.Foot_Top_REP_X[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Left_Front_Main_Joint_Top_REP_X + Gqx(Foot_Front_Back_Angle, Foot_Distance_To_Joint)
    GV.Foot_Top_REP_Y[GV.LEFT_FRONT_FOOT_ID_NUM] = GV.Left_Front_Main_Joint_Top_REP_Y + GV.Gqy#(Foot_Front_Back_Angle, Foot_Distance_To_Joint)
    #===============================================================================================================================


    #Place foot live top view
    if GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM] >= GV.Main_Joint_SideV_X[GV.RIGHT_FRONT_FOOT_ID_NUM]:
      Foot_Distance_To_Joint = (GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM] - GV.Main_Joint_SideV_X[GV.RIGHT_FRONT_FOOT_ID_NUM])
      Foot_Front_Back_Angle = Right_Shoulder_Y_Rotate - 90#this places the foot in front of shoulder (sort of)
    #====
    if GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM] < GV.Main_Joint_SideV_X[GV.RIGHT_FRONT_FOOT_ID_NUM]:
      Foot_Distance_To_Joint = (GV.Main_Joint_SideV_X[GV.RIGHT_FRONT_FOOT_ID_NUM] - GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM])
      Foot_Front_Back_Angle = Right_Shoulder_Y_Rotate + 90#this places the foot in front of shoulder (sort of)
    #-------------------------------------------------------------------------------------------------------------------------
    GV.Foot_Top_REP_X[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Right_Front_Main_Joint_Top_REP_X + Gqx(Foot_Front_Back_Angle, Foot_Distance_To_Joint)
    GV.Foot_Top_REP_Y[GV.RIGHT_FRONT_FOOT_ID_NUM] = GV.Right_Front_Main_Joint_Top_REP_Y + GV.Gqy#(Foot_Front_Back_Angle, Foot_Distance_To_Joint)
    #===============================================================================================================================









    #Place foot live top view
    if GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM] >= GV.Main_Joint_SideV_X[GV.LEFT_REAR_FOOT_ID_NUM]:
      Foot_Distance_To_Joint = (GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM] - GV.Main_Joint_SideV_X[GV.LEFT_REAR_FOOT_ID_NUM])
      Foot_Rear_Back_Angle = 0
    #====
    if GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM] < GV.Main_Joint_SideV_X[GV.LEFT_REAR_FOOT_ID_NUM]:
      Foot_Distance_To_Joint = (GV.Main_Joint_SideV_X[GV.LEFT_REAR_FOOT_ID_NUM] - GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM])
      Foot_Rear_Back_Angle = 180
    #-------------------------------------------------------------------------------------------------------------------------
    GV.Foot_Top_REP_X[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Left_Rear_Main_Joint_Top_REP_X + Gqx(Foot_Rear_Back_Angle, Foot_Distance_To_Joint)
    GV.Foot_Top_REP_Y[GV.LEFT_REAR_FOOT_ID_NUM] = GV.Left_Rear_Main_Joint_Top_REP_Y + GV.Gqy#(Foot_Rear_Back_Angle, Foot_Distance_To_Joint)
    #===============================================================================================================================


    #Place foot live top view
    if GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM] >= GV.Main_Joint_SideV_X[GV.RIGHT_REAR_FOOT_ID_NUM]:
      Foot_Distance_To_Joint = (GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM] - GV.Main_Joint_SideV_X[GV.RIGHT_REAR_FOOT_ID_NUM])
      Foot_Rear_Back_Angle = 0
    #====
    if GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM] < GV.Main_Joint_SideV_X[GV.RIGHT_REAR_FOOT_ID_NUM]:
      Foot_Distance_To_Joint = (GV.Main_Joint_SideV_X[GV.RIGHT_REAR_FOOT_ID_NUM] - GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM])
      Foot_Rear_Back_Angle = 180
    #-------------------------------------------------------------------------------------------------------------------------
    GV.Foot_Top_REP_X[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Right_Rear_Main_Joint_Top_REP_X + Gqx(Foot_Rear_Back_Angle, Foot_Distance_To_Joint)
    GV.Foot_Top_REP_Y[GV.RIGHT_REAR_FOOT_ID_NUM] = GV.Right_Rear_Main_Joint_Top_REP_Y + GV.Gqy#(Foot_Rear_Back_Angle, Foot_Distance_To_Joint)
    #===============================================================================================================================




    #now create the sector triangles showing weight shift right before foot lift
    








    #show me stuff
    if GV.Select_View_To_Draw_NUM == 2:
      GV.DrawMatrix_NUM_IN = 2

      #draw line from center mass to shoulder mid point
      Add_Draw_Points(GV.Body_Center_Of_Mass_X, GV.Body_Center_Of_Mass_Y, GV.Shoulder_Top_REP_X, GV.Shoulder_Top_REP_Y, 0)
      Add_Draw_Points(GV.Body_Center_Of_Mass_X, GV.Body_Center_Of_Mass_Y, 0, 0, 2)
      Add_Draw_Points(GV.Body_Center_Of_Mass_X, GV.Body_Center_Of_Mass_Y, GV.Hip_Top_REP_X, GV.Hip_Top_REP_Y, 0)
      #show neck line
      Add_Draw_Points(GV.Shoulder_Top_REP_X, GV.Shoulder_Top_REP_Y, GV.Neck_Top_REP_Pos_X, GV.Neck_Top_REP_Pos_Y, 0)
      #show head line
      Add_Draw_Points(GV.Neck_Top_REP_Pos_X, GV.Neck_Top_REP_Pos_Y, GV.Head_Top_REP_Pos_X, GV.Head_Top_REP_Pos_Y, 0)

      #show front main joints
      Add_Draw_Points(GV.Shoulder_Top_REP_X, GV.Shoulder_Top_REP_Y, GV.Left_Front_Main_Joint_Top_REP_X, GV.Left_Front_Main_Joint_Top_REP_Y, 0)
      Add_Draw_Points(GV.Shoulder_Top_REP_X, GV.Shoulder_Top_REP_Y, GV.Right_Front_Main_Joint_Top_REP_X, GV.Right_Front_Main_Joint_Top_REP_Y, 0)
      #show rear main joints
      Add_Draw_Points(GV.Hip_Top_REP_X, GV.Hip_Top_REP_Y, GV.Left_Rear_Main_Joint_Top_REP_X, GV.Left_Rear_Main_Joint_Top_REP_Y, 0)
      Add_Draw_Points(GV.Hip_Top_REP_X, GV.Hip_Top_REP_Y, GV.Right_Rear_Main_Joint_Top_REP_X, GV.Right_Rear_Main_Joint_Top_REP_Y, 0)


      #show the front feet
      Add_Draw_Points(GV.Left_Front_Main_Joint_Top_REP_X, GV.Left_Front_Main_Joint_Top_REP_Y, GV.Foot_Top_REP_X[GV.LEFT_FRONT_FOOT_ID_NUM], GV.Foot_Top_REP_Y[GV.LEFT_FRONT_FOOT_ID_NUM], 2)
      Add_Draw_Points(GV.Right_Front_Main_Joint_Top_REP_X, GV.Right_Front_Main_Joint_Top_REP_Y, GV.Foot_Top_REP_X[GV.RIGHT_FRONT_FOOT_ID_NUM], GV.Foot_Top_REP_Y[GV.RIGHT_FRONT_FOOT_ID_NUM], 2)

      Add_Draw_Points(GV.Left_Rear_Main_Joint_Top_REP_X, GV.Left_Rear_Main_Joint_Top_REP_Y, GV.Foot_Top_REP_X[GV.LEFT_REAR_FOOT_ID_NUM], GV.Foot_Top_REP_Y[GV.LEFT_REAR_FOOT_ID_NUM], 2)
      Add_Draw_Points(GV.Right_Rear_Main_Joint_Top_REP_X, GV.Right_Rear_Main_Joint_Top_REP_Y, GV.Foot_Top_REP_X[GV.RIGHT_REAR_FOOT_ID_NUM], GV.Foot_Top_REP_Y[GV.RIGHT_REAR_FOOT_ID_NUM], 2)
    #-----END_Foot_Top_REP----------------------------------------------------------------------------------------------------------------























    #--------------get center point of FRONT feet--------------------------
    Feet_Distance = GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM] - GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM]
    GV.Center_Front_X = 0
    Center_Div = 0
    if Feet_Distance < 0:
    
      Feet_Distance = Feet_Distance * -1
      Center_Div = Feet_Distance / 2
      #place the FRONT center point half distance----------------------------
      GV.Center_Front_X = GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FOOT_ID_NUM] + Center_Div
    #ENDEX================
    else:
    
      Center_Div = Feet_Distance / 2
      #place the FRONT center point half distance----------------------------
      GV.Center_Front_X = GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FOOT_ID_NUM] + Center_Div
    #ENDEX================
    #-----------------------------------------------------------------------

    #--------------get center point of rear feet--------------------------
    Feet_Distance = GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM] - GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM]
    GV.Center_Rear_X = 0
    if Feet_Distance < 0:
    
      Feet_Distance = Feet_Distance * -1
      Center_Div = Feet_Distance / 2
      #place the rear center point half distance----------------------------
      GV.Center_Rear_X = GV.Foot_Current_Pos_X[GV.LEFT_REAR_FOOT_ID_NUM] + Center_Div
    #ENDEX================
    else:
    
      Center_Div = Feet_Distance / 2
      #place the rear center point half distance----------------------------
      GV.Center_Rear_X = GV.Foot_Current_Pos_X[GV.RIGHT_REAR_FOOT_ID_NUM] + Center_Div
    #ENDEX================
    #-----------------------------------------------------------------------


    #-----Now get the body center point of front and rear feet------------
    Feet_Distance = GV.Center_Rear_X - GV.Center_Front_X
    if Feet_Distance < 0:
    
      Feet_Distance = Feet_Distance * -1
      Center_Div = Feet_Distance / 2
      #place the rear center point half distance----------------------------
      GV.Center_BODY_Feet_X = GV.Center_Rear_X + Center_Div
    #ENDEX================
    else:
    
      Center_Div = Feet_Distance / 2
      #place the rear center point half distance----------------------------
      GV.Center_BODY_Feet_X = GV.Center_Front_X + Center_Div
    #ENDEX================
    #bring feet ceter front abit (to bring body forwar abit) wit ofset value
    #GV.Center_BODY_Feet_X = GV.Center_BODY_Feet_X + 21#24
    GV.Center_BODY_Feet_X = (int) (GV.Center_BODY_Feet_X + 21)#24
    #---------------------------------------------------------------------
    DriveServos()




  #ENDEX================
  #====================

















