<html>
<body>
	<h1><b><u>EXAMINATION RESULT</u></b></h1>
	<form id="form1" name="form1" method="POST" action="<?php $_SERVER['PHP_SELF'];?>">
		Enter Examination No. : <label><input type="text" name="exno"></label>
		<br>
		<br>
		Enter Student Name : <label><input type="text" name="name"></label>
		<br>
		<br>
	<form action="upload.php" method="post" enctype="multipart/form-data">
    	Select image to upload:<input type="file" name="fileToUpload" id="fileToUpload">
    	<br>
    	<br>
		Enter Your course : <label><select name="course">
										<option>MCA</option>
										<option>BCA</option>
										<option>MSc</option>
										<option>BE</option>
										<option>BTech</option>
										<option>Diploma</option>
							</select></label>
		<br>
		<br>
		Enter Semester : <label><select name="sem">
										<option>1</option>
										<option>2</option>
										<option>3</option>
										<option>4</option>
										<option>5</option>
										<option>6</option>
										<option>7</option>
										<option>8</option>
							</select></label>
		<br>
		<br>
		Enter Subject 1 Marks : <label><input type="text" name="m1"></label>
		<br>
		<br>
		Enter Subject 2 Marks : <label><input type="text" name="m2"></label>
		<br>
		<br>
		Enter Subject 3 Marks : <label><input type="text" name="m3"></label>
		<br>
		<br>
		Enter Subject 4 Marks : <label><input type="text" name="m4"></label>
		<br>
		<br>
		Enter Subject 5 Marks : <label><input type="text" name="m5"></label>
		<br>
		<br>
		<label><input type="Submit" name="Submit" value="Submit"></label>
		<br>
		<br>
	</form>
</body>
</html>
<?php
	$examno=$_POST[ "exno"];
	$sname=$_POST[ "name"];
	$scourse=$_POST[ "course"];
	$semester=$_POST[ "sem"];
	$mark1=$_POST[ "m1"];
	$mark2=$_POST[ "m2"];
	$mark3=$_POST[ "m3"];
	$mark4=$_POST[ "m4"];
	$mark5=$_POST[ "m5"];
	$image="C:/xampp/htdocs/practical5";
	$target_file=$image.basename($_FILES["file"]["name"]);
	$flag=1;
	$imageFileType=strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
	if(isset($_POST["submit"]))
	{
		$check=getimagesize($_FILES["fileToUpload"]["tmp_name"]);
		if($check!==false)
		{
			echo "File is an image-".$check["mime"].".";
			echo "<br>";
			$flag=1;
		}
		else
		{
			echo "File is not an image.";
			echo "<br>";
		}
	}
   	if($_FILES["fileToUpload"]["size"] > 25000)
   	{
    	echo "Sorry, your file is too large.";
    	echo "<br>";
    	$uploadOk=0;
	}
	if($imageFileType!="jpeg") 
	{
    	echo "Sorry, only JPEG files are allowed.";
    	echo "<br>";
    	$uploadOk=0;
	}
	else
	{
		echo "Your file uploaded successfully";
		echo "<br>";
		$uploadOk=1;
	}
	if($_POST)
	{
		echo "Exam No. : $examno";
		echo "<br>";
		echo "Student Name : $sname";
		echo "<br>";
		echo "Student's Course : $scourse";
		echo "<br>";
		echo "Semester : $semester";
		echo "<br>";
		echo "Subject 1 Marks : $mark1";
		echo "<br>";
		echo "Subject 2 Marks : $mark2";
		echo "<br>";
		echo "Subject 3 Marks : $mark3";
		echo "<br>";
		echo "Subject 4 Marks : $mark4";
		echo "<br>";
		echo "Subject 5 Marks : $mark5";
		echo "<br>";
		$total=$mark1+$mark2+$mark3+$mark4+$mark5;
		$per=$total/5;
		echo "Total Marks : $total";
		echo "<br>";
		echo "Percentage : $per";
		echo "<br>";
		if($per>=70)
		{
			echo "Result : PASS";
			echo "<br>";
			echo "Grade : Distinction";
		}
		else if($per>=60)
		{
			echo "Result : PASS";
			echo "<br>";
			echo "Grade : First Class";
		}
		else if($per>=50)
		{
			echo "Result : PASS";
			echo "<br>";
			echo "Grade : Second Class";
		}
		else if($per>=40)
		{
			echo "Result : PASS";
			echo "<br>";
			echo "Grade : Third Class";
		}
		else
		{
			echo "Result : FAIL";
		}
	}
?>