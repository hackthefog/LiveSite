var timer, delay = 500; // 500 milliseconds = half a second
timer = setInterval(function(){
    $.ajax({
		url: "/update_recent_posts",
		type: "get",
		data: null,
		success: function(response) {
			$("#location_recent_post").html(response);
		},
		error: function(xhr) {
			//Do Something to handle error
		}
    });
}, delay);