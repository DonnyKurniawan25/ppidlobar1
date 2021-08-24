<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Laporan PPID </title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="description" content="">
		<meta name="author" content="">
		<!-- Le styles -->
		<link href="assets/css/bootstrap.css" rel="stylesheet">
		<style type="text/css">	body {
				padding-top: 60px;
				padding-bottom: 40px;
			}
			.sidebar-nav {
				padding: 9px 0;
			}
</style>
		<link href="assets/css/bootstrap-responsive.css" rel="stylesheet">
		<!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
		<!--[if lt IE 9]>
		<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
		<![endif]-->
		<!-- Le fav and touch icons -->
		<script type="text/javascript" src="assets/js/jquery.js"></script>
	</head>
	<body>
		<div class="navbar navbar-inverse navbar-fixed-top">
			<div class="navbar-inner" align="center"><a href="../mn_skpd.php">Kembali Ke Menu ADMIN SKPD</a></div>
		</div>
		<div class="container-fluid">
			<div class="row">
				<div class="span8 offset2">
					<div>

<h2 id="headings"> Data DIP </h2>
<hr>
<p class='pull-right'>
	<a href='export/ppidskpd_xls.php'
	target='_blank'
	class="btn" ><i class='icon-download-alt'></i> Excel</a>
	<a href='export/ppid_pdf.php?cetak=skpdpdf '
	target='_blank'
	class="btn" ><i class='icon-download-alt'></i> PDF</a>
	<a href='export/ppid_cetak.php?cetak=skpd'
	target='_blank'
	class="btn" ><i class='icon-print'></i>cetak</a>
</p>
<table  class="table  table-condensed table-hover">
	<thead>
		<th><td><b>Kode DIP </b></td><td><b>Judul DIP </b></td><td class='pull-right'><b>Tanggal Upload </b></td></th>
	</thead>
	<tbody>
		


<?php
include "inc/lap_ats.php";
include "inc/tgl.php";
include "inc/config.php";
$query="select * from data_ppid where id_dinas = $_SESSION[skpd] ";
$result=mysql_query($query) or die(mysql_error());
$no=1;
//proses menampilkan data
while($rows=mysql_fetch_array($result)){

		?>
		<tr>
			</td><td><?		echo $rows -> no;?></td>
            <td><?		echo $rows['kode_ppid'];?></td>
			<td><?		echo $rows['judul_ppid'];?></td>
			<td ><p class='pull-right'><?	echo "".tgl_indo($rows['tgl'])."";?></td>
		</tr>
		<?
}


?>

	</tbody>
</table>
</div><!--/span-->
				</div><!--/row-->
			</div>
			<footer>
				<p style="text-align: center">
					&copy;PPID Lombok Barat
				</p>
			</footer>
		</div><!--/.fluid-container-->
	</body>
</html>
