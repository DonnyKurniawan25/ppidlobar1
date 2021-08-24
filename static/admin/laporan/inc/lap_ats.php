<?php

error_reporting(E_ALL^E_NOTICE);
error_reporting(E_ALL ^ (E_NOTICE | E_WARNING));
session_start();
if (empty($_SESSION['userskpd']) AND empty($_SESSION['passw']) ){  

  ?>

	<script language="javascript">			
	document.location="log_skpd.php";			
	</script>

<?php

}
else{
$nama_admin= $_SESSION['nama_admin']; 
$username= $_SESSION['userskpd'];
$id_skpd = $_SESSION['skpd'];
}
?>