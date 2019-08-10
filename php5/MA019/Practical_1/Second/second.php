<!DOCTYPE html>
<html>
<head>
	<h1>Cultural Fair</h1>
</head>
<body>
<form method="get" action="data.php">
<table border="1">
	<tr>
		<td><label>Name</label></td>
		<td><input type="text" name="nm" size="40"></td>
	</tr>

	<tr>
		<td>Branch</td>
		<td>
			<select style="width:270px" name="br">
					<option>---Select Branch---</option>
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
			<td>Rollno</td>
			<td><input type="text" name="rn" size="40"></td>
	</tr>

	<tr>
			<td>Email id</td>
			<td><input type="text" name="em" size="40"></td>
	</tr>

	<tr>
			<td>ContactNo</td>
			<td><input type="text" name="cn" size="40"></td>
	</tr>

	<tr>
			<td>Subjects</td>
			<td>
				<input type="checkbox" name="sub1" value="Cultural,">Cultural<br>
				<input type="checkbox" name="sub2" value="Web Publishing,">Web Publishing<br>
				<input type="checkbox" name="sub3" value="Technical,">Technical<br>
				<input type="checkbox" name="sub4" value="Finance,">Finance<br>
				<input type="checkbox" name="sub5" value="Publication,">Publication<br>
				<input type="checkbox" name="sub6" value="Reception and Hosting,">Reception and Hosting<br>
			</td>	
	</tr>

	<tr>	
			<td>Signature</td>
			<td><input type="file" name="sg"></td>
	</tr>

	<tr>	
			<td>Experience</td>
			<td><input type="text" name="ex" size="40"></td>
	</tr>

	<tr>	
			<td align="center" colspan="2"><button>Submit</button></td>
	</tr>

</table>
</form>
</body>
</html>