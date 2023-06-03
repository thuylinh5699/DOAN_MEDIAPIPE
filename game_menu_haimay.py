from dudoan import *
import time
import random
import cvzone
from console import *


class PLAY_GAME_HAIMAY:
    timer = 0
    stateResult = True
    startGame = False
    scores = [0, 0]  # [AI, Player]
    initialTime = 0
    dudoan = None
    roundnow=0
    def __init__(self) -> None:
        self.name = 'GAME PLAY'  


playgame_option_haimay = PLAY_GAME_HAIMAY()

def play_game_haimay(total_round):
    
    print('TOTAL ROUND' , total_round)
    while True:
        imgBG = cv2.imread("assets/BG_2may.png")
        # imgtest = cv2.imread("assets/1.png")
        # imgScaled = cv2.resize(imgtest, (0, 0), None, 0.875, 0.875)
        # imgScaled = imgScaled[:, 80:480]
        if playgame_option_haimay.stateResult is False:
            playgame_option_haimay.timer = time.time() - playgame_option_haimay.initialTime
            cv2.putText(imgBG, str(int(playgame_option_haimay.timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            try:
                if playgame_option_haimay.timer > 3:
                    playgame_option_haimay.stateResult = True
                    playgame_option_haimay.timer = 0
                    # if playgame_option_haimay.dudoan != None:
                        
                    AI2_random = random.randint(1, 3)
                    AI1_random = random.randint(1, 3)
                    imgAI = cv2.imread(f'assets/{AI1_random}.png', cv2.IMREAD_UNCHANGED)
                    imgAI2 = cv2.imread(f'assets/{AI2_random}.png', cv2.IMREAD_UNCHANGED)
                    if (AI2_random == 1 and AI1_random == 3) or \
                            (AI2_random == 2 and AI1_random == 1) or \
                            (AI2_random == 3 and AI1_random == 2):
                        playgame_option_haimay.scores[1] += 1

                    if (AI2_random == 3 and AI1_random == 1) or \
                            (AI2_random == 1 and AI1_random == 2) or \
                            (AI2_random == 2 and AI1_random == 3):
                        playgame_option_haimay.scores[0] += 1
                    playgame_option_haimay.roundnow +=1
                    
            except Exception as e:
                pass
        
        # imgBG[234:654, 795:1195] = imgScaled
        try:
            if playgame_option_haimay.stateResult:
                imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
                imgBG = cvzone.overlayPNG(imgBG, imgAI2, (850, 310))
        except:
            pass
        cv2.putText(imgBG, str(playgame_option_haimay.scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv2.putText(imgBG, str(playgame_option_haimay.scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        str_round = "ROUND " + str(playgame_option_haimay.roundnow)
        
        cv2.putText(imgBG, str_round, (500, 300), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4) 
        if playgame_option_haimay.roundnow >=  total_round:
            if playgame_option_haimay.scores[0] > playgame_option_haimay.scores[1] :
                whowin = "AI1 WIN, PRESS S KEY TO RESTART GAME"
            elif playgame_option_haimay.scores[0] < playgame_option_haimay.scores[1] :
                whowin = "AI2 WIN, PRESS S KEY TO RESTART GAME"
            elif playgame_option_haimay.scores[0] == playgame_option_haimay.scores[1] :
                whowin = "NO WHO WIN, PRESS S KEY TO RESTART GAME"
            
            cv2.putText(imgBG,whowin, (100, 700), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4) 
        cv2.imshow("BG", imgBG)
        # cv2.imshow("Scaled", imgScaled)
        
        
        
            
            
        key = cv2.waitKey(1)
        if key == ord('s'):
            playgame_option_haimay.startGame = True
            playgame_option_haimay.initialTime = time.time()
            playgame_option_haimay.stateResult = False
            if playgame_option_haimay.roundnow >=  total_round:
                playgame_option_haimay.roundnow = 0
                playgame_option_haimay.scores[1] = 0 
                playgame_option_haimay.scores[0] = 0
        if key == ord('q'):
            playgame_option_haimay.roundnow = 0
            playgame_option_haimay.scores[1] = 0 
            playgame_option_haimay.scores[0] = 0
            # cap.release()
            
            # Closes all the frames
            cv2.destroyAllWindows()
            
            break
        