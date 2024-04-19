import flet
from flet import *
from controls import return_control_refrence
from form_helper import FormHelper
import sqlite3
import cv2
import os
import numpy as np
from PIL import Image 


def banner_without_offset():
    folder = 'banner'
    card = cv2.imread('imgs/mainCard2.png')
    cardResize = cv2.resize(card,(260,400))
    images = os.listdir('finalCard')
    
    image_objects = [cv2.imread(f'finalCard/{filename}') for filename in images]
    


    len_image_objects = len(image_objects)
    print(len_image_objects)

    if(len_image_objects==1):
        h_stack1 = np.hstack(image_objects[0])
        v_stack = np.vstack([h_stack1])
        # cv2.imshow("Collage",v_stack)
        # cv2.waitKey(0)
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==2):
        h_stack1 = np.hstack([image_objects[0],image_objects[1]])
        v_stack = np.vstack([h_stack1])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==3):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2]])
        v_stack = np.vstack([h_stack1])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==4):
        h_stack1 = np.hstack([image_objects[0],image_objects[1]])
        h_stack2 = np.hstack([image_objects[2],image_objects[3]])
        v_stack = np.vstack([h_stack1,h_stack2])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==5):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[1]])
        h_stack2 = np.hstack([image_objects[2],image_objects[3],cardResize])
        v_stack = np.vstack([h_stack1,h_stack2])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==6):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[4]])
        h_stack2 = np.hstack([image_objects[2],image_objects[3],image_objects[5]])
        v_stack = np.vstack([h_stack1,h_stack2])



        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==7):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[4]])
        h_stack2 = np.hstack([image_objects[2],image_objects[3],image_objects[5]])
        h_stack3 = np.hstack([cardResize,image_objects[6],cardResize])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==8):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[4],image_objects[6]])
        h_stack2 = np.hstack([image_objects[2],image_objects[3],image_objects[5],image_objects[7]])
        v_stack = np.vstack([h_stack1,h_stack2])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==9):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2]])
        h_stack2 = np.hstack([image_objects[3],image_objects[4],image_objects[5]])
        h_stack3 = np.hstack([image_objects[6],image_objects[7],image_objects[8]])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==10):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[4]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[9]])
        v_stack = np.vstack([h_stack1,h_stack2])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==11):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[4]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[9]])
        h_stack3 = np.hstack([cardResize,cardResize,image_objects[7],cardResize,cardResize])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==12):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3]])
        h_stack2 = np.hstack([image_objects[4],image_objects[5],image_objects[6],image_objects[7]])
        h_stack3 = np.hstack([image_objects[8],image_objects[9],image_objects[10],image_objects[11]])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==13):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[12]])
        h_stack2 = np.hstack([image_objects[4],image_objects[5],image_objects[8],image_objects[6],image_objects[7]])
        h_stack3 = np.hstack([cardResize,image_objects[9],image_objects[10],image_objects[11],cardResize])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==14):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[12]])
        h_stack2 = np.hstack([image_objects[4],image_objects[5],cardResize,image_objects[6],image_objects[7]])
        h_stack3 = np.hstack([image_objects[8],image_objects[9],image_objects[10],image_objects[11],image_objects[13]])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==15):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[4]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[9]])
        h_stack3 = np.hstack([image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[14]])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==16):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8]])
        h_stack3 = np.hstack([image_objects[10],image_objects[11],image_objects[12],image_objects[13]])
        h_stack4 = np.hstack([image_objects[4],image_objects[9],image_objects[14],image_objects[15]])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==17):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[4]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[9]])
        h_stack3 = np.hstack([image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[14]])
        h_stack4 = np.hstack([image_objects[15],image_objects[16],cardResize,cardResize,cardResize])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==18):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[4],image_objects[9]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[14],image_objects[15]])
        h_stack3 = np.hstack([image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[17],image_objects[16]])
        # h_stack4 = np.hstack([,,,])
        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==19):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([cardResize,image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==20):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==21):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20]])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==22):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20]])
        h_stack4 = np.hstack([cardResize,cardResize,cardResize,image_objects[21],cardResize,cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==23):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20]])
        h_stack4 = np.hstack([cardResize,cardResize,image_objects[22],cardResize,image_objects[21],cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==24):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20]])
        h_stack4 = np.hstack([cardResize,cardResize,image_objects[22],image_objects[23],image_objects[21],cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==25):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20]])
        h_stack4 = np.hstack([cardResize,image_objects[24],image_objects[22],image_objects[23],image_objects[21],cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==26):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20]])
        h_stack4 = np.hstack([cardResize,image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[25],cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==27):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20]])
        h_stack4 = np.hstack([image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[25],cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==28):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20]])
        h_stack4 = np.hstack([image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[25],image_objects[27]])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==29):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([cardResize,image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==30):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([cardResize,image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])

        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==31):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==32):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],image_objects[31]])
        h_stack5 = np.hstack([cardResize,cardResize,cardResize,image_objects[31],cardResize,cardResize,cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4,h_stack5])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==33):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],image_objects[31]])
        h_stack5 = np.hstack([cardResize,cardResize,cardResize,image_objects[31],image_objects[32],cardResize,cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4,h_stack5])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==34):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],image_objects[31]])
        h_stack5 = np.hstack([cardResize,cardResize,image_objects[33],image_objects[31],image_objects[32],cardResize,cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4,h_stack5])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==35):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],image_objects[31]])
        h_stack5 = np.hstack([cardResize,cardResize,image_objects[33],image_objects[31],image_objects[32],image_objects[34],cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4,h_stack5])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==36):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],image_objects[31]])
        h_stack5 = np.hstack([cardResize,image_objects[35],image_objects[33],image_objects[31],image_objects[32],image_objects[34],cardResize,cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4,h_stack5])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==37):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],image_objects[31]])
        h_stack5 = np.hstack([cardResize,image_objects[35],image_objects[33],image_objects[31],image_objects[32],image_objects[34],image_objects[36],cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4,h_stack5])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==38):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],image_objects[31]])
        h_stack5 = np.hstack([image_objects[37],image_objects[35],image_objects[33],image_objects[31],image_objects[32],image_objects[34],image_objects[36],cardResize])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4,h_stack5])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==39):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],image_objects[31]])
        h_stack5 = np.hstack([image_objects[37],image_objects[35],image_objects[33],image_objects[31],image_objects[32],image_objects[34],image_objects[36],image_objects[38]])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4,h_stack5])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    elif(len_image_objects==40):
        h_stack1 = np.hstack([image_objects[0],image_objects[1],image_objects[2],image_objects[3],image_objects[18],image_objects[14],image_objects[16],image_objects[28]])
        h_stack2 = np.hstack([image_objects[5],image_objects[6],image_objects[7],image_objects[8],image_objects[4],image_objects[15],image_objects[17],image_objects[27]])
        h_stack3 = np.hstack([image_objects[19],image_objects[10],image_objects[11],image_objects[12],image_objects[13],image_objects[9],image_objects[20],image_objects[25]])
        h_stack4 = np.hstack([image_objects[30],image_objects[26],image_objects[24],image_objects[22],image_objects[23],image_objects[21],image_objects[29],image_objects[31]])
        h_stack5 = np.hstack([image_objects[37],image_objects[35],image_objects[33],image_objects[31],image_objects[32],image_objects[34],image_objects[36],image_objects[38]])

        v_stack = np.vstack([h_stack1,h_stack2,h_stack3,h_stack4,h_stack5])
        cv2.imwrite(f'{folder}/offset.png',v_stack)

    

    
    cv2.imwrite(f'{folder}/offset.png',v_stack)
    folder = 'banner'
    final = cv2.imread('banner/offset.png')
    (w,h,d) = final.shape
    hplace = 30
    hplace = int(hplace)
    wplace = w*0.4
    wplace = int(wplace)
    name = 'BHARTI VIDYAPEETH COLLEGE OF ENGINEERING PLACEMENT'
    cv2.putText(final,name,(wplace,hplace),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,0,0),2)
    cv2.imwrite(f'{folder}/offset.png',final)
    # cv2.imshow('Banner',final)
    cv2.waitKey(0)

