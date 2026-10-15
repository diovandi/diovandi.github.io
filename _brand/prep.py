import sys
from PIL import Image, ImageFilter, ImageDraw
import numpy as np
S=4
g=Image.open('ref_gray.png')
g=g.resize((g.width*S,g.height*S),Image.LANCZOS).filter(ImageFilter.GaussianBlur(S*0.9))
a=np.array(g)
m=(a<128)
img=Image.fromarray(np.where(m,0,255).astype('uint8'))
d=ImageDraw.Draw(img)
L,R=float(sys.argv[1]),float(sys.argv[2])   # stem edges in ref px (inclusive-ish)
gapL,gapR=(float(sys.argv[3]),float(sys.argv[4])) if len(sys.argv)>4 else (10,17)
# clear the old stem and keep the crescent gaps
d.rectangle([ (L-gapL)*S, 150*S, (R+gapR)*S, 640*S], fill=255)
# restore crescent arms outside the new gaps: original mask outside
orig=Image.fromarray(np.where(m,0,255).astype('uint8'))
keep=Image.new('L',img.size,0); kd=ImageDraw.Draw(keep)
kd.rectangle([0,150*S,(L-gapL)*S-1,640*S],fill=255); kd.rectangle([(R+gapR)*S+1,150*S,img.width,640*S],fill=255)
img.paste(orig,(0,0),keep)
# new stem: chamfered top, straight sides, blend into flare below 640
top=180
bot=float(sys.argv[6]) if len(sys.argv)>6 else 660
d.polygon([(L*S,(top+33)*S),(R*S,top*S),(R*S,bot*S),(L*S,bot*S)],fill=0)
img.save(sys.argv[5] if len(sys.argv)>5 else 'prep.pbm')
img.save('prep.png')
