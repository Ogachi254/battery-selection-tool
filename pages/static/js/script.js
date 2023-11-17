function openForm() {
	document.getElementById("myChatPopup").style.display = "block";
}

function closeForm() {
	document.getElementById("myChatPopup").style.display = "none";
}

window.onload = function() {
	var chatPopup = document.getElementById("myChatPopup");
	chatPopup.classList.add("show");
}