control_map = return_control_refrence()

def update_text(e):
    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()

def get_input_data(e):
    for key,value in control_map.items():
        if key == "AppForm":
            data = DataRow(cells=[])

            for user_input in value.controls[0].content.controls[0].controls[:]:
                folder = 'finalCard'

                card = cv2.imread('imgs/mainCard3.png')
                cardResize = cv2.resize(card,(260,400)) 
                
                data.cells.append(
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e)
                    )
                )
                print(user_input.content.controls[1].value)
                fullname = user_input.content.controls[1].value
                cv2.putText(cardResize, user_input.content.controls[1].value, (58,240), cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0))

            for user_input in value.controls[0].content.controls[1].controls[:]:
                data.cells.append(
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e)
                    )
                )
                print(user_input.content.controls[1].value)
                cv2.putText(cardResize, user_input.content.controls[1].value, (90,283), cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0))

            for user_input in value.controls[0].content.controls[2].controls[:]:
                data.cells.append(
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e)
                    )
                )
                print(user_input.content.controls[1].value)
                cv2.putText(cardResize, user_input.content.controls[1].value, (92,311), cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0))

            for user_input in value.controls[0].content.controls[3].controls[:]:
                data.cells.append(
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e)
                    )
                )
                print(user_input.content.controls[1].value)
                cv2.putText(cardResize, user_input.content.controls[1].value, (92,340), cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0))
        
        if key == 'AppDataTable':
            value.controls[0].controls[0].rows.append(data)
            value.controls[0].controls[0].update()
            cv2.imshow("Card",cardResize)
            key = cv2.waitKey(1)
            cv2.imwrite(f'{folder}/{fullname}.png',cardResize)



