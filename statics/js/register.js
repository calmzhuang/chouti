$(function () {
    $('.btn-getcode').on('click', function () {
        getCode();
    });
    $('.btn-register').on('click', function () {
        next_register();
    })
});

var next_register = function () {
    let rgmobile = $(".rgmobile").val().trim();
    let rgcode = $(".rgcode").val().trim();
    let rgpwd = $(".rgpwd").val().trim();
    if (rgmobile == '') {
        $('.box-register-mobile>.err-msg').html('手机号不能为空');
    }
    else if (rgcode == '') {
        $('.box-register-mobile>.err-msg').html('验证码不能为空');
    }
    else if (rgpwd == '') {
        $('.box-register-mobile>.err-msg').html('密码不能为空');
    }
    else if (rgpwd.length < 6 && rgpwd.length > 18){
        $('.box-register-mobile>.err-msg').html('密码长度应为6-18位');
    }
    else {
        $.ajax({
            url: '/next_page/',
            type: 'post',
            dataType: 'JSON',
            data: {
                rgmobile: rgmobile,
                rgcode: rgcode,
            },
            success: function (data) {
                if (data) {
                    $('.box-register-mobile').hide();
                    $('.box-register-detail').show();
                }
            }
        })
    }
};

var getCode = function () {
        $('.box-register-mobile>.err-msg').empty();
        let telephonenum = $(".rgmobile").val();
        let mobilereg = /^(\d){11}$/;
        if (mobilereg.test(telephonenum)) {
            $.ajax({
                url: '/getcode/',
                type: 'post',
                data: {
                    telephonenum: telephonenum,
                },
                success: function (data) {
                    if (data == '') {
                        let timer = 60;
                        let interval = setInterval(() => {$(".btn-getcode").html(`已发送(${timer})`).addClass('btn-disable').css('cursor', 'default'); timer-=1;$('.btn-getcode').unbind('click');if(timer < 0){clearInterval(interval);$(".btn-getcode").html('发送验证码').removeClass('btn-disable').css('cursor', 'pointer');$('.btn-getcode').bind('click', function () {
                            getCode()
                        });}}, 1000)
                    }
                    else {
                        $('.box-register-mobile>.err-msg').html(data)
                    }
                }
            })
        }
        else {
            $('.box-register-mobile>.err-msg').html('请输入正确手机号');
        }

}