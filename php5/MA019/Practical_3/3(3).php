<?php
	echo "<table width='100' align='center'>"; 
	for($i=0; $i<=5; $i=$i+1) 
	{
		if($i % 2 == 0)   
			{    
				echo "<tr>";    
				echo "<td style='background-color:red'>";    
				echo $i;    
				echo "</td>";    
				echo "</tr>";   
			}
		else   
			{    
				echo "<tr>";    
				echo "<td style='background-color:green'>";    
				echo $i;    
				echo "</td>";    
				echo "</tr>";   
			}   
	}
	echo "</table>"; 
?>