def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor='#081d33',
            color='white',
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12,
                    ),
                    Text(
                        "Add",
                        size=11,
                        weight='bold'
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "":RoundedRectangleBorder(radius=6),
                },
                color={
                    "":'white',
                },
            ),
            height=42,
            width=220,
        ),
    )



#****************Image section
# def add_images():
#     for key,value in control_map.items():
#         if key == "AppForm":
#             data = DataRow(cells=[])

#             for user_input in value.controls[0].content.controls[0].controls[:]:
#                 folder = 'finalCard'

#                 card = cv2.imread('imgs/mainCard3.png')
#                 cardResize = cv2.resize(card,(260,400)) 
                
#                 data.cells.append(
#                     DataCell(
#                         FormHelper(user_input.content.controls[1].value),
#                         on_double_tap=lambda e: update_text(e)
#                     )
#                 )
#                 print(user_input.content.controls[1].value)
#                 fullname = user_input.content.controls[1].value
                
#                 images = os.listdir('finalCard')
#                 image_objects = [Image.open(f'photos/{filename}') for filename in images]
#                 image_objects_len = len(image_objects)
#                 print(image_objects_len)
                
#                 card = os.listdir('photos')
#                 card_objects = [Image.open(f'finalCard/{filename}') for filename in card]
#                 card_objects_len = len(card_objects)
#                 print(card_objects_len)
                
#                 for i in range(0,image_objects_len):
#                     if image_objects[i] == card_objects[i]:
#                         img1 = Image.open(f'{r"finalCard/{card_objects[i]}.png"}')
#                         img2 = Image.open(f'{r"photos/image_objects[i].jpg"}') 
#                         Image.Image.paste(img1, img2, (60, 70))
                
#                         img1.show()
                        
                        
# def add_imagesss():
#     images = os.listdir('photos')
#     image_objects = [Image.open(f'photos/{filename}') for filename in images]
#     image_objects_len = len(image_objects)
#     # print(image_objects_len)
#     # print(image_objects)
#     print(images)
    
                
#     card = os.listdir('finalCard')
#     card_objects = [Image.open(f'finalCard/{filename}') for filename in card]
#     card_objects_len = len(card_objects)
#     # print(card_objects_len)
#     # print(card_objects)
                
    
#     if card_objects_len == 10:
        
#         Ashishp = Image.open(r"photos/Ashish.png") 
#         Abhimanyup = Image.open(r"photos/Abhimanyu.png") 
#         Adityap = Image.open(r"photos/Aditya.png") 
#         Chiragp = Image.open(r"photos/Chirag.png") 
#         Deepp = Image.open(r"photos/Deep.png") 
#         Kankalp = Image.open(r"photos/Kankal.png") 
#         Paramp = Image.open(r"photos/Param.png") 
#         Shreep = Image.open(r"photos/Shree.png") 
#         Vedantp = Image.open(r"photos/Vedant.png") 
#         Vigneshp = Image.open(r"photos/Vignesh.png") 
        
