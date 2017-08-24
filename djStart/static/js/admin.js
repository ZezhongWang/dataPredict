/**
 * Created by w2w on 17-8-23.
 */


function test_expert_number() {
    var expert_number = document.getElementById('expert_number');
    var re = /^\d{8}$/;
    if(!re.test(expert_number.value)){
        document.getElementById('expert_number_tip').removeAttribute('hidden');
        return false;
    }
    else{
        document.getElementById('expert_number_tip').setAttribute('hidden', 'hidden');
        return true;
    }
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

function toValidAdmin() {
    var t1 = test_expert_number();
    var t2 = test_valid_time();

    if( t1 == false || t2 == false ){
        alert("校验失败，不能提交");
        return false;
    }
    else{
        return true;
    }
}