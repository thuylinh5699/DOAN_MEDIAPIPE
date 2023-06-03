from dudoan import *
import time
import random
import cvzone
from mqtt_server import *

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


class PLAY_GAME_HAINGUOI:
    timer = 0
    stateResult = True
    startGame = False
    scores = [0, 0]  # [AI, Player]
    initialTime = 0
    dudoan = None
    roundnow=0
    def __init__(self) -> None:
        self.name = 'GAME PLAY'  


playgame_option_hainguoi = PLAY_GAME_HAINGUOI()

def play_game_hainguoi(total_round):
    print('TOTAL ROUND' , total_round)
    while True:
        imgBG = cv2.imread("assets/BG_2nguoi_sv.png")
        ret, img = cap.read()

        imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
        imgScaled = imgScaled[:, 80:480]
        if playgame_option_hainguoi.stateResult is False:
            playgame_option_hainguoi.timer = time.time() - playgame_option_hainguoi.initialTime
            cv2.putText(imgBG, str(int(playgame_option_hainguoi.timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            try:
                img,playgame_option_hainguoi.dudoan = nhandien(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                if playgame_option_hainguoi.timer > 3:
                    playgame_option_hainguoi.stateResult = True
                    playgame_option_hainguoi.timer = 0
                    if playgame_option_hainguoi.dudoan != None:
                        if playgame_option_hainguoi.dudoan == "ROCK":
                            luachon_server = 1
                        if playgame_option_hainguoi.dudoan == "PAPER":
                            luachon_server = 2
                        if playgame_option_hainguoi.dudoan == "SCISSORS":
                            luachon_server = 3
                        guidudoan_to_cli(str(luachon_server))
                        
                        
                        while mqtt_option.cli_duaradudoan == False:
                            playgame_option_hainguoi.timer = time.time() - playgame_option_hainguoi.initialTime
                            if playgame_option_hainguoi.timer > 30 or mqtt_option.dudoan_cli != None :
                                break
                        
                        
                        luachon_cli = mqtt_option.dudoan_cli
                        if luachon_cli == None :
                            luachon_cli = random.randint(1, 3)
                        imgAI = cv2.imread(f'assets/{luachon_cli}.png', cv2.IMREAD_UNCHANGED)
                        imgUSER = cv2.imread(f'assets/{luachon_server}.png', cv2.IMREAD_UNCHANGED)
                        if (luachon_server == 1 and luachon_cli == 3) or \
                                (luachon_server == 2 and luachon_cli == 1) or \
                                (luachon_server == 3 and luachon_cli == 2):
                            playgame_option_hainguoi.scores[1] += 1

                        # AI Wins
                        if (luachon_server == 3 and luachon_cli == 1) or \
                                (luachon_server == 1 and luachon_cli == 2) or \
                                (luachon_server == 2 and luachon_cli == 3):
                            playgame_option_hainguoi.scores[0] += 1
                        playgame_option_hainguoi.roundnow +=1
                        # print(playgame_option_hainguoi.roundnow)
                        mqtt_option.dudoan_cli = None
                cv2.putText(imgBG, playgame_option_hainguoi.dudoan, (500, 600), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4) 
                
            except Exception as e:
                pass
        
        if playgame_option_hainguoi.stateResult is False:
            imgBG[234:654, 795:1195] = imgScaled
        try:
            if playgame_option_hainguoi.stateResult:
                imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
                imgBG = cvzone.overlayPNG(imgBG, imgUSER, (850, 310))
        except:
            pass
        cv2.putText(imgBG, str(playgame_option_hainguoi.scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv2.putText(imgBG, str(playgame_option_hainguoi.scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        str_round = "ROUND " + str(playgame_option_hainguoi.roundnow)
        
        cv2.putText(imgBG, str_round, (500, 300), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4) 
        if playgame_option_hainguoi.roundnow >=  total_round:
            if playgame_option_hainguoi.scores[0] > playgame_option_hainguoi.scores[1] :
                whowin = "USER CLI WIN, PRESS S KEY TO RESTART GAME"
            elif playgame_option_hainguoi.scores[0] < playgame_option_hainguoi.scores[1] :
                whowin = "USER SV WIN, PRESS S KEY TO RESTART GAME"
            elif playgame_option_hainguoi.scores[0] == playgame_option_hainguoi.scores[1] :
                whowin = "NO WHO WIN, PRESS S KEY TO RESTART GAME"
            
            cv2.putText(imgBG,whowin, (100, 700), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4) 
        cv2.imshow("BG", imgBG)
        # cv2.imshow("Scaled", imgScaled)
        
        
        
            
            
        key = cv2.waitKey(1)
        if key == ord('s'):
            if mqtt_option.vaophong == True:
                playgame_option_hainguoi.startGame = True
                playgame_option_hainguoi.initialTime = time.time()
                playgame_option_hainguoi.stateResult = False
                start_time_game()
                if playgame_option_hainguoi.roundnow >=  total_round:
                    playgame_option_hainguoi.roundnow = 0
                    playgame_option_hainguoi.scores[1] = 0 
                    playgame_option_hainguoi.scores[0] = 0
                    reset_scores()
            else:
                print('CLI chưa vào phòng')
                
        if key == ord('q'):
            playgame_option_hainguoi.roundnow = 0
            playgame_option_hainguoi.scores[1] = 0 
            playgame_option_hainguoi.scores[0] = 0
            # When everything done, release the video capture object
            cap.release()
            
            # Closes all the frames
            cv2.destroyAllWindows()
            break
        