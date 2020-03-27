#Code writen by Yeshim, year 2020(youtube channel Y-Spectrum-2), free to use for everyone, hope it helps
#you will need to install python 3 (im using IDLE version(3.5.3) on my pc) and pygame on your pc or raspberry pi for this code to work
#should run on raspberry py 3 and above
#using pygame 1.9.4 on my pc



#for drawing using pygame
import pygame # Using the 'pygame' library

#to use time.sleep(1)
import time
#-----------
import math
from math import pi as M_PI

from Global_Essentials_Class import Global_Essentials_Class
GE = Global_Essentials_Class
from Global_Variables_Only_Class import Global_Variables_Only_Class
GV = Global_Variables_Only_Class





#initialize the esentials and body start position
GE.Initialize_Positions()


pygame.init()
#for playing sounds
#pygame.mixer.init()

# Create the window
screen = pygame.display.set_mode((GV.TempWidth, GV.TempHeight))
pygame.display.set_caption("Bot Dog World")






#returns the ID num of the foot oposite balance of the input foot
def Get_Oposite_Foot(Foot_ID_NUM):
  Oposite_Foot_ID_NUM = 0
  
  #if this is Left Rear foot
  if Foot_ID_NUM == GV.LEFT_REAR_FOOT_ID_NUM:
    Oposite_Foot_ID_NUM = GV.RIGHT_FRONT_FOOT_ID_NUM
  #ENDEX================
    #if this is Left Rear foot
  if Foot_ID_NUM == GV.RIGHT_FRONT_FOOT_ID_NUM or Foot_ID_NUM == GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM:
    Oposite_Foot_ID_NUM = GV.LEFT_REAR_FOOT_ID_NUM
  #ENDEX================
  #if this is Rith Rear foot
  if Foot_ID_NUM == GV.RIGHT_REAR_FOOT_ID_NUM:
    Oposite_Foot_ID_NUM = GV.LEFT_FRONT_FOOT_ID_NUM
  #ENDEX================
    #if this is Right front foot
  if Foot_ID_NUM == GV.LEFT_FRONT_FOOT_ID_NUM or Foot_ID_NUM == GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM:
    Oposite_Foot_ID_NUM = GV.RIGHT_REAR_FOOT_ID_NUM
  #ENDEX================
  return Oposite_Foot_ID_NUM
#------------------------------------------------------------------------------------------







#New oposite foot Z_Tilt additive (so if lifting front left foot then first lift rear right foot to contain more of body weight before lifting left front foot
def  Z_Tilt_Additive(Foot_ID_NUM, Wanted_Z_Tilt_IN, Z_Tilt_Speed_IN):
  Feet_Adjust_Done = False
  Oposite_Foot_ID_NUM = Get_Oposite_Foot(Foot_ID_NUM)
  Up_Lift_Speed_Increse = Z_Tilt_Speed_IN

  #if this is not a reset then add 1 so the foot thats lifting will lift faster always
  if Wanted_Z_Tilt_IN > 0:
    Up_Lift_Speed_Increse = Z_Tilt_Speed_IN + 1
#=========================================================

  #NEW to not push too hard, reduce the push foot amount
  Reduced_Push_Amount = Wanted_Z_Tilt_IN
  if Wanted_Z_Tilt_IN > 2:
    Reduced_Push_Amount = Wanted_Z_Tilt_IN - 1
  #-----------------------------------------------------
  
  
  #push the this foot down and lift the oposite foot upward to carry more body weight
  if GE.Foot_Y_Pos_ADJUST_Func(Foot_ID_NUM, -Reduced_Push_Amount, Z_Tilt_Speed_IN) == True and GE.Foot_Y_Pos_ADJUST_Func(Oposite_Foot_ID_NUM, (Wanted_Z_Tilt_IN + 1), Up_Lift_Speed_Increse) == True:
    Feet_Adjust_Done = True

  return Feet_Adjust_Done
#------------------------------------------------------------------------------------------




  


