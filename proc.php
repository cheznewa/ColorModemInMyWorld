<?php
set_time_limit(0);
$tmp = exec("mktemp -d");
// $uploadfile = $tmp."/".$_FILES["userfile"]["name"];
if (!move_uploaded_file($_FILES["userfile"]["tmp_name"],$tmp."/video"))
{
echo "I'm Sorry";
}
$country = $_POST["country"];
$mode = $_POST["mode"];
exec("ffmpeg -i ".$tmp."/video -vf framerate=".$_POST["framerate"].",scale=720x576 ".$tmp."/%d.png ".$tmp."/a.wav");
$frame = count(scandir($tmp))-2;
exec("python3 procpy.py ".$frame." ".$tmp." ".$country." ".$mode);

if ("multi" == $mode)
{
exec("ffmpeg -r ".$_POST["framerate"]." -i ".$tmp."/%d_b.png -r 24 -i ".$tmp."/%d_a.png -i ".$tmp."/a.wav -vcodec png -acodec copy -map 0 -map 1 -map 2 -f avi ".$tmp."/videodone.avi");
}
else
{
exec("ffmpeg -r ".$_POST["framerate"]." -i ".$tmp."/%d_a.png -i ".$tmp."/a.wav -vcodec png -f avi ".$tmp."/videodone.avi");
}
header("Content-Description: File Transfer"); 
header("Content-Type: application/octet-stream"); 
header("Content-Disposition: attachment; filename=\"".$_FILES["userfile"]["name"]."_".$country.".avi\"");
readfile($tmp."/videodone.avi");
