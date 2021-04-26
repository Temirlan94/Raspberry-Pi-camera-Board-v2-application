import picamera
from time import sleep
import Tkinter
import time
from PIL import ImageTk, Image
import os

def quit():
    camera.stop_preview()
    global tkTop
    tkTop.destroy()

def loadJpg(file):

    #JpgWin = Tkinter.Toplevel(tkTop)
    #JpgWin.title('New Window')
    #JpgWin.geometry('400x300')

    #image = Image.open(file)
    #image = image.resize((400, 300), Image.ANTIALIAS)
    #img = ImageTk.PhotoImage(image)
    #panel = Tkinter.Label(JpgWin, image=img)
    #panel.pack(side = "bottom", fill = "both", expand = "yes")

    JpgWin.mainloop()

def capture(s,tf):
    #set parameter
    camera.sharpness = scaleSharpness.get()
    camera.contrast = scaleContrast.get()
    camera.brightness = scaleBrightness.get()
    camera.saturation = scaleSaturation.get()
    camera.exposure_compensation = scaleExpCompensation.get()
    #("%Y%m%d-%H%M%S")
    timeStamp = time.strftime("%d_%m_%Y-%H_%M_%S")
    jpgFile='img_'+timeStamp+'.jpg'
    #camera.capture ('/home/pi/Desktop/lettuce_dataset/ornek.jpg')
    #print (s)
    print (tf)
    if (s=="01"):
        #os.chdir('/home/pi/Desktop/photo_main/01')
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/01/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/01/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/01')
            camera.capture (jpgFile)
    elif (s=="02"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/02/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/02/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/02')
            camera.capture (jpgFile)
    elif (s=="03"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/03/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/03/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/03')
            camera.capture (jpgFile)
    elif (s=="04"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/04/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/04/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/04')
            camera.capture (jpgFile)
    elif (s=="05"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/05/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/05/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/05')
            camera.capture (jpgFile)
    elif (s=="06"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/06/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/06/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/06')
            camera.capture (jpgFile)
    elif (s=="07"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/07/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/07/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/07')
            camera.capture (jpgFile)
    elif (s=="08"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/08/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/08/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/08')
            camera.capture (jpgFile)
    
    elif (s=="11"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/11/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/11/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/11')
            camera.capture (jpgFile)
    elif (s=="12"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/12/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/12/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/12')
            camera.capture (jpgFile)
    elif (s=="13"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/13/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/13/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/13')
            camera.capture (jpgFile)
    elif (s=="14"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/14/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/14/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/14')
            camera.capture (jpgFile)
    elif (s=="15"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/15/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/15/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/15')
            camera.capture (jpgFile)
    elif (s=="16"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/16/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/16/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/16')
            camera.capture (jpgFile)
    elif (s=="17"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/17/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/17/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/17')
            camera.capture (jpgFile)
    elif (s=="18"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/18/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/18/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/18')
            camera.capture (jpgFile)
    
    elif (s=="21"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/21/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/21/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/21')
            camera.capture (jpgFile)
    elif (s=="22"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/22/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/22/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/22')
            camera.capture (jpgFile)
    elif (s=="23"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/23/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/23/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/23')
            camera.capture (jpgFile)
    elif (s=="24"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/24/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/24/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/24')
            camera.capture (jpgFile)
    elif (s=="25"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/25/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/25/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/25')
            camera.capture (jpgFile)
    elif (s=="26"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/26/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/26/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/26')
            camera.capture (jpgFile)
    elif (s=="27"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/27/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/27/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/27')
            camera.capture (jpgFile)
    elif (s=="28"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/28/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/28/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/28')
            camera.capture (jpgFile)
    
    elif (s=="31"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/31/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/31/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/31')
            camera.capture (jpgFile)
    elif (s=="32"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/32/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/32/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/32')
            camera.capture (jpgFile)
    elif (s=="33"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/33/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/33/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/33')
            camera.capture (jpgFile)
    elif (s=="34"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/34/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/34/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/34')
            camera.capture (jpgFile)
    elif (s=="35"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/35/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/35/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/35')
            camera.capture (jpgFile)
    elif (s=="36"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/36/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/36/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/36')
            camera.capture (jpgFile)
    elif (s=="37"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/37/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/37/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/37')
            camera.capture (jpgFile)
    elif (s=="38"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/38/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/38/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/38')
            camera.capture (jpgFile)
        
    elif (s=="41"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/41/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/41/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/41')
            camera.capture (jpgFile)
    elif (s=="42"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/42/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/42/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/42')
            camera.capture (jpgFile)
    elif (s=="43"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/43/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/43/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/43')
            camera.capture (jpgFile)
    elif (s=="44"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/44/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/44/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/44')
            camera.capture (jpgFile)
    elif (s=="45"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/45/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/45/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/45')
            camera.capture (jpgFile)
    elif (s=="46"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/46/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/46/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/46')
            camera.capture (jpgFile)
    elif (s=="47"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/47/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/47/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/47')
            camera.capture (jpgFile)
    elif (s=="48"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/48/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/48/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/48')
            camera.capture (jpgFile)
        
    elif (s=="51"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/51/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/51/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/51')
            camera.capture (jpgFile)
    elif (s=="52"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/52/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/52/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/52')
            camera.capture (jpgFile)
    elif (s=="53"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/53/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/53/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/53')
            camera.capture (jpgFile)
    elif (s=="54"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/54/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/54/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/54')
            camera.capture (jpgFile)
    elif (s=="55"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/55/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/55/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/55')
            camera.capture (jpgFile)
    elif (s=="56"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/56/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/56/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/56')
            camera.capture (jpgFile)
    elif (s=="57"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/57/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/57/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/57')
            camera.capture (jpgFile)
    elif (s=="58"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/58/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/58/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/58')
            camera.capture (jpgFile)
        
    elif (s=="61"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/61/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/61/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/61')
            camera.capture (jpgFile)
    elif (s=="62"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/62/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/62/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/62')
            camera.capture (jpgFile)
    elif (s=="63"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/63/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/63/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/63')
            camera.capture (jpgFile)
    elif (s=="64"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/64/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/64/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/64')
            camera.capture (jpgFile)
    elif (s=="65"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/65/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/65/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/65')
            camera.capture (jpgFile)
    elif (s=="66"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/66/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/66/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/66')
            camera.capture (jpgFile)
    elif (s=="67"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/67/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/67/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/67')
            camera.capture (jpgFile)
    elif (s=="68"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/68/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/68/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/68')
            camera.capture (jpgFile)
    
    elif (s=="71"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/71/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/71/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/71')
            camera.capture (jpgFile)
    elif (s=="72"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/72/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/72/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/72')
            camera.capture (jpgFile)
    elif (s=="73"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/73/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/73/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/73')
            camera.capture (jpgFile)
    elif (s=="74"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/74/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/74/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/74')
            camera.capture (jpgFile)
    elif (s=="75"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/75/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/75/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/75')
            camera.capture (jpgFile)
    elif (s=="76"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/76/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/76/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/76')
            camera.capture (jpgFile)
    elif (s=="77"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/77/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/77/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/77')
            camera.capture (jpgFile)
    elif (s=="78"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/78/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/78/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/78')
            camera.capture (jpgFile)
    
    elif (s=="81"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/81/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/81/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/81')
            camera.capture (jpgFile)
    elif (s=="82"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/82/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/82/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/82')
            camera.capture (jpgFile)
    elif (s=="83"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/83/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/83/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/83')
            camera.capture (jpgFile)
    elif (s=="84"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/84/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/84/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/84')
            camera.capture (jpgFile)
    elif (s=="85"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/85/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/85/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/85')
            camera.capture (jpgFile)
    elif (s=="86"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/86/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/86/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/86')
            camera.capture (jpgFile)
    elif (s=="87"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/87/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/87/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/87')
            camera.capture (jpgFile)
    elif (s=="88"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/88/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/88/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/88')
            camera.capture (jpgFile)
    
    elif (s=="91"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/91/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/91/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/91')
            camera.capture (jpgFile)
    elif (s=="92"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/92/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/92/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/92')
            camera.capture (jpgFile)
    elif (s=="93"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/93/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/93/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/93')
            camera.capture (jpgFile)
    elif (s=="94"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/94/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/94/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/94')
            camera.capture (jpgFile)
    elif (s=="95"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/95/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/95/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/95')
            camera.capture (jpgFile)
    elif (s=="96"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/96/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/96/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/96')
            camera.capture (jpgFile)
    elif (s=="97"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/97/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/97/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/97')
            camera.capture (jpgFile)
    elif (s=="98"):
        if (tf=="t"):
            os.chdir('/home/pi/Desktop/photo_main/98/Top')
            camera.capture (jpgFile)
        elif (tf=="f"):
            os.chdir('/home/pi/Desktop/photo_main/98/Front')
            camera.capture (jpgFile)
        else:
            os.chdir('/home/pi/Desktop/photo_main/98')
            camera.capture (jpgFile)
        
    elif (s=="led"):
        os.chdir('/home/pi/Desktop/photo_main/led')
        camera.capture (jpgFile)
    
        
    else:
        os.chdir('/home/pi/Desktop/photo_main/default')
        camera.capture(jpgFile)
        
    os.chdir('/home/pi/Desktop/photo_main')    
    loadJpg(jpgFile)
    

camera = picamera.PiCamera()

#set default
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
#camera.rotation = 0
camera.rotation = 270
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)
camera.resolution = (3280,2464)
#camera.resolution = (2592, 1944)
#end of set default

camera.start_preview(fullscreen=False, window = (0, 5, 400, 250))
camera.brightness = 50
    

tkTop = Tkinter.Tk()
tkTop.wm_title("Raspberry Pi Camera - Brightness")
tkTop.geometry('800x500')
    
entry1 = Tkinter.Entry(tkTop)
entry1.pack()
tf = entry1.get()

entry = Tkinter.Entry(tkTop)
entry.pack()
s = entry.get()



def getPhoto():
    tf= entry1.get()
    s = entry.get()
    capture (s,tf)
    #print (s)
    #print(tf)
    
    
tkButtonGet = Tkinter.Button(
    tkTop, text="PATH", command=getPhoto)
tkButtonGet.pack()



SCALE_WIDTH = 780;

scaleSharpness = Tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="sharpness")
scaleSharpness.set(0)
scaleSharpness.pack(anchor=Tkinter.CENTER)

scaleContrast = Tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="contrast")
scaleContrast.set(0)
scaleContrast.pack(anchor=Tkinter.CENTER)

scaleBrightness = Tkinter.Scale(
    tkTop,
    from_=0, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="brightness")
scaleBrightness.set(50)
scaleBrightness.pack(anchor=Tkinter.CENTER)

scaleSaturation = Tkinter.Scale(
    tkTop,
    from_=-100, to=100,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="saturation")
scaleSaturation.set(0)
scaleSaturation.pack(anchor=Tkinter.CENTER)

scaleExpCompensation = Tkinter.Scale(
    tkTop,
    from_=-25, to=25,
    length=SCALE_WIDTH,
    orient=Tkinter.HORIZONTAL,
    label="exposure_compensation")
scaleExpCompensation.set(0)
scaleExpCompensation.pack(anchor=Tkinter.CENTER)

#tkButtonCapture = Tkinter.Button(
#    tkTop, text="Capture", command=capture)
#tkButtonCapture.pack()
tkButtonQuit = Tkinter.Button(
    tkTop, text="Quit", command=quit)
tkButtonQuit.pack()

Tkinter.mainloop()