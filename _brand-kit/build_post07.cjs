const sharp = require('sharp');
const fs = require('node:fs/promises');
const path = require('node:path');

const ROOT = __dirname;
const ASSETS = path.join(ROOT, 'source-assets');
const MASTERS = path.join(ROOT, 'masters');
const W = 1200;
const H = 1200;
const HEADER_H = 106;

const C = {
  navy: '#102D3D',
  teal: '#177C7B',
  ivory: '#F4F0E8',
  paper: '#E7E0D5',
  white: '#FFFDF8',
};

const slides = [
  { file: '10-1753687052955149045977.jpg', out: '01-confidence-creates-opportunity', pos: 'center' },
  { file: '2-17536870529661133796647.jpg', out: '02-begin-with-self-worth', pos: 'center' },
  { file: '8-1753687052944410526071.jpg', out: '03-create-room-to-practice', pos: 'center' },
  { file: '4-1753687052865777309038.jpg', out: '04-let-her-define-the-dream', pos: 'center' },
];

function esc(s) {
  return s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
}

function svg(body) {
  return Buffer.from(`<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg">
    <style>
      .serif{font-family:'P052','DejaVu Serif',serif}
      .sans{font-family:'Nimbus Sans','DejaVu Sans',sans-serif}
      .caps{font-family:'Nimbus Sans','DejaVu Sans',sans-serif;font-weight:700;letter-spacing:5px}
    </style>${body}</svg>`);
}

async function photo(file, width, height, position='center') {
  return sharp(path.join(ASSETS,file)).resize(width,height,{fit:'cover',position}).modulate({saturation:0.92}).png().toBuffer();
}

async function makeSlide1(header) {
  const p = await photo(slides[0].file, W, H-HEADER_H, 'center');
  const overlay = svg(`
    <defs>
      <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
        <stop offset="38%" stop-color="${C.navy}" stop-opacity="0"/>
        <stop offset="100%" stop-color="${C.navy}" stop-opacity=".96"/>
      </linearGradient>
    </defs>
    <rect y="${HEADER_H}" width="1200" height="1094" fill="url(#g)"/>
    <rect x="54" y="160" width="8" height="138" fill="${C.teal}"/>
    <text x="86" y="192" class="caps" font-size="21" fill="${C.white}">FIELD NOTE 07</text>
    <text x="86" y="232" class="caps" font-size="18" fill="${C.white}" opacity=".92">LEARNING &amp; OPPORTUNITY</text>
    <text x="70" y="825" class="serif" font-size="104" fill="${C.white}">Confidence</text>
    <text x="70" y="930" class="serif" font-size="104" font-style="italic" fill="#77D1C6">creates</text>
    <text x="70" y="1035" class="serif" font-size="104" fill="${C.white}">opportunity.</text>
    <line x1="72" y1="1080" x2="770" y2="1080" stroke="#77D1C6" stroke-width="3"/>
    <text x="72" y="1122" class="sans" font-size="27" fill="${C.white}">Room to be seen. Heard. Taken seriously.</text>
    <text x="1125" y="1140" text-anchor="end" class="caps" font-size="18" fill="${C.white}">01</text>
  `);
  return sharp({create:{width:W,height:H,channels:3,background:C.ivory}})
    .composite([{input:p,left:0,top:HEADER_H},{input:header,left:0,top:0},{input:overlay,left:0,top:0}]).png().toBuffer();
}

async function makeSlide2(header) {
  const p = await photo(slides[1].file, W, 650, 'center');
  const overlay = svg(`
    <rect y="756" width="1200" height="444" fill="${C.ivory}"/>
    <rect x="0" y="106" width="56" height="1094" fill="${C.teal}"/>
    <text x="28" y="1110" class="caps" font-size="18" fill="${C.white}" transform="rotate(-90 28 1110)">FIELD NOTE 07 · SELF-WORTH</text>
    <text x="92" y="814" class="caps" font-size="18" fill="${C.teal}">01 — BEGIN WITH SELF-WORTH</text>
    <text x="92" y="895" class="serif" font-size="68" fill="${C.navy}">A stronger voice starts</text>
    <text x="92" y="966" class="serif" font-size="68" font-style="italic" fill="${C.teal}">by knowing your worth.</text>
    <line x1="92" y1="1012" x2="1108" y2="1012" stroke="${C.teal}" stroke-width="2"/>
    <text x="92" y="1060" class="sans" font-size="25" fill="${C.navy}">Support should help girls name their strengths, make choices</text>
    <text x="92" y="1095" class="sans" font-size="25" fill="${C.navy}">and speak with confidence.</text>
    <text x="1110" y="1150" text-anchor="end" class="caps" font-size="18" fill="${C.navy}">02</text>
  `);
  return sharp({create:{width:W,height:H,channels:3,background:C.ivory}})
    .composite([{input:p,left:0,top:HEADER_H},{input:header,left:0,top:0},{input:overlay,left:0,top:0}]).png().toBuffer();
}

