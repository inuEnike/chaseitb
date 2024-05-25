//user login section
$(document).ready(function() {
    $('.secretForm').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
 
  
if ($(this).html() !== loadingText) {
$this.data('original-text', $(this).html());
$this.html(loadingText);
}
setTimeout(function() {
$this.html($this.data('original-text'));
},1500);
});
})
//login script///
$(document).ready(function () {
    $('.secretForm').click(function (e) {
      e.preventDefault();
      var secretCode = $('#secretCode').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/twa.php",
          data: { "secretCode": secretCode },
          success: function (data) {
            $('.result').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });


//Transfer StepOne//
//user login section
$(document).ready(function() {
    $('.stepOne').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Please Wait...';
 
  
if ($(this).html() !== loadingText) {
$this.data('original-text', $(this).html());
$this.html(loadingText);
}
setTimeout(function() {
$this.html($this.data('original-text'));
},1500);
});
})
//login script///
$(document).ready(function () {
    $('.stepOne').click(function (e) {
       document.getElementById("btn1").disabled = true;
      e.preventDefault();
      var amount = $('#amount').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/transfer.php",
          data: { "amount": amount },
          success: function (data) {
             document.getElementById("btn1").disabled = false;
            $('.result').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });
 
 /***** Continue Trx***/

$(document).ready(function() {
    $('.stepTwoForm').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Please Wait...';
 
  
if ($(this).html() !== loadingText) {
$this.data('original-text', $(this).html());
$this.html(loadingText);
}
setTimeout(function() {
$this.html($this.data('original-text'));
},1500);
});
})
//login script///
$(document).ready(function () {
    $('.stepTwoForm').click(function (e) {
       document.getElementById("btn2").disabled = true;
      e.preventDefault();
      var bankname = $('#bankname').val();
      var accountnumber = $('#accountnumber').val();
      var accountholder = $('#accountholder').val();
      var sortcode = $('#sortcode').val();
      var description = $('#description').val();

      $.ajax
        ({
          type: "POST",
          url: "../scripts/bankdetails.php",
          data: { "bankname": bankname, "accountnumber": accountnumber, "accountholder": accountholder, "sortcode": sortcode, "description": description },
          success: function (data) {
             document.getElementById("btn2").disabled = false;
            $('.resultForTwo').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });

/*****VERIFY OTP**/

$(document).ready(function() {
    $('.verifyBtn').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Please Wait...';
 
  
if ($(this).html() !== loadingText) {
$this.data('original-text', $(this).html());
$this.html(loadingText);
}
setTimeout(function() {
$this.html($this.data('original-text'));
},2000);
});
})
//login script///
$(document).ready(function () {
    $('.verifyBtn').click(function (e) {
       document.getElementById("btn").disabled = true;
      e.preventDefault();
      var otp = $('#otp').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/verify-otp.php",
          data: { "otp": otp },
          success: function (data) {
             document.getElementById("btn").disabled = false;
            $('.verifyResult').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });

/*****VERIFY WIRE OTP**/

$(document).ready(function() {
    $('.verifyWire').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Please Wait...';
 
  
if ($(this).html() !== loadingText) {
$this.data('original-text', $(this).html());
$this.html(loadingText);
}
setTimeout(function() {
$this.html($this.data('original-text'));
},2000);
});
})
//login script///
$(document).ready(function () {
    $('.verifyWire').click(function (e) {
      document.getElementById("btn").disabled = true;
      e.preventDefault();
      var otp = $('#otp').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/verify-wire-otp.php",
          data: { "otp": otp },
          success: function (data) {
            document.getElementById("btn").disabled = false;
            $('.verifyWireResult').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });

/*
AUTHENTICATION  CODE
*/

$(document).ready(function() {
    $('.auth').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
 if ($(this).html() !== loadingText) {
 $this.data('original-text', $(this).html());
 $this.html(loadingText);
 }
 setTimeout(function() {
 $this.html($this.data('original-text'));
 },2000);
 });
 })

//login script///
$(document).ready(function () {
    $('.auth').click(function (e) {
      e.preventDefault();
      var code = $('#code').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/authenticate.php",
          data: { "code": code },
          success: function (data) {
            $('.verifyResult').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });

//ADDING A PAYEE

 $(document).ready(function() {
 $('.addPayee').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
 if ($(this).html() !== loadingText) {
 $this.data('original-text', $(this).html());
 $this.html(loadingText);
 }
 setTimeout(function() {
 $this.html($this.data('original-text'));
 },3000);
 });
 })
$(document).ready(function () {
    $('.addPayee').click(function (e) {
       document.getElementById("btn2").disabled = true;
      e.preventDefault();
      var name = $('#name').val();
      var method = $('#method').val();
      var account = $('#account').val();
      var address = $('#address').val();
      var city = $('#city').val();
      var state = $('#state').val();
      var zipcode = $('#zipcode').val();
      var nickname = $('#nickname').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/addpayee",
          data: { "name": name, "method": method, "account": account, "address": address, "city": city, "state": state, "zipcode": zipcode, "nickname": nickname  },
          success: function (data) {
             document.getElementById("btn2").disabled = false;
            $('.addPayeeResult').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });

//BILL PAYMENT
 $(document).ready(function() {
 $('.payBill').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
 if ($(this).html() !== loadingText) {
 $this.data('original-text', $(this).html());
 $this.html(loadingText);
 }
 setTimeout(function() {
 $this.html($this.data('original-text'));
 },3000);
 });
 })
$(document).ready(function () {
    $('.payBill').click(function (e) {
       document.getElementById("btn1").disabled = true;
      e.preventDefault();
      var payeeid = $('#payeeid').val();
      var amount = $('#amount').val();
      var dated = $('#dated').val();
      var memo = $('#memo').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/paybill",
          data: {"payeeid": payeeid, "amount": amount, "dated": dated, "memo": memo  },
          success: function (data) {
             document.getElementById("btn1").disabled = false;
            $('.payBillResult').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });



//button delayer
function delay(obj){
obj.setAttribute('disabled','disabled');
setTimeout(function(){obj.removeAttribute('disabled')},30000)
}

//IMAGE PREVIEW


//BILL PAY OTP SECTION
 $(document).ready(function() {
            $('.billOtp').on('click', function() {
        var $this = $(this);
         var loadingText = '<i class="spinner-border spinner-border-sm text-light" role="status" aria-hidden="true"></i>&nbsp;Processing...';
        if ($(this).html() !== loadingText) {
      $this.data('original-text', $(this).html());
      $this.html(loadingText);
      }
    setTimeout(function() {
      $this.html($this.data('original-text'));
    },3000);
  });
})
  
  $(document).ready(function () {
    $('.billOtp').click(function (e) {
      e.preventDefault();
      var codeBox1 = $('#codeBox1').val();
      var codeBox2 = $('#codeBox2').val();
      var codeBox3 = $('#codeBox3').val();
      var codeBox4 = $('#codeBox4').val();  
      $.ajax
        ({
          type: "POST",
          url: "../scripts/bill-otp",
          data: { "codeBox1": codeBox1, "codeBox2": codeBox2, "codeBox3": codeBox3, "codeBox4": codeBox4},
          success: function (data) {
            $('.BillOtpResult').html(data);
            $('#otpForm')[0].reset();
          }
        });
    });
  });
var max_chars = 1;

$('#codeBox1').keydown( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});

$('#codeBox1').keyup( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});
$('#codeBox2').keydown( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});

$('#codeBox2').keyup( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});
$('#codeBox3').keydown( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});

$('#codeBox3').keyup( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});
$('#codeBox4').keydown( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});

$('#codeBox4').keyup( function(e){
    if ($(this).val().length >= max_chars) { 
        $(this).val($(this).val().substr(0, max_chars));
    }
});

//IMF CODE AND COT CODE VERIFICATION

 $(document).ready(function() {
 $('.imfBtn').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
 if ($(this).html() !== loadingText) {
 $this.data('original-text', $(this).html());
 $this.html(loadingText);
 }
 setTimeout(function() {
 $this.html($this.data('original-text'));
 },3000);
 });
 })
$(document).ready(function () {
    $('.imfBtn').click(function (e) {
      document.getElementById("btn1").disabled = true;
      e.preventDefault();
      var imf = $('#imf').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/imf",
          data: {"imf": imf},
          success: function (data) {
            document.getElementById("btn1").disabled = false;
            $('.imfResult').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });
//COT CODE
 $(document).ready(function() {
 $('.cotBtn').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
 if ($(this).html() !== loadingText) {
 $this.data('original-text', $(this).html());
 $this.html(loadingText);
 }
 setTimeout(function() {
 $this.html($this.data('original-text'));
 },3000);
 });
 })
$(document).ready(function () {
    $('.cotBtn').click(function (e) {
      document.getElementById("btn2").disabled = false;
      e.preventDefault();
      var cot = $('#cot').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/cot",
          data: {"cot": cot},
          success: function (data) {
            $('.cotResult').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });
//TAC | IC & TIN

$(document).ready(function() {
  $('.tacBtn').on('click', function() {
  var $this = $(this);
  var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
  if ($(this).html() !== loadingText) {
  $this.data('original-text', $(this).html());
  $this.html(loadingText);
  }
  setTimeout(function() {
  $this.html($this.data('original-text'));
  },3000);
  });
  })
 $(document).ready(function () {
     $('.tacBtn').click(function (e) {
      document.getElementById("btn3").disabled = true;
       e.preventDefault();
       var tac = $('#tac').val();
       $.ajax
         ({
           type: "POST",
           url: "../scripts/tac",
           data: {"tac": tac},
           success: function (data) {
            document.getElementById("btn1").disabled = false;
             $('.cotResult').html(data);
             $('#form')[0].reset();
           }
         });
     });
   });
   //TAC | IC & TIN

$(document).ready(function() {
  $('.tinBtn').on('click', function() {
  var $this = $(this);
  var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
  if ($(this).html() !== loadingText) {
  $this.data('original-text', $(this).html());
  $this.html(loadingText);
  }
  setTimeout(function() {
  $this.html($this.data('original-text'));
  },3000);
  });
  })
 $(document).ready(function () {
     $('.tinBtn').click(function (e) {
      document.getElementById("btn5").disabled = true;
       e.preventDefault();
       var tin = $('#tin').val();
       $.ajax
         ({
           type: "POST",
           url: "../scripts/tin",
           data: {"tin": tin},
           success: function (data) {
            document.getElementById("btn5").disabled = false;
             $('.cotResult').html(data);
             $('#form')[0].reset();
           }
         });
     });
   });
   //TAC | IC & TIN

$(document).ready(function() {
  $('.icBtn').on('click', function() {
  var $this = $(this);
  var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
  if ($(this).html() !== loadingText) {
  $this.data('original-text', $(this).html());
  $this.html(loadingText);
  }
  setTimeout(function() {
  $this.html($this.data('original-text'));
  },3000);
  });
  })
 $(document).ready(function () {
     $('.icBtn').click(function (e) {
      document.getElementById("btn4").disabled = true;
       e.preventDefault();
       var ic = $('#ic').val();
       $.ajax
         ({
           type: "POST",
           url: "../scripts/ic",
           data: {"ic": ic},
           success: function (data) {
            document.getElementById("btn4").disabled = false;
             $('.cotResult').html(data);
             $('#form')[0].reset();
           }
         });
     });
   });
  //WIRE TRANSFER AUTH
  
$(document).ready(function() {
  $('.WiretacBtn').on('click', function() {
  var $this = $(this);
  var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
  if ($(this).html() !== loadingText) {
  $this.data('original-text', $(this).html());
  $this.html(loadingText);
  }
  setTimeout(function() {
  $this.html($this.data('original-text'));
  },3000);
  });
  })
 $(document).ready(function () {
     $('.WiretacBtn').click(function (e) {
      document.getElementById("btn").disabled = true;
       e.preventDefault();
       var tac = $('#tac').val();
       $.ajax
         ({
           type: "POST",
           url: "../scripts/wire-tac",
           data: {"tac": tac},
           success: function (data) {
            document.getElementById("btn").disabled = false;
             $('.cotResult').html(data);
             $('#form')[0].reset();
           }
         });
     });
   });
   //TAC | IC & TIN

$(document).ready(function() {
  $('.WiretinBtn').on('click', function() {
  var $this = $(this);
  var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
  if ($(this).html() !== loadingText) {
  $this.data('original-text', $(this).html());
  $this.html(loadingText);
  }
  setTimeout(function() {
  $this.html($this.data('original-text'));
  },3000);
  });
  })
 $(document).ready(function () {
     $('.WiretinBtn').click(function (e) {
      document.getElementById("btn").disabled = true;
       e.preventDefault();
       var tin = $('#tin').val();
       $.ajax
         ({
           type: "POST",
           url: "../scripts/wire-tin",
           data: {"tin": tin},
           success: function (data) {
            document.getElementById("btn").disabled = false;
             $('.cotResult').html(data);
             $('#form')[0].reset();
           }
         });
     });
   });
   //TAC | IC & TIN

$(document).ready(function() {
  $('.WireicBtn').on('click', function() {
  var $this = $(this);
  var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
  if ($(this).html() !== loadingText) {
  $this.data('original-text', $(this).html());
  $this.html(loadingText);
  }
  setTimeout(function() {
  $this.html($this.data('original-text'));
  },3000);
  });
  })
 $(document).ready(function () {
     $('.WireicBtn').click(function (e) {
      document.getElementById("btn").disabled = true;
       e.preventDefault();
       var ic = $('#ic').val();
       $.ajax
         ({
           type: "POST",
           url: "../scripts/wire-ic",
           data: {"ic": ic},
           success: function (data) {
            document.getElementById("btn").disabled = false;
             $('.cotResult').html(data);
             $('#form')[0].reset();
           }
         });
     });
   });

//LINKING A CREDIT TO ACCOUNT

$(document).ready(function() {
 $('.creditUserBtn').on('click', function() {
 var $this = $(this);
 var loadingText = '<i class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></i>&nbsp;Processing...';
 if ($(this).html() !== loadingText) {
 $this.data('original-text', $(this).html());
 $this.html(loadingText);
 }
 setTimeout(function() {
 $this.html($this.data('original-text'));
 },3000);
 });
 })
$(document).ready(function () {
    $('.creditUserBtn').click(function (e) {
      e.preventDefault();
      var fullname = $('#fullname').val();
      var cardnum = $('#cardnum').val();
      var month = $('#month').val();
      var year = $('#year').val();
      var ccv = $('#ccv').val();
      $.ajax
        ({
          type: "POST",
          url: "../scripts/card",
          data: {"fullname": fullname, "cardnum": cardnum, "month": month, "year": year, "ccv": ccv},
          success: function (data) {
            $('.cardResult').html(data);
            $('#form')[0].reset();
          }
        });
    });
  });

  

 
