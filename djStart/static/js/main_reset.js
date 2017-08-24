/**
 * Created by w2w on 17-8-21.
 */
document.getElementById('id_captcha_1').addEventListener('focus', verifyPassword);


function verifyPassword() {
    var p1 = document.reset_form.password_after.value;
    var p2 = document.reset_form.password_again.value;

    if(p1 !== p2) {
        window.alert("两次密码不一致");
        document.RegisterForm.password2.focus();
    }
}
