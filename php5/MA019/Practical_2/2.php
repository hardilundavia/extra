<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<table border="1">
	<tr>Value-------->Type<br>
		<td><?php
				echo "True";
			?> 
	<td>	
		<?php
			$myVar=True;
			echo gettype($myVar);
		?><br>
	</td>
	</tr>

	<tr>
		<td><?php
				echo "9";
			?> 
	<td>	
		<?php
			$myVar=9;
			echo gettype($myVar);
		?><br>
	</td>
	</tr>

	<tr>
		<td><?php
				echo "7.8";
			?> 
	<td>	
		<?php
			$myVar=7.8;
			echo gettype($myVar);
		?><br>
	</td>
	</tr>

	<tr>
		<td><?php
				echo "Hello123";
			?> 
	<td>	
		<?php
			$myVar="Hello123";
			echo gettype($myVar);
		?><br>
	</td>
	</tr>

	<tr>
		<td><?php
				echo "Array(1,2,3)";
			?> 
	<td>	
		<?php
			$myVar=array(1,2,3);
			echo gettype($myVar);
		?><br>
	</td>
	</tr>

	<tr>
		<td><?php
				echo "NULL";
			?> 
	<td>	
		<?php
			$myVar=NULL;
			echo gettype($myVar);
		?><br>
	</td>
	</tr>

	<tr>
		<td><?php
				echo "tmpfile()";
			?> 
	<td>	
		<?php
			$myVar=tmpfile();
			echo gettype($myVar);
		?><br>
	</td>
	</tr>

</table>
</body>
</html>