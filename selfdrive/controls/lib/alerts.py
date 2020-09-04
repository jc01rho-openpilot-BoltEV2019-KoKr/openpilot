from cereal import car, log

# Priority
class Priority:
  LOWEST = 0
  LOWER = 1
  LOW = 2
  MID = 3
  HIGH = 4
  HIGHEST = 5

AlertSize = log.ControlsState.AlertSize
AlertStatus = log.ControlsState.AlertStatus
AudibleAlert = car.CarControl.HUDControl.AudibleAlert
VisualAlert = car.CarControl.HUDControl.VisualAlert

class Alert():
  def __init__(self,
               alert_type,
               alert_text_1,
               alert_text_2,
               alert_status,
               alert_size,
               alert_priority,
               visual_alert,
               audible_alert,
               duration_sound,
               duration_hud_alert,
               duration_text,
               alert_rate=0.):

    self.alert_type = alert_type
    self.alert_text_1 = alert_text_1
    self.alert_text_2 = alert_text_2
    self.alert_status = alert_status
    self.alert_size = alert_size
    self.alert_priority = alert_priority
    self.visual_alert = visual_alert
    self.audible_alert = audible_alert

    self.duration_sound = duration_sound
    self.duration_hud_alert = duration_hud_alert
    self.duration_text = duration_text

    self.start_time = 0.
    self.alert_rate = alert_rate

    # typecheck that enums are valid on startup
    tst = car.CarControl.new_message()
    tst.hudControl.visualAlert = self.visual_alert

  def __str__(self):
    return self.alert_text_1 + "/" + self.alert_text_2 + " " + str(self.alert_priority) + "  " + str(
      self.visual_alert) + " " + str(self.audible_alert)

  def __gt__(self, alert2):
    return self.alert_priority > alert2.alert_priority


