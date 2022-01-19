product_id_list=[];
$(document).ready(function(){
$(document).on("click",".search_button",function(){
	search_text=$(this).parent().find("input").val();
	URL="http://127.0.0.1:8000/search?q=";
	window.location.href=URL+search_text;
});

$(document).on('click','.add_to_cart', function(){
            product_id = $(this).parent().find("input").val();
            $.ajax({
                url: '/add_Cart/',
			
			type: "GET",
			data: {
			"product_id": product_id,
			},
			success: function(data) 
			{
			}
		});
				alert("Product added to cart successfully.");
            
            
});
});
