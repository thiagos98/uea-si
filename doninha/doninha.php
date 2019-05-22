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

    function getIndex($indexList, $maxIndex){
        $index = 0;
        for ($i=0; $i < count($indexList); $i++) {
            // code...
            if ($indexList[$i] == $maxIndex) {
                $index = $i;
            }
        }
        return $index;
    }

    $loopNumber = 0;
    $strFound = false;
    $randStr = randomStr();
    $resultList = [];
    while(!$strFound){
        $strList = [];
        $indexList = [];
        for ($i=0; $i < CONST_SIZE; $i++) {
            // code...
            $strList[$i] = '';
            $indexList[$i] = NULL;
        }
        for ($i=0; $i < CONST_SIZE; $i++) {
            $strList[$i] = modRandomStr($randStr);
            $indexList[$i] = compareStr($strList[$i]);
        }
        $maxIndex = max($indexList);
        if($maxIndex == strlen($target)){
            $strFound = true;
        }
        //$index = $indexList[$maxIndex];
        $index = getIndex($indexList, $maxIndex);
        $randStr = $strList[$index];
        //echo($loopNumber . ": " . $randStr . " -- Score: ". $maxIndex . "<br>");
        for ($i=0; $i < $loopNumber; $i++) { 
            $resultList[$i] = $loopNumber . ": " . $randStr . " -- Score: ". $maxIndex . "<br>";
        }
        $loopNumber++;
    }

 ?>
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    <div class="container">
        <div class="row">
            <table>
                <tr>
                    <th>Score</th>
                    <th>String</th>
                    <th>Generation</th>
                </tr>
                <tr>
                    <?php
                        
                        for ($i=0; $i < count($resultList); $i++) { 
                             # code...
                            echo "<td>" . $resultList[$i] . "</td>";
                         }  
                    ?>
                </tr>
            </table>
        </div>
    </div>
</body>
</html>