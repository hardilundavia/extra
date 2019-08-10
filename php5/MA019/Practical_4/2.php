<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form method="GET" action="2.php">
	<table border="1">
		<tr><td>Enter number</td>
			<td><input type="text" name="text"><td><button>Submit</button></td></tr>
<?php
	if(isset($_GET['text']))
	{
		$number=$_GET['text'];
		$sum=0;
		$i=1;
		while($i<$number)
		{
			if($number%$i==0)
			{
				$sum=$sum+$i;
			}
			$i++;	
		}
		if($number==$sum)
		{
			echo "the number ".$number." is perfect";
		}
		else
		{
			echo "the number ". $number ." is not perfect";
		}
	}
?>
</table>
</form>
</body>
</html>