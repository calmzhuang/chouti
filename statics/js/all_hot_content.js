$(function () {
   //展示发布页面
   $('#publishBtn').on('click', function () {
       publish_page_show();
   });

   //关闭发布页面
   $('#dialog-btn-close').on('click', function () {
       publish_page_hide();
   });

   //上传并预览图片
   $('#imgUrl').on('change', function () {
       let curent_pic = this.files[0];
       preview_picture(curent_pic);
       FileUpload(curent_pic);
   });

   //发布链接页面
   $('#pubTabZixun').on('click', function () {
       let sharetype = 'zixun';
       let _that = $(this);
       ShareType(sharetype, _that);
   });

   //发布文字页面
   $('#pubTabDuanzi').on('click', function () {
       let sharetype = 'duanzi';
       let _that = $(this);
       ShareType(sharetype, _that);
   });

   //发布图片页面
   $('#pubTabPic').on('click', function () {
       let sharetype = 'tabpic';
       let _that = $(this);
       ShareType(sharetype, _that);
   });

   //切换发布对象
   $('.toclass-btn').on('click', function () {
       let _that = $(this);
       PubIcon(_that);
   })

   $('.digg-a').on('click', function () {
       if (username == '') {
           login_register();
       }
       else {

       }
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
};

function ShareType(sharetype, _that) {
    if (sharetype === 'zixun') {
        _that.addClass('w-active').addClass('color');
        _that.siblings().removeClass('w-active').removeClass('color');
        $('#publish-content-zixun').show();
        $('#publish-content-zixun').siblings().hide();
    }
    else if (sharetype === 'duanzi') {
        _that.addClass('w-active').addClass('color');
        _that.siblings().removeClass('w-active').removeClass('color');
        $('#publish-content-duanzi').show();
        $('#publish-content-duanzi').siblings().hide();
    }
    else {
        _that.addClass('w-active').addClass('color');
        _that.siblings().removeClass('w-active').removeClass('color');
        $('#publish-content-pic').show();
        $('#publish-content-pic').siblings().hide();
    }
};

function PubIcon(_that) {
    _that.addClass('toclass-btn-valid').removeClass('toclass-btn-unvalid');
    _that.siblings().addClass('toclass-btn-unvalid').removeClass('toclass-btn-valid');
};