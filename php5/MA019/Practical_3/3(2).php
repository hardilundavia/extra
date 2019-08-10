<?php 

$articles = array 
( 
	 "PHP Variables" => "A variable is a mean to store values   
	 such as strings or integers so we can easily   
	 reuse those values in our code...", 

	  "PHP Strings" => "A string is a sequence of letters, symbols,   
	  characters and arithmetic values...", 

	   "PHP Loops" => "In programming, we often repeat an action or a   
	   piece of code a number of times using loops   
	   to solve a problem..." 
);

echo "<table border='1'>"; 

foreach ($articles as $article_title => $article_body) {
 	
 	echo "<tr>";  
 	echo "<td>";
 	echo $article_title;  
 	echo "</td>"; 

 	echo "<td>";  
 	echo $article_body;  
 	echo "</td>";  
 	echo "</tr>";  
 } 
 echo "</table>"; 
 ?>