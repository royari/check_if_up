import cv2
import os
import os.path
import glob
import time
import torch
import torchvision
from ocr.CNN import Net
import matplotlib.pyplot as plt
import numpy as np
import time
from torchvision import transforms
import PIL


def imshow(img,Time):
    img = 2*(img - 0.5)     # unnormalize
    npimg = img.numpy()
    plt.close('all')
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show(block=False)
    plt.pause(Time)
    

def Div(img):


    backup = img.copy()   #taking backup of the input image

    grey= cv2.cvtColor(backup, cv2.COLOR_BGR2GRAY)
# backup = 255-backup    #colour inversion
    thresh = cv2.threshold(grey, 200, 255, cv2.THRESH_BINARY_INV )[1]
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(hierarchy)
    # print(contours)
    transform_img = transforms.Compose([transforms.Resize((24,14)),\
                                    transforms.Grayscale(num_output_channels=1),transforms.ToTensor(),\
    transforms.Normalize((0.5,),(0.5,))])

    transforming_org_img = transforms.Compose([transforms.Resize((24,14)),transforms.ToTensor()])
    imgTensor = torch.zeros(6,1,24,14)
    orgTensor = torch.zeros(6,1,24,14)
    image_regions = []
    org_img = []
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



    for i,letter_box in enumerate(image_regions):

        x,y,w,h = letter_box
        letter_image = grey[y - 2: y + h + 2, x - 2:x + w + 2]


        # letter_image = cv2.resize(letter_image,(14,24))
        letter_image = transform_img(PIL.Image.fromarray(letter_image))

        org_img = thresh[y - 2: y + h + 2, x - 2:x + w + 2]/255
        # org_img = cv2.resize(org_img,(14,24))
        # org_img = transforming_org_img(PIL.Image.fromarray(org_img))
        imgTensor[i][0] = letter_image.clone().detach()
        # orgTensor[i][0] = torch.tensor(org_img)
        # greyTensor[i][0]=
        # imshow(torchvision.utils.make_grid(orgTensor,0.1))
    # imshow(orgTensor,5)
    imshow(torchvision.utils.make_grid(imgTensor), 5)
    return imgTensor

if __name__ == "__main__":

    classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',\
         'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',\
                   'X', 'Y', 'Z']

    image_file = "./captcha.jpg"

    img = cv2.imread(image_file)

    tens = torch.zeros(6,1,24,14)
    tens = Div(img)
    net = Net()
    print(f'the div shape is {tens.size}\n\n {tens}')
    net.load_state_dict(torch.load("ocr/mod.pt"))

    with torch.no_grad():
        result = net(tens)
        _,pred = torch.max(result,1)

    predArray= []
    for i in range(6):
        predArray.append(classes[pred[i]])
        print(f'{classes[pred[i]]} ',sep=" ",end = " ")
    print(f"{predArray}")

    

    



        
