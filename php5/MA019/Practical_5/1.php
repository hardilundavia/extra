 <!DOCTYPE html>
<html>
<head>
	<h1>Student Form</h1>
</head>
<body>
<form method="post" action="d1.php" enctype="multipart/form-data">
<table border="1">
	<tr>
		<td><label>Exam no</label></td>
		<td><input type="text" name="en" size="40"></td>
	</tr>

	<tr>
		<td>Branch</td>
		<td>
			<select style="width:270px" name="br">
					<option>---Select Course---</option>
					<option>MCA</option>
					<option>BCA</option>
					<option>BBA</option>
					<option>MBA</option>
					<option>Engineering</option>
					<option>IT</option>
				</select>
		</td>
	</tr>	

	<tr>	
			<td>Student photo</td>
			<td><input type="file" name="sp"></td>
	</tr>

	<tr>
		<td>Semester</td>
		<td>
			<input type="radio" name="rd" value="1">1<br>
			<input type="radio" name="rd" value="2">2<br>
			<input type="radio" name="rd" value="3">3<br>
			<input type="radio" name="rd" value="4">4<br>
			<input type="radio" name="rd" value="5">5<br>
			<input type="radio" name="rd" value="6">6<br>
		</td>
	</tr>

	<tr>
			<td>Sub1_marks</td>
			<td><input type="text" name="s1" size="40"></td>
	</tr>

	<tr>
			<td>Sub2_marks</td>
			<td><input type="text" name="s2" size="40"></td>
	</tr>

	<tr>
			<td>Sub3_marks</td>
			<td><input type="text" name="s3" size="40"></td>
	</tr>

	<tr>
			<td>Sub4_marks</td>
			<td><input type="text" name="s4" size="40"></td>
	</tr>	

	<tr>
			<td>Sub5_marks</td>
			<td><input type="text" name="s5" size="40"></td>
	</tr>

	<tr>	
			<td align="center" colspan="2"><input value="submit" type="submit" name="submit"></td>
	</tr>

</table>
</form>
</body>
</html>