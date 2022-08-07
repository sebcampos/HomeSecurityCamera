/**
 * This method checks the select option value, validates it does not
 * exists in the `Objects` ul list and appends it to that list to
 * display to the user
 * @return {void}
 */ 
function addToTracking() 
{
	let selectedOption = document.getElementById("select_option").value;
	if (existsInTracking(selectedOption)) 
	{	
		return;
	}
	var trackingList = document.getElementById("tracking_list");
	var newLi = document.createElement("li");
	var textNode = document.createTextNode(selectedOption);
	newLi.appendChild(textNode);
	trackingList.appendChild(newLi);
}



/**
 * This method checks the select option value, validates it does 
 * exist in the `Objects` ul list and removes it to that list to
 * display to the user
 * @return {void}
 */ 
function removeFromTracking()
{
	let selectedOption = document.getElementById("select_option").value;
	var trackingIndex = existsInTracking(selectedOption, index=true); 
	console.log(trackingIndex);
	if (trackingIndex == false && trackingIndex != 0) 
	{
		return;
	}
	var trackingList = document.getElementById("tracking_list");
	var nodeToRemove = trackingList.children[trackingIndex];
	trackingList.removeChild(nodeToRemove);
}


/**
 * This method checks for an existing label in the Objects
 * ul list. returning true or false, if the index flag is 
 * set to true then it will return the index of the existsing
 * element
 * @param {String} label - text expected in the li element
 * @param {boolean} index - flag to return the index of the found element    
 */
function existsInTracking(label, index=false) 
{	
	let trackingList = document.getElementById("tracking_list");	
	for (let i = 0; i <  trackingList.children.length; i++) 
	{	
		if (trackingList.children[i].textContent == label)
		{
			if (index)
			{
				return i;
			}
			return true;
		}
	}
	return false;
}

/**
 *This method collects all the ul objects designated for tracking
 * to post it to an endpoint
 * @return {void} 
 */
function collectObjects()
{
	let trackingList = document.getElementById("tracking_list");	
	let payloadData = "";
	for (let i = 0; i <  trackingList.children.length; i++) 
	{
		payloadData += trackingList.children[i].textContent.trim()+","
	}
	return payloadData;	
}


/**
 * This method collects the objects marked to be tracked
 * and sends the xhr post request to update the tracking logic
 * @return {void}
 */ 
function submitUpdate()
{
	let xhr = new XMLHttpRequest();
	var csrftoken = document.cookie.split("=")[1];
	var labels = document.getElementById("tracking_list").textContent;
	xhr.open("POST", "http://192.168.7.207:8000/cam/view/update");
	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.setRequestHeader("X-CSRFToken", csrftoken);

	let data = {
		"labels": collectObjects(),
	};
	
	data = JSON.stringify(data);
	
	xhr.send(data);
    xhr.onload = () => {
        console.log(xhr.responseText);
    }
}


function updateBatteryLife()
{
	let xhr = new XMLHttpRequest();
	var csrftoken = document.cookie.split("=")[1];
	xhr.open("GET", "http://192.168.7.207:8000/cam/view/battery");
	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.setRequestHeader("X-CSRFToken", csrftoken);
	
	xhr.send();
	xhr.onload = () => {
		let newText = JSON.parse(xhr.responseText).charge_level;
		document.getElementById("battery").text = newText
	}
}

window.setTimeout(updateBatteryLife, 5000);

