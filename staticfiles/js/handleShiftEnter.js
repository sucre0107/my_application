

var MyEnterFunction = {
    handleShiftEnter: function(event) {
        if (event.shiftKey && event.keyCode == 13) {
            // 阻止默认行为（例如，不发送表单）
            event.preventDefault();
            // 在光标位置插入换行符
            var cursorPos = event.target.selectionStart;
            var textBefore = event.target.value.substring(0, cursorPos);
            var textAfter = event.target.value.substring(cursorPos, event.target.value.length);
            event.target.value = textBefore + "\n" + textAfter;
        }
    },

    handleEnter: function(event, streamEvent) {
        if (event.keyCode == 13) {
            // 运行streamEvent函数
            event.preventDefault()
            streamEvent()
        }
    }
}
