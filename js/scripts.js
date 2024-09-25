/*!
* Start Bootstrap - Freelancer v7.0.5 (https://startbootstrap.com/theme/freelancer)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-freelancer/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 72,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});


//
// isotope.js
//
// Initialize the isotope plugin and retrigger the layout when images load
// init Isotope

var $grid = $('.isotope').each(function (index, element) {
    $(element).isotope({
      itemSelector: '.grid-item',
      layoutMode: 'masonry',
      filter: $(element).attr('data-default-filter')
    });
  }); // layout Isotope after each image loads
  
  $grid.imagesLoaded().progress(function () {
    $grid.isotope('layout');
  }); // filtering
  
  $('[data-isotope-filter]').on('click', function (e) {
    e.preventDefault();
    var isotopeId = ".isotope[data-isotope-id=\"" + $(e.target).closest('[data-isotope-id]').attr('data-isotope-id') + "\"]";
    var filterValue = $(e.target).attr('data-isotope-filter');
    $(isotopeId).isotope({
      filter: filterValue
    }).find('[data-flickity]').each(function (index, instance) {
      var $instance = $(instance);
  
      if ($instance.data().flickity.isInitActivated) {
        $instance.flickity('resize');
      }
    }).end().isotope({
      filter: filterValue
    });
    $(e.target).siblings().removeClass('active');
    $(e.target).addClass('active');
  }); //
