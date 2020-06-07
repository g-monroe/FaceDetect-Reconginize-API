<?php
//error_reporting(E_ALL);
//ini_set("display_errors", 1);
header('Content-Type: application/json');
//if ($_SERVER['SERVER_ADDR'] != $_SERVER['REMOTE_ADDR']){
//    header("HTTP/1.1 401 Unauthorized");
//    echo(json_encode(['status' => '401', 'info' =>"No remote access allowed."]));
//    exit; //just for good measure
//}
$path = 'python/temp/';
$name = rand(1,9999999999);
$name2 = rand(1,9999999999);

function checkType($input){
    if($input != "jpg" && $input != "png" && $input != "jpeg") {
        return false;
    }else{
        return true;
    }
}
if (isset($_FILES['image']) && isset($_FILES['image2'])){
    $imageExt = strtolower(pathinfo(basename($_FILES["image"]["name"]),PATHINFO_EXTENSION));
    $image2Ext = strtolower(pathinfo(basename($_FILES["image2"]["name"]),PATHINFO_EXTENSION));
    $check = getimagesize($_FILES["image"]["tmp_name"]);
    $check2 = getimagesize($_FILES["image2"]["tmp_name"]);
    if($check !== false && $check2 !== false && checkType($imageExt) !== false && checkType($image2Ext) !== false) {
        $imagePath = $path.$name.".".$imageExt;
        $image2Path = $path.$name2.".".$image2Ext;
        if (move_uploaded_file($_FILES["image"]["tmp_name"], $imagePath) && move_uploaded_file($_FILES["image2"]["tmp_name"], $image2Path)){
            echo(json_encode(json_decode(shell_exec("exec python3.6 python/recognize.py -i ".$imagePath." -c ".$image2Path))));
            //unlink($imagePath);
            //unlink($image2Path);
        }
    }else{
        header("HTTP/1.1 401 Unauthorized");
        echo(json_encode(['status' => '400', 'info' =>"Input didn't classify as images or supported image types."]));
        exit;
    }
}else{
    header("HTTP/1.1 401 Unauthorized");
    echo(json_encode(['status' => '401', 'info' =>"Didn't meet all required parameters!"]));
    exit;
}
