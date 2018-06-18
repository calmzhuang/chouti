$(function () {
   $('#publishBtn').on('click', function () {
       publish_page_show();
   });
   $('#dialog-btn-close').on('click', function () {
       publish_page_hide();
   });
   $('#imgUrl').on('change', function () {
       let curent_pic = this.files[0];
        preview_picture(curent_pic);
        FileUpload(curent_pic);
   })
});

publish_page_show = () => {
  $('#digg-dialog-publish').show();
  $('#mask').show();
};

publish_page_hide = () => {
  $('#digg-dialog-publish').hide();
  $('#mask').hide();
};

preview_picture = pic => {
  let r = new FileReader();
  r.readAsDataURL(pic);
  r.onload = event => {
      let percent = 50 * event.loaded / event.total;
      percent = parseFloat(percent).toFixed(2);
      $('#upload-img').attr("src", event.target.result);
      $('#upload-img-area').hide();
      $('#show-img-area').show();
      $('#upload-img').css('width', percent + '%').css('height', percent + '%');
      // $('#uploadPicFrm').submit();
  }
};

function FileUpload(curent_pic) {
    let form_data = new FormData();
    form_data.append('file',curent_pic);
    //if(curent_pic==undefined)暂且不许要判断是否有附件
        //alert('你没有选择任何文件');
        //return false
    $.ajax({
        url:'/link/pic/upload/',
        type:'POST',
        data: form_data,
        processData: false,  // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function(callback) {
            console.log('ok')
        }
    });
}