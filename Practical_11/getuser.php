<!DOCTYPE html>
<html>
<head>
<style>
table {
    width: 100%;
    border-collapse: collapse;
}

table, td, th {
    border: 1px solid black;
    padding: 5px;
}

th {text-align: left;}
</style>
</head>
<body>

<?php
$q = intval($_GET['q']);

$con = mysqli_connect('localhost','root','','users');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

mysqli_select_db($con,"ajax_demo");
$sql="SELECT * FROM getuser WHERE id = '".$q."'";
$result = mysqli_query($con,$sql);

echo "<table>
<tr>
<th>Firstname</th>
<th>Lastname</th>
<th>Age</th>
<th>Date of Birth</th>
<th>Contact</th>
</tr>";
//$row = mysqli_fetch_array($result);
while($row = mysqli_fetch_array($result)) {
    echo "<tr>";
    echo "<td>" . $row['fname'] . "</td>";
    echo "<td>" . $row['lname'] . "</td>";
    echo "<td>" . $row['age'] . "</td>";
    echo "<td>" . $row['dob'] . "</td>";
    echo "<td>" . $row['contact'] . "</td>";
    echo "</tr>";
}
echo "</table>";
mysqli_close($con);
?>
</body>
</html>