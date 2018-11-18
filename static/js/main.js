(function ($) {
  "use strict";

  // Preloader
  $(window).on('load', function () {
    if ($('#preloader').length) {
      $('#preloader').delay(100).fadeOut('slow', function () {
        $(this).remove();
      });
    }
  });

  // Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });
  $('.back-to-top').click(function(){
    $('html, body').animate({scrollTop : 0},1500, 'easeInOutExpo');
    return false;
  });

  // Initiate the wowjs animation library
  new WOW().init();

  // Initiate superfish on nav menu
  $('.nav-menu').superfish({
    animation: {
      opacity: 'show'
    },
    speed: 400
  });

  // Mobile Navigation
  if ($('#nav-menu-container').length) {
    var $mobile_nav = $('#nav-menu-container').clone().prop({
      id: 'mobile-nav'
    });
    $mobile_nav.find('> ul').attr({
      'class': '',
      'id': ''
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" id="mobile-nav-toggle"><i class="fa fa-bars"></i></button>');
    $('body').append('<div id="mobile-body-overly"></div>');
    $('#mobile-nav').find('.menu-has-children').prepend('<i class="fa fa-chevron-down"></i>');

    $(document).on('click', '.menu-has-children i', function(e) {
      $(this).next().toggleClass('menu-item-active');
      $(this).nextAll('ul').eq(0).slideToggle();
      $(this).toggleClass("fa-chevron-up fa-chevron-down");
    });

    $(document).on('click', '#mobile-nav-toggle', function(e) {
      $('body').toggleClass('mobile-nav-active');
      $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
      $('#mobile-body-overly').toggle();
    });

    $(document).click(function(e) {
      var container = $("#mobile-nav, #mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
      }
    });
  } else if ($("#mobile-nav, #mobile-nav-toggle").length) {
    $("#mobile-nav, #mobile-nav-toggle").hide();
  }

  // Smooth scroll for the menu and links with .scrollto classes
  $('.nav-menu a, #mobile-nav a, .scrollto').on('click', function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        var top_space = 0;

        if ($('#header').length) {
          top_space = $('#header').outerHeight();

          if( ! $('#header').hasClass('header-fixed') ) {
            top_space = top_space - 20;
          }
        }

        $('html, body').animate({
          scrollTop: target.offset().top - top_space
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu').length) {
          $('.nav-menu .menu-active').removeClass('menu-active');
          $(this).closest('li').addClass('menu-active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Header scroll class
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('#header').addClass('header-scrolled');
    } else {
      $('#header').removeClass('header-scrolled');
    }
  });

  // Intro carousel
  var introCarousel = $(".carousel");
  var introCarouselIndicators = $(".carousel-indicators");
  introCarousel.find(".carousel-inner").children(".carousel-item").each(function(index) {
    (index === 0) ?
    introCarouselIndicators.append("<li data-target='#introCarousel' data-slide-to='" + index + "' class='active'></li>") :
    introCarouselIndicators.append("<li data-target='#introCarousel' data-slide-to='" + index + "'></li>");

    $(this).css("background-image", "url('" + $(this).children('.carousel-background').children('img').attr('src') +"')");
    $(this).children('.carousel-background').remove();
  });

  $(".carousel").swipe({
    swipe: function(event, direction, distance, duration, fingerCount, fingerData) {
      if (direction == 'left') $(this).carousel('next');
      if (direction == 'right') $(this).carousel('prev');
    },
    allowPageScroll:"vertical"
  });

  // Skills section
  $('#skills').waypoint(function() {
    $('.progress .progress-bar').each(function() {
      $(this).css("width", $(this).attr("aria-valuenow") + '%');
    });
  }, { offset: '80%'} );

  // jQuery counterUp (used in Facts section)
  $('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 1000
  });

  // Porfolio isotope and filter
  var portfolioIsotope = $('.portfolio-container').isotope({
    itemSelector: '.portfolio-item',
    layoutMode: 'fitRows'
  });

  $('#portfolio-flters li').on( 'click', function() {
    $("#portfolio-flters li").removeClass('filter-active');
    $(this).addClass('filter-active');

    portfolioIsotope.isotope({ filter: $(this).data('filter') });
  });

  // Clients carousel (uses the Owl Carousel library)
  $(".clients-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    responsive: { 0: { items: 2 }, 768: { items: 4 }, 900: { items: 6 }
    }
  });

  // Testimonials carousel (uses the Owl Carousel library)
  $(".testimonials-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

})(jQuery);

function agregarExp(){ 
  var divContExp = document.createElement("div");
  var divGroupEmpresa = document.createElement("div");
  var divGroupUbicacion = document.createElement("div");
  var divGroupPuesto = document.createElement("div");
  var divGroupTareas = document.createElement("div");
  var divGroupInicio = document.createElement("div");
  var divGroupFinal = document.createElement("div");
  var inputPuesto = document.createElement("input");
  var inputEmpresa = document.createElement("input");
  var inputEmpresaUbicacion = document.createElement("input");
  var inputAñoInicio = document.createElement("input");
  var inputAñoFinal = document.createElement("input");
  var inputTareas = document.createElement("input");
  var labelPuesto = document.createElement("label");
  var nodePuesto = document.createTextNode("Puesto que ejercia");
  var labelEmpresa = document.createElement("label");
  var nodeEmpresa = document.createTextNode("Empresa en la que trabajaba");
  var labelUbicacion = document.createElement("label");
  var nodeUbicacion = document.createTextNode("Ubicacion de la empresa");
  var labelAñoInicio = document.createElement("label");
  var nodeAñoInicio = document.createTextNode("Fecha en que inicio");
  var labelAñoFinal = document.createElement("label");
  var nodeAñoFinal = document.createTextNode("Fecha en que finalizo");
  var labelTareas = document.createElement("label");
  var nodeTareas = document.createTextNode("Tareas que realizaba");
  var divCont = document.getElementById("experiencia");
  

  divGroupEmpresa.setAttribute("class","form-group col-md-8");
  divGroupUbicacion.setAttribute("class","form-group col-md-8");
  divGroupPuesto.setAttribute("class","form-group col-md-8");
  divGroupTareas.setAttribute("class","form-group col-md-8");
  divGroupInicio.setAttribute("class","form-group col-md-8");
  divGroupFinal.setAttribute("class","form-group col-md-8");
  divContExp.setAttribute("style","padding:10px; border:solid; margin-right:400px; margin-botton:15px; display:center; vertical-align:middle;");
  inputAñoInicio.setAttribute("type","date");
  inputAñoFinal.setAttribute("type","date");

  inputEmpresa.setAttribute("class","form-control");
  inputEmpresa.setAttribute("placeholder","Nombre de la empresa");
  inputEmpresaUbicacion.setAttribute("class","form-control");
  inputEmpresaUbicacion.setAttribute("placeholder","Ubicacion de la empresa");
  inputPuesto.setAttribute("class","form-control");
  inputPuesto.setAttribute("placeholder","Nombre del puesto que ejercia");
  inputTareas.setAttribute("class","form-control");
  inputTareas.setAttribute("placeholder","Ingrese las tareas separadas por ','");
  inputAñoInicio.setAttribute("class","form-control");
  inputAñoInicio.setAttribute("placeholder","dd/mm/aaaa");
  inputAñoFinal.setAttribute("class","form-control");
  inputAñoFinal.setAttribute("placeholder","dd/mm/aaaa");
  
  
  labelEmpresa.appendChild(nodeEmpresa);
  labelUbicacion.appendChild(nodeUbicacion);
  labelPuesto.appendChild(nodePuesto);
  labelTareas.appendChild(nodeTareas);
  labelAñoInicio.appendChild(nodeAñoInicio);
  labelAñoFinal.appendChild(nodeAñoFinal);
  divGroupEmpresa.appendChild(labelEmpresa);
  divGroupEmpresa.appendChild(inputEmpresa);
  divGroupUbicacion.appendChild(labelUbicacion);
  divGroupUbicacion.appendChild(inputEmpresaUbicacion);
  divGroupPuesto.appendChild(labelPuesto);
  divGroupPuesto.appendChild(inputPuesto);
  divGroupTareas.appendChild(labelTareas);
  divGroupTareas.appendChild(inputTareas);
  divGroupInicio.appendChild(labelAñoInicio);
  divGroupInicio.appendChild(inputAñoInicio);
  divGroupFinal.appendChild(labelAñoFinal);
  divGroupFinal.appendChild(inputAñoFinal);
  divContExp.appendChild(divGroupEmpresa);
  divContExp.appendChild(divGroupUbicacion);
  divContExp.appendChild(divGroupPuesto);
  divContExp.appendChild(divGroupTareas);
  divContExp.appendChild(divGroupInicio);
  divContExp.appendChild(divGroupFinal);
  divCont.appendChild(divContExp);
  $('html,body').animate({
    	scrollTop: $("#experiencia").offset().top
	}, 1000);
}

function agregarEducacion(){
  var divContExp = document.createElement("div");
  var divRow = document.createElement("div");
  var divGroup = document.createElement("div");
  var divGroupGrado = document.createElement("div");
  var divGroupEsp = document.createElement("div");
  var input = document.createElement("input");
  var divCont = document.getElementById("educacion");
  var label = document.createElement("label");
  var node = document.createTextNode("Institucion");
  var inputGrado = document.createElement("input");
  var labelGrado = document.createElement("label");
  var nodeGrado = document.createTextNode("Grado academico");
  var inputEsp = document.createElement("input");
  var labelEsp = document.createElement("label");
  var nodeEsp = document.createTextNode("Especializacion");
  
  divContExp.setAttribute("style","padding:10px; border:solid; margin-right:400px; margin-botton:15px; display:center; vertical-align:middle;");
  divRow.setAttribute("class","form-row");
  divGroup.setAttribute("class","form-group col-md-8");
  divGroupGrado.setAttribute("class","form-group col-md-8");
  divGroupEsp.setAttribute("class","form-group col-md-8");
  input.setAttribute("class","form-control");
  input.setAttribute("placeholder","Ingrese el nombre de la institucion");
  inputGrado.setAttribute("class","form-control");
  inputGrado.setAttribute("placeholder","Ingrese el grado academico");
  inputEsp.setAttribute("class","form-control");
  inputEsp.setAttribute("placeholder","Ingrese la Especializacion obtenida");
  
  label.appendChild(node);
  labelGrado.appendChild(nodeGrado);
  labelEsp.appendChild(nodeEsp);
  divGroup.appendChild(label);
  divGroup.appendChild(input);
  divGroupGrado.appendChild(labelGrado);
  divGroupGrado.appendChild(inputGrado);
  divGroupEsp.appendChild(labelEsp);
  divGroupEsp.appendChild(inputEsp);
  divContExp.appendChild(divGroup);
  divContExp.appendChild(divGroupGrado);
  divContExp.appendChild(divGroupEsp);
  divCont.appendChild(divContExp);
  $('html,body').animate({
    	scrollTop: $("#educacion").offset().top
	}, 1000);
}

function agregarHabilidad(){
  var divContExp = document.createElement("div");
  var divRow = document.createElement("div");
  var divGroup = document.createElement("div");
  var input = document.createElement("input");
  var divCont = document.getElementById("habilidades");
  var label = document.createElement("label");
  var node = document.createTextNode("Habilidad");
  
  divContExp.setAttribute("style","padding:10px; border:solid; margin-right:400px; margin-botton:15px; display:center; vertical-align:middle;");
  divRow.setAttribute("class","form-row");
  divGroup.setAttribute("class","form-group col-md-8");
  input.setAttribute("class","form-control");
  input.setAttribute("placeholder","Ingrese la habilidad");
  
  label.appendChild(node);
  divGroup.appendChild(label);
  divGroup.appendChild(input);
  divRow.appendChild(divGroup);
  divContExp.appendChild(divRow); 
  divCont.appendChild(divContExp);
  $('html,body').animate({
    	scrollTop: $("#habilidades").offset().top
	}, 1000);

}

function limpiar(){
  
  var opcion = confirm("¿Desea limpiar el formulario?");
  if (opcion) {
    document.getElementById("formCV").reset();
    document.getElementById("txtNombre").focus();
    $('html, body').animate({scrollTop:0}, 'slow');
  }else{

  }
}

function limpiarRegistroForm(){
  var opcion = confirm("¿Desea limpiar el formulario?");
  if (opcion) {
    document.getElementById("registroForm").reset();
    document.getElementById("first_name").focus();
    $('html, body').animate({scrollTop:0}, 'slow');
  }else{

  }
}
