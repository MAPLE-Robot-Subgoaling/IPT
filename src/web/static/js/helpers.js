function handleSubmit(f){
	for(var i = 0; i < f.elements.length; i++){
		var node = f.elements[i];
		if(node.nodeName == "SELECT" && node.value == "?" && !node.disabled){
			alert("You checked a box, but didn't label a line.")
			return false;
		}
	}
	return true;
}

function handleClick(cb){
	var line = document.getElementsByClassName(cb.className);
	line[0].disabled = !(cb.checked);
}

function highlight(e) {
	
}