#recieves a foot to move and does nessary body weight shift (takes body weight off the foot) then moves the foot to the trajectory selected
def Tilt_Body_And_Lift_Foot(Foot_ID_NUM, Walk_Type_IN):

  Move_Status = 0
  Feet_Adjust_Done = False
  Body_Adjust_Select = 0
  done_Move_Foot = False


  STATUS_DONE_01 = False
  STATUS_DONE_02 = False
  MOVEMENT_ACTIVE = False


  #setup stuf for foot movement
  if GV.Foot_Move_Steps == 0:

    #new add to reset body to center mass speed to not dart forward
    GV.Body_Center_Accel_Deccel_INC = 0


    GV.Wanted_ZZ_Tilt_AA = GV.Wanted_Z_Tilt
    #To move LEFT_REAR_FOOT_ID_NUM, or LEFT_FRONT_FOOT_ID_NUM tilt body to the Right 5 degrees -GV.Wanted_Z_Tilt
    if GV.LEFT_REAR_FOOT_ID_NUM == Foot_ID_NUM or GV.LEFT_FRONT_FOOT_ID_NUM == Foot_ID_NUM or GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM == Foot_ID_NUM:
      GV.Wanted_ZZ_Tilt_AA = -GV.Wanted_Z_Tilt + (-1)#cause right tilt needs a bit more
    #===============================================

    #say if this foot is a front foot that is being moved
    GV.Is_A_Front_Foot = False
    if GV.RIGHT_FRONT_FOOT_ID_NUM == Foot_ID_NUM or GV.LEFT_FRONT_FOOT_ID_NUM == Foot_ID_NUM or GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM == Foot_ID_NUM or GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM == Foot_ID_NUM:
      GV.Is_A_Front_Foot = True
    #===============================================
    #say if this foot is a rear foot that is being moved
    GV.Is_A_Rear_Foot = False
    if GV.RIGHT_REAR_FOOT_ID_NUM == Foot_ID_NUM or GV.LEFT_REAR_FOOT_ID_NUM == Foot_ID_NUM:
      GV.Is_A_Rear_Foot = True
    #===============================================
    

    #go to next step
    GV.Foot_Move_Steps = 1
  #ENDEX================
  






  
  #Make nessesary body adjustments to prepare to lift this foot
  if GV.Foot_Move_Steps == 1:
    Feet_Adjust_Done = 0
    Feet_Adjust_Done = False
    
    #for walking forward if this is the first front foot step (left of right front) to move back a bit
    if Walk_Type_IN == GV.WALK_TYPE_01 and GV.Front_Feet_Positions_ID == 1 and GV.Is_A_Front_Foot == True:
      GV.Center_BODY_Feet_X_Offset = -25#35
      Body_Adjust_Select = 1
    #=============================================================
    #New now move forward a bit more to lift rear feet whenw walking
    if Walk_Type_IN == GV.WALK_TYPE_01:
      if GV.Is_A_Rear_Foot == True:
        GV.Center_BODY_Feet_X_Offset = 12#40
        Body_Adjust_Select = 1
    #=============================================================
        

    #for returning to idle front foot balance (move back a bit)
    if Walk_Type_IN == GV.WALK_TO_IDLE and GV.Is_A_Front_Foot == True:
      GV.Center_BODY_Feet_X_Offset = -40#35
      Body_Adjust_Select = 1
    #=============================================================
    #for returning to idle rear foot balance (move front a bit)
    if Walk_Type_IN == GV.WALK_TO_IDLE:
      if GV.Is_A_Rear_Foot == True:
        GV.Center_BODY_Feet_X_Offset = 20#25
        Body_Adjust_Select = 1
    #=============================================================







    #do the selected body adjustment
    if Body_Adjust_Select > 0:

      #do the selected center of mass adjustment then go to next step
      if Body_Adjust_Select == 1:
        if GE.Body_To_Center_Mass_Move_Func(GV.Body_To_Center_Mass_Speed) == True:
          Feet_Adjust_Done = True
          GV.Center_BODY_Feet_X_Offset = 0
      #===========================================================

      #go to next step when selected body adjust is done
      if Feet_Adjust_Done == True:
        GV.Foot_Move_Steps = 2
      #===========================================================
        
    else:
      #if no center mass ajustment selected then just go to next step
      GV.Foot_Move_Steps = 2
  #ENDEX================
   







  #step 2 shift weight
  if GV.Foot_Move_Steps == 2:
    #%%%%---Tilt to shift body weight
    Feet_Adjust_Done = False
    if GE.Do_Z_TILT_Func(GV.Wanted_ZZ_Tilt_AA, GV.Z_Tilt_SPeed) == True and Z_Tilt_Additive(Foot_ID_NUM, GV.Z_Tilt_Add_Amount, GV.Z_Tilt_Add_Speed):
      Feet_Adjust_Done = True
    #ENDEX================
    #%%%%%---===============================================================================================

    #====make sure the body is on the ground (robot is not lifted off ground)
    if Feet_Adjust_Done == True:
      #if Body_Feet_Grounded() == True:
      GV.Foot_Move_Steps = 3
    #ENDEX================
    #=============================================





  #step check to make sure body accelerometer has settled and body is truely tilted
  if GV.Foot_Move_Steps == 3:
    Feet_Adjust_Done = True
    #if adjustments done
    if Feet_Adjust_Done == True:
      GV.Foot_Move_Steps = 4
  #==============================================================
        
        

  #step take forward step with the foot
  if GV.Foot_Move_Steps == 4:
    #***===============================================================================================
    if GE.Move_Foot_To_Target(Foot_ID_NUM, GV.Leg_Lift_Height) == 1:
      #if foot was moved successfully to destination then proceed
      if GV.Move_Foot_Situation == 0:
        GV.Foot_Move_Steps = 5
      #if foot was reveresed cause of steping on obstacle
      if GV.Move_Foot_Situation == 1:
        GV.Foot_Move_Steps = 9#
        print("steped on something")
      #if foot was successfully to destination but we fell towards the lifted foot proceed as usual but maybe tilt more next time
      if GV.Move_Foot_Situation == 2:
        GV.Foot_Move_Steps = 5
    #ENDEX================
  #ENDEX================




  #if this is a front foot that landed then and movement direction is forward then move to center mass and return z tilt to center
  if GV.Foot_Move_Steps == 5:
    STATUS_DONE_01 = False
    STATUS_DONE_02 = False
    MOVEMENT_ACTIVE = False
    
    #reset z tilt is done for all feet in all walk types
    if Z_Tilt_Additive(Foot_ID_NUM, 0, GV.Z_Tilt_Add_RESET_Speed) == True:
      STATUS_DONE_01 = True
    #==================================================================
    

    #all movements that happen on front feet landing completion
    if GV.Is_A_Front_Foot == True:

      #if this is forward walk then move body to the centergrav also tilt body to opposite side to prepare for feet on opposite side to lift
      if Walk_Type_IN == GV.WALK_TYPE_01:
        #just to acknwoledge that we are moving to front feet center
        MOVEMENT_ACTIVE = True
        #if this is left front foot landed then tilt body to left (to setup for right feet lift)
        if GV.LEFT_FRONT_FOOT_ID_NUM == Foot_ID_NUM:
          GV.Wanted_ZZ_Tilt_AA = GV.Wanted_Z_Tilt
        #===============================================
        #if this is left front foot landed then tilt body to right (to setup for left feet lift)
        if GV.RIGHT_FRONT_FOOT_ID_NUM == Foot_ID_NUM:
          GV.Wanted_ZZ_Tilt_AA = -GV.Wanted_Z_Tilt
        #===============================================
        
        if GE.Body_To_Center_Mass_Move_Func(GV.Body_To_Center_Mass_Speed) == True and GE.Do_Z_TILT_Func(GV.Wanted_ZZ_Tilt_AA, GV.Z_Tilt_SPeed) == True:
          STATUS_DONE_02 = True
      #ENDEX=================================================================================================================

      #if this is return to idle then return body to center mass and z tilt back to center
      if Walk_Type_IN == GV.WALK_TO_IDLE:
        #just to acknwoledge that we are moving to front feet center
        MOVEMENT_ACTIVE = True
        if GE.Body_To_Center_Mass_Move_Func(GV.Body_To_Center_Mass_Speed) == True and GE.Do_Z_TILT_Func(0, GV.Z_Tilt_SPeed) == True:
          STATUS_DONE_02 = True
      #ENDEX=================================================================================================================



    #if no movement active above then allow move to next move or be stuck here
    if MOVEMENT_ACTIVE == False:
      STATUS_DONE_02 = True
    #=========================================================================

    #if all done move to next step
    if STATUS_DONE_01 == True and STATUS_DONE_02 == True:
      GV.Foot_Move_Steps = 6
    
  #ENDEX================
  #-------------------------------------------------------------------------------------------


  #say we are done
  if GV.Foot_Move_Steps == 6:
    GV.Foot_Move_Steps = 0
    done_Move_Foot = True



  return done_Move_Foot

