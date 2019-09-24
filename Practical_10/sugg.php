<?php
if(isset($_REQUEST['q']))
{
	$a[]="Hari";
	$a[]="Hardil";
	$a[]="Harsh";
	$a[]="Aarav";
	$a[]="Aman";
	$a[]="Bhargav";
	$a[]="Bhoomit";
	$a[]="Kavil";
	$a[]="Poojan";
	$a[]="Digvijay";

	$q=$_REQUEST["q"];
	$sugg="";
	//echo $q;
	foreach ($a as $name)
	{ 	
	 	if(substr(strtolower($name),0,strlen($q)) == $q)
	 		$sugg=$sugg.$name."<br>";
	 } 
	echo "No Suggestions Found ".$sugg;
}
?>