<h2 id="headings"> Data Permintaan DIP </h2>
<hr>
<p class='pull-right'>
	<a href='../export/perminskpd_xls.php'
	target='_blank'
	class="btn" ><i class='icon-download-alt'></i> Excel</a>
	<!--
    <a href='../export/ppid_pdf.php?cetak=skpdpdf '
	target='_blank'
	class="btn" ><i class='icon-download-alt'></i> PDF</a>
	<a href='../export/ppid_cetak.php?cetak=skpd'
	target='_blank'
	class="btn" ><i class='icon-print'></i>cetak</a>
    -->
</p>
<table  class="table  table-condensed table-hover">
	<thead>
		<th><td><b>Nomer Tiket </b></td><td><b>Nama </b></td><td><b>Kota </b></td><td><b>Judul DIP </b></td><td><b>Keperluan </b></td><td class='pull-right'><b>Tanggal </b></td></th>
	</thead>
	<tbody>
		


<?php
include "../inc/lap_ats.php";
include "../inc/tgl.php";
include "../inc/config.php";
$query="select * from add_data, user_ppid where add_data.id_user = user_ppid.id_user  ";
$result=mysql_query($query) or die(mysql_error());
$no=1;
//proses menampilkan data
while($rows=mysql_fetch_array($result)){

		?>
		<tr>
			</td><td><?		echo $rows -> no;?></td>
            <td><?		echo $rows['tiket'];?></td>
			<td><?		echo $rows['nama'];?></td>
			<td><?		echo $rows['kota'];?></td>

			<td><?		echo $rows['judul_data'];?></td>
            <td><?		echo $rows['keperluan'];?></td>
			<td ><p class='pull-right'><?	echo "".tgl_indo($rows['tgl'])."";?></td>
		</tr>
		<?
}


?>

	</tbody>
</table>