#--end tilt body And lift foot-------------------------------------------------------------------------------------------------------------





#Function for waiting a while
def General_Wait_Interval_Func(Wait_Interval_IN):
  done_count = False
  #do count up
  GV.General_Wait_Interval_INC = GV.General_Wait_Interval_INC + 1
  if GV.General_Wait_Interval_INC > Wait_Interval_IN:
    GV.General_Wait_Interval_INC = 0#Wait_Interval_IN
    done_count = True
  #--------------------------------------
  return done_count
#==============================================================







#used to stay at whatever position the body is
def General_IDLE_Func(Action_Type_IN):

  Body_Adjust_Done = False
  #test foot step
  if GV.Move_Steps == 0:
    GV.Move_Steps = 1
  #ENDEX================  

  
  #if sitting then Return head X to normal resting position and turn head Y to look straight
  if GV.Move_Steps == 1:
    GV.X_Head_Rotate_Speed = 8#
    #set speed for this head rotation to be really fast
    GV.Y_Head_Rotate_Speed = 8#10
    #If body is sitting then lower slightly more for a ground scan
    if GV.Body_Is_Sitting == True:
      GV.HEAD_X_Tilt_Angle_Select = 55
      #---------------------------------------
    else:
      #if standing
      GV.HEAD_X_Tilt_Angle_Select = 85
      #ENDEX================
    #---------------------------------------------------
    #go to next step if done
    if GE.Do_Head_X_Rotate_UP_DOWN_Accel(GV.HEAD_X_Tilt_Angle_Select, GV.X_Head_Rotate_Speed) == True and GE.Do_Head_Y_Rotate_Left_Right(90, GV.Y_Head_Rotate_Speed) == True:
      GV.Move_Steps = 2
  #ENDEX================




  #wait 100 frames to pass
  if GV.Move_Steps == 2:
    if General_Wait_Interval_Func(80) == True:
      Body_Adjust_Done = True
    #============================================

    #move to next step
    if  Body_Adjust_Done == True:
      #move to next step
      GV.Move_Steps = 3
    #===========================================================
  #====================



  #step 21 say a walk cycle is complete
  if GV.Move_Steps == 3:
  
    GV.Number_Of_Times_Act_Done = GV.Number_Of_Times_Act_Done + 1
    if GV.Number_Of_Times_Act_Done > 10000:
    
      GV.Number_Of_Times_Act_Done = 10000
    #ENDEX================
    #go to first step to restart walk process
    GV.Move_Steps = 0
    #log the completed activity
    #Activity_Complete_Log()
  #ENDEX================
  #======================

