(function(){
  var d=document, root=d.documentElement;
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.add('loaded')})});

  /* nav: scrolled state, active link, mobile sheet */
  var nav=d.querySelector('.nav'), sheet=d.getElementById('sheet'), burger=d.querySelector('.burger');
  function onScroll(){nav.classList.toggle('scrolled',scrollY>24)}
  addEventListener('scroll',onScroll,{passive:true}); onScroll();
  function setSheet(open){sheet.classList.toggle('open',open);burger.setAttribute('aria-expanded',open);sheet.toggleAttribute('inert',!open)}
  burger.addEventListener('click',function(){setSheet(!sheet.classList.contains('open'))});
  sheet.addEventListener('click',function(e){if(e.target.closest('a'))setSheet(false)});
  d.addEventListener('keydown',function(e){if(e.key==='Escape')setSheet(false)});
  setSheet(false);
  var links=[].slice.call(d.querySelectorAll('.links a[href^="#"]'));
  if('IntersectionObserver' in window){
    var spy=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){links.forEach(function(a){a.classList.toggle('active',a.getAttribute('href')==='#'+en.target.id)})}})},{rootMargin:'-45% 0px -50% 0px'});
    links.forEach(function(a){var s=d.querySelector(a.getAttribute('href'));if(s)spy.observe(s)});
  }

  /* countdown to 9 Jan 2027, 10:00 Dhaka */
  var BND='০১২৩৪৫৬৭৮৯';
  function isBn(){return root.getAttribute('data-lang')==='bn'}
  function bd(s){return String(s).replace(/[0-9]/g,function(x){return BND[x]})}
  function T(en,bn){return '<span class="en">'+en+'</span><span class="bn" lang="bn">'+bn+'</span>'}
  var target=new Date(root.dataset.start).getTime(), cd=d.getElementById('cd'), timer;
  function pad(n){return n<10?'0'+n:''+n}
  function tick(){
    clearTimeout(timer);var ms=target-Date.now();
    if(ms<=0){cd.innerHTML=ms>-7*3600e3?'<div class="u"><div class="n">'+T('Live','লাইভ')+'</div><div class="t">'+T('happening now','এখন চলছে')+'</div></div>':'<div class="u"><div class="n">'+T('Thank you','ধন্যবাদ')+'</div><div class="t">'+T('for lighting the way','পথ আলোকিত করার জন্য')+'</div></div>';return}
    var s=Math.floor(ms/1000),v=[Math.floor(s/86400),Math.floor(s%86400/3600),Math.floor(s%3600/60),s%60],bn=isBn();
    cd.querySelectorAll('.n').forEach(function(n,i){var t=i?pad(v[i]):''+v[i];if(bn)t=bd(t);if(n.textContent!==t)n.textContent=t});
    timer=setTimeout(tick,1000-Date.now()%1000);
  }
  tick();

  /* language toggle (shared with register.html via the same storage key) */
  var lb=d.querySelectorAll('.lang button');
  function setLang(l,save){
    root.setAttribute('data-lang',l);root.lang=l;
    document.title=root.getAttribute(l==='bn'?'data-title-bn':'data-title-en');
    lb.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.l===l)});
    if(save){try{sessionStorage.setItem('alokbortika.site.lang',l);localStorage.setItem('alokbortika.lang.v1',JSON.stringify(l))}catch(e){}}
    tick();
  }
  lb.forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.l,true)})});
  setLang(isBn()?'bn':'en',false);


  /* phases: mark done / now from today's date */
  var today=new Date(); d.querySelectorAll('.phase').forEach(function(p){
    var a=new Date(p.dataset.from+'T00:00:00+06:00'),b=new Date(p.dataset.to+'T23:59:59+06:00');
    if(today>b)p.classList.add('done');else if(today>=a){p.classList.add('now');p.querySelector('.when').insertAdjacentHTML('beforeend','<i>'+T('Now','চলছে')+'</i>')}
  });
  var next=d.querySelector('.phase.now'); if(!next){var up=[].filter.call(d.querySelectorAll('.phase'),function(p){return !p.classList.contains('done')})[0]; if(up){up.classList.add('now');up.querySelector('.when').insertAdjacentHTML('beforeend','<i>'+T('Up next','আসছে')+'</i>')}}

  /* evidence counters: numbers climb in step with the bars and rings */
  function runCount(el){
    var to=parseFloat(el.dataset.count),dec=+el.dataset.dec||0,pre=el.dataset.pre||'',suf=el.dataset.suf||'',b=el.hasAttribute('data-b'),t0=null,dur=1600;
    function out(v){var s=pre+v.toFixed(dec)+suf;el.textContent=b?bd(s):s}
    if(reduce){out(to);return}
    out(0);function f(t){if(!t0)t0=t;var p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);out(to*e);if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f);
  }
  if('IntersectionObserver' in window&&!reduce){
    var cio=new IntersectionObserver(function(es){es.forEach(function(en){if(!en.isIntersecting)return;cio.unobserve(en.target);runCount(en.target)})},{threshold:.6});
    d.querySelectorAll('.ct').forEach(function(el){cio.observe(el)});
  }
  /* in-view: count-up, bars, rings, climb, reveals */
  function countUp(el){
    var raw=el.dataset.n, m=raw.match(/^(\D*)([\d,]+)(.*)$/); if(!m||reduce){return}
    var pre=m[1],end=parseInt(m[2].replace(/,/g,''),10),post=m[3],t0=null,dur=1400,b=el.hasAttribute('data-b');
    function out(n){var s=pre+n.toLocaleString('en-US')+post;el.textContent=b?bd(s):s}
    function f(t){if(!t0)t0=t;var p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);out(Math.round(end*e));if(p<1)requestAnimationFrame(f)}
    out(0); requestAnimationFrame(f);
  }
  var watch=d.querySelectorAll('[data-n],.bars,.gaps,.climb,.rubric,.rv');
  if('IntersectionObserver' in window&&!reduce){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(!en.isIntersecting)return;var el=en.target;io.unobserve(el);if(el.dataset.n)countUp(el);else el.classList.add('in')})},{threshold:.28});
    watch.forEach(function(el){io.observe(el)});
  }else watch.forEach(function(el){el.classList.add('in')});

  /* speaker filters */
  var fb=d.querySelectorAll('.filters button'), cards=d.querySelectorAll('.person');
  fb.forEach(function(b){b.addEventListener('click',function(){
    fb.forEach(function(x){x.setAttribute('aria-pressed',x===b)});
    var f=b.dataset.f; cards.forEach(function(c){c.hidden=!(f==='all'||c.dataset.g===f||c.dataset.p===f)});
  })});

  /* open a panel when linked from a speaker card */
  d.addEventListener('click',function(e){var a=e.target.closest('a[href^="#panel-"]');if(!a)return;var p=d.querySelector(a.getAttribute('href'));if(p&&p.tagName==='DETAILS')p.open=true});

  /* venue legend <-> map */
  var spots=d.querySelectorAll('.map .spot'), lg=d.querySelectorAll('.legend button');
  function hl(k){spots.forEach(function(s){s.classList.toggle('on',s.dataset.k===k)});lg.forEach(function(b){b.classList.toggle('on',b.dataset.k===k)})}
  lg.forEach(function(b){['mouseenter','focus','click'].forEach(function(ev){b.addEventListener(ev,function(){hl(b.dataset.k)})})});
  spots.forEach(function(s){s.addEventListener('mouseenter',function(){hl(s.dataset.k)});s.addEventListener('click',function(){hl(s.dataset.k)})});
  hl('1');

