<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form method="GET" action="1.php">
	<table border="1">
		<tr><td>Enter number</td>
			<td><input type="text" name="text"><td><button>Submit</button></td></tr>
<?php
	if(isset($_GET['text']))
	{
		$number=$_GET['text'];
		$r=strrev($number);
		if($r==$number)
		{
			echo "the number ".$number." is palindrome";
		}
		else
		{
			echo "the number ". $number ." is not palindrome";
		}
	}
?>
</table>
</form>
</body>
</html>
