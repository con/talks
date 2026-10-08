# Generates pics/neuroconv-formats-cloud.svg (NeuroConv formats, colored by modality).
# Needs only Pillow; run from the repo root: python3 2026-dhmc-ieeg/neuroconv-formats-cloud.py
import math, random
from PIL import ImageFont
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
W,H=1500,800
cats={ # name: (color, center, words)
 'Extracellular ephys: recording':('#1f5fa8',(420,330),"AlphaOmega Axona Biocam Blackrock EDF Intan MaxOne MCSRaw MEArec Neuralynx NeuroScope OpenEphys Plexon Spike2 Spikegadgets SpikeGLX TDT WhiteMatter".split()),
 'Extracellular ephys: sorting':('#5b8fd1',(420,330),"Blackrock CellExplorer KiloSort Neuralynx NeuroScope Phy Plexon".split()),
 'Intracellular ephys':('#6a3d9a',(760,120),["ABF"]),
 'Optical: imaging':('#c8501a',(1050,250),"Bruker HDF5 Micro-Manager Miniscope Scanbox ScanImage Tiff Thor Inscopix".split()),
 'Optical: segmentation':('#e8963c',(1050,250),"Caiman CNMFE EXTRACT Suite2P".split()),
 'Natural behavior':('#2a8a4a',(1000,600),"Audio DeepLabCut FicTrac LightningPose SLEAP Videos Facemap Moseq".split()),
 'Behavioral events':('#8a7a1a',(560,650),"CSV Excel MedPC".split()),
}
soon={'Inscopix','Facemap','Moseq'}  # greyed out on the NeuroConv listing
pad=8; placed=[]; out=[]
def fits(b):
    x0,y0,x1,y1=b
    if x0<10 or y0<10 or x1>W-10 or y1>H-85: return False
    return all(x1+pad<=a or x0-pad>=c or y1+pad<=b2 or y0-pad>=d for a,b2,c,d in placed)
random.seed(4)
items=[]
for cat,(col,ctr,words) in cats.items():
    for w in words: items.append((cat,col,ctr,w))
items.sort(key=lambda t:-len(t[3]))
for cat,col,ctr,w in items:
    size=44 if len(w)<=5 else 38 if len(w)<=8 else 32
    f=ImageFont.truetype(FONT,size); tw=f.getlength(w); th=size*0.95
    ok=False; t=0
    while not ok and t<4000:
        r=2.2*t**0.5*4; a=t*0.55; x=ctr[0]+r*math.cos(a)-tw/2; y=ctr[1]+r*math.sin(a)*0.6-th/2
        b=(x,y,x+tw,y+th); ok=fits(b); t+=1
    assert ok,w
    placed.append(b)
    op=0.35 if w in soon else 1
    out.append(f'<text x="{x:.1f}" y="{y+th*0.82:.1f}" font-size="{size}" fill="{col}" opacity="{op}">{w}</text>')
legend=[('Extracellular ephys: recording','#1f5fa8'),('spike sorting','#5b8fd1'),('Intracellular ephys','#6a3d9a'),
        ('Optical: imaging','#c8501a'),('segmentation','#e8963c'),('Natural behavior','#2a8a4a'),('Behavioral events','#8a7a1a'),('faded: in progress','#bbbbbb')]
legsvg=[]; x=20; y=H-62
for label,col in legend:
    f=ImageFont.truetype(FONT,20); tw=f.getlength(label)
    if x+tw+50>W-10: x=20; y+=30
    legsvg.append(f'<rect x="{x}" y="{y}" width="20" height="20" rx="4" fill="{col}"/><text x="{x+28}" y="{y+16}" font-size="20" fill="#333" font-weight="normal">{label}</text>')
    x+=tw+56
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Verdana, sans-serif" font-weight="bold"><rect width="{W}" height="{H}" fill="#ffffff"/>'+''.join(out)+''.join(legsvg)+'</svg>'
open('/home/user/talks/pics/neuroconv-formats-cloud.svg','w').write(svg)
print(len(svg),'bytes',len(out),'words; legend width',x)
