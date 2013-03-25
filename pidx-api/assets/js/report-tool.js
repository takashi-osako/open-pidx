selection_id={}
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
			id = ui.draggable.attr("id");
			value = ui.draggable.attr("value");
			my_selection_id = get_selection_id(id);
			new_element = $(value);
			new_element.attr("id", my_selection_id);
			span_element = $('<span></span>');
			span_element.attr("id","span_" + my_selection_id);
			new_element.appendTo(span_element);
			span_element.appendTo(this)
		}
	});

});

function get_selection_id(id) {
	uid = selection_id[id];
	if (uid === undefined) {
		selection_id[id] = 0;
		uid = 0;
	}
	selection_id[id]++;
	return id + "_" + uid;
}
