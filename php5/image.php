<html>
<body>
<form action="<?php $_SERVER['PHP_SELF'];?>" method="post" enctype="multipart/form-data">
    	Select image to upload:<input type="file" name="fileToUpload" id="fileToUpload">
    						   <input type="submit" value="Upload Image" name="submit">
 </form>
</body>
</html>
<?php
	$image="C:/xampp/htdocs/practical5";
	$target_file=$image.basename($_FILES["fileToUpload"]["name"]);
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
	if($imageFileType!="png") 
	{
    	echo "Sorry, only PNG files are allowed.";
    	echo "<br>";
    	$uploadOk=0;
	}
	else
	{
		echo "Your file uploaded successfully";
		echo "<br>";
		$uploadOk=1;
	}
?>