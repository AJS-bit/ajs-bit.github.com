// 아트보드 전 · 후 스크린샷. node ba_shot.cjs <출력 폴더> <이름>... → <이름>.before.png(git HEAD) · <이름>.after.png(작업 트리)
// 환경변수: NAVI_UI_PLAYWRIGHT_MODULE · NAVI_UI_BROWSER. render_png.py 가 이 브라우저로 안 찍힐 때 쓴다.
const fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const {execFileSync}=require('node:child_process');
const {chromium}=require(process.env.NAVI_UI_PLAYWRIGHT_MODULE);
const REPO=path.resolve(__dirname,'../../..');
const sizes=Object.fromEntries(JSON.parse(fs.readFileSync(path.join(REPO,'design/canvas/canvas.json'),'utf8')).artboards.map(a=>[a.file,[a.w,a.h]]));
const names=process.argv.slice(3);const out=process.argv[2];fs.mkdirSync(out,{recursive:true});
function standalone(t,w,h){const helm=t.match(/<helmet>([\s\S]*?)<\/helmet>/)[1];const body=t.match(/<\/helmet>([\s\S]*?)<\/x-dc>/)[1];return `<!doctype html><html><head><meta charset="utf-8">${helm}<style>html,body{margin:0;background:#fff}.frame{width:${w}px;height:${h}px;overflow:hidden;position:relative}</style></head><body><div class="frame">${body}</div></body></html>`}
(async()=>{
 const b=await chromium.launch({headless:true,executablePath:process.env.NAVI_UI_BROWSER,args:['--no-proxy-server']});
 const page=await (await b.newContext({deviceScaleFactor:1})).newPage();
 for(const n of names){
  const f=`${n}.dc.html`;const [w,h]=sizes[f];
  await page.setViewportSize({width:w,height:h});
  for(const k of ['before','after']){
   const t=k==='before'?execFileSync('git',['-C',REPO,'show',`HEAD:design/canvas/${f}`],{encoding:'utf8',maxBuffer:1<<28}):fs.readFileSync(path.join(REPO,'design/canvas',f),'utf8');
   const p=path.join(os.tmpdir(),`shot-${n}-${k}.html`);fs.writeFileSync(p,standalone(t,w,h));
   await page.goto('file://'+p);await page.evaluate(()=>document.fonts.ready);await page.waitForTimeout(500);
   await page.locator('.frame').screenshot({path:path.join(out,`${n}.${k}.png`)});
  }
  console.log('shot',n,w,h);
 }
 await b.close();
})();
