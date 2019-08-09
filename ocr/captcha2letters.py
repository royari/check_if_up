import cv2
import os
import os.path
import glob
import time

CAPTCHA_FOLDER = '../captcha_data'
LETTER_FOLDER = '../letters'

image_files = glob.glob(os.path.join(CAPTCHA_FOLDER,"*"))
# print(f'Total files = {len(image_files)}')
# for i,_ in enumerate(image_files):
#     print(f'image ({i+1}/{len(image_files)}) is ----------> {_}')
#     time.sleep(0.1)
counts = {}

for i,image_file in enumerate(image_files):
    print(f'Processing image file --------- ({i+1}/{len(image_files)})')
    filename = os.path.basename(image_file)
    # print(f"BASE NAME IS {filename}")
    captcha_text = list(filename.split(".")[0])
    # print(f'the captcha text is {captcha_text}')



    img = cv2.imread(image_file)
    backup = img.copy()   #taking backup of the input image

    grey= cv2.cvtColor(backup, cv2.COLOR_BGR2GRAY)
# backup = 255-backup    #colour inversion
    thresh = cv2.threshold(grey, 200, 255, cv2.THRESH_BINARY_INV )[1]
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(hierarchy)
    # print(contours)
    image_regions = []
    for j, topology in enumerate(hierarchy[0]):
        if  topology[-1] != -1 :
            continue    
        x, y, w, h = cv2.boundingRect(contours[j])
        # print("ok")
        if w/h > 1.25:
            w_half = int(w/2)

            image_regions.append((x,y,w_half,h))
            cv2.rectangle(img, (x, y), (x + w_half, y + h), (0, 255, 0), 1)
            image_regions.append((x+w_half,y,w_half,h))
            cv2.rectangle(img, (x+w_half, y), (x +w_half + w_half, y + h), (0, 255, 0), 1)
        
        else:
            image_regions.append((x,y,w,h))
    


        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
        if len(image_regions)!=6:
            continue
    # print("out of loop 1")
    image_regions = sorted(image_regions, key = lambda x: x[0])
    for letter_box ,letter_text in zip(image_regions,captcha_text):
        # print("hi")
        x,y,w,h = letter_box
        letter_image = grey[y - 2: y + h + 2, x - 2:x + w + 2]
        # print(f'this is line 59 {letter_text}')
        save_path = os.path.join(LETTER_FOLDER,letter_text)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        count = counts.get(letter_text,1)
        l = os.path.join(save_path,"{}.png".format(str(count).zfill(6)))
        cv2.imwrite(l,letter_image)

        counts[letter_text] = count + 1


    # cv2.imwrite('output3.png', img)