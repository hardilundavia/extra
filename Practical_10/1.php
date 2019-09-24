<html>
<head>
	<title></title>
</head>
<body>
	<table border="2">
		<tr>
			<td>UserName</td>
			<td><input type="text" id="sugg" name="uname" onkeyup="myFunction(this.value)"></td>
		</tr>
	</table>
	<p id="sugg1"></p>
	<script type="text/javascript">
		function myFunction(str) 
		{
			if(str.length==0)
			{
				document.getElementById("sugg1").innerHTML="";
				return;
			}
			else
			{
				alert(str);
				var xmlhttp=new XMLHttpRequest();
				xmlhttp.onreadystatechange=function()
				{
					if(this.readyState==4 && this.status==200)
					{
						document.getElementById("sugg1").innerHTML=this.responseText;
					}
				};
				xmlhttp.open("GET","sugg.php?q="+str,true);
				xmlhttp.send();
			}
		}
	</script>
	
</body>
</html>