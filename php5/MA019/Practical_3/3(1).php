<?php
	$browsers=array("firefox","Internet explorer","Opera");
	echo "<select>";
	foreach ($browsers as $browser) {
		echo "<option name='$browser'>$browser</option>"; 
	}
	echo "<select>";
?>