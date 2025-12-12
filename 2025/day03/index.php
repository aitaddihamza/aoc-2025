<?php

function partOne($filename)
{
  $fp = fopen($filename, 'r') or die('Failled to read the file ');
  $result = 0;

  while (($line = fgets($fp)) !== false) {
    $mx = $line[0];
    for ($i = 0; $i < strlen($line); $i++) {
      for ($j = $i + 1; $j < strlen($line); $j++) {
        $n = $line[$i] . $line[$j];
        if (intval($mx) < intval($n)) {
          $mx = $n;
        }
      }
    }
    $result += intval($mx);
  }

  return $result;
  fclose($fp);
}

echo partOne("input.txt");
echo PHP_EOL;
