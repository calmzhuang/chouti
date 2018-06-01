$(function () {
    $('.btn-getcode').on('click', function () {
        $('.box-register-mobile>.err-msg').empty();
        let telephonenum = $(".rgmobile").val();
        let mobilereg = /^(\d){11}$/;
        if (mobilereg.test(telephonenum)) {
            $.ajax({
                url: '/test/',
                type: 'post',
                data: {
                    telephonenum: telephonenum,
                },
                success: function (data) {
                    let timer = 60;
                    let interval = setInterval(() => {$(".btn-getcode").html(`已发送(${timer})`).addClass('btn-disable').css('cursor', 'default'); timer-=1;$('.btn-getcode').unbind('click');console.log(timer);if(timer < 0){clearInterval(interval);$(".btn-getcode").html('发送验证码').removeClass('btn-disable').css('cursor', 'pointer');$('.btn-getcode').bind('click');}}, 1000)
                }
            })
        }
        else {
            $('.box-register-mobile>.err-msg').html('请输入正确手机号');
        }
    })
});