#         Ashishpc = Image.open(r"finalCard/Ashish.png") 
#         Abhimanyuc = Image.open(r"finalCard/Abhimanyu.png") 
#         Adityac = Image.open(r"finalCard/Aditya.png") 
#         Chiragc = Image.open(r"finalCard/Chirag.png") 
#         Deepc = Image.open(r"finalCard/Deep.png") 
#         Kankalc = Image.open(r"finalCard/Kankal.png") 
#         Paramc = Image.open(r"finalCard/Param.png") 
#         Shreec = Image.open(r"finalCard/Shree.png") 
#         Vedantc = Image.open(r"finalCard/Vedant.png") 
#         Vigneshc = Image.open(r"finalCard/Vignesh.png") 
        
#         Image.Image.paste(Ashishpc, Ashishp, (146, 165))
#         Image.Image.paste(Abhimanyuc, Abhimanyup, (146, 165))
#         Image.Image.paste(Adityac, Adityap, (146, 165))
#         Image.Image.paste(Chiragc, Chiragp, (146, 165))
#         Image.Image.paste(Deepc, Deepp, (146, 165))
#         Image.Image.paste(Kankalp, Kankalc, (146, 165))
#         Image.Image.paste(Paramc, Paramp, (146, 165))
#         Image.Image.paste(Shreec, Shreep, (146, 165))
#         Image.Image.paste(Vedantc, Vedantp, (146, 165))
#         Image.Image.paste(Vigneshc, Vigneshp, (146, 165))
        
#         Ashishpc.show()
#         Ashishpc.save(f'finalCards/{Ashishpc}.png')
#         Abhimanyuc.show()
#         Abhimanyuc.save(f'finalCards/{Abhimanyuc}.png')
#         Adityac.show()
#         Adityac.save(f'finalCards/{Adityac}.png')
#         Deepc.show()
#         Deepc.save(f'finalCards/{Deepc}.png')
#         Kankalp.show()
#         Kankalp.save(f'finalCards/{Kankalp}.png')
#         Paramc.show()
#         Paramc.save(f'finalCards/{Paramc}.png')
#         Shreec.show()
#         Shreec.save(f'finalCards/{Shreec}.png')
#         Vedantc.show()
#         Vedantc.save(f'finalCards/{Vedantc}.png')
#         Vigneshc.show()
#         Vigneshc.save(f'finalCards/{Vigneshc}.png')
#         Chiragc.show()
#         Chiragc.save(f'finalCards/{Chiragc}.png')
                
                
def add_image():
    
    img1 = Image.open(r"banner/offset.png") 
  
    img2 = Image.open(r"photos/Aditya.png") 
    img3 = Image.open(r"photos/Aryan.png") 
    img4 = Image.open(r"photos/Ashish.png") 
    img5 = Image.open(r"photos/Bhushan.png") 
    img6 = Image.open(r"photos/Kartik.png") 
    img7 = Image.open(r"photos/Sanika.png") 
    img8 = Image.open(r"photos/Sejal.png") 
    img9 = Image.open(r"photos/Shree.png") 
    img10 = Image.open(r"photos/Shreyash.png") 
    img11 = Image.open(r"photos/Sumedh.png") 
    
    # img1.paste(img2, (0,0), mask=img2) 
    Image.Image.paste(img1, img2, (60, 70))
    Image.Image.paste(img1, img3, (320, 70))
    Image.Image.paste(img1, img4, (580, 70))
    Image.Image.paste(img1, img5, (840, 70))
    Image.Image.paste(img1, img6, (1100, 70))
    Image.Image.paste(img1, img7, (60, 470))
    Image.Image.paste(img1, img8, (320, 470))
    Image.Image.paste(img1, img9, (580, 470))
    Image.Image.paste(img1, img10, (840, 470))
    Image.Image.paste(img1, img11, (1100, 470))
    img1.save('final/final.png')
    img1.show()
                
