
/**
 * Recieves the size of an elements width or height then 
 * modifies size by 10px based on increase arg returning 
 * the new size
 * @param {String} - pixels element size in px's
 * @param {boolean} - increase flag to decrease or increase size  
 * @return {String} - new size formated in px
 */
function modifySize(pixels, increase)
{	
	var original = parseInt(pixels.replace("px",""));
	if (increase)
	{
		var newInteger = original + 5;
		var newString = newInteger.toString()+"px";
		return newString;
	}
	var newInteger = original - 5;
	var newString = newInteger.toString()+"px";
	return newString;
	
}


/**
 * triggerd by an element this function will take that elements
 * class and sets the visibility of the related `small` class to hidden
 * then sets the related `large` class to visible 
 * @param event {MouseOverEvent} - event triggered by mousover
 * @return {void}
 */
function enlarge(event)
{
	var element = event.target;
	if (element.tagName == "DIV")
	{
		element = element.parentElement;
	}
	var className = element.className;
	var title = document.getElementById("title-"+className);
	var style = window.getComputedStyle(title);
	var fontSize = style.getPropertyValue('font-size');
	var newFontSize = modifySize(fontSize, true);
	title.style.fontSize = newFontSize;
	document.getElementById("small-"+className).style.visibility = "hidden";
	document.getElementById("large-"+className).style.visibility = "visible";
}

/**
 * triggerd by an element this function will take that elements
 * class and sets the visibility of the related `small` class to visible
 * then sets the related `large` class to hidden 
 * @param event {MouseOverEvent} - event triggered by mouseout
 * @return {void}
 */
function decrease(event)
{
	var element = event.target;
	if (element.tagName == "DIV")
	{
		element = element.parentElement;
	}
	var className = element.className;
	var title = document.getElementById("title-"+className);
	var style = window.getComputedStyle(title);
	var fontSize = style.getPropertyValue('font-size');
	var newFontSize = modifySize(fontSize, false);
	title.style.fontSize = newFontSize;
	document.getElementById("small-"+className).style.visibility = "visible";
	document.getElementById("large-"+className).style.visibility = "hidden";
}


/**
 * First component of the fading in presentation method
 * fades in the data classes
 * @return {void}
 */ 
function fade1() 
{
	$(".data").each(function() {
		$(this).fadeIn(1500, "swing", fade2);
    });
}

/**
 * Second component of the fading in presentation method
 * fades in the web-dev classes
 * @return {void}
 */ 
function fade2() 
{
	$(".web-dev").each(function() {
		$(this).fadeIn(2500, "swing", fade3);
    });
}

/**
 * Third component of the fading in presentation method
 * fades in the backend classes
 * @return {void} 
 */ 
function fade3() 
{
	$(".backend").each(function() {
		$(this).fadeIn(1500, "swing", fade4);
    });
}

/**
 * Fourth component of the fading in presentation method
 * fades in the app-dev classes
 * @return {void} 
 */ 
function fade4() 
{
	$(".app-dev").each(function() {
		$(this).fadeIn(1500, "swing", fade5);
    });
}

/**
 * Fifth component of the fading in presentation method
 * fades in the data machine learning
 * @return {void} 
 */ 
function fade5() 
{
	$(".machinelearning").each(function() {
		$(this).fadeIn(1500, "swing");
    });
}

/**
 * presentation method starts a chain of jquery fade
 * in methos to fade in classes consecutivley. Calling the automation
 * method first, every subsequest step is a callback of the previous
 * @return {void} 
 */ 
function presentation() 
{
	$(".automation").each(function() {
		$(this).fadeIn(1500, "swing", fade1);
    });
}


/**
 * This event listener waits untill the dom has loaded then attaches
 * event listeners to all needed web elements to have them enlarge
 * and shrink when hovered over. 
 */
document.addEventListener("DOMContentLoaded", function()
{	
	var webDev = document.getElementsByClassName("web-dev");
	document.getElementById("large-web-dev").style.visibility = "hidden";
	for (var i = 0; i < webDev.length; i++)
	{
		var item = webDev[i];
		item.addEventListener("mouseover", enlarge);
		item.addEventListener("mouseout", decrease);
	}
	var automation = document.getElementsByClassName("automation");
	document.getElementById("large-automation").style.visibility = "hidden";
	for (var i = 0; i < automation.length; i++)
	{
		var item = automation[i];
		item.addEventListener("mouseover", enlarge);
		item.addEventListener("mouseout", decrease);
	}
	var backend = document.getElementsByClassName("backend");
	document.getElementById("large-backend").style.visibility = "hidden";
	for (var i = 0; i < backend.length; i++)
	{
		var item = backend[i];
		item.addEventListener("mouseover", enlarge);
		item.addEventListener("mouseout", decrease);
	}
	var appDev = document.getElementsByClassName("app-dev");
	document.getElementById("large-app-dev").style.visibility = "hidden";
	for (var i = 0; i < appDev.length; i++)
	{
		var item = appDev[i];
		item.addEventListener("mouseover", enlarge);
		item.addEventListener("mouseout", decrease);
	}
	var machinelearning = document.getElementsByClassName("machinelearning");
	document.getElementById("large-machinelearning").style.visibility = "hidden";
	for (var i = 0; i < machinelearning.length; i++)
	{
		var item = machinelearning[i];
		item.addEventListener("mouseover", enlarge);
		item.addEventListener("mouseout", decrease);
	}
	var data = document.getElementsByClassName("data");
	document.getElementById("large-data").style.visibility = "hidden";
	for (var i = 0; i < data.length; i++)
	{
		var item = data[i];
		item.addEventListener("mouseover", enlarge);
		item.addEventListener("mouseout", decrease);
	}
	presentation();
})

