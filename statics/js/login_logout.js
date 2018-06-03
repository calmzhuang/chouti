$(function () {
    $('.login-btn-a').on('click', function () {
        login_register();
    });
    $('.btn-login').on('click', function () {
        login();
    });
});

var login_register = function () {
    $('.module-login-mask').show();
};

var login = function () {
    let username = $('#mobile').val();
    let pwd = $('#mbpwd').val();
    let keeplogin = $(".keeplogin:checked").val()? 1 : 0;
    $.ajax({
        url: '/login/',
        type: 'post',
        data: {
            'username': username,
            'pwd': pwd,
            'keeplogin': keeplogin,
        },
        success: function (data) {
            if (data == '') {
                location.reload();
            }
            else {
                $('.box-mobilelogin>.err-msg').html('手机号或密码不正确');
            }
        }
    })
}