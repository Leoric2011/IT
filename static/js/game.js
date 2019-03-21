function printRating(r) {
   			var x ="", i;
   			for (i=1; i<=r; i++) {
       			 x = x + "<i class='fas fa-star'></i> ";  
   			 }		
    		document.getElementById("rating").innerHTML = x;
}