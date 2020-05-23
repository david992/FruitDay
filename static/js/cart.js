window.onload = function (){

	/*-----------图片轮播-----------*/
	//1. 获取图片数组
	//2. 定时器实现图片切换
	//3. 图片切换主要切换数组下标，防止数组越界

	var banner = document.getElementsByClassName('wrapper')[0];
	var imgs = banner.children; //图片数组
	var imgNav = document.getElementsByClassName('imgNav')[0];
	var indInfo = imgNav.children; //索引数组
	var imgIndex = 0; //初始下标
	var timer;
	timer = setInterval(autoPlay,1000); //定时器
	function autoPlay(){
		//设置元素隐藏与显示
		imgs[imgIndex].style.display = "none";
		/*
		++ imgIndex;
		if(imgIndex == imgs.length){
			imgIndex = 0;
		}
		*/
		imgIndex = ++ imgIndex == imgs.length ? 0 : imgIndex;

		imgs[imgIndex].style.display = "block";

		for(var i = 0; i < indInfo.length; i ++){
			indInfo[i].style.background = "gray";
		}
		//切换索引 切换背景色
		indInfo[imgIndex].style.background = "red";
	}
	banner.onmouseover = function (){
		//停止定时器
		clearInterval(timer);
	};

	banner.onmouseout = function (){
		timer = setInterval(autoPlay,1000);
	};

};


$(function(){
	/*调用check_login检查登录状态*/
	check_login();

    cart();
});

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
      // console.log(typeof jsongoods)
      // console.log(jsongoods)
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