/* ---------- helpers for canvases ---------- */
  function sprite(rgb,size){var c=d.createElement('canvas');c.width=c.height=size;var x=c.getContext('2d'),g=x.createRadialGradient(size/2,size/2,0,size/2,size/2,size/2);
    g.addColorStop(0,'rgba('+rgb+',1)');g.addColorStop(.25,'rgba('+rgb+',.55)');g.addColorStop(1,'rgba('+rgb+',0)');x.fillStyle=g;x.fillRect(0,0,size,size);return c}
  function runWhenVisible(el,frame){
    var on=true,vis=true,raf;
    function loop(t){if(!on)return;frame(t);raf=requestAnimationFrame(loop)}
    function sync(){var want=vis&&!d.hidden;if(want&&!on){on=true;raf=requestAnimationFrame(loop)}else if(!want){on=false;cancelAnimationFrame(raf)}}
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting;sync()}).observe(el);
    d.addEventListener('visibilitychange',sync);
    raf=requestAnimationFrame(loop);
  }
  
  /* ---------- hero map: light spreading from Rangpur ---------- */
  (function(){
    var cv=d.getElementById('map'); if(!cv)return;
    var M=JSON.parse(d.getElementById('mapdata').textContent), ctx=cv.getContext('2d');
    var shape=new Path2D(M.d), R=M.C.Rangpur, GOLD=sprite('255,184,0',64), CYAN=sprite('19,181,214',64), WHITE=sprite('255,240,200',64);
    var NAMES={Dhaka:'ঢাকা',Chattogram:'চট্টগ্রাম',Sylhet:'সিলেট',Khulna:'খুলনা',Rajshahi:'রাজশাহী',Barishal:'বরিশাল',Mymensingh:'ময়মনসিংহ'};
    var cities=Object.keys(M.C).filter(function(k){return k!=='Rangpur'}).map(function(k){var c=M.C[k],dx=c[0]-R[0],dy=c[1]-R[1],len=Math.hypot(dx,dy);
      return {k:k,x:c[0],y:c[1],dist:len,cx:(R[0]+c[0])/2+dy*.18,cy:(R[1]+c[1])/2-dx*.18,ph:Math.random()}});
    var maxD=0, pts=M.pts.map(function(p,i){var dd=Math.hypot(p[0]-R[0],p[1]-R[1]);maxD=Math.max(maxD,dd);return {x:p[0],y:p[1],dist:dd,j:(Math.sin(i*12.9898)*43758.5453%1+1)%1}});
    var W,H,s,dpr,base=d.createElement('canvas'),bctx=base.getContext('2d');
    function size(){dpr=Math.min(devicePixelRatio||1,2);W=cv.clientWidth;H=cv.clientHeight;if(!W)return;s=W/M.W;cv.width=W*dpr;cv.height=H*dpr;
      base.width=cv.width;base.height=cv.height;bctx.setTransform(dpr*s,0,0,dpr*s,0,0);
      bctx.save();bctx.translate(6/s,7/s);bctx.fillStyle='#0B1220';bctx.fill(shape);bctx.restore();
      var g=bctx.createLinearGradient(0,0,0,M.H);g.addColorStop(0,'#0F4C86');g.addColorStop(1,'#0A2A52');
      bctx.fillStyle=g;bctx.fill(shape);bctx.lineWidth=2.6/s;bctx.lineJoin='round';bctx.strokeStyle='#0B1220';bctx.stroke(shape);
      bctx.save();bctx.clip(shape);bctx.globalAlpha=.06;bctx.strokeStyle='#fff';bctx.lineWidth=.6/s;
      for(var y=0;y<M.H;y+=14){bctx.beginPath();bctx.moveTo(0,y);bctx.lineTo(M.W,y);bctx.stroke()}bctx.restore()}
    size(); addEventListener('resize',size);
    var SPREAD=5200, t0=null;
    function ease(x){return 1-Math.pow(1-x,3)}
    function glow(img,x,y,r,a){if(a<=0.01)return;ctx.globalAlpha=Math.min(1,a);ctx.drawImage(img,x-r,y-r,r*2,r*2)}
    function draw(now){
      if(!W){size();if(!W)return}
      if(t0===null)t0=now; var t=reduce?99999:now-t0;
      ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,W,H);ctx.globalAlpha=1;ctx.drawImage(base,0,0,W,H);
      var wave=ease(Math.min(1,t/SPREAD))*maxD*1.02;
      // repeating ripple after the first spread
      var rp=t>SPREAD?((t-SPREAD)%4600)/4600:-1, ripR=rp>=0?ease(rp)*maxD*1.05:-999;
      ctx.save();ctx.scale(s,s);
      // spreading ring
      ctx.save();ctx.clip(shape);
      if(t<SPREAD+400){ctx.globalAlpha=Math.max(0,1-t/(SPREAD+400))*.5;ctx.strokeStyle='#FFB800';ctx.lineWidth=2/s;ctx.beginPath();ctx.arc(R[0],R[1],wave,0,6.2832);ctx.stroke()}
      if(rp>=0){ctx.globalAlpha=(1-rp)*.35;ctx.strokeStyle='#FFD35C';ctx.lineWidth=1.4/s;ctx.beginPath();ctx.arc(R[0],R[1],ripR,0,6.2832);ctx.stroke()}
      ctx.restore();
      // arcs to divisional cities
      cities.forEach(function(c){
        var reach=wave/c.dist; if(reach<=0)return; var p=Math.min(1,(t-SPREAD*c.dist/maxD)/900); if(reach<1)p=0; if(reduce)p=1; if(p<=0)return;
        ctx.globalAlpha=.55;ctx.strokeStyle='#13B5D6';ctx.lineWidth=1.3/s;ctx.setLineDash([]);
        ctx.beginPath();var n=24,q=Math.round(n*p);ctx.moveTo(R[0],R[1]);
        for(var i=1;i<=q;i++){var u=i/n,a=(1-u)*(1-u),b=2*(1-u)*u,e=u*u;ctx.lineTo(a*R[0]+b*c.cx+e*c.x,a*R[1]+b*c.cy+e*c.y)}ctx.stroke();
        if(p>=1&&!reduce){var u2=((t/2600)+c.ph)%1,a2=(1-u2)*(1-u2),b2=2*(1-u2)*u2,e2=u2*u2;glow(GOLD,a2*R[0]+b2*c.cx+e2*c.x,a2*R[1]+b2*c.cy+e2*c.y,9,.9*Math.sin(u2*Math.PI))}
      });
      // communities
      for(var i=0;i<pts.length;i++){var p=pts[i],lit=wave>=p.dist+p.j*30;
        if(!lit){ctx.globalAlpha=.35;ctx.fillStyle='#5D8BBE';ctx.fillRect(p.x-1,p.y-1,2,2);continue}
        var since=reduce?9e9:t-SPREAD*(p.dist/maxD), flash=Math.max(0,1-since/700);
        var tw=.55+.18*Math.sin(t/900+p.j*20), boost=rp>=0?Math.exp(-Math.pow((ripR-p.dist)/18,2))*.6:0;
        glow(GOLD,p.x,p.y,6+flash*8+boost*5,tw+flash*.6+boost);
        ctx.globalAlpha=1;ctx.fillStyle='#FFE9A8';ctx.fillRect(p.x-.9,p.y-.9,1.8,1.8);
      }
      // cities + labels
      var bn=isBn(); ctx.font='600 '+(12/s*.9)+'px '+(bn?'"Noto Sans Bengali"':'"Schibsted Grotesk"')+',sans-serif';
      cities.forEach(function(c){var on=wave>=c.dist;glow(CYAN,c.x,c.y,on?14:8,on?1:.35);ctx.globalAlpha=1;ctx.fillStyle=on?'#BFF3FF':'#4B6488';ctx.beginPath();ctx.arc(c.x,c.y,2.6,0,6.2832);ctx.fill();
        if(on){ctx.globalAlpha=Math.min(1,(t-SPREAD*c.dist/maxD)/600)*.85;if(reduce)ctx.globalAlpha=.85;ctx.fillStyle='#D5ECFA';var lbl=bn?NAMES[c.k]:c.k;if(c.x>M.W*.78){ctx.textAlign='right';ctx.fillText(lbl,c.x-7,c.y+4);ctx.textAlign='left'}else ctx.fillText(lbl,c.x+7,c.y+4)}});
      // Rangpur beacon
      var pulse=(t%2400)/2400;
      if(!reduce)for(var k=0;k<2;k++){var ph=(pulse+k*.5)%1;ctx.globalAlpha=(1-ph)*.6;ctx.strokeStyle='#FFB800';ctx.lineWidth=1.4/s;ctx.beginPath();ctx.arc(R[0],R[1],6+ph*34,0,6.2832);ctx.stroke()}
      glow(WHITE,R[0],R[1],34,.9);glow(GOLD,R[0],R[1],22,1);
      ctx.globalAlpha=1;ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(R[0],R[1],4,0,6.2832);ctx.fill();
      ctx.restore();ctx.globalAlpha=1;
    }
    if(reduce){draw(0);addEventListener('resize',function(){draw(0)});return}
    runWhenVisible(d.querySelector('.mapbox'),draw);
  })();
  
  
  /* hero light motes */
  var cv=d.getElementById('motes'); if(!cv||reduce)return;
  var ctx=cv.getContext('2d'),W,H,dpr,ps=[],run=true,cols=['255,205,0','255,138,0','1,186,220','255,255,255'];
  function size(){dpr=Math.min(devicePixelRatio||1,2);W=cv.clientWidth;H=cv.clientHeight;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0)}
  function spawn(init){var w=W>900;return{x:w?W*(.5+Math.random()*.5):Math.random()*W,y:init?Math.random()*H:H+20,r:1+Math.random()*3.2,v:.25+Math.random()*.7,a:Math.random()*Math.PI*2,s:.004+Math.random()*.01,c:cols[Math.random()*4|0],o:.35+Math.random()*.55}}
  size(); addEventListener('resize',size);
  var N=W<600?28:56; for(var i=0;i<N;i++)ps.push(spawn(true));
  function frame(){
    if(!run)return; ctx.clearRect(0,0,W,H);
    for(var i=0;i<ps.length;i++){var p=ps[i];p.y-=p.v;p.a+=p.s;p.x+=Math.sin(p.a)*.4;
      var fade=Math.min(1,p.y/(H*.35));
      if(p.y<-10){ps[i]=spawn(false);continue}
      var g=ctx.createRadialGradient(p.x,p.y,0,p.x,p.y,p.r*4);
      g.addColorStop(0,'rgba('+p.c+','+(p.o*fade)+')');g.addColorStop(1,'rgba('+p.c+',0)');
      ctx.fillStyle=g;ctx.beginPath();ctx.arc(p.x,p.y,p.r*4,0,6.283);ctx.fill();}
    requestAnimationFrame(frame);
  }
  var hero=d.querySelector('.hero'),seen=true;
  function sync(){var want=seen&&!d.hidden;if(want&&!run){run=true;requestAnimationFrame(frame)}else if(!want)run=false}
  if('IntersectionObserver' in window){new IntersectionObserver(function(es){seen=es[0].isIntersecting;sync()}).observe(hero)}
  d.addEventListener('visibilitychange',sync);
  requestAnimationFrame(frame);
})();
