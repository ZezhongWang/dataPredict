// document.querySelector('.img__btn').addEventListener('click', function() {
//   document.querySelector('.cont').classList.toggle('s--signup');
// });

document.querySelector('.img__btn').addEventListener('click', function() {
    var changeEle = document.querySelector('.cont');
    var isSignUp = changeEle.classList.contains('s--signup');
    if(isSignUp==false){
        changeEle.classList.add('s--signup');
    }
    else{
        changeEle.classList.remove('s--signup');
    }
});

document.getElementById('id_captcha_1').addEventListener('focus', verifyPassword);


function verifyPassword() {
    var p1 = document.RegisterForm.password.value;
    var p2 = document.RegisterForm.password2.value;

    if(p1 !== p2) {
        window.alert("两次密码不一致");
        document.RegisterForm.password2.focus();
    }
}