#ENDEX================






def WALK_TYPE_01_Func(Walk_Type_IN):




  #Setup movement parameters
  if GV.Move_Steps == 0 and GV.WALK_Reached_Good_Exit_Point == False:
    GE.Set_Walk_Values(Walk_Type_IN)
    GV.Walk_Completed_Steps = 0
  #=====================================================






  #step 1
  if GV.Move_Steps == 1 and GV.WALK_Reached_Good_Exit_Point == False:   
    #%%%%---Tilt to shift body weight to Front Right leg (Z tilt must be done with Hip Y rotate to match)
    Feet_Adjust_Done = False
    if Tilt_Body_And_Lift_Foot(GV.Feet_Move_Sequence[GV.Move_Steps], Walk_Type_IN) == True:
      GV.Move_Steps = 2
      #see if there is a condition to skip to end of this act
      #Check_Interupt_Condition(5, Walk_Type_IN)
    #ENDEX================
  #============
  #step 2
  if GV.Move_Steps == 2 and GV.WALK_Reached_Good_Exit_Point == False:  
    #%%%%---Tilt to shift body weight to Front Right leg (Z tilt must be done with Hip Y rotate to match)
    Feet_Adjust_Done = False
    if Tilt_Body_And_Lift_Foot(GV.Feet_Move_Sequence[GV.Move_Steps], Walk_Type_IN) == True:
      GV.Move_Steps = 3
      #see if there is a condition to skip to end of this act
      #Check_Interupt_Condition(5, Walk_Type_IN)
    #ENDEX================
  #============
  #step 3
  if GV.Move_Steps == 3 and GV.WALK_Reached_Good_Exit_Point == False:   
    #%%%%---Tilt to shift body weight to Front Right leg (Z tilt must be done with Hip Y rotate to match)
    Feet_Adjust_Done = False
    if Tilt_Body_And_Lift_Foot(GV.Feet_Move_Sequence[GV.Move_Steps], Walk_Type_IN) == True:
      GV.Move_Steps = 4
      #see if there is a condition to skip to end of this act
      #Check_Interupt_Condition(5, Walk_Type_IN)
    #ENDEX================
  #============
  #step 4
  if GV.Move_Steps == 4 and GV.WALK_Reached_Good_Exit_Point == False:   
    #%%%%---Tilt to shift body weight to Front Right leg (Z tilt must be done with Hip Y rotate to match)
    Feet_Adjust_Done = False
    if Tilt_Body_And_Lift_Foot(GV.Feet_Move_Sequence[GV.Move_Steps], Walk_Type_IN) == True:
      GV.Move_Steps = 5
      #see if there is a condition to skip to end of this act
      #Check_Interupt_Condition(5, Walk_Type_IN)
    #ENDEX================
  #============



  #step 5
  if GV.Move_Steps == 5:
    #get the ID number of the activity that just completed
    GV.Last_Completed_Body_Position_ID_NUM = Walk_Type_IN


    #count number of times this activity has been done
    GV.Number_Of_Times_Act_Done = GV.Number_Of_Times_Act_Done + 1
    if GV.Number_Of_Times_Act_Done > 10000:
      GV.Number_Of_Times_Act_Done = 10000
    #ENDEX================
    #go to first step to restart walk process
    GV.Move_Steps = 0
    #log the completed activity
    #Activity_Complete_Log()
  #ENDEX================
  #======================



#ENDEX================









