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
                    alert(1);
                    let timer = 60;
                    do {
                        setInterval(() => {$(".rgmobile").val(`已发送（${timer}）`); timer-=1;$('.btn-getcode').removeEventListener('click');}, 1000)
                    }while (timer > 0)
                }
            })
        }
        else {
            $('.box-register-mobile>.err-msg').html('请输入正确手机号');
        }
    })
});