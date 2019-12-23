function update_all_post() {
	$.ajax({
		url: "/update_all_posts",
		type: "get",
		data: null,
		success: function(response) {
			$("#location_all_post").html(response);
		},
		error: function(xhr) {
			//Do Something to handle error
		}
	});
}

update_all_post()
var timer, delay = 500; // 500 milliseconds = half a second
timer = setInterval(function(){
    update_all_post()
}, delay);