from . import color as smColor, artist as smArtist, supportSVG, supportCairo

# Color function:
colorRatio= smColor.colorRatio
rgbColor= smColor.rgbColor
percentColor= smColor.percentColor
webColor= smColor.webColor
colorFromWeb= smColor.colorFromWeb
color= smColor.color

# Support:
SupportVoid= smArtist.SupportVoid
SupportSVG= supportSVG.SupportSVG
SupportPNG= supportCairo.SupportPNG

Artist= smArtist.Artist
