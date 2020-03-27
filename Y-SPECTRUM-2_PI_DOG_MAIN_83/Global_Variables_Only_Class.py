#Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.
#>>> 
class Global_Variables_Only_Class:
  #function for alocating fixed memory to array so I can use them like in C++
  def INI_Array_With_Size(Array_IN, Array_Size):
    for i in range(Array_Size):
      Array_IN.append(0)#ini with zero
  #=======================================================


  #-------------------NEW FOR BODY MOVEMENT ACTIVITIES-VARIABLES-----------------------------------------
  Uper_Arm_Angle_Help_X = 0
  Uper_Arm_Angle_Help_Y = 0

  #create space for variable
  Uper_Arm_Angle_HelpARR_X = []
  Uper_Arm_Angle_HelpARR_Y = []
  INI_Array_With_Size(Uper_Arm_Angle_HelpARR_X, 7)
  INI_Array_With_Size(Uper_Arm_Angle_HelpARR_Y, 7)


  Foot_Current_Pos_X = []
  Foot_Current_Pos_Y = []
  INI_Array_With_Size(Foot_Current_Pos_X, 7)
  INI_Array_With_Size(Foot_Current_Pos_Y, 7)


  Foot_GROUND_Pos_Y = []
  INI_Array_With_Size(Foot_GROUND_Pos_Y, 7)



  #--
  Rear_upperArmLength = 0
  Rear_forearmLength = 0
  Rear_footLength = 0

  Front_upperArmLength = 0
  Front_forearmLength = 0
  Front_footLength = 0
  #==============================

  Head_Pos_X = 0
  Head_Pos_Y = 0

  All_Leg_Angles = []
  INI_Array_With_Size(All_Leg_Angles, 20)

  #like if angles 0 to 10 = 10
  Group_Angles_180 = []
  INI_Array_With_Size(Group_Angles_180, 200)
  X_Head_Balance_Incr = 0
  Foot_Target_Dist = 0

  #
  Left_Rear_Uper_Arm_X_Angle = 0
  Left_Rear_Fore_Arm_Angle = 0
  #
  Right_Rear_Uper_Arm_X_Angle = 0
  Right_Rear_Fore_Arm_Angle = 0
  #
  Left_Front_Uper_Arm_X_Angle = 0
  Left_Front_Uper_Arm_Z_Angle = 0
  Left_Front_Fore_Arm_Angle = 0
  #
  Right_Front_Uper_Arm_X_Angle = 0
  Right_Front_Uper_Arm_Z_Angle = 0
  Right_Front_Fore_Arm_Angle = 0

  Head_X_Rotation_Angle = 0
  Head_Y_Rotation_Angle = 0

  Foot_Anim_Position = []
  INI_Array_With_Size(Foot_Anim_Position, 7)


  The_Foot_Pos_X = 0
  The_Foot_Pos_Y = 0

  Foot_Speed_INC = []
  INI_Array_With_Size(Foot_Speed_INC, 7)

  LEFT_REAR_FOOT_ID_NUM = 1
  LEFT_FRONT_FOOT_ID_NUM = 2
  RIGHT_REAR_FOOT_ID_NUM = 3
  RIGHT_FRONT_FOOT_ID_NUM = 4
  LEFT_FRONT_FVIEW_FOOT_ID_NUM = 5#brought back
  RIGHT_FRONT_FVIEW_FOOT_ID_NUM = 6#brought back

  
  Right_Front_MAX_Sensor_VAL = 1
  Left_Front_Sensor_VAL = 2
  Left_Front_MAX_Sensor_VAL = 3
  Right_Front_Sensor_VAL = 4
  Temperature_Sensor_VAL = 5
  Nose_Lidar_Sensor_VAL = 6
  X_Accel_Tilt_Sensor_VAL = 7
  Y_Accel_Tilt_Sensor_VAL = 8
  Z_Accel_Tilt_Sensor_VAL = 9
  X_Magneto_Sensor_VAL = 10
  Y_Magneto_Sensor_VAL = 11
  Z_Magneto_Sensor_VAL = 12
  X_Gyro_Sensor_VAL = 13
  Y_Gyro_Sensor_VAL = 14
  Z_Gyro_Sensor_VAL = 15

  Head_Top_Proximity_Sensor_VAL = 16
  Head_Top_Gesture_Sensor_VAL = 17
  Head_Top_Light_Sensor_VAL = 18


  Foot_Trajectory_PosX = 0
  Foot_Trajectory_PosY = 0


  Uper_Arm_X_Angle_OUT = 0
  Fore_Arm_Angle_OUT = 0


  Ang = 0
  Dstc = 0

  Uper_Body_Front_Back_Mover = 0
  Uper_Body_Front_Side_Turn_Mover = 0
  Body_Height = 0
  Body_Height_Total = 0
  Hip_Position_X = 0
  Hip_Position_Y = 0
  Shoulder_Position_X = 0
  Shoulder_Position_Y = 0#
  Ground_Level_Y = 0


  Traj_Calc_X = []
  Traj_Calc_Y = []
  INI_Array_With_Size(Traj_Calc_X, 150)
  INI_Array_With_Size(Traj_Calc_Y, 150)


  Foot_Grounded = []#bool nor more, using ints now
  INI_Array_With_Size(Foot_Grounded, 7)


  Move_Steps = 0
  Total_Trajectory_Dots = 0


  Foot_Traje_Target_X = []
  Foot_Traje_Target_Y = []
  INI_Array_With_Size(Foot_Traje_Target_X, 7)
  INI_Array_With_Size(Foot_Traje_Target_Y, 7)


  Inital_Front_Foot_SideV_Position_X = 0
  Inital_Rear_Foot_SideV_Position_X = 0

  Inital_Left_Foot_FrontV_Position_X = 0
  Inital_Right_Foot_FrontV_Position_X = 0


  #place Left and right shoulder main joints
  Left_Front_Joint_Front_View_X = 0
  Left_Front_Joint_Front_View_Y = 0
  Right_Front_Joint_Front_View_X = 0
  Right_Front_Joint_Front_View_Y = 0


  Body_Center_X = 0
  Body_Center_Y = 0
  Body_X_Tilt_Angle = 0
  Body_Torso_Radius = 0
  Shoulder_X_Tilt_Angle = 0
  Hip_X_Tilt_Angle = 0



  Number_Of_Times_Act_Done = 0
  Ground_Presure_Sensivity = 1


  Leg_Speeds = 0
  Leg_INC_Speed = 0
  Leg_Deccelaration_INC_Speed = 0

  Wanted_Z_Tilt = 0
  Z_Tilt_SPeed = 0
  Z_TILT_Reset_Speed = 0
  Z_Tilt_Mover_Value = 0


  #Left_Front_Foot_Sensor_VAL = 1
  #Right_Front_Foot_Sensor_VAL = 2
  #Left_Rear_Foot_Sensor_VAL = 3
  #Right_Rear_Foot_Sensor_VAL = 4


  
  SensorS_Values = []
  INI_Array_With_Size(SensorS_Values, 20)


  Sonic_Sensor_Pulse_Start_Time = []
  INI_Array_With_Size(Sonic_Sensor_Pulse_Start_Time, 12)
  Sonic_Sensor_Triggered = []
  INI_Array_With_Size(Sonic_Sensor_Triggered, 12)
  

  Main_Joint_SideV_X = []
  Main_Joint_SideV_Y = []
  INI_Array_With_Size(Main_Joint_SideV_X, 7)
  INI_Array_With_Size(Main_Joint_SideV_Y, 7)

  Main_Joint_SideVADJUST_Y = []
  INI_Array_With_Size(Main_Joint_SideVADJUST_Y, 7)


  Center_BODY_Feet_X = 0
  Center_BODY_Feet_Side_X = 0#for turning left right
  Body_To_Center_Mass_Speed = 0
  Body_To_Center_Mass_Speed_Front = 0


  Y_Body_Rotate = 0#default to face up of screen 0 degrees
  Shoulder_Top_View_X = 0
  Shoulder_Top_View_Y = 0
  Shoulder_TopV_Raduis = 0
  Neck_Top_Pos_X = 0
  Neck_Top_Pos_Y = 0
  Head_Top_Pos_X = 0
  Head_Top_Pos_Y = 0
  Left_Front_Main_Joint_TopV_X = 0
  Left_Front_Main_Joint_TopV_Y = 0
  Right_Front_Main_Joint_X = 0
  Right_Front_Main_Joint_Y = 0
  Head_Lenght = 0
  Neck_Length = 0

  Y_Head_Rotate_Speed = 0
  X_Head_Rotate_Speed = 0


  Center_Front_X = 0
  Center_Rear_X = 0
  TempWidth = 0
  TempHeight = 0
  screen_Center = 0


  #----ROBOT AI Activities
  IDLE_STAND_01 = 0
  WALK_TYPE_01 = 0
  WALK_TO_IDLE = 0


  Robot_Initial_Switched_ON = 0
  Activity_Select = 0
  Activity_Start_Steps = 0#will be reset before each activity is started
  Number_Of_Times_To_Do_Act = 0
  Current_Situation_We_Were_Handling = 0

  Current_Activity_Name = ""
  New_Act_Name = ""#The name of the newly selected activity
  Activity_Names_Collection = []
  INI_Array_With_Size(Activity_Names_Collection, 20)

  Total_Possible_Activities = 0

  TestVarME = 0
  #==
  #----------------------END MOVEMENT VARIABLES--------------------------------------------------------------------------------------------------




  #----------servo stuff---------
  MAX_NUMBER_SERVOS = 0
  #for servo smoothening
  ServoAnglePos = []
  INI_Array_With_Size(ServoAnglePos, 25)
  ServoAnglePosOLD = []
  INI_Array_With_Size(ServoAnglePosOLD, 25)
  SmootherInc = []
  INI_Array_With_Size(SmootherInc, 25)
  #------------------------------------


  #for drawing points and lines================================================================================
  X_ReAjust_1 = 0
  Y_ReAjust_1 = 0
  X_ReAjust_2 = 0
  Y_ReAjust_2 = 0
  Num_Point_To_Draw = 0
  Drawer_X = []
  INI_Array_With_Size(Drawer_X, 1000)
  Drawer_Y = []
  INI_Array_With_Size(Drawer_Y, 1000)
  This_is_a_Line = []
  INI_Array_With_Size(This_is_a_Line, 1000)
  DrawMatrix_NUM = []
  INI_Array_With_Size(DrawMatrix_NUM, 1000)
  Default_Color_Select = []
  INI_Array_With_Size(Default_Color_Select, 1000)
  DrawMatrix_NUM_IN = 0

  recenter_X = []
  INI_Array_With_Size(recenter_X, 5)

  Z_Tilt_Speed_INC = 0
  Center_BODY_Feet_X_Offset = 0

  Z_Tilt_INC_Accel_Deccel = 0

  Sholder_Rotate_Angle = 0
  Sholder_Rotate_Speed_INC = 0
  Sholder_Rotate_Accel_Deccel = 0

  
  All_Feet_Positions_ID = 0
  Front_Feet_Positions_ID = 0
  Rear_Feet_Positions_ID = 0

  Feet_Move_Sequence = []
  INI_Array_With_Size(Feet_Move_Sequence, 6)
  

  #to make top view representation of whole body including live movement parts positions and trangle weight shift sector represetation
  Shoulder_Top_REP_X = 0
  Shoulder_Top_REP_Y = 0
  Shoulder_Top_REP_Raduis = 0
  Hip_Top_REP_X = 0
  Hip_Top_REP_Y = 0
  Hip_Top_REP_Raduis = 0
  Neck_Top_REP_Pos_X = 0
  Neck_Top_REP_Pos_Y = 0
  Head_Top_REP_Pos_X = 0
  Head_Top_REP_Pos_Y = 0
  Left_Front_Main_Joint_Top_REP_X = 0
  Left_Front_Main_Joint_Top_REP_Y = 0
  Right_Front_Main_Joint_Top_REP_X = 0
  Right_Front_Main_Joint_Top_REP_Y = 0
  Left_Rear_Main_Joint_Top_REP_X = 0
  Left_Rear_Main_Joint_Top_REP_Y = 0
  Right_Rear_Main_Joint_Top_REP_X = 0
  Right_Rear_Main_Joint_Top_REP_Y = 0
  Head_Lenght_Top_REP = 0
  Neck_Length_Top_REP = 0
  #--
  Foot_Top_REP_X = []
  Foot_Top_REP_Y = []
  INI_Array_With_Size(Foot_Top_REP_X, 6)
  INI_Array_With_Size(Foot_Top_REP_Y, 6)
  #--
  Body_Center_Of_Mass_X = 0
  Body_Center_Of_Mass_Y = 0


  
  Balance_Triagle_X = []
  Balance_Triagle_Y = []
  INI_Array_With_Size(Balance_Triagle_X, 6)
  INI_Array_With_Size(Balance_Triagle_Y, 6)


  Balance_Triagle_CentrX = []
  Balance_Triagle_CentrY = []
  INI_Array_With_Size(Balance_Triagle_CentrX, 6)
  INI_Array_With_Size(Balance_Triagle_CentrY, 6)


  CentGrav_Triagle_CentrX = []
  CentGrav_Triagle_CentrY = []
  INI_Array_With_Size(CentGrav_Triagle_CentrX, 6)
  INI_Array_With_Size(CentGrav_Triagle_CentrY, 6)
  
  Balance_Triangle_Points_Num = 0
  Half_Point_Out_X = 0
  Half_Point_Out_Y = 0


  Move_Foot_Situation = 0
  Foot_Anim_Direction = 0

  Leg_Lift_Height = 0

  #Foot_Move_Steps = []
  #INI_Array_With_Size(Foot_Move_Steps, 6)

  Foot_Move_Steps = 0
  
  Over_Stretch_Height_Manager = 0
  Selected_Feet_Sequence = 0

  Wanted_ZZ_Tilt_AA = 0
  Is_A_Front_Foot = False
  Is_A_Rear_Foot = False


  #Z tilt oposite foot push lift settings
  Z_Tilt_Add_Amount = 0
  Z_Tilt_Add_Speed = 0
  Z_Tilt_Add_RESET_Speed = 0
  #=========================================

  Foot_Lifted_Off_Ground_Count = 0
  Real_World_Foot_Just_Hit_Ground = False

  Body_Center_Accel_Deccel_INC = 0

  Body_Set_Height_Offset = 0
  Body_Set_Height_Offset_Speed = 0
  Last_Completed_Body_Position_ID_NUM = 0
  Body_Is_Sitting = False
  Select_View_To_Draw_NUM = 0


  Center_Plus_FrontBackOffset = 0
  Calc_Body_To_Center_Mass_Dist_Done = False
  Body_To_CentMass_Advance = 0
  destDist = 0

  Body_To_CMass_Chop = []
  INI_Array_With_Size(Body_To_CMass_Chop, 105)

  Ztilt_Inc_Chop = []
  INI_Array_With_Size(Ztilt_Inc_Chop, 105)
  Ztilt_Calc_Dist_Done = False
  Ztilt_Advance = 0

    
  Environment_Scan_Steps = 0
  Number_Of_Times_EnvrSCAN_Done = 0
  Environment_Scan_Interval = 0
  Environment_Scan_Wait_Time = 0

  Lidar_Angle_Dist = []
  INI_Array_With_Size(Lidar_Angle_Dist, 181)

  Scan_Used_Angles_Count = 0
  Scan_Used_Angles = []
  INI_Array_With_Size(Scan_Used_Angles, 181)

  Scan_Dots_X = []
  INI_Array_With_Size(Scan_Dots_X, 181)
  Scan_Dots_Y = []
  INI_Array_With_Size(Scan_Dots_Y, 181)
  Scan_Feel_Array = []
  INI_Array_With_Size(Scan_Feel_Array, 181)
  Scan_Bumps = []
  INI_Array_With_Size(Scan_Bumps, 181)
  Scan_Bumps_Num = 0

  Clear_Path_Dots_Count = []
  INI_Array_With_Size(Clear_Path_Dots_Count, 4)
  Clear_Path_Seleted_Result = 0


  MID_Clear_Path_Dots_Count = []
  INI_Array_With_Size(MID_Clear_Path_Dots_Count, 4)

  MID_Clear_Path_Dots_Average = []
  INI_Array_With_Size(MID_Clear_Path_Dots_Average, 4)
  
  

  Fan_Cooling_INCrement = 0
  Fan_Cooling_Binary_ON_OF = 0
  Cooling_Fan_ON = False
  CPU_Temperature = 0

  #for playing sounds
  Number_Of_Sounds = 0 #starts from zero(cause uses array index zero)
  Sounds_All = []
  #define defualt sounds
  WAKE_UP_SOUND = 0
  SCAN_DONE_SOUND = 0
  BARK_SOUND = 0
  IDLE_SOUND = 0
  JUST_SAT_DOWN_SOUND = 0
  WAGG_TAIL_SOUND = 0
  OBJECT_DETECTED_WALKING_FORWARD = 0
  ACTION_SCROLL_SOUND = 0
  ACTION_SELECTED_SOUND = 0
  GESTURE_DETECTION_ENABLED = 0
  FEET_ARE_OF_THE_GROUND = 0

  AREA_EXPLORED_SOUND = 0
  PASSED_OBJECT_SOUND = 0
  BACKING_UP_SOUND = 0
  TURN_REPEAT_SOUND = 0

  SHUTDOWN_SOUND = 0
  

  General_Wait_Interval_INC = 0
  Lidar_Data_Colection_Rate_INC = 0
  Lidar_Skip_Frames = 0


  HEAD_X_Tilt_Angle_Select = 0

  Gqy = 0

  Head_X_UPDOWN_INC = 0
  Last_Scan_Position_Reached = False


  #create the low scan distances reff (values gotten from actual low scan)
  Low_Scan_Distances_REF = []
  INI_Array_With_Size(Low_Scan_Distances_REF, 181)
  
  Scan_Result_Output_NUM = 0
  Wagg_Tail_Amount = 0

  WALK_Reached_Good_Exit_Point = False
  Foot_Trajectory_Hiest_Point = 0

  Activity_Log = []
  Activities_Completed_NUM = 0

  Back_Front_Repeat_Check = 0

  Clearest_Turn_Direction = 0
  #used to keep moving forward even if there is an object (like a wall perpendicular) other wise will be stuck scaning an not moving
  Forward_Direction_Cleared_Twice = 0
  Forward_Walk_Interupted_Twice = 0
  Ignore_Close_Object = False
  Walk_Completed_Steps = 0
  Get_Oposite_MoveFoot_ID_NUM = 0

  POSition_Accel_X = 0
  POSition_Accel_Y = 0

  POSition_Accel_X_Average = 0
  POSition_Accel_Y_Average = 0
  Accel_Average_Count = 0

  RAW_Accel_X = 0
  RAW_Accel_Y = 0

  Max_Z_Tilt = 0
  Count_Good_Tilt_Values = 0
  Mid_Range_Scan_Clearest_Path = 0

  Low_Scan_Left_Right_both_Clear = False
  Do_Seek_Clear_Space_To_Explore = False
  Ignored_object_On_Side_Count = 0

  Clear_Space_To_Explore_Steps = 0
  LED_Pulse_Width_Val = 0

  Last_Environment_Scan_Type = 0

  Head_LED_Pulse_Count = 0

  Detect_Dead_End_Steps = 0
  Turn_Until_Forward_Clear = 0
  Completed_Forward_Walks_Count = 0
  Foot_To_Ground_Dist = 0
  Foot_Coming_Down_Tracker = 0

  Two_Bumps_In_A_Row = 0
  Default_Scan_Low_Object_Detected = False
  Head_Top_Proximity_Activated = False
  Low_Scan_Closest_Distance = 0



  Detect_Gestures = False
  Detected_Gesture_Value = 0
  Scroll_Through_Actions = 0
  Time_Gesture_INC = 0
  Time_Gesture_Seconds = 0

  Play_Feet_Off_Ground_Sound_Once = 0

  Enable_ShutDown = 0
  Clear_Turn_Path_Threshold = 10

  Driving_Head_Y_Rotate = False
  Count_To_Disble_Head_Y_Servo = 0

  Left_Edge_Blocked_Count = 0
  Right_Edge_Blocked_Count = 0

  Left_Edge_Closest_Distance = 0
  Right_Edge_Closest_Distance = 0

  Stoped_Turn_Object_Detected = 0



  Area_Exprore_Progress_Count = 0
  Went_Around_Obstacle = 0
  Enable_Detect_Dead_End = False

  Last_TURN_DIRECTION = 0
  Left_Right_Turn_Repeat_Count = 0
  Turn_Off_Head_Y_Once = False
  #---------------------------------------------------------------------------------------------------------------------