ALERTS = [
  # Miscellaneous alerts
  Alert(
      "enable",
      "",
      "",
      AlertStatus.normal, AlertSize.none,
      #Priority.MID, VisualAlert.none, AudibleAlert.chimeEngage, .2, 0., 0.),
      Priority.MID, VisualAlert.none, AudibleAlert.chimeEngage, 2., 0., 0.),

  Alert(
      "disable",
      "",
      "",
      AlertStatus.normal, AlertSize.none,
      #Priority.MID, VisualAlert.none, AudibleAlert.chimeDisengage, .2, 0., 0.),
      Priority.MID, VisualAlert.none, AudibleAlert.chimeDisengage, 2., 0., 0.),

  Alert(
      "fcw",
      "브레이크!",  #"BRAKE!",
      "충돌 위험!",   #"Risk of Collision",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.fcw, AudibleAlert.chimeWarningRepeat, 1., 2., 2.),

  Alert(
      "fcwStock",
      "브레이크!",  #"BRAKE!",
      "충돌 위험!",   #"Risk of Collision",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.fcw, AudibleAlert.none, 1., 2., 2.),  # no EON chime for stock FCW

  Alert(
      "steerSaturated",
      "핸들을 잡아주세요",     #"TAKE CONTROL",
      "조향 한계를 초과함!",  #"Turn Exceeds Steering Limit",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 1., 2., 3.),

  Alert(
      "steerTempUnavailable",
      "핸들을 잡아주세요",     #"TAKE CONTROL",
      "일시적으로 조종 불가!",    #"Steering Temporarily Unavailable",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimeWarning1, .4, 2., 3.),

  Alert(
      "steerTempUnavailableMute",
      "핸들을 잡아주세요",     #"TAKE CONTROL",
      "일시적으로 조종 불가!",    #"Steering Temporarily Unavailable",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .2, .2, .2),

  Alert(
      "manualSteeringRequired",
      "핸들을 잡아주세요: 차선유지기능 꺼짐!",  #"STEERING REQUIRED: Lane Keeping OFF",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .0, .1, .1, alert_rate=0.25),

  Alert(
      "manualSteeringRequiredBlinkersOn",
      "핸들을 잡아주세요: 방향지시등 켜짐!", #"STEERING REQUIRED: Blinkers ON",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .0, .1, .1, alert_rate=0.25),

  Alert(
      "preDriverDistracted",
      "도로를 주시하세요 : 사용자 도로주시 불안!", #"KEEP EYES ON ROAD: Driver Distracted",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "promptDriverDistracted",
      "전방 주시 유지",   #"KEEP EYES ON ROAD",
      "사용자 도로주시 불안!",  #"Driver Appears Distracted",
      AlertStatus.userPrompt, AlertSize.mid,
      #Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, .1, .1),
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeRoadWarning, 3., .1, .1),

  Alert(
      "driverDistracted",
      "바로 연결 해제",   #"DISENGAGE IMMEDIATELY",
      "사용자 도로주시 불안!",  #"Driver Was Distracted",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "preDriverUnresponsive",
      "핸들을 잡아주세요 : 얼굴 인식 불가!",    #"TOUCH STEERING WHEEL: No Face Detected",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "promptDriverUnresponsive",
      "핸들을 잡아주세요", #"TOUCH STEERING WHEEL",
      "사용자 응답하지않음!",  #"Driver Is Unresponsive",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, .1, .1),

  Alert(
      "driverUnresponsive",
      "조향제어가 강제로 해제됩니다",   #"DISENGAGE IMMEDIATELY",
      "사용자 응답하지않음!",  #"Driver Was Unresponsive",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "driverMonitorLowAcc",
      "운전자 모니터링 확인", #"CHECK DRIVER FACE VISIBILITY",
      "운전자 모니터링이 비정상입니다!",    #"Driver Monitor Model Output Uncertain",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .4, 0., 1.),

  Alert(
      "geofence",
      "오픈파일럿을 해제하세요",     #"DISENGAGEMENT REQUIRED",
      "지오펜스 영역이 아닙니다!",  #"Not in Geofenced Area",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "startup",
      "오픈파일럿 사용준비 완료",  #"Be ready to take over at any time",
      "항상 핸들을 잡고 도로를 주시하세요!",    #"Always keep hands on wheel and eyes on road",
      AlertStatus.normal, AlertSize.mid,
      #Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),
      Priority.LOWER, VisualAlert.none, AudibleAlert.chimeReady, 4., 0., 5.),

  Alert(
      "startupMaster",
      "경고: 테스트 되지않은 브랜치",    #"WARNING: This branch is not tested",
      "항상 핸들을 잡고 도로를 주시하세요!",    #"Always keep hands on wheel and eyes on road",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "startupNoControl",
      "대시캠 모드", #"Dashcam mode",
      "항상 핸들을 잡고 도로를 주시하세요!",    #"Always keep hands on wheel and eyes on road",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "startupNoCar",
      "대시캠 모드 : 호환 되지않는 차량", #"Dashcam mode for unsupported car",
      "항상 핸들을 잡고 도로를 주시하세요!",    #"Always keep hands on wheel and eyes on road",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "ethicalDilemma",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "인정기준 탐지 딜레마",    #"Ethical Dilemma Detected",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 3.),

  Alert(
      "steerTempUnavailableNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "핸들조향 일시적으로 사용불가",    #"Steering Temporarily Unavailable",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "manualRestart",
      "핸들을 잡아주세요",     #"TAKE CONTROL",
      "수동으로 재활성화 하세요!",   #"Resume Driving Manually",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "resumeRequired",
      "멈춤", #"STOPPED",
      "이동 하려면 계속 누르세요!", #"Press Resume to Move",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "belowSteerSpeed",
      "핸들을 잡아주세요",     #"TAKE CONTROL",
      "사용 할수없는 자동조향 속도",  #"Steer Unavailable Below ",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.none, 0., 0.4, .3),

  Alert(
      "debugAlert",
      "디버그 경고", #"DEBUG ALERT",
      "",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .1, .1, .1),
  Alert(
      "preLaneChangeLeft",
      "좌측차선으로 변경하기 위해 조향시작",  #"Steer Left to Start Lane Change",
      "좌측차선의 차량을 확인하세요!",    #"Monitor Other Vehicles",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "preLaneChangeRight",
      "우측차선으로 변경하기 위해 조향시작",  #"Steer Right to Start Lane Change",
      "우측차선의 차량을 확인하세요!",    #"Monitor Other Vehicles",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "laneChange",
      "차선 변경",  #"Changing Lane",
      "측후방 차량을 확인하세요!",  #"Monitor Other Vehicles",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1),

  Alert(
      "posenetInvalid",
      "핸들을 잡아주세요",     #"TAKE CONTROL",
      "차선인식 상태가 좋지않으니 주의운전하세요!",  #"Vision Model Output Uncertain",
      AlertStatus.userPrompt, AlertSize.mid,
      #Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimeWarning1, .4, 2., 3.),
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimeViewUncertain, 3., 2., 3.),

  # Non-entry only alerts
  Alert(
      "wrongCarModeNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "메인 스위치 꺼짐",  #"Main Switch Off",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "dataNeededNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "캘리브레이션에 필요한 데이터가 없음, 주행후 재시도하세요!",   #"Calibration Needs Data. Upload Drive, Try Again",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "outOfSpaceNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "저장공간 부족",    #"Out of Storage Space",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "pedalPressedNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "페달 눌림감지",   #"Pedal Pressed During Attempt",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, "brakePressed", AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "speedTooLowNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "차량 속도가 너무 느립니다!", #"Speed Too Low",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "brakeHoldNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "브레이크 감지됨",   #"Brake Hold Active",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "parkBrakeNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "주차 브레이크를 해제하세요!", #"Park Brake Engaged",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "lowSpeedLockoutNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "크루즈 에러 : 차량을 다시 시작하세요!",  #"Cruise Fault: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "lowBatteryNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "배터리 부족", #"Low Battery",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "sensorDataInvalidNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "EON 센서 데이타 부족",  #"No Data from Device Sensors",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "soundsUnavailableNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "스피커가 없습니다!",  #"Speaker not found",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "tooDistractedNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "작동 방해수준이 너무높음",    #"Distraction Level Too High",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  # Cancellation alerts causing soft disabling
  Alert(
      "overheat",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "시스템 과열", #"System Overheated",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),

  Alert(
      "wrongGear",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "기어가 드라이브[D] 상태가 아닙니다", #"Gear not D",
      AlertStatus.critical, AlertSize.full,
      #Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeGearDrive, 3., 2., 2.),

  Alert(
      "calibrationInvalid",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "캘리브레이션 에러 : EON 위치변경 후 재시도하세요!",  #"Calibration Invalid: Reposition Device and Recalibrate",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),

  Alert(
      "calibrationIncomplete",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "캘리브레이션 진행중", #"Calibration in Progress",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),

  Alert(
      "doorOpen",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "도어 열림",  #"Door Open",
      AlertStatus.critical, AlertSize.full,
      #Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeDoorOpen, 3., 2., 2.),

  Alert(
      "seatbeltNotLatched",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "안전벨트를 착용해주세요!",   #"Seatbelt Unlatched",
      AlertStatus.critical, AlertSize.full,
      #Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeSeatBelt, 2., 2., 2.),

  Alert(
      "espDisabled",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "ESP 꺼짐", #"ESP Off",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),

  Alert(
      "lowBattery",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "배터리 부족", #"Low Battery",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),

  Alert(
      "commIssue",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "프로세스간 통신문제", #"Communication Issue between Processes",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),

  Alert(
      "radarCommIssue",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "Radar Communication Issue",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),

  Alert(
      "radarCanError",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "Radar 에러 : 차량을 다시 시작하세요!",  #"Radar Error: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),

  Alert(
      "radarFault",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "Radar 에러 : 차량을 다시 시작하세요!",  #"Radar Error: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),


  Alert(
      "lowMemory",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "메모리 부족 : EON을 재부팅하세요!",   #"Low Memory: Reboot Your Device",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, 2., 2.),

  # Cancellation alerts causing immediate disabling
  Alert(
      "controlsFailed",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "컨트롤 오류", #"Controls Failed",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),

  Alert(
      "controlsMismatch",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "컨트롤 불일치",    #"Controls Mismatch",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),

  Alert(
      "canError",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "CAN 에러 : 연결상태를 확인하세요!",   #"CAN Error: Check Connections",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),

  Alert(
      "steerUnavailable",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "LKAS 에러 : 차량을 다시시작하세요!",  #"LKAS Fault: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),

  Alert(
      "brakeUnavailable",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "크루즈 에러 : 차량을 다시시작하세요!",   #"Cruise Fault: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),

  Alert(
      "gasUnavailable",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "Gas 에러 : 차량을 다시시작하세요!",   #"Gas Fault: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),

  Alert(
      "reverseGear",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "후진기어[R] 상태",  #"Reverse Gear",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),

  Alert(
      "cruiseDisabled",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "크루즈 꺼짐", #"Cruise Is Off",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),

  Alert(
      "plannerError",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "Planner Solution 에러",    #"Planner Solution Error",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),

  Alert(
      "relayMalfunction",
      "핸들을 즉시 잡아주세요",   #"TAKE CONTROL IMMEDIATELY",
      "하네스 오작동",    #"Harness Malfunction",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 2.2, 3., 4.),


  # not loud cancellations (user is in control)
  Alert(
      "noTarget",
      "오픈파일럿 취소됨",  #"openpilot Canceled",
      "근접한 차량이 없습니다!",   #"No close lead car",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "speedTooLow",
      "오픈파일럿 취소됨",  #"openpilot Canceled",
      "속도가 너무낮음",   #"Speed too low",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "speedTooHigh",
      "속도가 너무 높음",  #"Speed Too High",
      "작동을 재개하려면 속도를 줄여주세요!",    #"Slow down to resume operation",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  # Cancellation alerts causing non-entry
  Alert(
      "overheatNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "시스템 과열", #"System overheated",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "wrongGearNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "기어가 드라이브[D] 상태가 아닙니다", #"Gear not D",
      AlertStatus.normal, AlertSize.mid,
      #Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeGearDrive, 3., 2., 3.),

  Alert(
      "calibrationInvalidNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "캘리브레이션 오류: EON을 재 장착하고 다시 시작하세요",  #"Calibration Invalid: Reposition Device & Recalibrate",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "calibrationIncompleteNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "캘리브레이션 진행 중...",  #"Calibration in Progress",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "doorOpenNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "도어 열림",  #"Door open",
      AlertStatus.normal, AlertSize.mid,
      #Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeDoorOpen, 3., 2., 3.),

  Alert(
      "seatbeltNotLatchedNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "안전벨트를 착용해주세요!",   #"Seatbelt unlatched",
      AlertStatus.normal, AlertSize.mid,
      #Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeSeatBelt, 2., 2., 3.),

  Alert(
      "espDisabledNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "ESP 꺼짐", #"ESP Off",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "geofenceNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "지오펜스 영역이 아닙니다!",  #"Not in Geofenced Area",
      AlertStatus.normal, AlertSize.mid,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "radarCanErrorNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "Radar 에러 : 차량을 다시 시작하세요!",  #"Radar Error: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "radarFaultNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "Radar 에러 : 차량을 다시 시작하세요!",  #"Radar Error: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "posenetInvalidNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "차선인식 상태가 좋지않으니 주의운전하세요!",  #"Vision Model Output Uncertain",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "controlsFailedNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "컨트롤 오류", #"Controls Failed",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "canErrorNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "CAN 에러 : 연결상태를 확인하세요!",   #"CAN Error: Check Connections",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "steerUnavailableNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "LKAS 에러 : 차량을 다시 시작하세요!", #"LKAS Fault: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "brakeUnavailableNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "크루즈 에러 : 차량을 다시 시작하세요!",  #"Cruise Fault: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "gasUnavailableNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "Gas 에러 : 차량을 다시 시작하세요!",  #"Gas Error: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "reverseGearNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "후진기어[R] 상태", #"Reverse Gear",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "cruiseDisabledNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "크루즈 오프 상태",  #"Cruise is Off",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "noTargetNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "근접한 차량이 없습니다!",   #"No Close Lead Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "plannerErrorNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "Planner Solution 에러",    #"Planner Solution Error",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "commIssueNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "프로세스간 통신문제", #"Communication Issue between Processes",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "radarCommIssueNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "Radar 통신문제",   #"Radar Communication Issue",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "internetConnectivityNeededNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "인터넷을 연결하세요!",    #"Please Connect to Internet",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "lowMemoryNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "메모리 부족: EON을 다시 시작하세요",   #"Low Memory: Reboot Your Device",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "speedTooHighNoEntry",
      "속도가 너무 높음",    #"Speed Too High",
      "속도를 줄여야 활성화됩니다!", #"Slow down to engage",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "relayMalfunctionNoEntry",
      "오픈파일럿 사용불가", #"openpilot Unavailable",
      "하네스 오작동",    #"Harness Malfunction",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  # permanent alerts
  Alert(
      "steerUnavailablePermanent",
      "LKAS 오류: 차량을 다시 시작하세요",    #"LKAS Fault: Restart the car to engage",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "brakeUnavailablePermanent",
      "크루즈 오류: 차량을 다시 시작하세요",    #"Cruise Fault: Restart the car to engage",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "lowSpeedLockoutPermanent",
      "크루즈 오류: 차량을 다시 시작하세요",    #"Cruise Fault: Restart the car to engage",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "calibrationIncompletePermanent",
      "캘리브레이션 진행중 : ",  #"Calibration in Progress: ",
      "정속 주행",  #"Drive Above ",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "invalidGiraffeToyotaPermanent",
      "지원되지 않는 지라프 설정",  #"Unsupported Giraffe Configuration",
      "comma.ai/tg 참조",  #"Visit comma.ai/tg",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "invalidLkasSettingPermanent",
      "차량 LKAS 버튼 상태확인",    #"Stock LKAS is turned on",
      "차량 LKAS 버튼 OFF후 활성화됩니다!", #"Turn off stock LKAS to engage",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "internetConnectivityNeededPermanent",
      "인터넷에 연결하세요",  #"Please connect to Internet",
      "활성화를 위해 업데이트를 확인해야 합니다",  #"An Update Check Is Required to Engage",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "communityFeatureDisallowedPermanent",
      "커뮤니티 기능 감지", #"Community Feature Detected",
      "개발자 설정에서 커뮤니티 기능 활성화", #"Enable Community Features in Developer Settings",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 0., 0., .2),  # LOW priority to overcome Cruise Error

  Alert(
      "sensorDataInvalidPermanent",
      "EON 센서 데이타 부족",  #"No Data from Device Sensors",
      "EON을 재부팅하세요!",    #"Reboot your Device",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "soundsUnavailablePermanent",
      "스피커가 없습니다",  #"Speaker not found",
      "EON을 재부팅하세요!",    #"Reboot your Device",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "lowMemoryPermanent",
      "메모리 매우 낮음",  #"RAM Critically Low",
      "EON을 재부팅하세요!",    #"Reboot your Device",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "carUnrecognizedPermanent",
      "대시캠 모드", #"Dashcam Mode",
      "차량인식 불가",    #"Car Unrecognized",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "relayMalfunctionPermanent",
      "하네스 오작동",    #"Harness Malfunction",
      "하드웨어를 점검하세요!",    #"Please Check Hardware",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWER, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "vehicleModelInvalid",
      "차량 매개변수 인식 실패",  #"Vehicle Parameter Identification Failed",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOWEST, VisualAlert.steerRequired, AudibleAlert.none, .0, .0, .1),

  Alert(
      "ldwPermanent",
      "핸들을 잡아주세요",     #"TAKE CONTROL",
      "차선이탈 감지됨",   #"Lane Departure Detected",
      AlertStatus.userPrompt, AlertSize.mid,
      #Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimePrompt, 1., 2., 3.),
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimeLaneDeparture, 4., 2., 3.),
]
