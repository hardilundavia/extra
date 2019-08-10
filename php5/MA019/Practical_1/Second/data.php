<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<?php
	echo "Name:".$_GET['nm']."<br>";
	echo "Branch:".$_GET['br']."<br>";
	echo "Semester:".$_GET['rd']."<br>";
	echo "Roll no:".$_GET['rn']."<br>";
	echo "Email:".$_GET['em']."<br>";
	echo "Contact no:".$_GET['cn']."<br>";
	echo "Subjects : ";
	if(isset($_GET['sub1']))
		echo $_GET['sub1'];
	if(isset($_GET['sub2']))
		echo $_GET['sub2'];
	if(isset($_GET['sub3']))
		echo $_GET['sub3'];
	if(isset($_GET['sub4']))
		echo $_GET['sub4'];
	if(isset($_GET['sub5']))
		echo $_GET['sub5'];
	if(isset($_GET['sub6']))
		echo $_GET['sub6'];
	echo "Signature:".$_GET['sg']."<br>";
	echo "Experience:".$_GET['ex']."<br>";
?>
</body>
</html>