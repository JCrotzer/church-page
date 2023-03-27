var owl = $('.owl-carousel');
owl.owlCarousel({
    items: 1,
    loop:true,
    margin:30,
    // nav:true,
    autoplay: true,
    autoplayTimeout:3000,
    autoplayHoverPause:true,
    responsive:{
        0:{
            items:1,
        },
        700:{
            items:2
        },
        1000:{
            items:3
        }
    }
})