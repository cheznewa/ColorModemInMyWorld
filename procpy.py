import sys
from PIL import Image
from color_modem.color.mac import MacModem, MacVariant
from color_modem.color.niir import NiirModem, HueCorrectingNiirModem
from color_modem.color.ntsc import NtscCombModem, NtscVariant, NtscModem
from color_modem.color.pal import Pal3DModem, PalVariant, PalDModem, PalSModem
from color_modem.color.protosecam import ProtoSecamModem, ProtoSecamVariant
from color_modem.color.secam import SecamModem, SecamVariant
from color_modem.comb import Simple3DCombModem, SimpleCombModem, ColorAveragingModem
from color_modem.image import ImageModem
from color_modem.line import LineStandard, LineConfig
line_config = LineConfig((720,576))
if sys.argv[3] == "bt":
 modem = SecamModem(line_config,variant=SecamVariant.SECAM_III)
if sys.argv[3] == "ph":
 modem = SecamModem(line_config,variant=SecamVariant.SECAM)
if sys.argv[3] == "eu":
 modem = SecamModem(line_config,variant=SecamVariant.SECAM_A)
if sys.argv[3] == "mo":
 modem = Pal3DModem(line_config,variant=PalVariant.PAL)
if sys.argv[3] == "in":
 modem = Pal3DModem(line_config,variant=PalVariant.PAL_M)
if sys.argv[3] == "so":
 modem = NtscModem(line_config,variant=NtscVariant.NTSC_I)
if sys.argv[3] == "mv":
 modem = NtscModem(line_config,variant=NtscVariant.NTSC)
if sys.argv[3] == "js":
 modem = NiirModem(line_config)
if sys.argv[3] == "ln":
 modem = MacModem(line_config,variant_or_width=720)
if sys.argv[3] == "ns":
 modem = SecamModem(line_config,variant=SecamVariant.SECAM_M)
if sys.argv[3] == "as":
 modem = NtscModem(line_config,variant=NtscVariant.NTSC443)
img_modem = ImageModem(modem)
tmp = sys.argv[2]
if sys.argv[4] == "mod":
 for n in range(1,int(sys.argv[1])+1):
  img = Image.open("%s/%s.png" %(tmp,n))
  img = img_modem.modulate(img,n)
  img.save("%s/%s_a.png" %(tmp,n))
if sys.argv[4] == "demod":
 for n in range(1,int(sys.argv[1])+1):
  img = Image.open("%s/%s.png" %(tmp,n))
  img = img_modem.demodulate(img,n+2)
  img.save("%s/%s_a.png" %(tmp,n))
if sys.argv[4] == "modem":
 for n in range(1,int(sys.argv[1])+1):
  img = Image.open("%s/%s.png" %(tmp,n))
  img = img_modem.modulate(img,n)
  img = img_modem.demodulate(img,n)
  img.save("%s/%s_a.png" %(tmp,n))
if sys.argv[4] == "multi":
 for n in range(1,int(sys.argv[1])+1):
  img = Image.open("%s/%s.png" %(tmp,n))
  img = img_modem.modulate(img,n)
  img.save("%s/%s_a.png" %(tmp,n))
  img = img_modem.demodulate(img,n)
  img.save("%s/%s_b.png" %(tmp,n))
