var score = "";

$(document).ready(function() {
  var score1, score2, score3;
  $('input:radio[name=rate1]').change(function() {
    if (this.value == 'terrible') {
      //alert("you have picked design to be terrible");
      score1 = 2;
      console.log(score1);
      $("#efficiency").text(score1);
    } else if (this.value == 'poor') {
      //alert("you have picked design to be poor");
      score1 = 4;
      console.log(score1);
      $("#efficiency").text(score1);
    } else if (this.value == 'average') {
      //alert("you have picked designto be average");
      score1 = 6;
      console.log(score1);
      $("#efficiency").text(score1);
    } else if (this.value == 'very good') {
      //alert("you have picked design to be very good");
      score1 = 8;
      console.log(score1)
      $("#efficiency").text(score1);
    } else if (this.value == 'excellent') {
      //alert("you have picked design to be excellent");
      score1 = 10;
      console.log(score1)
      $("#efficiency").text(score1);
    }
    $("#id_efficiency").val(score1)
  });

  $('input:radio[name=rate2]').change(function() {
    if (this.value == 'terrible') {
      //alert("you have picked usability to be terrible");
      score2 = 2;
      console.log(score2)
      $("#time").text(score2);
    } else if (this.value == 'poor') {
      //alert("you have picked usability to be poor");
      score2 = 4;
      console.log(score2)
      $("#time").text(score2);
    } else if (this.value == 'average') {
      //alert("you have picked usability to be average");
      score2 = 6;
      console.log(score2)
      $("#time").text(score2);
    } else if (this.value == 'very good') {
      //alert("you have picked usability to be very good");
      score2 = 8;
      console.log(score2)
      $("#time").text(score2);
    } else if (this.value == 'excellent') {
      //alert("you have picked usability to be excellent");
      score2 = 10;
      console.log(score2)
      $("#time").text(score2);
    }
    $("#id_time").val(score2)
  });

  $('input:radio[name=rate3]').change(function() {
    if (this.value == 'terrible') {
      //alert("you have picked creativity to be terrible");
      score3 = 2;
      console.log(score3)
      $("#response").text(score3);
    } else if (this.value == 'poor') {
      //alert("you have picked creativity to be poor");
      score3 = 4;
      console.log(score3)
      $("#response").text(score3);
    } else if (this.value == 'average') {
      //alert("you have picked creativity to be average");
      score3 = 6;
      console.log(score3)
      $("#response").text(score3);
    } else if (this.value == 'very good') {
      //alert("you have picked creativity to be very good");
      score3 = 8;
      console.log(score3)
      $("#response").text(score3);
    } else if (this.value == 'excellent') {
      //alert("you have picked creativity to be excellent");
      score3 = 10;
      console.log(score3)
      $("#response").text(score3);
    }
    $("#id_response").val(score3)
  });

  $("#questions").submit(function(event) {
    event.preventDefault();
    var rated = new Rate;
    // rated.total(score1, score2, score3);
    console.log(rated.total(score1, score2, score3));
    // Rate.average();
    console.log(rated.average());
    $("#id_average").val(rated.average());
    $("#ratingform").submit()
  });
  //business logic
function Rate() {
  this.totalScore = 0;
  this.averageScore = 0;
}
Rate.prototype.total = function(sc1, sc2, sc3) {
  this.totalScore = sc1 + sc2 + sc3;
  return this.totalScore;
}
Rate.prototype.average = function() {
  this.averageScore = (this.totalScore / 3 | 0);
  return this.averageScore;
}
});
$('input[name=rate1]').attr('checked',false);
$('input[name=rate2]').attr('checked',false);
$('input[name=rate3]').attr('checked',false);

$(".hover").mouseleave(
  function () {
    $(this).removeClass("hover");
  }
);