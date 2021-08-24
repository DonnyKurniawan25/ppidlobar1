<h2 id="headings"> Data DIP </h2>
<hr>
<p class='pull-right'>
	<a href='export/ppid_xls.php'
	target='_blank'
	class="btn" ><i class='icon-download-alt'></i> Excel</a>
	<a href='export/ppid_pdf.php '
	target='_blank'
	class="btn" ><i class='icon-download-alt'></i> PDF</a>
	<a href='export/ppid_cetak.php'
	target='_blank'
	class="btn" ><i class='icon-print'></i>cetak</a>
</p>
<table  class="table  table-condensed table-hover">
	<thead>
		<th><td><b>Judul DIP </b></td><td class='pull-right'><b>Tanggal Upload </b></td></th>
	</thead>
	<tbody>
		<?php
include "../inc/config.php";
$query="select * from data_ppid";
$result=mysql_query($query) or die(mysql_error());
$no=1;
//proses menampilkan data
while($rows=mysql_fetch_object($result)){

		?>
		<tr>
			</td><td><?		echo $rows -> no;?></td>
			<td><?		echo $rows -> judul_ppid;?></td>
			<td ><p class='pull-right'><?	echo $rows -> tgl;?></td>
		</tr>
		<?
}?>
	</tbody>
</table>
