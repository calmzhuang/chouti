$(function () {
    $('.login-btn-a').on('click', function () {
        login_register();
    });
    $('.btn-login').on('click', function () {
        login();
    });
    $('#picode').on('click', function () {
        this.src = this.src + '?';
    });
});

var login_register = function () {
    $('.module-login-mask').show();
};

var login = function () {
    let username = $('#mobile').val();
    let pwd = $('#mbpwd').val();
    let keeplogin = $(".keeplogin:checked").val()? 1 : 0;
    let pilcode = $("#pcd").val();
    $.ajax({
        url: '/login/',
        type: 'post',
        data: {
            'username': username,
            'pwd': pwd,
            'keeplogin': keeplogin,
            'pilcode': pilcode,
        },
        success: function (data) {
            if (data == '') {
                location.reload();
            }
            else {
                $('.box-mobilelogin>.err-msg').html(data);
            }
        }
    })
}