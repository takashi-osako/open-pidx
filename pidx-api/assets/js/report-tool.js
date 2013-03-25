//selection_id={}
$(function () {
	$('body').layout({
		applyDefaultStyles : true
	});
	$("#selections").accordion();
	$("#selections li").draggable({
		appendTo : "body",
		helper : "clone"
	});
	$("#canvas").droppable({
		activeClass : "ui-state-default",
		hoverClass : "ui-state-hover",
		drop : function(event, ui) {
			if (ui.draggable.attr("id") == "text box") {
				$('<span><textarea id="resizable" rows="1" cols="20">text</textarea></span>').appendTo(this);
			}
		}
	});
	$("#resizable").resizable({
		handle : "se"
	});
});
