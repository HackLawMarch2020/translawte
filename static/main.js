$( document ).ready(function() {

    $("input").click(function(){
      $.post("http://127.0.0.1:5000/translate", { data: $('#src_text').val()}, function(result, status){
        $('#results').html(result)
      });
    });

    $(".buttons").click(function () {
      var cntrl = $(this).val();
      $("#src_text").html(cntrl);
    });

})