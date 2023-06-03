from dudoan import *
import time
import random
import cvzone


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


class PLAY_GAME_MOTMAY:
    timer = 0
    stateResult = True
    startGame = False
    scores = [0, 0]  # [AI, Player]
    initialTime = 0
    dudoan = None
    roundnow=0
    def __init__(self) -> None:
        self.name = 'GAME PLAY'  


playgame_option_motmay = PLAY_GAME_MOTMAY()

def play_game_motmay(total_round):
    print('TOTAL ROUND' , total_round)
    while True:
        imgBG = cv2.imread("assets/BG.png")
        ret, img = cap.read()
    
        imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
        imgScaled = imgScaled[:, 80:480]
        if playgame_option_motmay.stateResult is False:
            playgame_option_motmay.timer = time.time() - playgame_option_motmay.initialTime
            cv2.putText(imgBG, str(int(playgame_option_motmay.timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            try:
                img,playgame_option_motmay.dudoan = nhandien(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                
                if playgame_option_motmay.timer > 3:
                    playgame_option_motmay.stateResult = True
                    playgame_option_motmay.timer = 0
                    if playgame_option_motmay.dudoan != None:
                        if playgame_option_motmay.dudoan == "ROCK":
                            playerMove = 1
                        if playgame_option_motmay.dudoan == "PAPER":
                            playerMove = 2
                        if playgame_option_motmay.dudoan == "SCISSORS":
                            playerMove = 3
                        randomNumber = random.randint(1, 3)
                        imgAI = cv2.imread(f'assets/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
                        if (playerMove == 1 and randomNumber == 3) or \
                                (playerMove == 2 and randomNumber == 1) or \
                                (playerMove == 3 and randomNumber == 2):
                            playgame_option_motmay.scores[1] += 1
            
                        # AI Wins
                        if (playerMove == 3 and randomNumber == 1) or \
                                (playerMove == 1 and randomNumber == 2) or \
                                (playerMove == 2 and randomNumber == 3):
                            playgame_option_motmay.scores[0] += 1
                        playgame_option_motmay.roundnow +=1
                        
                cv2.putText(imgBG, playgame_option_motmay.dudoan, (500, 600), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4) 
                
            except Exception as e:
                pass
        
        imgBG[234:654, 795:1195] = imgScaled
        try:
            if playgame_option_motmay.stateResult:
                imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
        except:
            pass
        cv2.putText(imgBG, str(playgame_option_motmay.scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv2.putText(imgBG, str(playgame_option_motmay.scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        str_round = "ROUND " + str(playgame_option_motmay.roundnow)
        
        cv2.putText(imgBG, str_round, (500, 300), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4) 
        if playgame_option_motmay.roundnow >=  total_round:
            if playgame_option_motmay.scores[0] > playgame_option_motmay.scores[1] :
                whowin = "COMPUTER WIN, PRESS S KEY TO RESTART GAME"
            elif playgame_option_motmay.scores[0] < playgame_option_motmay.scores[1] :
                whowin = "USER WIN, PRESS S KEY TO RESTART GAME"
            elif playgame_option_motmay.scores[0] == playgame_option_motmay.scores[1] :
                whowin = "NO WHO WIN, PRESS S KEY TO RESTART GAME"
            
            cv2.putText(imgBG,whowin, (100, 700), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4) 
        cv2.imshow("BG", imgBG)
        # cv2.imshow("Scaled", imgScaled)
        
        
        
            
            
        key = cv2.waitKey(1)
        if key == ord('s'):
            playgame_option_motmay.startGame = True
            playgame_option_motmay.initialTime = time.time()
            playgame_option_motmay.stateResult = False
            if playgame_option_motmay.roundnow >=  total_round:
                playgame_option_motmay.roundnow = 0
                playgame_option_motmay.scores[1] = 0 
                playgame_option_motmay.scores[0] = 0
        if key == ord('q'):
            playgame_option_motmay.roundnow = 0
            playgame_option_motmay.scores[1] = 0 
            playgame_option_motmay.scores[0] = 0
            # When everything done, release the video capture object
            cap.release()
            
            # Closes all the frames
            cv2.destroyAllWindows()
            break
        