<?php
$cetak=$_GET['cetak'];
if($cetak=='skpd'){
		
			require ('../inc/config.php');
			include "../inc/lap_ats.php";
			include "../inc/tgl.php";

			$query = "select * from data_ppid where id_dinas = $_SESSION[skpd] ";
			$result = mysql_query($query) or die(mysql_error());
			$no = 1;?>
<html>
	<head>
		<link href="../assets/css/bootstrap.css" rel="stylesheet">
		<style type="text/css">		body {
				padding-top: 20px;
				padding-bottom: 40px;
				font-size: 0.7em;
			}
</style>
	</head>
	<body>
		<div class='span8  offset2'>
           <?php
                $tampil=mysql_query("select * from dinas where id_dinas = $_SESSION[skpd] ");
while($dt=mysql_fetch_array($tampil)){
	?>
			<h3 style='text-align: center'> Daftar Informasi Publik <br> <?php echo"$dt[dinas] "; }?> </h3>
			<hr>
			<table  class="table  table-condensed table-hover">
				<thead>
             
					<th><td><b>Kode DIP </b></td><td><b>Judul DIP </b></td><td class='pull-right'><b>Tanggal Upload </b></td></th>
				</thead>
				<tbody>
					<?php
$query="select * from data_ppid where id_dinas = $_SESSION[skpd]";
$result=mysql_query($query) or die(mysql_error());
$no=0;
//proses menampilkan data
while($rows=mysql_fetch_array($result)){
	$no++;
					?>
					<tr>
						</td><td><?		echo $no;?></td>
                        <td><?		echo $rows['kode_ppid'];?></td>
						<td><?		echo $rows['judul_ppid'];?></td>
						<td ><p class='pull-right'><?	echo "".tgl_indo($rows['tgl'])."";?></p></td>
					</tr>
					<?
}
}?>
				</tbody>
			</table>
			<p align='center'>
		<a href="ppid_cetak.php" cls='btn' onClick="window.print();return false"> <i class='icon-print'></i>Cetak </a>
			</p>
		</div>
	</body>
</html>
