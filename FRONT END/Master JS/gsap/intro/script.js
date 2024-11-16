//For timeline
var tl = gsap.timeline()

tl.from("h2",{
    y:-30,
    duration:0.5,
    delay:0.5,
    opacity:0
})

tl.from("li",{
    y:-30,
    duration:0.5,
    opacity:0,
    stagger:0.3
})

gsap.to("#box1",{
    x:1000,
    duration:2,
    delay:1,
    backgroundColor:"blue",
    rotate:360,
    borderRadius:"50%"
})

gsap.from("#box2",{
    x:1000,
    duration:2,
    delay:1,
    backgroundColor:"red",
    repeat:-1,
    yoyo:true
})

gsap.from("h1",{
    y:120,
    duration:2,
    delay:0.3,
    opacity:0,
    stagger:0.4
})