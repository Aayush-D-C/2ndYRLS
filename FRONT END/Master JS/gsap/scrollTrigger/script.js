//Timeline Recap
var tl = gsap.timeline()

tl.from("#page1 #box1",{
    opacity:0,
    scale:0,
    duration:1,
    delay:1,
})

tl.from("#page1 h3",{
    y:30,
    opacity:0,
    duration:1
})

tl.from("#page1 img",{
    opacity:0,
    scale:1.3,
    duration:1.8,
    repeat:-1
})

//Scroll Trigger
gsap.from("#page2 #box2",{
    opacity:0,
    scale:0,
    duration:1,
    rotate:360,
    // scrollTrigger:"#page2 #box2"
    scrollTrigger:{
        trigger:"#page2 #box2",
        scroller:"body",
        markers:true,
        start:"top 60%"
    }
})


gsap.from("#page3 h1",{
    x:1000,
    opacity:0,
    duration:1,
    scrollTrigger:{
        trigger:"#page3 h1",
        toggleActions: "play restart play reverse",
        scroller:"body",
        start:"top 60%"
    }
})

gsap.from("#page3 h2",{
    x:-1000,
    opacity:0,
    duration:1,
    scrollTrigger:{
        trigger:"#page3 h2",
        toggleActions: "play restart play reverse",
        scroller:"body",
        start:"top 80%"
    }
})

gsap.to("#page3",{
    backgroundColor:"purple",
    duration:2,
    scrollTrigger:{
        trigger:"#page3",
        scroller:"body",
        start:"top 30%"
    }
})

//Scrolling horizontally

gsap.to("#page4 h1",{
    transform:"translate(-80%)",
    scrollTrigger:{
        trigger:"#page4",
        scroller:"body",
        toggleActions: "play reverse",
        scrub:2,
        start:"top 0%",
        end:"top -800%",
        pin:true
    }
})