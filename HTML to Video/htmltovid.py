import bs4 as bs
from PIL import Image, ImageDraw
import os
import cv2
print (os.getcwd())

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

ans_dir = 'C:/Data/python/html to video/question&answer/question&answer/answer'
que_dir = 'C:/Data/python/html to video/question&answer/question&answer/question'

def sort(folder):
    folder = [int(s[:(s.find('.html'))]) for s in folder]
    folder.sort()
    folder = [str(s)+'.html' for s in folder]
    return folder

def video(answer,question):

    k = 1

    for i in answer:
        j = 20
        im = Image.new('RGB',(512,512),'white')
        d= ImageDraw.Draw(im)
        ans = ans_dir + '/' + i

        with open(ans,'r') as f:
            ans_soup = bs.BeautifulSoup(f.read(),'lxml')

        for para in ans_soup.find_all('p'):
            #print(para.text)
            try:
                d.text((20,j),para.text,fill='black')
                j+=10
            except Exception as e:
                print(i)
                print(e)

        pic = ans_dir + '/' +'ans' + str(k) + '.jpeg'
        im.save(pic)
        img1 = cv2.imread(pic)

        h,w,l = img1.shape
        if k==1:
            video = cv2.VideoWriter('video.avi',fourcc,float(1),(w,h))

        video.write(img1)
        cv2.waitKey(500)
        k+=1
        d = None
        im = None

    cv2.destroyAllWindows()
    video.release()


answer = os.listdir(ans_dir)
answer = sort(answer)

question = os.listdir(que_dir)
question = sort(question)

if (len(answer)<len(question)):
    video(answer,question)
elif (len(answer)>len(question)):
    pass

'''
with open('C:/Data/python/html to video/question&answer/question&answer/answer/2.html','r') as f:
    soup = bs.BeautifulSoup(f.read(),'lxml')

for para in soup.find_all('p'):
    #print(para.text)
    d.text((20,i),para.text,fill='black')
    i+=10

im.save('test3.jpeg')

img1 = cv2.imread('test3.jpeg')

h,w,l = img1.shape

video = cv2.VideoWriter('video.avi',fourcc,float(1),(w,h))

video.write(img1)


cv2.destroyAllWindows()
video.release()

'''


'''text = soup.get_text()

lines = [line.strip() for line in text.splitlines()]

print (lines)'''
