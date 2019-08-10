<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form method="GET" action="5.php">
	<table border="1">
		<tr><td>Enter number</td>
			<td><input type="text" name="text"><td><button>Submit</button></td></tr>
<?php
	if(isset($_GET['text']))
	{
		$number=$_GET['text'];
		$sum=0;
		$n=$number;
		while($n>0 || $sum>9)
		{
			if($n==0)
			{
				$n=$sum;
				$sum=0;
			}
			$sum=$sum+$n%10;
			$n=$n/10;
		}
		if($sum==1)
		{
			echo "the number ".$number." is Magic";
		}
		else
		{
			echo "the number ". $number ." is not Magic";
		}
	}
?>