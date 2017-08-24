/**
 * Created by w2w on 17-8-15.
 */


checkIfEditable();
addListener();

function checkIfEditable() {
    var expert_number = document.getElementById('expert_number');
    var valid_time = document.getElementById('valid_time');
    var name = document.getElementById('name');
    var gender = document.getElementById('gender');
    var birthday = document.getElementById('birthday');
    var certificate_type = document.getElementById('certificate_type');
    var certificate_number = document.getElementById('certificate_number');

    expert_number.setAttribute('readonly', 'readonly');
    valid_time.setAttribute('readonly', 'readonly');

    if(name.value != null && name.value != ""){
        name.setAttribute('readonly', 'readonly');
    }
    if(gender.value != null && gender.value != ""){
        gender.setAttribute('readonly', 'readonly');
    }
    if(birthday.value != null && birthday.value != ""){
        birthday.setAttribute('readonly', 'readonly');
    }
    if(certificate_type.value != null && certificate_type.value != ""){
        certificate_type.setAttribute('readonly', 'readonly');
    }
    if(certificate_number.value != null && certificate_number.value != ""){
        certificate_number.setAttribute('readonly', 'readonly');
    }
}

function addListener() {
    // document.getElementById('name').addEventListener('focus', test_valid_time);
    document.getElementById('phone_number').addEventListener('focus', test_birthday);
    document.getElementById('email').addEventListener('focus', test_phone_number);
    document.getElementById('picture').addEventListener('focus', test_certificate_number);
}

function test_valid_time() {
    var valid_time = document.getElementById('valid_time');
    var re = /^\d{4}-\d{1,2}-\d{1,2}$|^d{4}年\d{1,2}月\d{1,2}|^\d{4}\/\d{1,2}\/\d{1,2}$/;
    if(!re.test(valid_time.value)){
        document.getElementById('valid_time_tip').removeAttribute('hidden');
        return false;
    }
    else{
        document.getElementById('valid_time_tip').setAttribute('hidden', 'hidden');
        return true;
    }
}

function test_birthday() {
    var birthday = document.getElementById('birthday');
    var re = /^\d{4}-\d{1,2}-\d{1,2}$|^d{4}年\d{1,2}月\d{1,2}|^\d{4}\/\d{1,2}\/\d{1,2}$/;
    if(!re.test(birthday.value)){
        document.getElementById('birthday_tip').removeAttribute('hidden');
        return false;
    }
    else{
        document.getElementById('birthday_tip').setAttribute('hidden', 'hidden');
        return true;
    }
}

function test_phone_number() {
    var phone_number = document.getElementById('phone_number');
    var re = /^1[34578]\d{9}$/;
    if(!re.test(phone_number.value)){
        document.getElementById('phone_number_tip').removeAttribute('hidden');
        return false;
    }
    else{
        document.getElementById('phone_number_tip').setAttribute('hidden', 'hidden');
        return true;
    }
}

function test_certificate_number() {
    var certificate_number = document.getElementById('certificate_number');
    var re = /^\d{18}$/;
    if(!re.test(certificate_number.value)){
        document.getElementById('certificate_number_tip').removeAttribute('hidden');
        return false;
    }
    else{
        document.getElementById('certificate_number_tip').setAttribute('hidden', 'hidden');
        return true;
    }
}

function toValid() {
    // var t1 = test_valid_time();
    var t2 = test_birthday();
    var t3 = test_phone_number();
    var t4 = test_certificate_number();
    if(t2 == false || t3 == false || t4 == false){
        alert("校验失败，不能提交");
        return false;
    }
    else{
        return true;
    }
}
