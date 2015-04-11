$( "#update-button" ).click(function() {
  $.ajax({
		type: 'GET',
		url: "/update",
		dataType: "html",
		success: function(result){
			$('#rubiks-cube').html("").append(result);
			console.log("Rubik's cube updated");
		},
		error: function(xhr, textStatus, errorThrown){
			alert('request failed');
		}
	});
});

$( "#manual-controls td button" ).click(function() {
	$.ajax({
		type: 'GET',
		url: "/move/" + $(this).data("direction"),
		dataType: "html",
		success: function(result){
			$('#rubiks-cube').html("").append(result);
			console.log("Rubik's cube updated");
		},
		error: function(xhr, textStatus, errorThrown){
			alert('request failed');
		}
	});
});

$( "#scramble" ).click(function() {
  $.ajax({
		type: 'GET',
		url: "/scramble",
		dataType: "html",
		success: function(result){
			$('#rubiks-cube').html("").append(result);
			console.log("Rubik's cube has been scrambled");
		},
		error: function(xhr, textStatus, errorThrown){
			alert('request failed');
		}
	});
});