def ROBOT_AI_CONTROL_FUNC():



  #Use this as entry point (select the first activity, and how many times it should be done) if this is the first time the robot is switched on
  if GV.Robot_Initial_Switched_ON == 0:
    #do do this only once in the whole ini
    GV.Robot_Initial_Switched_ON = 1
    #---ACTIVITY CHANGE,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    GE.ACTIVITY_CHANGE(GV.IDLE_STAND_01, 1)#GV.WALK_TYPE_01
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  #ENDEX================
  #=============================================




  #>>>>----ACTIVITY GV.IDLE_STAND_01
  if GV.Activity_Select == GV.IDLE_STAND_01:
    #do activity initialization stuff
    if GV.Activity_Start_Steps == 0:
    
      GV.Activity_Start_Steps = 1
      GV.Current_Activity_Name = GV.New_Act_Name
    #ENDEX================
    #do activity
    if GV.Activity_Start_Steps == 1:
      General_IDLE_Func(GV.IDLE_STAND_01)
    #ENDEX================

  #ENDEX================
  #>>END_ACTIVITY====================================================================================





  #>>>>----ACTIVITY GV.WALK_TYPE_01
  if GV.Activity_Select == GV.WALK_TYPE_01:
  
    #do activity initialization stuff
    if GV.Activity_Start_Steps == 0:
    
      GV.Activity_Start_Steps = 1
      GV.Current_Activity_Name = GV.New_Act_Name
    #ENDEX================
    #do activity
    if GV.Activity_Start_Steps == 1:
    
      WALK_TYPE_01_Func(GV.WALK_TYPE_01)
    #ENDEX================

  #ENDEX================
  #>>END_ACTIVITY====================================================================================






  #>>>>----ACTIVITY GV.WALK_TO_IDLE
  if GV.Activity_Select == GV.WALK_TO_IDLE:#WALK_TO_IDLE
  

    #do activity initialization stuff
    if GV.Activity_Start_Steps == 0:
    
      GV.Activity_Start_Steps = 1
      GV.Current_Activity_Name = GV.New_Act_Name
    #ENDEX================
    #do activity
    if GV.Activity_Start_Steps == 1:
      WALK_TYPE_01_Func(GV.WALK_TO_IDLE)
    #ENDEX================


  #ENDEX================
  #>>END_ACTIVITY====================================================================================









  #$$$$$$$$$$$Situation handler (switches activities)$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  #Check if Activity is done
  GV.Activity_Just_Finnished = 0
  if GV.Number_Of_Times_Act_Done > 0 and GV.Number_Of_Times_To_Do_Act > 0 and GV.Number_Of_Times_Act_Done >= GV.Number_Of_Times_To_Do_Act:
    GV.Activity_Just_Finnished = GV.Activity_Select
  #ENDEX================




  #just for testing movment types for now (this will loop between three activites==WALK_TYPE_01,WALK_TO_IDLE,IDLE_STAND_01==============
  Do_Environment_Explore_Activity = True#False

  #All activities must be finnished or terminated before starting another
  if Do_Environment_Explore_Activity == True:
    #if WALK_TYPE_01 is finished then switch activity
    if GV.Activity_Just_Finnished == GV.WALK_TYPE_01:
      #ACTIVITY CHANGE,,,,,,,,,,,,,,,,,,,,,,,,,,,,
      GE.ACTIVITY_CHANGE(GV.WALK_TO_IDLE, 1)# 
      #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #ENDEX================
    #======================================================
    #if WALK_TO_IDLE is finished then switch activity
    if GV.Activity_Just_Finnished == GV.WALK_TO_IDLE:
      #ACTIVITY CHANGE,,,,,,,,,,,,,,,,,,,,,,,,,,,,
      GE.ACTIVITY_CHANGE(GV.IDLE_STAND_01, 1)#
      #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #ENDEX================
    #======================================================
    #if IDLE_STAND_01 is finished then switch activity
    if GV.Activity_Just_Finnished == GV.IDLE_STAND_01:
      #ACTIVITY CHANGE,,,,,,,,,,,,,,,,,,,,,,,,,,,,
      GE.ACTIVITY_CHANGE(GV.WALK_TYPE_01, 4)#
      #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #ENDEX================
    #====================================================== 
  #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




  #playerText.text = "Act: "  + GV.Activity_Select#

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


