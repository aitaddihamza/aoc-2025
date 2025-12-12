<?php

function partOne($content)
{
  $ranges = explode(',', $content);
  $output = 0;
  foreach ($ranges as $rangeKey => $value) {
    $range = explode('-', $value);
    $start = intval($range[0]);
    $end = intval($range[1]);
    for ($i = $start; $i < $end + 1; $i++) {
      $str = strval($i);
      if (strlen($str) % 2 == 0) {
        if (substr($str, 0, intdiv(strlen($str), 2)) == substr($str, intdiv(strlen($str), 2))) {
          $output += $i;
        }
      }
    }
  }
  return $output;
}

function getFileContent($filePath)
{
  $fp = fopen($filePath, 'r') or die('Failled to read the file');
  $content = fread($fp, filesize($filePath));
  return $content;
  fclose($fp);
}


$filePath = 'exp.txt';
# echo partOne(getFileContent($filePath));


$fp = fopen($filePath, 'r') or die('Failled to open the file');

if ($fp) {
  while (($line = fgets($fp)) !== false) {
    echo $line . PHP_EOL;
  }

  if (!feof($fp)) {
    echo "Error fgets failled \n";
  }

  fclose($fp);
}




echo PHP_EOL;
