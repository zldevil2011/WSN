
function checkform() {
		var val;
	
		if($('#selType2').val() %100== 0) {
			alert("请选择文章类型");
			return;
		}
		val = $.trim($('#txtTitle').val());
		if(val == '' || val == null) {
			alert("标题不能为空!");
			return ;
		}
		alert("发布成功!");
		$('#pubnewsform').submit();
	}

function pub_news(){ 
	 checkform();
}

function save_draft() {
	$('#pubnewsform').ajaxSubmit({
		target: '#sp_note',
		type: 'post',
		url: 'Savedraft', 
		beforeSubmit: function (formData, jqForm, options) {
			var val;
			
			if($('#selType2').val() %100== 0) {
				alert("请选择文章类型");
				return false;
			}
			val = $.trim($('#txtTitle').val());
			if(val == '' || val == null) {
				alert("标题不能为空!");
				return false;
			}
			document.getElementById('sp_note').innerText = '草稿正在保存中...';
			return true;
		},
		success: function(data) {
			if(data == 'success') {
				var myDate = new Date();  
				document.getElementById('sp_note').innerText = '草稿保存成功，'+ '保存时间'+myDate.getHours() + ':' + myDate.getMinutes();
			}
		}
	});
}