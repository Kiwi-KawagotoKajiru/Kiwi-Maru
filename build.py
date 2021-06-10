from fontmake import __main__
from fontTools.ttLib import TTFont, newTable
import shutil, glob
import subprocess
from pathlib import Path

__main__.main(("-g","sources/KiwiMaru-Light.glyphs", "-o","ttf",))
__main__.main(("-g","sources/KiwiMaru-Medium.glyphs", "-o","ttf",))
__main__.main(("-g","sources/KiwiMaru-Regular.glyphs", "-o","ttf",))

path = Path("master_ttf")

def GASP_set(font:TTFont):
    if "gasp" not in font:
        font["gasp"] = newTable("gasp")
        font["gasp"].gaspRange = {}
    if font["gasp"].gaspRange != {65535: 0x000A}:
        font["gasp"].gaspRange = {65535: 0x000A}

for font in path.glob("*.ttf"):
    modifiedFont = TTFont(font)
    print ("["+str(font).split("/")[1][:-4]+"]Adding additional bits")
    modifiedFont["DSIG"] = newTable("DSIG")     #need that stub dsig
    modifiedFont["DSIG"].ulVersion = 1
    modifiedFont["DSIG"].usFlag = 0
    modifiedFont["DSIG"].usNumSigs = 0
    modifiedFont["DSIG"].signatureRecords = []
    modifiedFont["head"].flags |= 1 << 3        #sets flag to always round PPEM to integer

    if "Light" in str(font):
        modifiedFont["name"].addMultilingualName({'ja':'キウイ 丸'}, modifiedFont, nameID = 1, windows=True, mac=False)
        modifiedFont["OS/2"].usWeightClass = 300
    elif "Regular" in str(font):
        modifiedFont["name"].addMultilingualName({'ja':'キウイ 丸'}, modifiedFont, nameID = 1, windows=True, mac=False)
    elif "Medium" in str(font):
        modifiedFont["name"].addMultilingualName({'ja':'キウイ 丸'}, modifiedFont, nameID = 1, windows=True, mac=False)
        modifiedFont["OS/2"].usWeightClass = 500

    GASP_set(modifiedFont)
    modifiedFont.save("fonts/ttf/"+str(font).split("/")[1])

shutil.rmtree("instance_ufo")
shutil.rmtree("master_ufo")
shutil.rmtree("master_ttf")