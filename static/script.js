$(document).ready(function(){
	console.log("yay");
	$('#repo_name').autocomplete({
		source: "/github_new",
		minLength: 1,
	});
});