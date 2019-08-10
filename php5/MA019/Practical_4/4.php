<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form method="GET" action="4.php">
	<table border="1">
		<tr><td>Enter number</td>
			<td><input type="text" name="text"><td><button>Submit</button></td></tr>
<?php
	if(isset($_GET['text']))
	{
		$number=$_GET['text'];
		$sum=0;
		$n=$number;
		while($n!=0)
		{
			$rm=$n%10;
			$sum=$sum+$rm*$rm*$rm;
			$n=$n/10;
		}
		if($number==$sum)
		{
			echo "the number ".$number." is Armstrong";
		}
		else
		{
			echo "the number ". $number ." is not Armstrong";
		}
	}
?>
</table>
</form>
</body>
</html>