async function makeSlide3(header) {
  const p = await photo(slides[2].file, 690, H-HEADER_H, 'center');
  const overlay = svg(`
    <rect x="690" y="106" width="510" height="1094" fill="${C.navy}"/>
    <rect x="690" y="106" width="10" height="1094" fill="#77D1C6"/>
    <text x="748" y="186" class="caps" font-size="18" fill="#77D1C6">02 — PRACTICE</text>
    <text x="748" y="292" class="serif" font-size="66" fill="${C.white}">Create</text>
    <text x="748" y="360" class="serif" font-size="66" fill="${C.white}">room to</text>
    <text x="748" y="428" class="serif" font-size="66" font-style="italic" fill="#77D1C6">participate.</text>
    <line x1="748" y1="484" x2="1128" y2="484" stroke="${C.white}" stroke-opacity=".5"/>
    <text x="748" y="555" class="sans" font-size="27" fill="${C.white}">Confidence grows through</text>
    <text x="748" y="594" class="sans" font-size="27" fill="${C.white}">learning, creating, presenting</text>
    <text x="748" y="633" class="sans" font-size="27" fill="${C.white}">and being taken seriously.</text>
    <circle cx="773" cy="738" r="16" fill="#77D1C6"/><text x="807" y="747" class="caps" font-size="19" fill="${C.white}">TRY</text>
    <circle cx="773" cy="807" r="16" fill="#77D1C6"/><text x="807" y="816" class="caps" font-size="19" fill="${C.white}">SPEAK</text>
    <circle cx="773" cy="876" r="16" fill="#77D1C6"/><text x="807" y="885" class="caps" font-size="19" fill="${C.white}">BE HEARD</text>
    <text x="1126" y="1144" text-anchor="end" class="caps" font-size="18" fill="${C.white}">03</text>
  `);
  return sharp({create:{width:W,height:H,channels:3,background:C.navy}})
    .composite([{input:p,left:0,top:HEADER_H},{input:header,left:0,top:0},{input:overlay,left:0,top:0}]).png().toBuffer();
}

async function makeSlide4(header) {
  const p = await photo(slides[3].file, W, H-HEADER_H, 'center');
  const overlay = svg(`
    <defs><linearGradient id="g4" x1="0" y1="0" x2="0" y2="1"><stop offset="25%" stop-color="${C.navy}" stop-opacity="0"/><stop offset="100%" stop-color="${C.navy}" stop-opacity=".92"/></linearGradient></defs>
    <rect y="106" width="1200" height="1094" fill="url(#g4)"/>
    <rect x="70" y="680" width="1060" height="430" rx="0" fill="${C.ivory}" fill-opacity=".94"/>
    <text x="108" y="742" class="caps" font-size="18" fill="${C.teal}">03 — KEEP THE FUTURE OPEN</text>
    <text x="108" y="838" class="serif" font-size="76" fill="${C.navy}">Let her define</text>
    <text x="108" y="918" class="serif" font-size="76" font-style="italic" fill="${C.teal}">the dream.</text>
    <line x1="108" y1="960" x2="1090" y2="960" stroke="${C.teal}" stroke-width="2"/>
    <text x="108" y="1010" class="sans" font-size="25" fill="${C.navy}">The goal is not to choose a future for her. It is to expand</text>
    <text x="108" y="1046" class="sans" font-size="25" fill="${C.navy}">the choices she can make for herself.</text>
    <text x="108" y="1084" class="caps" font-size="16" fill="${C.navy}">BACKING PROGRESS THAT LASTS</text>
    <text x="1110" y="1150" text-anchor="end" class="caps" font-size="18" fill="${C.white}">04</text>
  `);
  return sharp({create:{width:W,height:H,channels:3,background:C.ivory}})
    .composite([{input:p,left:0,top:HEADER_H},{input:header,left:0,top:0},{input:overlay,left:0,top:0}]).png().toBuffer();
}

async function main() {
  await fs.mkdir(MASTERS,{recursive:true});
  const header = await fs.readFile(path.join(ASSETS,'brand-header.png'));
  const buffers = [await makeSlide1(header),await makeSlide2(header),await makeSlide3(header),await makeSlide4(header)];
  const thumbs=[];
  for(let i=0;i<buffers.length;i++){
    const base=slides[i].out;
    await fs.writeFile(path.join(MASTERS,`${base}-1200x1200.png`),buffers[i]);
    await sharp(buffers[i]).jpeg({quality:95,chromaSubsampling:'4:4:4'}).toFile(path.join(ROOT,`${base}-1200x1200.jpg`));
    thumbs.push({input:await sharp(buffers[i]).resize(684,684).png().toBuffer(),left:8+(i%2)*700,top:8+Math.floor(i/2)*700});
  }
  await sharp({create:{width:1400,height:1400,channels:3,background:C.paper}}).composite(thumbs).jpeg({quality:93}).toFile(path.join(ROOT,'post-07-grid-preview.jpg'));
}

main().catch(err=>{console.error(err);process.exit(1)});
