$(function () {
  $("#post").click(function(){
    $.ajax({
      url: 'http://localhost:5000/httpAPI',
      type: 'POST',
      success: function(result) {
        alert(result);
        $("p").text(result);
        var myName = $("#firstname").val() + $("#lastname").val();
        $("#p_yourName").text($("#firstname").val() + $("#lastname").val());
        if (myName != result) {
          return alert("login fail!");
        }
          return alert("login success!")
      }
    });
  });
});

$(function () {
  $("#delete").click(function(){
    $.ajax({
      url: 'http://127.0.0.1:5000/httpAPI',
      type: 'DELETE',
      success: function(result) {
        alert(result);
        $("p").text(result);
        var myName = $("#firstname").val() + $("#lastname").val();
        $("#p_yourName").text($("#firstname").val() + $("#lastname").val());
        if (myName != result) {
          return alert("login fail!");
        }
          return alert("login success!")
      }
    });
  });
});

$(function () {
  $("#put").click(function(){
    $.ajax({
      url: 'http://127.0.0.1:5000/httpAPI',
      type: 'put',
      success: function(result) {
        alert(result);
        $("p").text(result);
        var myName = $("#firstname").val() + $("#lastname").val();
        $("#p_yourName").text($("#firstname").val() + $("#lastname").val());
        if (myName != result) {
          return alert("login fail!");
        }
          return alert("login success!")
      }
    });
  });
});

$(function () {
  $("#get").click(function(){
    $.ajax({
      url: 'http://127.0.0.1:5000/httpAPI',
      type: 'GET',
      success: function(result) {
        alert(result);
        $("p").text(result);
        var myName = $("#firstname").val() + $("#lastname").val();
        $("#p_yourName").text($("#firstname").val() + $("#lastname").val());
        if (myName != result) {
          return alert("login fail!");
        }
          return alert("login success!")
      }
    });
  });
});
