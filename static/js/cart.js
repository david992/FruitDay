
//全选
    function demo(){
        var allcheck=document.getElementById("checkall");
        // var allcheck=document.getElementsByName("allcheck");
        var choice=document.getElementsByName("choice");
        for(var i=0;i<choice.length;i++){
            choice[i].checked=allcheck.checked;
        }
    }

/**
 * 异步向服务器发送请求，检查用户是否处于登录状态
 * */
function check_login(){
  $.get('/check_login/',function(data){
    var html = "";
    if(data.loginStatus == 0){
      html += "<a href='/login/'>[登录]</a>,";
      html += "<a href='/register/'>[注册有惊喜]</a>";
    }else{
      html += "欢迎："+data.uname;
      html += "<a href='/logout/'>退出</a>";
    }
    $("#login").html(html);
  },'json');
}


function cart(){
  $.get('/cart_server/',function (data) {
    console.log(data);
    var show = "";
    $.each(data,function (i,obj) {
      //string格式
      // console.log(obj.good_list);
      // console.log(typeof obj.good_list)
      var jsongoods = JSON.parse(obj.good_list);
      //json格式
      console.log(typeof jsongoods)
      console.log(jsongoods)
      $.each(jsongoods,function (i,obj) {
      show += " <div class='g-item'>";
      show += " <p class='check-box'>";
      show += " <input type='checkbox' name='choice'  >"
      show += " <img src='/"+obj.fields.picture+"' width='80'></p>";
      show += " <p class='goods'>&yen;"+obj.fields.title+"</p>"
      show += " <p class='price'>"+obj.fields.price+"</p>"
      show += " <p class='quantity'>"+obj.fields.price+"</p>"
      show += " <p class='t-sum'><b>&yen;"+obj.fields.price+"</b></p>"
      show += " <p class='action'><a href=‘#’>"+"移除"+"</a></p>"

      show += "</div>";
      })
    });
    $("#good-content").html(show);
  },'json');
}

$(function(){
	/*调用check_login检查登录状态*/
	check_login();
    cart();
});