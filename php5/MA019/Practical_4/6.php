<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form method="post" action="5.php">
	<table border="1">
		<tr><td>Enter Username</td>
			<td><input type="text" name="un">
		</tr>
		<tr>
			<td>Enter Password</td>
			<td><input type="Password" name="ps">
		</tr>
		<tr><td><button>Submit</button></td></tr>

	</body>
	</form>
	</table>
</body>
</html>
<?php
	$Username=$_POST["un"];
	$Password=$_POST["ps"];
	if($Username!="admin" && $Password!="abc123")
		echo "incorrect";
	else
		echo "welcome";
?>