<?php
	$s1=array("rollno"=>19,"name"=>"Hari");
	$s2=array("rollno"=>19,"marks"=>64);
	//var_dump($s1);
	//var_dump($s2);
	$student=array_merge($s1,$s2);
	$student[3]=66;
	$student[4]=65;
	echo "<br>0 : ".$student['rollno'];
	echo "<br>1 : ".next($student);
	echo "<br>2 : ".next($student);
	echo "<br>3 : ".next($student);
	echo "<br>4 : ".next($student);
	extract($student,EXTR_PREFIX_SAME,"myrollno");
	echo"<br>";
	echo "\$myrollno = $rollno; \$myname = $name; \$mymarks = $marks; \$mymarks=$student[3]; \$mymarks=$student[4]";
?>