def Draw_The_Stuff(Select_View_To_Draw):

  global screen

  i = 0
  d = 0
  color = (100, 100, 255)

  GV.Select_View_To_Draw_NUM = Select_View_To_Draw
  

  #draw the balance triangle if it exists
  if GV.Select_View_To_Draw_NUM == 2:
    GV.DrawMatrix_NUM_IN = 2

    #place the accelerometerz tilt position
    #Add_Draw_Points(GV.POSition_Accel_X, GV.POSition_Accel_Y, 0, 0, 1)
    pygame.draw.circle(screen, color, [(int) (GV.POSition_Accel_X), (int) (GV.POSition_Accel_Y)], 4)
    #==============================================================================================

    #====
  #=============================================================


  


  #-----------top view points and line
  #show me Head and neck positin
  if GV.Select_View_To_Draw_NUM == 1:
    GV.DrawMatrix_NUM_IN = 1
    Add_Draw_Points(GV.Shoulder_Top_View_X, GV.Shoulder_Top_View_Y, GV.Neck_Top_Pos_X, GV.Neck_Top_Pos_Y, 0)
    Add_Draw_Points(GV.Neck_Top_Pos_X, GV.Neck_Top_Pos_Y, GV.Head_Top_Pos_X, GV.Head_Top_Pos_Y, 0)
    Add_Draw_Points(GV.Shoulder_Top_View_X, GV.Shoulder_Top_View_Y, GV.Left_Front_Main_Joint_TopV_X, GV.Left_Front_Main_Joint_TopV_Y, 0)
    Add_Draw_Points(GV.Shoulder_Top_View_X, GV.Shoulder_Top_View_Y, GV.Right_Front_Main_Joint_X, GV.Right_Front_Main_Joint_Y, 0)
    #==
    Add_Draw_Points(GV.Neck_Top_Pos_X, GV.Neck_Top_Pos_Y, 0, 0, 0)
    Add_Draw_Points(GV.Head_Top_Pos_X, GV.Head_Top_Pos_Y, 0, 0, 0)
    Add_Draw_Points(GV.Left_Front_Main_Joint_TopV_X, GV.Left_Front_Main_Joint_TopV_Y, 0, 0, 0)
    Add_Draw_Points(GV.Right_Front_Main_Joint_X, GV.Right_Front_Main_Joint_Y, 0, 0, 0)
  #===============================================================







  #Front View stuff show me front view feet center (RIGHT SIDE RED, LEFT SIDE GREEN DRAW)
  if GV.Select_View_To_Draw_NUM == 4:
    GV.DrawMatrix_NUM_IN = 4
    Add_Draw_Points(GV.Center_BODY_Feet_Side_X, GV.Ground_Level_Y, 0, 0, 0)

    Add_Draw_Points(GV.Uper_Body_Front_Side_Turn_Mover, GV.Shoulder_Position_Y, GV.Left_Front_Joint_Front_View_X, GV.Left_Front_Joint_Front_View_Y, 0)
    Add_Draw_Points(GV.Uper_Body_Front_Side_Turn_Mover, GV.Shoulder_Position_Y, GV.Right_Front_Joint_Front_View_X, GV.Right_Front_Joint_Front_View_Y, 1)
    Add_Draw_Points(GV.Left_Front_Joint_Front_View_X, GV.Left_Front_Joint_Front_View_Y, GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM], GV.Foot_Current_Pos_Y[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM], 0)
    Add_Draw_Points(GV.Right_Front_Joint_Front_View_X, GV.Right_Front_Joint_Front_View_Y, GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM], GV.Foot_Current_Pos_Y[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM], 1)
    #==
    Add_Draw_Points(GV.Uper_Body_Front_Side_Turn_Mover, GV.Shoulder_Position_Y, 0, 0, 0)
    Add_Draw_Points(GV.Left_Front_Joint_Front_View_X, GV.Left_Front_Joint_Front_View_Y, 0, 0, 0)
    Add_Draw_Points(GV.Right_Front_Joint_Front_View_X, GV.Right_Front_Joint_Front_View_Y, 0, 0, 1)
    Add_Draw_Points(GV.Foot_Current_Pos_X[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM], GV.Foot_Current_Pos_Y[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM], 0, 0, 0)
    Add_Draw_Points(GV.Foot_Current_Pos_X[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM], GV.Foot_Current_Pos_Y[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM], 0, 0, 1)
    #==
    Add_Draw_Points(GV.Foot_Traje_Target_X[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM], GV.Foot_Traje_Target_Y[GV.LEFT_FRONT_FVIEW_FOOT_ID_NUM], 0, 0, 0)
    Add_Draw_Points(GV.Foot_Traje_Target_X[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM], GV.Foot_Traje_Target_Y[GV.RIGHT_FRONT_FVIEW_FOOT_ID_NUM], 0, 0, 1)#Right side red
  #---------------------------------------------------------------------------------------------------










  #SIDE VIEW STUFF show body x tilt torso level side view
  if GV.Select_View_To_Draw_NUM == 3:
    GV.DrawMatrix_NUM_IN = 3
    Add_Draw_Points(GV.Hip_Position_X, GV.Hip_Position_Y, GV.Shoulder_Position_X, GV.Shoulder_Position_Y, 2)#bgr
    #============================================================================================																						 #show me the foot target points
    Add_Draw_Points(GV.Foot_Traje_Target_X[GV.LEFT_REAR_FOOT_ID_NUM], GV.Foot_Traje_Target_Y[GV.LEFT_REAR_FOOT_ID_NUM], 0, 0, 0)
    Add_Draw_Points(GV.Foot_Traje_Target_X[GV.RIGHT_REAR_FOOT_ID_NUM], GV.Foot_Traje_Target_Y[GV.RIGHT_REAR_FOOT_ID_NUM], 0, 0, 0)
    Add_Draw_Points(GV.Foot_Traje_Target_X[GV.LEFT_FRONT_FOOT_ID_NUM], GV.Foot_Traje_Target_Y[GV.LEFT_FRONT_FOOT_ID_NUM], 0, 0, 0)
    Add_Draw_Points(GV.Foot_Traje_Target_X[GV.RIGHT_FRONT_FOOT_ID_NUM], GV.Foot_Traje_Target_Y[GV.RIGHT_FRONT_FOOT_ID_NUM], 0, 0, 0)
    #show me Head and neck positin
    Add_Draw_Points(GV.Shoulder_Position_X, GV.Shoulder_Position_Y, GV.Head_Pos_X, GV.Head_Pos_Y, 2)
    Add_Draw_Points(GV.Head_Pos_X, GV.Head_Pos_Y, 0, 0, 2)
    #=======================================================
    #Draw foot trajectory
    #for i in range(1, GV.Total_Trajectory_Dots, 1):
      #Add_Draw_Points(GV.Traj_Calc_X[i], GV.Traj_Calc_Y[i], 0, 0, 2)
    #ENDEX================
    #========================================

    Add_Draw_Points(GV.Center_Front_X, GV.Ground_Level_Y, 0, 0, 2)
    #show rear mid point
    Add_Draw_Points(GV.Center_Rear_X, GV.Ground_Level_Y, 0, 0, 2)
    #show body mid point between front and rear feet combined
    Add_Draw_Points(GV.Center_BODY_Feet_X, GV.Ground_Level_Y, 0, 0, 2)
  #----------------------------------------------------------------









  #show ground level
  #line(Draw_Mat[2], Point(0, GV.Ground_Level_Y), Point(GV.TempWidth - 1, GV.Ground_Level_Y), Scalar(100, 128, 255), 2)#bgr, 2)#bgr
  #line(Draw_Mat[3], Point(0, GV.Ground_Level_Y), Point(GV.TempWidth - 1, GV.Ground_Level_Y), Scalar(100, 128, 255), 2)#bgr, 2)#bgr






  GV.recenter_X[1] = GV.Shoulder_Top_View_X#top view center x
  GV.recenter_X[2] = GV.Uper_Body_Front_Side_Turn_Mover#front view center x(use to be front view stuff)
  GV.recenter_X[3] = GV.Body_Center_X#Side view center x
  GV.recenter_X[4] = GV.Uper_Body_Front_Side_Turn_Mover#front view center x

  d = GV.Select_View_To_Draw_NUM
  if d == 1 or d == 3 or d == 4:
    for i in range(1, GV.Num_Point_To_Draw, 1):
      if GV.DrawMatrix_NUM[i] == GV.Select_View_To_Draw_NUM:#d:
        #use defaul green to draw joints
        color = (0, 255, 0)#rgb
                                                          #select circle preset to draw joints
        if GV.Default_Color_Select[i] == 1:
           color = (255, 100, 100)#rgb
        if GV.Default_Color_Select[i] == 2:
           color = (0, 100, 255)#rgb
        if GV.Default_Color_Select[i] == 3:
           color = (68, 180, 255)#rgb (ground color

        #if the farthest point has moved out of screen then bring all points bac a bit
        GV.X_ReAjust_1 = (int) (GV.screen_Center + ((GV.recenter_X[d] - GV.Drawer_X[i]) * -1))
        #circle(GV.Draw_Mat[DrawMatrix_NUM[i]], Point(GV.X_ReAjust_1, GV.Drawer_Y[i]), 4, color, -1, 8, 0)
        pygame.draw.circle(screen, color, [GV.X_ReAjust_1, (int) (GV.Drawer_Y[i])], 4)
        #pygame.draw.circle(screen, color, [60, 250], 40)

        if GV.This_is_a_Line[i] == True:
          GV.X_ReAjust_2 = GV.screen_Center + ((GV.recenter_X[d] - GV.Drawer_X[i - 1]) * -1)
          #line(GV.Draw_Mat[GV.DrawMatrix_NUM[i]], Point(GV.X_ReAjust_2, GV.Drawer_Y[i - 1]), Point(GV.X_ReAjust_1, GV.Drawer_Y[i]), Scalar(255, 128, 0), 2)#bgr, 2)#bgr
          pygame.draw.line(screen, color, [(int) (GV.X_ReAjust_2), (int) (GV.Drawer_Y[i - 1])], [(int) (GV.X_ReAjust_1), (int) (GV.Drawer_Y[i])], 2)
        #ENDEX================
       #ENDEX================
    #ENDEX================
  else:
    #to just draw stuff without moving it to screen coordinates view (this stuff is already in screen cordinates)
    for i in range(1, GV.Num_Point_To_Draw, 1):
      if GV.DrawMatrix_NUM[i] == GV.Select_View_To_Draw_NUM:#d:
        #use defaul green to draw joints
        color = (0, 255, 0)#rgb
                                                          #select circle preset to draw joints
        if GV.Default_Color_Select[i] == 1:
           color = (255, 100, 100)#rgb
        if GV.Default_Color_Select[i] == 2:
           color = (0, 100, 255)#rgb
        if GV.Default_Color_Select[i] == 3:
           color = (68, 180, 255)#rgb (ground color


        #circle(GV.Draw_Mat[DrawMatrix_NUM[i]], Point(GV.X_ReAjust_1, GV.Drawer_Y[i]), 4, color, -1, 8, 0)
        pygame.draw.circle(screen, color, [(int) (GV.Drawer_X[i]), (int) (GV.Drawer_Y[i])], 4)
        #pygame.draw.circle(screen, color, [60, 250], 40)

        if GV.This_is_a_Line[i] == True:
          #line(GV.Draw_Mat[GV.DrawMatrix_NUM[i]], Point(GV.X_ReAjust_2, GV.Drawer_Y[i - 1]), Point(GV.X_ReAjust_1, GV.Drawer_Y[i]), Scalar(255, 128, 0), 2)#bgr, 2)#bgr
          pygame.draw.line(screen, color, [(int) (GV.Drawer_X[i - 1]), (int) (GV.Drawer_Y[i - 1])], [(int) (GV.Drawer_X[i]), (int) (GV.Drawer_Y[i])], 2)
        #ENDEX================
       #ENDEX================
    #ENDEX================
