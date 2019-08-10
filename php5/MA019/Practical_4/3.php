<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form method="GET" action="3.php">
	<table border="1">
		<tr><td>Enter number</td>
			<td><input type="text" name="text"><td><button>Submit</button></td></tr>
<?php
	if(isset($_GET['text']))
	{
		$number=$_GET['text'];
		for($i=2;$i<$number-1;$i++)
		{
			if($number%$i==0)
			{
				break;
			}
		}
		if($number==$i)
		{
			echo "the number ".$number." is prime";
		}
		else
		{
			echo "the number ". $number ." is not prime";
		}

	}
?>
</table>
</form>
</body>
</html>