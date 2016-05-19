/**
 * Created by Gamer Think on 2016/3/4.
 */
KindEditor.ready(function(K) {
	K.create('textarea[name="blog_content"]', {
		width : "800px",
        height : "500px",
		uploadJson: '/admin/upload/kindeditor',
	});
});

KindEditor.ready(function(K) {
	K.create('textarea[name="bbs_content"]', {
		width : "800px",
        height : "500px",
		uploadJson: '/admin/upload/kindeditor',
	});
});