#ENDEX================
#========================================================================================================









 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#use defualt the font (None)---------------------------------------
zorqueFont = pygame.font.Font(None, 30)
textSurface = zorqueFont.render("Score: 0", True, (255, 255, 255))
Activity_Name_Sfc = zorqueFont.render("Act: <>", True, (255, 255, 255))
#-----------------------------------------------------------------



#done = False # False / True
#while not done:


# Throttling the FPS
clock = pygame.time.Clock()


#set up USB serial comunication with arduino
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#clear out serial port data
#ser.flush()
#---------------------




#while True:
done = False # False / True
while not done:


  # Listen for events from the OS
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
       done = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
           done = True
  #------------------------------




  #$$$$$$$colect sensor data from USB arduino$$$$$$$$$$$$$$$
  #if ser.in_waiting > 0:
  #  GV.Line_str_IN = ser.readline().decode('utf-8').rstrip()
  #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


  #limit frame rate to 40 frame persecond for smoothening movement
  clock.tick(40)#30

  GV.Num_Point_To_Draw = 0

  #do dog living functions
  ROBOT_AI_CONTROL_FUNC()
  #time.sleep(0.0001)#0.02, 0.01
  GE.Do_IK_And_Generate_Joint_Angles()
  # Clear the screen and set the screen background
  screen.fill(BLACK)
  Draw_The_Stuff(3)#3=side view 2=top view ref 4=front view for turning
  #check temperature and turn cpu fan on or of
  #GE.Turn_Fan_On_OF()
  #------------------------------------------------
  #==============================================================================================

    

  #display fps
  fps_display = zorqueFont.render("FPS: " + str(int(clock.get_fps())), True, (255, 255, 255),(80, 80, 80))
  #fps_display = zorqueFont.render("foot: " + str(int(GV.SensorS_Values[GV.Left_Front_Sensor_VAL])), True, (255, 255, 255),(80, 80, 80))
  screen.blit(fps_display, (0, 0))
  #---------------------------------------------------------------------------------------------------------


  #show me foot movement steps------------------------------------------------------------
  textSurface = zorqueFont.render("step: " + str(int(GV.Move_Steps)), True, (255, 255, 255),(80, 80, 80))#Foot_Move_Steps
  screen.blit(textSurface, (0, 25))
  #-------------------------------------------------------------------------------------------


  #show current activity name------------------------------------------------------------
  Activity_Name_Sfc = zorqueFont.render("Act: " + GV.New_Act_Name, True, (255, 255, 255),(80, 80, 80))#Foot_Move_Steps
  screen.blit(Activity_Name_Sfc, (0, 50))
  #-------------------------------------------------------------------------------------------
  
  
  #pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
  # Go ahead and update the screen with what we've drawn.
  # This MUST happen after all the other drawing commands.
  pygame.display.flip()
#==========================================================



# Be IDLE friendly
#pygame.font.quit()
pygame.quit()


