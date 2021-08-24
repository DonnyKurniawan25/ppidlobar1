<?php

error_reporting(E_ALL);

require_once '../plugins/excel/PHPExcel.php';
require_once '../inc/config.php';
// Create new PHPExcel object
$objPHPExcel = new PHPExcel();


$query="select * from data_ppid ";
$hasil = mysql_query($query);
 
// Set properties
$objPHPExcel->getProperties()->setCreator("PPID Lombok Barat")
      ->setLastModifiedBy("PPID Lombok Barat")
      ->setTitle("Office 2007 XLSX Test Document")
      ->setSubject("Office 2007 XLSX Test Document")
       ->setDescription("Laporan DIP .")
       ->setKeywords("office 2007 openxml php")
       ->setCategory("DIP Lombok Barat");
 
// Add some data
$objPHPExcel->setActiveSheetIndex(0)
       ->setCellValue('A1', 'No')
	   ->setCellValue('B1', 'Kode DIP')
       ->setCellValue('C1', 'Judul DIP')
       ->setCellValue('D1', 'Tanggal');
 
$baris = 2;
$no = 0;			
while($row=mysql_fetch_array($hasil)){
$no = $no + 1;
$objPHPExcel->setActiveSheetIndex(0)
     ->setCellValue("A$baris", $no)
     ->setCellValue("B$baris", $row['kode_ppid'])
     ->setCellValue("C$baris", $row['judul_ppid'])
     ->setCellValue("D$baris", $row['tgl']);
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
 