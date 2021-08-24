<?php

error_reporting(E_ALL);

		

include "../inc/lap_ats.php";
require_once '../plugins/excel/PHPExcel.php';
require_once '../inc/config.php';

// Create new PHPExcel object
$objPHPExcel = new PHPExcel();


$query="select * from add_data, user_ppid where add_data.id_user = user_ppid.id_user AND add_data.id_skpd = $_SESSION[skpd]";
$hasil = mysql_query($query);
 
// Set properties
$objPHPExcel->getProperties()->setCreator("PPID Lombok Barat")
      ->setLastModifiedBy("PPID Lombok Barat")
      ->setTitle("Office 2007 XLSX PPID Document")
      ->setSubject("Office 2007 XLSX PPID Document")
       ->setDescription("Laporan DIP .")
       ->setKeywords("office 2007 openxml php")
       ->setCategory("DIP Lombok Barat");
 
// Add some data
$objPHPExcel->setActiveSheetIndex(0)
       ->setCellValue('A1', 'No')
	   ->setCellValue('B1', 'No. Tiket')
	   ->setCellValue('C1', 'Nama')
	   ->setCellValue('D1', 'Kota')
       ->setCellValue('E1', 'Judul DIP')
	   ->setCellValue('F1', 'Keperluan')
       ->setCellValue('G1', 'Tanggal');
 
$baris = 2;
$no = 0;			
while($row=mysql_fetch_array($hasil)){
$no = $no + 1;
$objPHPExcel->setActiveSheetIndex(0)
     ->setCellValue("A$baris", $no)
     ->setCellValue("B$baris", $row['tiket'])
	 ->setCellValue("C$baris", $row['nama'])
     ->setCellValue("D$baris", $row['kota'])
     ->setCellValue("E$baris", $row['judul_data'])
	 ->setCellValue("F$baris", $row['keperluan'])
     ->setCellValue("G$baris", $row['tgl']);
$baris = $baris + 1;
}
 
// Rename sheet
$objPHPExcel->getActiveSheet()->setTitle('DIP');
 
// Set active sheet index to the first sheet, so Excel opens this as the first sheet
$objPHPExcel->setActiveSheetIndex(0);
 
// Redirect output to a client’s web browser (Excel5)
header('Content-Type: application/vnd.ms-excel');

$query="select * from data_ppid ";
$hasil = mysql_query($query);
while($row=mysql_fetch_array($hasil)){
header('Content-Disposition: attachment;filename= LaporanPPID.xls');
}
header('Cache-Control: max-age=0');
 
$objWriter = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$objWriter->save('php://output');
exit;

?>
 