<!DOCTYPE html>
<html>
<head>
	<title>Student Result</title>
</head>
<body>
<?php

	
	if(isset($_POST['submit']))
	{	
	if(isset($_FILES['sp']) && $_FILES['sp']['error']==UPLOAD_ERR_OK)
	{
		$fileTmpPath = $_FILES['sp']['tmp_name'];
		$fileName = $_FILES['sp']['name'];
		$fileSize = $_FILES['sp']['size'];
		$fileType = $_FILES['sp']['type'];
		if($fileType!="image/jpeg")
		{
			echo "File must be jpeg format and must be 25kb size";
		}
		else
		{
			$namef=explode(".",$fileName);
			$filetext=strtolower(end($namef));
			$newfile=$_POST['en'].".".$filetext;
			$dest="C:/xampp/htdocs/MA019/Practical_5/img/".$newfile;
			move_uploaded_file($fileTmpPath, $dest);
			$sum=$_POST['s1']+$_POST['s2']+$_POST['s3']+$_POST['s4']+$_POST['s5'];
			$per=$sum/5;
			echo "<table border='1'>
					<tr>
						<td>Exam no</td>
						<td>".$_POST['en']."</td>
					</tr>

					<tr>
						<td>Branch</td>
						<td>".$_POST['br']."</td>
					</tr>
					<tr>
						<td>Student photo</td>
						<td><img src='$dest' width=100px height=100px></td>
					</tr>	
					<tr>
						<td>Semester</td>
						<td>".$_POST['rd']."</td>
					</tr>
					<tr>
						<td>Sub1_marks</td>
						<td>".$_POST['s1']."</td>
					</tr>
					<tr>
						<td>Sub2_marks</td>
						<td>".$_POST['s2']."</td>
					</tr>
					<tr>
						<td>Sub3_marks</td>
						<td>".$_POST['s3']."</td>
					</tr>
					<tr>
						<td>Sub4_marks</td>
						<td>".$_POST['s4']."</td>
					</tr>
					<tr>
						<td>Sub5_marks</td>
						<td>".$_POST['s5']."</td>
					</tr>
					<tr>
					<td>Total</td>
					<td>".$sum."</td></tr>
					<tr>
					<td>Percentage</td>
					<td>".$per."</td>
					</tr>
					<tr>
					<td>Result</td>
					<td>";if($per>35)
					{
						echo "Pass";
					}
					else
					{
						echo "Fail";
					}echo "</td></tr>
					<tr>
					<td>class</td>
					<td>";if($per>=70)
					{
						echo "first";
					}
					elseif ($per>=50 && $per<70) {
						echo "Second";
					}
					else{
						echo "Fail";
					}echo "</td></tr></table>";
		}
	}
	}
?>
</body>
</html>