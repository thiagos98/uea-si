<?php
    const CONST_SIZE = 100;
    const CONST_PROB = 5;

    $target = $_POST["target"];
    $alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ";

    function randomChr() {
        $alphabet = $GLOBALS['alphabet'];
        return $alphabet[rand(0,26)];
    }

    function randomStr() {
        $target = $GLOBALS['target'];
        $randomStr = '';
        for ($i=0; $i < strlen($target); $i++) {
            $randomStr = $randomStr . randomChr();
        }
        return $randomStr;
    }

    function compareStr($randomStr){
        $target = $GLOBALS['target'];
        $randomStrIndex = 0;
        for ($i=0; $i < strlen($target); $i++) {
            if($target[$i] == $randomStr[$i]){
                $randomStrIndex++;
            }
        }
        return $randomStrIndex;
    }

    function modRandomStr($randomStr){
        $target = $GLOBALS['target'];
        $newRandomStr = $randomStr;
        for ($i=0; $i < strlen($target); $i++) {
            $randomInt = rand(1,100);
            if($randomInt <= CONST_PROB){
                $newRandomStr = substr($newRandomStr, 0, $i) . randomChr() . substr($newRandomStr, ($i + 1));
            }
        }
        return $newRandomStr;
    }
/*
    $randStr = randomStr();
    echo modRandomStr($randStr);
*/
    $loopNumber = 0;
    $strFound = false;
    $randStr = randomStr();
    $resultList = [];
    while(!$strFound){
        for ($i=0; $i < CONST_SIZE; $i++) {
            // code...
            $strList[$i] = '';
            $indexList[$i] = 0;
            //echo $i . "<br>";
        }
        for ($i=0; $i < CONST_SIZE; $i++) {
            $strList[$i] = modRandomStr($randStr);
            $indexList[$i] = compareStr($strList[$i]);
        }
        $maxIndex = max($indexList);
        //echo $maxIndex . "<br>";
        if($maxIndex == strlen($target)){
            $strFound = true;
        }
        $index = $indexList[$maxIndex];
        $randStr = $strList[$index];
        //echo($loopNumber . ": " . $randStr . " -- Score: ". $maxIndex . "<br>");
        $loopNumber++;
    }
 ?>
