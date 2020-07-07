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
exec("ffmpeg -i ".$tmp."/video -vf framerate=25,scale=720x576 ".$tmp."/%d.png ".$tmp."/a.wav");
$frame = count(scandir($tmp))-2;
exec("python3 procpy.py ".$frame." ".$tmp." ".$country." ".$mode);

if ("multi" == $mode)
{
exec("ffmpeg -i ".$tmp."/%d_b.png -i ".$tmp."/%d_a.png -i ".$tmp."/a.wav -vcodec libx264 -map 0 -map 1 -map 2 -f avi ".$tmp."videodone.avi");
}
else
{
exec("ffmpeg -i ".$tmp."/%d_a.png -i ".$tmp."/a.wav -vcodec libx264 -f avi ".$tmp."videodone.avi");
}
header("Content-Description: File Transfer"); 
header("Content-Type: application/octet-stream"); 
header("Content-Disposition: attachment; filename=\"videodone.avi\"");
readfile($tmp."videodone.avi");