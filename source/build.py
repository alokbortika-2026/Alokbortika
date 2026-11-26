"""Builds site/index.html (English + Bangla in one page, toggled in the nav).
Content lives in data.py (English) and tr_bn.py (Bangla). Run: python3 build.py"""
import html, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import *
from tr_bn import BN, dept_bn, bd

SRC = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(SRC, '..')
MISSING = set()

def H(s): return html.escape(str(s))

def t(en, bn):
    """Both languages, raw HTML. CSS shows the active one."""
    if en == bn: return en
    return f'<span class="en">{en}</span><span class="bn" lang="bn">{bn}</span>'

def tr(s):
    """Bangla for a data string (English key)."""
    if s in BN: return BN[s]
    MISSING.add(s); return s

def tx(s):
    """Escaped data string in both languages."""
    return t(H(s), H(tr(s)))

ICON = {
 'down': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>',
 'plus': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>',
 'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>',
 'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
}
COL = {'sky': 'var(--sky)', 'pop': 'var(--pop)', 'bolt': 'var(--bolt)', 'mint': 'var(--mint)', 'grape': 'var(--grape)', 'coral': 'var(--coral)'}
TITLES = {'prof.', 'dr.', 'ms.', 'mr.', 'md.', 'mst.', 'brig.', 'gen.', 'assoc.', 'brigadier', 'general'}

def initials(name):
    n = re.sub(r'\(.*?\)|,.*$', '', name)
    w = [x for x in n.split() if x.lower() not in TITLES and not re.fullmatch(r'[A-Z]\.', x)]
    if not w: w = n.split()[-1:]
    return (w[0][0] + (w[-1][0] if len(w) > 1 else '')).upper()

def mono(name): return f'<span class="mono" aria-hidden="true">{H(initials(name))}</span>'
def mode_cls(m):
    m = m.lower(); return 'rec' if 'record' in m else 'live' if 'live' in m or m.startswith('virtual') else ''
def country(c): return 'Bangladesh' if c == 'BD' else c

def numspan(en, bn, cls=''):
    """Count-up number: data-n keeps ASCII digits; Bangla copy converts while animating."""
    ascii_bn = re.sub(r'[০-৯]', lambda m: str('০১২৩৪৫৬৭৮৯'.index(m.group())), bn)
    return f'<b class="en {cls}" data-n="{H(en)}">{H(en)}</b><b class="bn {cls}" lang="bn" data-n="{H(ascii_bn)}" data-b>{H(bn)}</b>'

STAT_BN = {"~1M": "~১০ লাখ", "10,000+": "১০,০০০+", "2,000+": "২,০০০+", "200+": "২০০+", "6": "৬", "600": "৬০০", "50": "৫০", "20+": "২০+"}

# ---------------- sections ----------------
def hero():
    import json as _j
    m = _j.load(open(os.path.join(SRC, 'map.json')))
    rx, ry = m['C']['Rangpur'][0] / m['W'] * 100, m['C']['Rangpur'][1] / m['H'] * 100
    return f"""
<section class="hero" id="top" aria-labelledby="h1">
  <div class="sky"></div><div class="grid-bg"></div>
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="kicker ld" style="--i:0"><b>আলোকবর্তিকা ২০২৭</b> {t("Healthcare stakeholder and recognition event", "স্বাস্থ্যসেবা অংশীজন ও স্বীকৃতি অনুষ্ঠান")}</span>
        <h1 id="h1"><span class="en"><span class="l"><span style="--i:0">Lighting</span></span><span class="l"><span style="--i:1">the <em>last mile.</em></span></span></span><span class="bn" lang="bn"><span class="l"><span style="--i:0">আলো পৌঁছাক</span></span><span class="l"><span style="--i:1"><em>শেষ প্রান্তে।</em></span></span></span></h1>
        <p class="lede ld" style="--i:4">{t("For the first time, Bangladesh's entire primary-care system meets in one room: public-health leaders, doctors, pharmacies, students and families, with experts from six countries. One day to agree how connected care reaches every community.",
          "প্রথমবারের মতো বাংলাদেশের পুরো প্রাথমিক স্বাস্থ্যসেবা ব্যবস্থা এক ছাদের নিচে: জনস্বাস্থ্য নেতৃবৃন্দ, চিকিৎসক, ফার্মেসি, শিক্ষার্থী ও পরিবার, সঙ্গে ছয় দেশের বিশেষজ্ঞ। একদিনে ঠিক হবে, কানেক্টেড কেয়ার কীভাবে পৌঁছাবে প্রতিটি কমিউনিটিতে।")}</p>
        <div class="cta-row ld" style="--i:5">
          <a class="btn" href="{REG}#competitions">{t("Register for competitions", "প্রতিযোগিতায় রেজিস্টার করো")}</a>
          <a class="btn ghost" href="#programme">{t("View programme", "অনুষ্ঠানসূচি দেখুন")} {ICON['down']}</a>
        </div>
      </div>
      <div class="stage" aria-hidden="true">
        <div class="mapbox"><canvas id="map"></canvas>
          <span class="maptag" style="--x:{rx:.1f};--y:{ry:.1f}">{t("Rangpur · 9 Jan", "রংপুর · ৯ জানুয়ারি")}</span></div>
        <div class="maplegend"><span><i></i>{t("Communities reached", "যেসব কমিউনিটিতে পৌঁছানো")}</span><span><i class="c"></i>{t("Divisional cities", "বিভাগীয় শহর")}</span></div>
      </div>
    </div>
    <dl class="facts ld" style="--i:6">
      <div><dt>{t("When", "কবে")}</dt><dd>{t("Saturday, 9 January 2027<br>10 AM to 5 PM", "শনিবার, ৯ জানুয়ারি ২০২৭<br>সকাল ১০টা থেকে বিকেল ৫টা")}</dd></div>
      <div><dt>{t("Where", "কোথায়")}</dt><dd>{t("RDRS, Rangpur City<br>Main Hall and Hallroom 2", "আরডিআরএস, রংপুর শহর<br>মেইন হল ও হলরুম ২")}</dd></div>
      <div><dt>{t("Programme", "আয়োজন")}</dt><dd>{t("2 keynotes, 6 panels,<br>22 speakers, 20 judges", "২টি কিনোট, ৬টি প্যানেল,<br>২২ জন বক্তা, ২০ জন বিচারক")}</dd></div>
      <div class="count" id="cd" aria-label="Countdown to the event" role="timer">
        <div class="u"><div class="n">--</div><div class="t">{t("days", "দিন")}</div></div><span class="sep">:</span>
        <div class="u"><div class="n">--</div><div class="t">{t("hrs", "ঘণ্টা")}</div></div><span class="sep">:</span>
        <div class="u"><div class="n">--</div><div class="t">{t("min", "মিনিট")}</div></div><span class="sep">:</span>
        <div class="u"><div class="n">--</div><div class="t">{t("sec", "সেকেন্ড")}</div></div>
      </div>
    </dl>
  </div>
  <script type="application/json" id="mapdata">{_j.dumps(m)}</script>
</section>"""

def about():
    ic = lambda p: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
    home, day, flag = ic('<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>'), ic('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'), ic('<path d="M5 21V4"/><path d="M5 4h12l-2 4 2 4H5"/>')
    return f"""
<section class="sec" id="about" aria-labelledby="about-h">
  <div class="wrap">
    <div class="split">
      <div><span class="tag">{t("About the event", "অনুষ্ঠান সম্পর্কে")}</span><h2 class="sh2" id="about-h">{t("The torch that lights the way.", "যে মশাল পথ দেখায়।")}</h2><p class="word" lang="bn">আলোকবর্তিকা</p></div>
      <div>
        <p class="statement">{t("<em>Alokbortika</em> brings doctors, policymakers, pharmaceutical and development partners, community pharmacies, students and patients together for one purpose: a shared National Connected Primary Care agenda.",
          "<em>আলোকবর্তিকা</em> চিকিৎসক, নীতিনির্ধারক, ওষুধ কোম্পানি ও উন্নয়ন সহযোগী, কমিউনিটি ফার্মেসি, শিক্ষার্থী ও রোগীদের এক জায়গায় আনছে একটি লক্ষ্যে: একটি জাতীয় কানেক্টেড প্রাইমারি কেয়ার এজেন্ডা।")}</p>
        <div class="about-cols">
          <p>{t("The agenda is built from commitments made across six panel discussions by public-health leaders, academia, Grameen Group, INGOs and pharmaceutical partners, then shared with policymakers after the event.",
                "ছয়টি প্যানেল আলোচনায় জনস্বাস্থ্য নেতৃবৃন্দ, শিক্ষাবিদ, গ্রামীণ গ্রুপ, আন্তর্জাতিক এনজিও ও ওষুধ কোম্পানির অঙ্গীকার থেকে তৈরি হবে এই এজেন্ডা, আর অনুষ্ঠানের পর তা পৌঁছাবে নীতিনির্ধারকদের কাছে।")}</p>
          <p>{t("The host, Grameen HealthTech Limited, runs Shukhee: a connected-care platform linking patients, pharmacies and doctors through teleconsultation, backed by a network of 7.7 million Grameen members.",
                "আয়োজক গ্রামীণ হেলথটেক লিমিটেড, যারা চালায় সুখী: টেলিকনসালটেশনের মাধ্যমে রোগী, ফার্মেসি ও চিকিৎসককে যুক্ত করা একটি কানেক্টেড-কেয়ার প্ল্যাটফর্ম, যার পেছনে আছে ৭৭ লাখ গ্রামীণ সদস্যের নেটওয়ার্ক।")}</p>
        </div>
      </div>
    </div>
    <div class="pillars">
      <div class="pillar">{home}<h3>{t("The last mile", "শেষ প্রান্ত")}</h3><p>{t("Community pharmacies as first contact, referral links to Community Clinics and Upazila Health Complexes, and digital inclusion for elderly, low-literacy and char-area families.", "প্রথম যোগাযোগের জায়গা হিসেবে কমিউনিটি ফার্মেসি, কমিউনিটি ক্লিনিক ও উপজেলা স্বাস্থ্য কমপ্লেক্সে রেফারেল, আর বয়স্ক, স্বল্পশিক্ষিত ও চরাঞ্চলের পরিবারের ডিজিটাল অন্তর্ভুক্তি।")}</p></div>
      <div class="pillar" style="--c:var(--sun)">{day}<h3>{t("The day", "দিনটি")}</h3><p>{t("Keynotes, six hybrid panels, student pitch finals, a partner showcase and the Alokbortika Awards, all on one green campus in Rangpur.", "কিনোট, ছয়টি হাইব্রিড প্যানেল, শিক্ষার্থীদের পিচ ফাইনাল, পার্টনার শোকেস আর আলোকবর্তিকা অ্যাওয়ার্ডস, সবই রংপুরের একটি সবুজ ক্যাম্পাসে।")}</p></div>
      <div class="pillar" style="--c:var(--grape)">{flag}<h3>{t("The outcome", "ফলাফল")}</h3><p>{t("A National Connected Primary Care agenda, with commitments shared through 15+ newspapers and partners from 10 to 20 January.", "একটি জাতীয় কানেক্টেড প্রাইমারি কেয়ার এজেন্ডা, যার অঙ্গীকার ১০ থেকে ২০ জানুয়ারির মধ্যে ১৫+ সংবাদপত্র ও সহযোগীদের মাধ্যমে প্রকাশ পাবে।")}</p></div>
    </div>
  </div>
</section>"""

def photo(slug):
    for ext in ('webp', 'jpg', 'jpeg', 'png'):
        if os.path.exists(os.path.join(SITE, 'assets', 'people', f'{slug}.{ext}')):
            return f'<img src="assets/people/{slug}.{ext}" alt="" loading="lazy">'
    return ''

LEADS = [
    dict(cls='l1', slug='muhammad-yunus', name=('Prof. Muhammad Yunus', 'অধ্যাপক মুহাম্মদ ইউনূস'), label=('Video message', 'ভিডিও বার্তা'),
         roles=[('Former Honorable Chairman', 'সাবেক সম্মানিত চেয়ারম্যান'), ('Nobel Peace Prize Recipient, 2006', 'নোবেল শান্তি পুরস্কারপ্রাপ্ত, ২০০৬'), ('US Congressional Gold Medal Winner, 2010', 'যুক্তরাষ্ট্রের কংগ্রেশনাল গোল্ড মেডেলজয়ী, ২০১০')],
         sess=('<b>Opening plenary, 10:10 AM.</b> A recorded message to open Alokbortika 2027.', '<b>উদ্বোধনী অধিবেশন, সকাল ১০:১০।</b> আলোকবর্তিকা ২০২৭-এর সূচনায় একটি রেকর্ড করা বার্তা।')),
    dict(cls='l2', slug=None, name=('Md Ashraful Hasan', 'Md Ashraful Hasan'), label=('Grameen Group', 'গ্রামীণ গ্রুপ'),
         roles=[('Chairman & Managing Director, Grameen Group', 'চেয়ারম্যান ও ব্যবস্থাপনা পরিচালক, গ্রামীণ গ্রুপ')], sess=None),
    dict(cls='l3', slug=None, name=('Dr. Ahmed Armaan Siddiqui', 'Dr. Ahmed Armaan Siddiqui'), label=('Keynote', 'কিনোট'),
         roles=[('CEO, Grameen HealthTech Limited', 'প্রধান নির্বাহী কর্মকর্তা, গ্রামীণ হেলথটেক লিমিটেড')],
         sess=("<b>Keynote 1, 10:15 AM.</b> The Alokbortika vision: Shukhee's connected care.", '<b>কিনোট ১, সকাল ১০:১৫।</b> আলোকবর্তিকার ভাবনা: সুখীর কানেক্টেড কেয়ার।')),
]

def leads():
    cards = ''
    for L in LEADS:
        roles = ''.join(f'<li>{t(a, b)}</li>' for a, b in L['roles'])
        ss = f'<p class="ss">{t(*L["sess"])}</p>' if L['sess'] else ''
        ph = f'<div class="lead-ph">{photo(L["slug"])}</div>' if L['slug'] else ''
        cards += f"""<article class="lead {L['cls']}{'' if L['slug'] else ' txt'}">{ph}<div class="tx"><span class="lb">{t(*L['label'])}</span><h3>{t(H(L['name'][0]), H(L['name'][1]))}</h3><ul class="rl">{roles}</ul>{ss}</div></article>"""
    return f"""
<section class="sec lead-sec" id="voices" aria-labelledby="lead-h">
  <div class="wrap">
    <div class="head"><span class="tag">{t("Opening voices", "উদ্বোধনী কণ্ঠ")}</span><h2 id="lead-h">{t("Leading the conversation.", "আলোচনার নেতৃত্বে।")}</h2></div>
    <div class="leads">{cards}</div>
  </div>
</section>"""

def numbers():
    cells = ''.join(f'<div class="num">{numspan(n, STAT_BN[n])}<span class="lbl">{tx(s)}</span></div>' for n, s in STATS)
    return f'''
<section class="sec" style="padding-top:0" aria-label="Alokbortika in numbers">
  <div class="wrap"><div class="nums">{cells}</div></div>
</section>'''

def cnt(to, dec=0, pre="", suf="", bn_pre=None, bn_suf=None, bn_to=None):
    to_s = f'{to:.{dec}f}'
    en = f'<span class="ct" data-count="{to_s}" data-dec="{dec}" data-pre="{H(pre)}" data-suf="{H(suf)}">{H(pre)}{to_s}{H(suf)}</span>'
    bt = bn_to if bn_to is not None else to; bts = f'{bt:.{dec}f}'
    bp = pre if bn_pre is None else bn_pre; bs = suf if bn_suf is None else bn_suf
    bn = f'<span class="ct" data-b data-count="{bts}" data-dec="{dec}" data-pre="{H(bp)}" data-suf="{H(bs)}">{H(bp)}{bd(bts)}{H(bs)}</span>'
    return f'<span class="en">{en}</span><span class="bn" lang="bn">{bn}</span>'

def evidence():
    bars = ''.join(f'<div class="bar{" hi" if c=="Bangladesh" else ""}" style="--i:{i}"><span class="lbl">{tx(c)}</span><span class="trk"><span class="fill" style="--v:{v}"></span></span><span class="val">{cnt(v, 1, suf="%")}</span></div>' for i, (c, v) in enumerate(OOP))
    L = 2 * 3.14159 * 50
    def ring(p, lbl, h, s):
        return f'<div class="gap"><div class="ring" style="--len:{L:.1f};--p:{p/100}"><svg viewBox="0 0 120 120" aria-hidden="true"><circle class="bg" cx="60" cy="60" r="50"/><circle class="fg" cx="60" cy="60" r="50"/></svg><b>{cnt(int(lbl.rstrip('%')), 0, suf='%')}</b></div><h4>{h}</h4><p>{s}</p></div>'
    return f'''
<section class="sec night" id="why" aria-labelledby="why-h">
  <div class="wrap" style="position:relative;z-index:1">
    <div class="head"><span class="tag">{t("Why this moment can't wait", "কেন এখনই")}</span><h2 id="why-h">{t("Families carry the cost of care alone.", "চিকিৎসার খরচ একাই বইছে পরিবারগুলো।")}</h2>
    <p>{t("Most health spending in Bangladesh comes straight out of household pockets, and most people with common conditions never get treated. The last mile is where that changes, or doesn't.",
          "বাংলাদেশে স্বাস্থ্য ব্যয়ের বেশিরভাগই সরাসরি পরিবারের পকেট থেকে যায়, আর সাধারণ রোগে ভোগা বেশিরভাগ মানুষ চিকিৎসাই পান না। বদলটা আসতে হবে শেষ প্রান্তেই।")}</p></div>
    <div class="ev-grid">
      <div class="ev-main"><div class="panel-dark">
        <h3>{t("Households pay most of the bill", "খরচের বড় অংশ পরিবারের ঘাড়ে")}</h3>
        <p class="sub">{t("Out-of-pocket share of health spending, 2023", "স্বাস্থ্য ব্যয়ে নিজের পকেট থেকে খরচের হার, ২০২৩")}</p>
        <div class="bars" role="img" aria-label="Out-of-pocket share of health spending in 2023: Bangladesh 79.3%, Nepal 59.4%, Sri Lanka 54.8%, Pakistan 52.9%, South Asia 46.6%, India 43.9%, World 17.3%">{bars}</div>
      </div>
      <div class="panel-dark">
        <h3>{t("Most people go untreated", "বেশিরভাগ মানুষ চিকিৎসার বাইরে")}</h3>
        <div class="gaps">
          {ring(92.3, '92%', t('Mental health', 'মানসিক স্বাস্থ্য'), t('16.8% of adults are affected. 92.3% of them get no treatment.', '১৬.৮% প্রাপ্তবয়স্ক আক্রান্ত। তাঁদের ৯২.৩% কোনো চিকিৎসা পান না।'))}
          {ring(71.5, '72%', t('High blood pressure', 'উচ্চ রক্তচাপ'), t('23.5% of adults are affected. 71.5% of them are not on medication.', '২৩.৫% প্রাপ্তবয়স্ক আক্রান্ত। তাঁদের ৭১.৫% ওষুধ খান না।'))}
        </div>
      </div></div>
      <div class="ev-side">
        <div class="panel-dark big-stat"><b>{cnt(4.6, 1, suf="×", bn_suf=" গুণ")}</b><p>{t("Bangladeshi families pay 79% of health costs directly, 4.6 times the global average.", "বাংলাদেশি পরিবার স্বাস্থ্য ব্যয়ের ৭৯% সরাসরি নিজেরা বহন করে, যা বৈশ্বিক গড়ের ৪.৬ গুণ।")}</p></div>
        <div class="panel-dark big-stat"><b>{cnt(5, 0, pre="US$", suf="B", bn_pre="", bn_suf=" কোটি ডলার", bn_to=500)}</b><p>{t("estimated yearly spending by Bangladeshis on treatment abroad.", "চিকিৎসার জন্য বিদেশে বাংলাদেশিদের আনুমানিক বার্ষিক ব্যয়।")}</p></div>
        <div class="panel-dark big-stat"><b>{cnt(15)} <span class="vs">{t("vs", "বনাম")}</span> {cnt(44.5, 1)}</b><p>{t("health workers per 10,000 people, against the WHO benchmark.", "প্রতি ১০,০০০ মানুষের জন্য স্বাস্থ্যকর্মী, বিশ্ব স্বাস্থ্য সংস্থার মানদণ্ডের তুলনায়।")}</p></div>
      </div>
    </div>
    <p class="src">{t("Sources", "সূত্র")}: World Bank WDI (SH.XPD.OOPC.CH.ZS, 2023); National Mental Health Survey 2019 (NIMH/WHO); WHO STEPS Bangladesh 2022; MoHFW via The Daily Star (2025); Bangladesh Bank Governor via The Financial Express.</p>
  </div>
</section>'''

def climb():
    steps = ''.join(f'<div class="step" style="--k:{k}"><div class="meta">{numspan(n, STAT_BN[n])}<h3>{tx(ti)}</h3><p>{tx(s)}</p></div><div class="riser"><span class="lamp"></span></div></div>' for k, (n, ti, s) in enumerate(CLIMB))
    return f'''
<section class="sec" id="reach" aria-labelledby="reach-h">
  <div class="wrap">
    <div class="head"><span class="tag">{t("Root to top", "তৃণমূল থেকে শীর্ষে")}</span><h2 id="reach-h">{t("One room. Every level of care.", "এক ছাদের নিচে। সেবার প্রতিটি স্তর।")}</h2>
    <p>{t("Alokbortika starts with communities at the root, grows through students and future doctors, and reaches the specialists, policymakers and global experts who shape care.",
          "আলোকবর্তিকা শুরু হয় তৃণমূলের কমিউনিটি থেকে, এগিয়ে যায় শিক্ষার্থী ও ভবিষ্যৎ চিকিৎসকদের হাত ধরে, পৌঁছায় সেই বিশেষজ্ঞ, নীতিনির্ধারক ও বৈশ্বিক বিশেষজ্ঞদের কাছে যাঁরা সেবার রূপ দেন।")}</p></div>
    <div class="climb">{steps}</div>
    <div class="climb-axis"><span>{t("Community", "কমিউনিটি")}</span><span>{t("Policy and global", "নীতি ও বৈশ্বিক")}</span></div>
  </div>
</section>'''

def road():
    out = ''
    for i, (a, b, when, ti, k, items) in enumerate(PHASES, 1):
        out += f'<article class="phase" data-from="{a}" data-to="{b}"><div class="dot">{t(str(i), bd(i))}</div><div class="card"><div class="when">{tx(when)}</div><h3>{tx(ti)}</h3><div class="k">{tx(k)}</div><ul>{"".join(f"<li>{tx(x)}</li>" for x in items)}</ul></div></article>'
    return f'''
<section class="sec" id="road" style="padding-top:40px" aria-labelledby="road-h">
  <div class="wrap">
    <div class="head"><span class="tag">{t("The road to Alokbortika", "আলোকবর্তিকার পথে")}</span><h2 id="road-h">{t("Seven weeks, four phases.", "সাত সপ্তাহ, চার ধাপ।")}</h2>
    <p>{t("It doesn't start or end on 9 January. Students get involved from 30 November, and the agenda travels out to the press and partners after the day.",
          "শুধু ৯ জানুয়ারিতেই শুরু বা শেষ নয়। ৩০ নভেম্বর থেকে শিক্ষার্থীরা যুক্ত হচ্ছে, আর অনুষ্ঠানের পর এজেন্ডা পৌঁছাবে গণমাধ্যম ও সহযোগীদের কাছে।")}</p></div>
    <div class="road">{out}</div>
    <p class="prog-note" style="margin-top:28px">{t("<strong>Running alongside:</strong> 200+ pharmacies and 600 link workers carry the message to around a million people, with 15 pieces of Bangla and English content across Facebook, LinkedIn, Instagram and the web.",
       "<strong>পাশাপাশি:</strong> ২০০+ ফার্মেসি ও ৬০০ লিংক ওয়ার্কার বার্তাটি পৌঁছে দেবেন প্রায় ১০ লাখ মানুষের কাছে, সঙ্গে ফেসবুক, লিংকডইন, ইনস্টাগ্রাম ও ওয়েবে বাংলা ও ইংরেজিতে ১৫টি কনটেন্ট।")}</p>
  </div>
</section>'''

def sp_sub(role, org, c, lang):
    L = (lambda s: s) if lang == 'en' else tr
    parts = [L(role)]
    if org and org not in role: parts.append(L(org))
    if c != 'BD': parts.append(L(country(c)))
    return ', '.join(parts)

def panel_details(n):
    p = PANELS[n]
    who = ''
    for s in SPEAKERS:
        if s[4] != n: continue
        name, role, org, c, _, mode, focus, g = s
        who += f'<div class="who">{mono(name)}<div><div class="nm"><strong>{H(name)}</strong><span class="mode {mode_cls(mode)}">{tx(mode)}</span></div><p class="sub">{t(H(sp_sub(role, org, c, "en")), H(sp_sub(role, org, c, "bn")))}</p><p class="fx">{tx(focus)}</p></div></div>'
    return f'''<details class="pn" id="panel-{n}" style="--c:{COL[p['color']]}"><summary><div><div class="ptop"><span class="pill">{t(f"Panel {n}", f"প্যানেল {bd(n)}")}</span>{tx(p['time'])} · {tx(p['topic'])}</div><h4>{tx(p['title'])}</h4><p class="q">{tx(p['q'])}</p></div><span class="plus">{ICON['plus']}</span></summary>
<div class="inner"><div class="stat"><b>{tx(p['stat'][0])}</b><span>{tx(p['stat'][1])}</span></div>{who}</div></details>'''

def programme():
    def li(tm, en, bn): return f'<li><time>{t(tm, bd(tm))}</time><span>{t(en, bn)}</span></li>'
    def tm(en, bn, en2='', bn2=''): return t(en + (f'<small>{en2}</small>' if en2 else ''), bn + (f'<small>{bn2}</small>' if bn2 else ''))
    MH, HR = f'<span class="room">{t("Main Hall", "মেইন হল")}</span>', f'<span class="room">{t("Hallroom 2", "হলরুম ২")}</span>'
    return f'''
<section class="sec" id="programme" aria-labelledby="prog-h">
  <div class="wrap">
    <div class="head"><span class="tag">{t("Programme · Saturday 9 January 2027", "অনুষ্ঠানসূচি · শনিবার, ৯ জানুয়ারি ২০২৭")}</span><h2 id="prog-h">{t("One day, from first welcome to celebration.", "প্রথম স্বাগত থেকে উদযাপন, একটি দিন।")}</h2>
    <p>{t("Mornings are for big ideas and young voices. Afternoons split into two rooms of 30-minute hybrid panels. The day ends with the Alokbortika Awards. Open a panel to see who's speaking.",
          "সকালটা বড় ভাবনা আর তরুণ কণ্ঠের। দুপুরের পর দুই কক্ষে চলবে ৩০ মিনিটের হাইব্রিড প্যানেল। দিন শেষ হবে আলোকবর্তিকা অ্যাওয়ার্ডস দিয়ে। কে কথা বলছেন দেখতে যেকোনো প্যানেল খুলুন।")}</p></div>
    <div class="prog">
      <div class="slot"><div class="time">{tm("9:30 AM", "সকাল ৯:৩০")}</div><div class="body"><div class="item" style="--c:var(--muted)"><h3>{t("Registration and welcome", "নিবন্ধন ও স্বাগত")}</h3><p>{t("Guest arrival and protocol reception.", "অতিথিদের আগমন ও প্রটোকল অভ্যর্থনা।")}</p></div></div></div>
      <div class="slot"><div class="time">{tm("10:00 AM", "সকাল ১০:০০", "to 10:40", "১০:৪০ পর্যন্ত")}</div><div class="body"><div class="item"><h3>{t("Opening plenary", "উদ্বোধনী অধিবেশন")} {MH}</h3><ul>
        {li('10:00', 'Opening film and welcome', 'উদ্বোধনী চলচ্চিত্র ও স্বাগত বক্তব্য')}
        {li('10:10', 'Video message from Prof. Muhammad Yunus', 'অধ্যাপক মুহাম্মদ ইউনূসের ভিডিও বার্তা')}
        {li('10:15', 'Keynote 1: Dr. Ahmed Armaan Siddiqui, CEO, Grameen HealthTech, on Shukhee’s connected care', 'কিনোট ১: Dr. Ahmed Armaan Siddiqui, প্রধান নির্বাহী, গ্রামীণ হেলথটেক; বিষয়: সুখীর কানেক্টেড কেয়ার')}
        {li('10:25', 'Keynote 2: Chief Guest Dr. Md. Wazed Ali, Divisional Director (Health), Rangpur', 'কিনোট ২: প্রধান অতিথি Dr. Md. Wazed Ali, বিভাগীয় পরিচালক (স্বাস্থ্য), রংপুর')}
        {li('10:35', 'Special Guest address: Dr. Shahin Sultana, Civil Surgeon, Rangpur', 'বিশেষ অতিথির বক্তব্য: Dr. Shahin Sultana, সিভিল সার্জন, রংপুর')}
      </ul></div></div></div>
      <div class="slot"><div class="time">{tm("10:40 AM", "সকাল ১০:৪০", "to 12:30 PM", "দুপুর ১২:৩০ পর্যন্ত")}</div><div class="body">
        <div class="item" style="--c:var(--sun)"><h3>{t("Partner showcase and expo", "পার্টনার শোকেস ও এক্সপো")} {MH}</h3><p>{t("Partner pavilions, pharma and INGO exhibits, a live Shukhee teleconsultation demo, sponsor keynotes and a guided VIP tour.", "পার্টনার প্যাভিলিয়ন, ওষুধ কোম্পানি ও আন্তর্জাতিক এনজিওর প্রদর্শনী, সুখী টেলিকনসালটেশনের লাইভ ডেমো, স্পনসর কিনোট ও ভিআইপিদের জন্য গাইডেড ট্যুর।")}</p></div>
        <div class="item" style="--c:var(--grape)"><h3>{t("Pitch Grand Final", "পিচ গ্র্যান্ড ফাইনাল")} {HR}</h3><ul>
          {li('10:40', 'Medical-student Grand Final: 3 teams, 15-minute pitch and 5 minutes of jury Q&amp;A each', 'মেডিকেল শিক্ষার্থীদের গ্র্যান্ড ফাইনাল: ৩টি দল, প্রত্যেকের ১৫ মিনিট পিচ ও ৫ মিনিট জুরির প্রশ্নোত্তর')}
          {li('11:40', 'Young Changemakers: 9 school, college and university students, 5 minutes each', 'তরুণ চেঞ্জমেকার: স্কুল, কলেজ ও বিশ্ববিদ্যালয়ের ৯ জন শিক্ষার্থী, প্রত্যেকে ৫ মিনিট')}
        </ul></div></div></div>
      <div class="slot break"><div class="time">{tm("12:30 PM", "দুপুর ১২:৩০", "to 2:00 PM", "দুপুর ২:০০ পর্যন্ত")}</div><div class="body"><div class="item" style="--c:var(--coral)"><h3>{t("Networking lunch", "নেটওয়ার্কিং লাঞ্চ")}</h3><p>{t("Lunch and informal networking, with a dedicated lunch for distinguished guests.", "দুপুরের খাবার ও আলাপ-পরিচয়, বিশিষ্ট অতিথিদের জন্য আলাদা আয়োজন।")}</p></div></div></div>
      <div class="slot"><div class="time">{tm("2:00 PM", "দুপুর ২:০০", "to 3:30 PM", "বিকেল ৩:৩০ পর্যন্ত")}</div><div class="body">
        <div class="tracks">
          <div><div class="track-h">{t("Track A", "ট্র্যাক এ")} <span>{t("Main Hall", "মেইন হল")}</span></div>{panel_details(1)}{panel_details(2)}{panel_details(3)}</div>
          <div><div class="track-h">{t("Track B", "ট্র্যাক বি")} <span>{t("Hallroom 2", "হলরুম ২")}</span></div>{panel_details(4)}{panel_details(5)}{panel_details(6)}</div>
        </div>
        <p class="prog-note" style="margin-top:4px">{t("Hybrid: speakers join in person and live from Thailand, China, Japan and India. Speakers in the USA send recorded messages.", "হাইব্রিড: বক্তারা সরাসরি এবং থাইল্যান্ড, চীন, জাপান ও ভারত থেকে লাইভে যুক্ত হবেন। যুক্তরাষ্ট্রের বক্তারা পাঠাবেন রেকর্ড করা বার্তা।")}</p>
      </div></div>
      <div class="slot"><div class="time">{tm("3:30 PM", "বিকেল ৩:৩০", "to 5:00 PM", "বিকেল ৫:০০ পর্যন্ত")}</div><div class="body"><div class="item" style="--c:var(--sun)"><h3>{t("Closing plenary and Alokbortika Awards 2027", "সমাপনী অধিবেশন ও আলোকবর্তিকা অ্যাওয়ার্ডস ২০২৭")} {MH}</h3><ul>
        {li('3:30', 'MD and sponsor remarks, with takeaways from all six panels', 'এমডি ও স্পনসরদের বক্তব্য, ছয় প্যানেলের মূল কথা')}
        {li('3:40', 'Award ceremony, presented by the Chief and Special Guests', 'অ্যাওয়ার্ড অনুষ্ঠান, প্রধান ও বিশেষ অতিথির হাতে')}
        {li('4:15', 'Music and cultural programme', 'গান ও সাংস্কৃতিক অনুষ্ঠান')}
        {li('4:45', 'Raffle draw', 'র‍্যাফেল ড্র')}
        {li('4:55', 'Closing remarks and farewell', 'সমাপনী বক্তব্য ও বিদায়')}
      </ul></div></div></div>
    </div>
    <p class="prog-note">{t("Times are indicative and may shift on the day.", "সময়সূচি আনুমানিক, অনুষ্ঠানের দিন কিছুটা বদলাতে পারে।")}</p>
  </div>
</section>'''

def people_list(rows, role_fn):
    return "".join(f"<li>{H(n)}<span>{t(H(r), H(role_fn(r)))}</span></li>" for n, r in rows)

def people():
    cards = ''
    for name, role, org, c, pn, mode, focus, g in SPEAKERS:
        p = PANELS[pn]
        orgline = org if org and org not in role else country(c)
        cards += f'''<article class="person" data-g="{g}" data-p="p{pn}"><div class="top">{mono(name)}<div><h4>{H(name)}</h4><p class="org">{tx(orgline)}</p></div></div>
<p class="role-l">{tx(role)}</p><p class="focus">{tx(focus)}</p>
<div class="pfoot"><span class="flag">{tx(country(c))}</span><span class="mode {mode_cls(mode)}" style="margin:0">{tx(mode)}</span><a class="pref" href="#panel-{pn}">{t(f"Panel {pn}: " + H(p['topic']), f"প্যানেল {bd(pn)}: " + H(tr(p['topic'])))}</a></div></article>'''
    filt = f'<button type="button" data-f="all" aria-pressed="true">{t("All 22", "সবাই (২২)")}</button><button type="button" data-f="intl" aria-pressed="false">{t("Global and partners", "বৈশ্বিক ও সহযোগী")}</button>' + ''.join(f'<button type="button" data-f="p{n}" aria-pressed="false">{tx(PANELS[n]["topic"])}</button>' for n in PANELS)
    honour = ''.join(f'<div class="inst"><h4>{tx(i)}</h4><ul>{"".join(f"<li><strong>{H(n)}</strong><span>{tx(r)}</span></li>" for n, r in ppl)}</ul></div>' for i, ppl in HONOUR)
    hods = ''.join(f'<div><h5>{tx(i)}</h5><ul>{people_list(ppl, dept_bn)}</ul></div>' for i, ppl in HODS)
    return f'''
<section class="sec" id="speakers" style="background:#fff" aria-labelledby="sp-h">
  <div class="wrap">
    <div class="head"><span class="tag">{t("Speakers and guests", "বক্তা ও অতিথি")}</span><h2 id="sp-h">{t("The people carrying the torch.", "যাঁদের হাতে মশাল।")}</h2>
    <p>{t("Divisional health leadership, the heads of Rangpur's three medical colleges, and specialists from Bangladesh, Thailand, China, Japan, India and the USA.",
          "বিভাগীয় স্বাস্থ্য নেতৃত্ব, রংপুরের তিন মেডিকেল কলেজের প্রধানেরা, আর বাংলাদেশ, থাইল্যান্ড, চীন, জাপান, ভারত ও যুক্তরাষ্ট্রের বিশেষজ্ঞরা।")}</p></div>
    <div class="vip">
      <div class="vip-card">{mono('Dr. Md. Wazed Ali')}<div><span class="role">{t("Chief Guest", "প্রধান অতিথি")}</span><h3>Dr. Md. Wazed Ali</h3><p>{t("Divisional Director (Health), Rangpur Division, Directorate General of Health Services (DGHS)", "বিভাগীয় পরিচালক (স্বাস্থ্য), রংপুর বিভাগ, স্বাস্থ্য অধিদপ্তর (DGHS)")}</p></div></div>
      <div class="vip-card sp">{mono('Dr. Shahin Sultana')}<div><span class="role">{t("Special Guest", "বিশেষ অতিথি")}</span><h3>Dr. Shahin Sultana</h3><p>{t("Civil Surgeon, Rangpur, Directorate General of Health Services (DGHS)", "সিভিল সার্জন, রংপুর, স্বাস্থ্য অধিদপ্তর (DGHS)")}</p></div></div>
    </div>

    <div class="sub-h"><h3>{t("Panel speakers", "প্যানেল বক্তা")}</h3><div class="filters" role="group" aria-label="Filter speakers">{filt}</div></div>
    <div class="people">{cards}</div>

    <div class="sub-h"><h3>{t("Guests of honour", "সম্মানিত অতিথি")}</h3><p>{t("Leaders of Rangpur's three medical colleges and their hospitals.", "রংপুরের তিন মেডিকেল কলেজ ও হাসপাতালের নেতৃবৃন্দ।")}</p></div>
    <div class="honour">{honour}</div>
    <details class="more"><summary>{t("50 heads of department invited", "৫০ জন বিভাগীয় প্রধান আমন্ত্রিত")} <span class="m">{t("From all three medical colleges", "তিন মেডিকেল কলেজ থেকে")}</span><span class="plus">{ICON['plus']}</span></summary><div class="cols">{hods}</div></details>
  </div>
</section>'''

ART = {
 'idea': '<svg viewBox="0 0 400 170" aria-hidden="true"><circle cx="330" cy="30" r="60" fill="#fff" opacity=".12"/><rect x="70" y="34" width="190" height="112" rx="18" fill="#fff" stroke="#0B1220" stroke-width="4"/><circle cx="165" cy="90" r="26" fill="#FFCD00" stroke="#0B1220" stroke-width="4"/><path d="M158 78v24l20-12z" fill="#0B1220"/><circle cx="92" cy="54" r="6" fill="#D63E9C"/><path d="M280 50h70a14 14 0 0 1 14 14v26a14 14 0 0 1-14 14h-40l-18 16v-16h-12a14 14 0 0 1-14-14V64a14 14 0 0 1 14-14Z" fill="#fff" stroke="#0B1220" stroke-width="4"/><path d="M296 72h40M296 86h26" stroke="#0B1220" stroke-width="4" stroke-linecap="round"/></svg>',
 'cmk': '<svg viewBox="0 0 400 170" aria-hidden="true"><circle cx="60" cy="140" r="70" fill="#fff" opacity=".15"/><rect x="40" y="40" width="96" height="96" rx="10" transform="rotate(-10 88 88)" fill="#fff" stroke="#0B1220" stroke-width="4"/><circle cx="86" cy="80" r="14" fill="#FFCD00" stroke="#0B1220" stroke-width="3"/><rect x="150" y="54" width="170" height="104" rx="22" fill="#0B1220"/><rect x="190" y="40" width="56" height="22" rx="8" fill="#0B1220"/><circle cx="235" cy="106" r="38" fill="#fff"/><circle cx="235" cy="106" r="24" fill="#2F6FE0" stroke="#0B1220" stroke-width="4"/><circle cx="228" cy="99" r="7" fill="#fff"/><circle cx="296" cy="74" r="6" fill="#FFCD00"/><path d="M352 30l6 14 14 6-14 6-6 14-6-14-14-6 14-6z" fill="#fff"/></svg>',
 'case': '<svg viewBox="0 0 400 170" aria-hidden="true"><circle cx="340" cy="150" r="80" fill="#fff" opacity=".12"/><rect x="60" y="28" width="130" height="150" rx="16" fill="#fff" stroke="#0B1220" stroke-width="4"/><text x="80" y="76" font-family="Bricolage Grotesque,sans-serif" font-weight="800" font-size="32" fill="#0B1220">Rx</text><path d="M80 98h88M80 116h70M80 134h80" stroke="#0B1220" stroke-width="4" stroke-linecap="round" opacity=".7"/><rect x="220" y="44" width="120" height="96" rx="14" fill="#fff" stroke="#0B1220" stroke-width="4"/><rect x="242" y="96" width="16" height="28" rx="4" fill="#2F6FE0"/><rect x="266" y="78" width="16" height="46" rx="4" fill="#D63E9C"/><rect x="290" y="66" width="16" height="58" rx="4" fill="#FFCD00"/><path d="M362 26l5 12 12 5-12 5-5 12-5-12-12-5 12-5z" fill="#FFCD00"/></svg>',
}

def competitions():
    cards = ''
    for c in COMPETITIONS:
        facts = ''.join(f'<div><dt>{tx(k)}</dt><dd>{tx(v)}</dd></div>' for k, v in c['facts'])
        note = f'<p class="note">{t("For medical college students only", "শুধু মেডিকেল কলেজের শিক্ষার্থীদের জন্য")}</p>' if c['key'] == 'case' else ''
        cards += f'''<article class="comp {c['theme']}"><div class="art">{ART[c['key']]}</div><div class="in"><h3>{tx(c['name'])}</h3><p class="line">{tx(c['line'])}</p><p class="desc">{tx(c['desc'])}</p><dl>{facts}</dl>{note}<a class="btn" href="{REG}#{c['hash']}" aria-label="Register for {H(c['name'])}">{t("Register now", "রেজিস্টার করো")}</a></div></article>'''
    jury = ''.join(f'<div class="juror{" chair" if r=="Jury Chair" else ""}">{mono(n)}<div><h4>{H(n)}<span class="r">{tx(r)}</span></h4><p>{tx(d)}</p></div></div>' for n, r, d in JURY)
    crit = ''.join(f'<div class="crit"><div class="row"><span>{tx(ti)}</span><b>{t(str(v), bd(v))}</b></div><div class="trk"><div class="fill" style="--v:{v};--i:{i}"></div></div><p>{tx(dsc)}</p></div>' for i, (v, ti, dsc) in enumerate(RUBRIC))
    gov = ''.join(f'<div><b>{tx(ti)}</b><p>{tx(p)}</p></div>' for ti, p in GOVERNANCE)
    local = ''.join(f'<div><h5>{tx(i)}</h5><ul>{people_list(ppl, dept_bn)}</ul></div>' for i, ppl in LOCAL_JUDGES)
    return f'''
<section class="sec comp-sec" id="competitions" aria-labelledby="comp-h">
  <div class="wrap">
    <div class="head"><span class="tag">{t("Competitions · Open to students across Rangpur", "প্রতিযোগিতা · রংপুরের শিক্ষার্থীদের জন্য উন্মুক্ত")}</span><h2 id="comp-h">{t("Pick your stage. Bring your idea.", "তোমার মঞ্চ বেছে নাও। ভাবনা নিয়ে এসো।")}</h2>
    <p>{t("Three competitions, each with its own registration. School, college, university, medical, degree college and madrasa students can all take part. You can enter more than one.",
          "তিনটি প্রতিযোগিতা, প্রতিটির আলাদা নিবন্ধন। স্কুল, কলেজ, বিশ্ববিদ্যালয়, মেডিকেল, ডিগ্রি কলেজ ও মাদ্রাসার শিক্ষার্থীরা অংশ নিতে পারবে। চাইলে একাধিকটিতেও অংশ নিতে পারো।")}</p></div>
    <div class="comps">{cards}</div>
    <div class="stagebar"><div class="lead">{t("On stage, 9 January", "মঞ্চে, ৯ জানুয়ারি")}</div><div><b>{t("3 medical-student teams", "৩টি মেডিকেল শিক্ষার্থী দল")}</b><span>{t("Grand Final: 15-minute pitch and 5 minutes of jury Q&amp;A", "গ্র্যান্ড ফাইনাল: ১৫ মিনিট পিচ ও ৫ মিনিট জুরির প্রশ্নোত্তর")}</span></div><div><b>{t("9 young changemakers", "৯ জন তরুণ চেঞ্জমেকার")}</b><span>{t("School, college and university students, 5 minutes each", "স্কুল, কলেজ ও বিশ্ববিদ্যালয়ের শিক্ষার্থী, প্রত্যেকে ৫ মিনিট")}</span></div></div>

    <div class="sub-h"><h3>{t("How the Grand Final is judged", "গ্র্যান্ড ফাইনালের বিচার যেভাবে হবে")}</h3><p>{t("An independent five-member jury scores every team on the same 100-point rubric, aligned with Universal Health Coverage and SDG 3.", "পাঁচ সদস্যের স্বাধীন জুরি প্রতিটি দলকে একই ১০০ নম্বরের মানদণ্ডে মূল্যায়ন করবেন, যা সর্বজনীন স্বাস্থ্যসেবা ও SDG ৩-এর সঙ্গে সামঞ্জস্যপূর্ণ।")}</p></div>
    <div class="jury-grid">
      <div class="jury">{jury}</div>
      <div class="rubric"><h4>{t("The 100-point rubric", "১০০ নম্বরের মানদণ্ড")}</h4><p>{t("What earns points with the jury.", "জুরির কাছে যেভাবে নম্বর মেলে।")}</p>{crit}</div>
    </div>
    <div class="gov">{gov}</div>
    <details class="more"><summary>{t("15 local-round judges", "স্থানীয় রাউন্ডের ১৫ জন বিচারক")} <span class="m">{t("Up to 5 heads of department per medical college", "প্রতি মেডিকেল কলেজে সর্বোচ্চ ৫ জন বিভাগীয় প্রধান")}</span><span class="plus">{ICON['plus']}</span></summary><div class="cols">{local}</div></details>
  </div>
</section>'''

def venue():
    spots = [
        ('1', 'Main Hall', 'মেইন হল', 'Plenaries, Track A and the showcase', 'প্লেনারি, ট্র্যাক এ ও শোকেস'),
        ('2', 'Hallroom 2', 'হলরুম ২', 'Pitch finals and Track B', 'পিচ ফাইনাল ও ট্র্যাক বি'),
        ('3', 'Dining area', 'ডাইনিং', 'Networking lunch', 'নেটওয়ার্কিং লাঞ্চ'),
        ('4', 'Registration', 'নিবন্ধন', 'Arrival and welcome', 'আগমন ও স্বাগত'),
        ('5', 'Recreation zone', 'রিক্রিয়েশন জোন', 'Networking and activations', 'নেটওয়ার্কিং ও নানা আয়োজন'),
        ('6', 'Guesthouse', 'গেস্টহাউস', 'On-site RDRS Guesthouse tower', 'ক্যাম্পাসেই আরডিআরএস গেস্টহাউস'),
        ('7', 'Parking', 'পার্কিং', 'Arrival and drop-off', 'আগমন ও নামা-ওঠা'),
    ]
    legend = ''.join(f'<li><button type="button" data-k="{k}"><i>{t(k, bd(k))}</i><span><b>{t(a, b)}</b><span>{t(c, d)}</span></span></button></li>' for k, a, b, c, d in spots)
    S = 'stroke="#0B1220" stroke-width="3"'
    def lab(x, y, en, bn, size):
        return (f'<text class="en" x="{x}" y="{y}" text-anchor="middle" font-family="Bricolage Grotesque,sans-serif" font-weight="800" font-size="{size}" fill="#0B1220">{en}</text>'
                f'<text class="bn" x="{x}" y="{y}" text-anchor="middle" font-family="Baloo Da 2,Hind Siliguri,sans-serif" font-weight="800" font-size="{size}" fill="#0B1220">{bn}</text>')
    def pin(x, y, k): return f'<g class="pin"><circle cx="{x}" cy="{y}" r="14" fill="#fff" {S}/>{lab(x, y+5, k, bd(k), 15)}</g>'
    svg = f'''<svg viewBox="0 0 640 460" role="img" aria-label="Indicative map of the RDRS campus in Rangpur">
<rect width="640" height="460" fill="#EAF8EE"/>
<path d="M0 410 C140 380 260 430 380 400 S560 380 640 400 V460 H0Z" fill="#D7F0DE"/>
<circle cx="560" cy="70" r="46" fill="#C9EBD3"/><circle cx="600" cy="120" r="30" fill="#C9EBD3"/><circle cx="40" cy="60" r="34" fill="#C9EBD3"/><circle cx="330" cy="40" r="22" fill="#C9EBD3"/><circle cx="470" cy="420" r="26" fill="#C9EBD3"/>
<path d="M60 440 V330 H600 M320 330 V120 M320 200 H520" fill="none" stroke="#fff" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M60 440 V330 H600 M320 330 V120 M320 200 H520" fill="none" stroke="#C8DCE6" stroke-width="2" stroke-dasharray="6 8"/>
<g class="spot" data-k="1"><rect class="bld" x="90" y="150" width="200" height="150" rx="16" fill="#fff" {S}/><rect x="90" y="150" width="200" height="34" rx="16" fill="#01BADC" {S}/>{lab(190, 250, "Main Hall", "মেইন হল", 20)}{pin(110,140,"1")}</g>
<g class="spot" data-k="2"><rect class="bld" x="350" y="220" width="150" height="90" rx="14" fill="#fff" {S}/><rect x="350" y="220" width="150" height="26" rx="13" fill="#A93391" {S}/>{lab(425, 285, "Hallroom 2", "হলরুম ২", 17)}{pin(368,212,"2")}</g>
<g class="spot" data-k="3"><rect class="bld" x="350" y="110" width="150" height="74" rx="14" fill="#fff" {S}/><rect x="350" y="110" width="150" height="24" rx="12" fill="#FF8A00" {S}/>{lab(425, 168, "Dining", "ডাইনিং", 17)}{pin(368,102,"3")}</g>
<g class="spot" data-k="4"><rect class="bld" x="94" y="344" width="110" height="52" rx="12" fill="#fff" {S}/>{lab(149, 376, "Registration", "নিবন্ধন", 15)}{pin(208,346,"4")}</g>
<g class="spot" data-k="5"><path class="b" d="M530 230 h70 a16 16 0 0 1 16 16 v60 a16 16 0 0 1 -16 16 h-70 a16 16 0 0 1 -16 -16 v-60 a16 16 0 0 1 16 -16Z" fill="#FFF3BF" {S} stroke-dasharray="8 6"/><circle cx="548" cy="262" r="8" fill="#14B8A6"/><circle cx="580" cy="290" r="8" fill="#D63E9C"/><circle cx="592" cy="256" r="6" fill="#2F6FE0"/>{pin(600,232,"5")}</g>
<g class="spot" data-k="6"><rect class="bld" x="140" y="34" width="120" height="80" rx="10" fill="#fff" {S}/><path d="M156 52h20M196 52h20M236 52h12M156 72h20M196 72h20M236 72h12M156 92h20M196 92h20M236 92h12" stroke="#0B1220" stroke-width="3" stroke-linecap="round" opacity=".5"/>{pin(152,30,"6")}</g>
<g class="spot" data-k="7"><rect class="bld" x="380" y="350" width="170" height="62" rx="12" fill="#fff" {S}/><path d="M410 350v62M440 350v62M470 350v62M500 350v62M530 350v62" stroke="#0B1220" stroke-width="2" opacity=".25"/>{lab(465, 388, "P", "P", 15)}{pin(392,346,"7")}</g>
<g><rect x="26" y="420" width="72" height="30" rx="8" fill="#FFCD00" {S}/>{lab(62, 441, "Entrance", "প্রবেশপথ", 12)}</g>
</svg>'''
    return f'''
<section class="sec" id="venue" aria-labelledby="venue-h">
  <div class="wrap">
    <div class="head"><span class="tag">{t("The venue", "ভেন্যু")}</span><h2 id="venue-h">{t("RDRS, Rangpur City.", "আরডিআরএস, রংপুর শহর।")}</h2>
    <p>{t("Every session happens on one green, easy-to-walk campus, with the RDRS Guesthouse on site.", "সব সেশন একটি সবুজ, সহজে হেঁটে ঘোরা যায় এমন ক্যাম্পাসে, আরডিআরএস গেস্টহাউসও ক্যাম্পাসের ভেতরেই।")}</p></div>
    <div class="gallery">
      <figure class="g1"><img src="assets/venue/rdrs-3.webp" width="760" height="804" loading="lazy" decoding="async" alt="{t("Ivy-covered RDRS building in Rangpur with its covered driveway", "লতায় ঢাকা আরডিআরএস ভবন ও প্রবেশপথ, রংপুর").replace('<span class="en">','').replace('</span><span class="bn" lang="bn">',' / ').replace('</span>','')}"></figure>
      <figure class="g2"><img src="assets/venue/rdrs-2.webp" width="900" height="500" loading="lazy" decoding="async" alt="Tree-lined driveway on the RDRS campus"></figure>
      <figure class="g3"><img src="assets/venue/rdrs-1.webp" width="495" height="619" loading="lazy" decoding="async" alt="The green RDRS campus seen from above"></figure>
      <figure class="cap"><b>{t("RDRS, Rangpur", "আরডিআরএস, রংপুর")}</b><span>{t("A green, walkable campus with everything in one place: halls, dining, gardens and the on-site guesthouse.", "হল, ডাইনিং, বাগান আর ক্যাম্পাসের গেস্টহাউস, সব এক জায়গায়, সবুজ আর হেঁটে ঘোরার মতো ক্যাম্পাস।")}</span></figure>
    </div>
    <div class="venue-grid">
      <div class="map">{svg}</div>
      <div><ul class="legend">{legend}</ul>
      <div class="venue-meta"><a class="btn ghost" href="https://www.google.com/maps/search/?api=1&amp;query=RDRS+Bangladesh+Rangpur" target="_blank" rel="noopener">{ICON['pin']} {t("Open in Google Maps", "গুগল ম্যাপসে খুলুন")}</a></div>
      <p class="prog-note">{t("Map is indicative, not to scale.", "ম্যাপটি আনুমানিক, স্কেল অনুযায়ী নয়।")}</p></div>
    </div>
  </div>
</section>'''

def partners():
    head = '<th scope="col"><span class="sr">Benefit</span></th>' + ''.join(f'<th scope="col">{tx(ti)}{"<small>" + t("Engagement Partner", "এনগেজমেন্ট পার্টনার") + "</small>" if ti=="Co-sponsor" else ""}</th>' for ti in TIERS)
    body = ''
    for g, rows in BENEFITS:
        body += f'<tr class="grp"><td colspan="5">{tx(g)}</td></tr>'
        for label, v in rows:
            body += '<tr><td>' + tx(label) + '</td>' + ''.join(f'<td>{"<span class=y>" + ICON["check"] + "<span class=sr>" + t("Included", "অন্তর্ভুক্ত") + "</span></span>" if x else "<span class=n aria-label=\"Not included\">–</span>"}</td>' for x in v) + '</tr>'
    why = [("200+", "২০০+", "Direct audience", "সরাসরি দর্শক", "Specialist doctors, 2,000+ medical students and 200+ pharmacies: prescribers, future prescribers and dispensers in one room.", "বিশেষজ্ঞ চিকিৎসক, ২,০০০+ মেডিকেল শিক্ষার্থী ও ২০০+ ফার্মেসি: যাঁরা প্রেসক্রিপশন লেখেন, ভবিষ্যতে লিখবেন এবং ওষুধ দেন, সবাই এক কক্ষে।"),
           ("30+", "৩০+", "Brand visibility", "ব্র্যান্ড দৃশ্যমানতা", "Promotional materials, 15 social content pieces, live coverage and outreach to 15+ newspapers.", "প্রচারসামগ্রী, ১৫টি সোশ্যাল কনটেন্ট, লাইভ কভারেজ ও ১৫+ সংবাদপত্রে প্রচার।"),
           ("6", "৬", "Thought leadership", "চিন্তার নেতৃত্ব", "Countries on stage, with keynote and panel slots alongside DGHS leaders and international experts.", "দেশের বক্তা মঞ্চে; স্বাস্থ্য অধিদপ্তরের নেতৃবৃন্দ ও আন্তর্জাতিক বিশেষজ্ঞদের পাশে কিনোট ও প্যানেলে অংশ নেওয়ার সুযোগ।"),
           ("~1M", "~১০ লাখ", "Purpose and impact", "উদ্দেশ্য ও প্রভাব", "People reached. Stand with connected primary care for last-mile communities.", "মানুষের কাছে পৌঁছানো। শেষ প্রান্তের কমিউনিটির কানেক্টেড প্রাইমারি কেয়ারের পাশে দাঁড়ান।")]
    whyh = ''.join(f'<div><b>{t(a, b)}</b><span><h4>{t(c, d)}</h4><p>{t(e, f)}</p></span></div>' for a, b, c, d, e, f in why)
    jour = [("30 Nov to 8 Jan", "৩০ নভেম্বর থেকে ৮ জানুয়ারি", "Before the event", "অনুষ্ঠানের আগে",
             [("Logo on event identity and approved collateral", "অনুষ্ঠানের পরিচিতি ও অনুমোদিত সামগ্রীতে লোগো"), ("Announcements on Shukhee social channels", "সুখীর সোশ্যাল চ্যানেলে ঘোষণা"), ("Visibility in student and campus outreach", "শিক্ষার্থী ও ক্যাম্পাস কার্যক্রমে দৃশ্যমানতা")]),
            ("9 Jan", "৯ জানুয়ারি", "On the day", "অনুষ্ঠানের দিন",
             [("Stall, pavilion and long banner", "স্টল, প্যাভিলিয়ন ও লং ব্যানার"), ("Keynote or panel slot, sponsor remarks", "কিনোট বা প্যানেলে অংশ, স্পনসর বক্তব্য"), ("Lunch, recreation zone, awards and raffle presence", "লাঞ্চ, রিক্রিয়েশন জোন, অ্যাওয়ার্ড ও র‍্যাফেলে উপস্থিতি")]),
            ("10 to 20 Jan", "১০ থেকে ২০ জানুয়ারি", "After the event", "অনুষ্ঠানের পরে",
             [("PR coverage and press release", "পিআর কভারেজ ও প্রেস রিলিজ"), ("Highlights, recap content and interview clips", "হাইলাইটস, রিক্যাপ কনটেন্ট ও সাক্ষাৎকারের ক্লিপ"), ("Website and blog features, media tracking", "ওয়েবসাইট ও ব্লগে ফিচার, গণমাধ্যম ট্র্যাকিং")])]
    jh = ''.join(f'<div><small>{t(a, b)}</small><h4>{t(c, d)}</h4><ul>{"".join(f"<li>{t(x, y)}</li>" for x, y in items)}</ul></div>' for a, b, c, d, items in jour)
    return f'''
<section class="sec" id="partners" style="background:#fff" aria-labelledby="pt-h">
  <div class="wrap">
    <div class="head"><span class="tag">{t("Partner with us", "সহযোগী হোন")}</span><h2 id="pt-h">{t("Light the way with us.", "আমাদের সঙ্গে আলো ছড়ান।")}</h2>
    <p>{t("Pharmaceutical companies, hospitals, health-tech firms, INGOs and institutions: Alokbortika puts your brand in front of every level of the health system in a single day.",
          "ওষুধ কোম্পানি, হাসপাতাল, হেলথ-টেক প্রতিষ্ঠান, আন্তর্জাতিক এনজিও ও অন্যান্য প্রতিষ্ঠান: এক দিনেই আলোকবর্তিকা আপনার ব্র্যান্ডকে পৌঁছে দেবে স্বাস্থ্যব্যবস্থার প্রতিটি স্তরে।")}</p></div>
    <div class="pgrid">
      <div class="why">{whyh}</div>
      <div class="tbl-wrap"><table class="tiers"><caption class="sr">Partnership packages and benefits</caption><thead><tr>{head}</tr></thead><tbody>{body}</tbody>
      <tfoot><tr><td colspan="5">{t("Packages can be tailored. Contact us for pricing. Final deliverables, logo size and placement depend on package confirmation and approved brand guidelines.", "প্যাকেজ চাহিদা অনুযায়ী সাজানো যায়। মূল্যের জন্য যোগাযোগ করুন। চূড়ান্ত সুবিধা, লোগোর আকার ও অবস্থান প্যাকেজ নিশ্চিতকরণ ও অনুমোদিত ব্র্যান্ড নির্দেশিকার ওপর নির্ভর করবে।")}</td></tr></tfoot></table></div>
    </div>
    <div class="journey">{jh}</div>
  </div>
</section>'''

def closing():
    return f'''
<section class="closing" id="contact" aria-labelledby="cl-h">
  <div class="grid-bg" aria-hidden="true"></div>
  <div class="wrap">
    <h2 id="cl-h">{t("Carry the torch with us.", "আমাদের সঙ্গে মশাল বহন করুন।")}</h2>
    <p>{t("Be among the first torchbearers of connected primary care in Bangladesh, whether you're on stage, in the audience, pitching an idea or partnering with us.", "বাংলাদেশে কানেক্টেড প্রাইমারি কেয়ারের প্রথম মশালবাহকদের একজন হোন: মঞ্চে, দর্শকসারিতে, ভাবনা নিয়ে কিংবা সহযোগী হয়ে।")}</p>
    <div class="cta-row"><a class="btn sun" href="{REG}#competitions">{t("Enter a competition", "প্রতিযোগিতায় অংশ নাও")}</a><a class="btn ghost" href="mailto:info@shukhee.com?subject=Alokbortika%202027%20partnership">{t("Talk to us about partnering", "সহযোগিতা নিয়ে কথা বলুন")}</a></div>
    <div class="contacts">
      <div class="contact"><small>{t("Hotline", "হটলাইন")}</small><b>{t("10657", "১০৬৫৭")}</b><p>{t("For guests and general questions", "অতিথি ও সাধারণ জিজ্ঞাসার জন্য")}</p></div>
      <div class="contact"><small>{t("Email", "ইমেইল")}</small><a href="mailto:info@shukhee.com"><b>info@shukhee.com</b></a><p>{t("To confirm participation or ask anything", "অংশগ্রহণ নিশ্চিত করতে বা যেকোনো প্রশ্নে")}</p></div>
    </div>
  </div>
</section>'''

def footer():
    return f'''
<footer>
  <div class="wrap">
    <div class="foot">
      <div><div class="logos"><span class="logo-bg" role="img" aria-label="Alokbortika 2027" style="width:85px;height:84px"></span><span class="sk"><img src="assets/shukhee.webp" alt="Shukhee" width="80" height="30"></span></div>
      <p>{t("Alokbortika 2027 is a healthcare stakeholder and recognition event organised by Grameen HealthTech Limited, the team behind Shukhee.", "আলোকবর্তিকা ২০২৭ একটি স্বাস্থ্যসেবা অংশীজন ও স্বীকৃতি অনুষ্ঠান, আয়োজনে গ্রামীণ হেলথটেক লিমিটেড, সুখীর পেছনের দল।")}</p></div>
      <div><h5>{t("Event", "অনুষ্ঠান")}</h5><ul><li><a href="#about">{t("About", "পরিচিতি")}</a></li><li><a href="#programme">{t("Programme", "অনুষ্ঠানসূচি")}</a></li><li><a href="#speakers">{t("Speakers", "বক্তা")}</a></li><li><a href="#venue">{t("Venue", "ভেন্যু")}</a></li></ul></div>
      <div><h5>{t("Take part", "অংশ নিন")}</h5><ul><li><a href="{REG}#competitions">{t("Competitions", "প্রতিযোগিতা")}</a></li><li><a href="{REG}#idea-competition">{tx("Idea Competition")}</a></li><li><a href="{REG}#changemaker">{tx("Become the Changemaker")}</a></li><li><a href="{REG}#case-study">{tx("Shukhee Case Study")}</a></li><li><a href="#partners">{t("Partner with us", "সহযোগী হোন")}</a></li></ul></div>
    </div>
    <div class="legal"><span>{t("© 2027 Grameen HealthTech Limited", "© ২০২৭ গ্রামীণ হেলথটেক লিমিটেড")}</span><span>{t("Saturday, 9 January 2027 · RDRS, Rangpur, Bangladesh", "শনিবার, ৯ জানুয়ারি ২০২৭ · আরডিআরএস, রংপুর, বাংলাদেশ")}</span></div>
  </div>
</footer>'''

LAT = 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
LATX = 'U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF'
BN_RANGE = 'U+0951-0952,U+0964-0965,U+0980-09FE,U+1CD0,U+1CD2,U+1CD5-1CD6,U+1CD8,U+1CE1,U+1CEA,U+1CED,U+1CF2,U+1CF5-1CF7,U+200C-200D,U+20B9,U+25CC,U+A8F1'
FONTS = [('Schibsted Grotesk', '400 900', 'schibsted-latin.woff2', LAT), ('Schibsted Grotesk', '400 900', 'schibsted-latin-ext.woff2', LATX),
         ('Noto Sans Bengali', '100 900', 'noto-bengali.woff2', BN_RANGE), ('Baloo Da 2', '800', 'baloo-bn-800.woff2', BN_RANGE)]

def fontface():
    out = ''
    for fam, w, f, ur in FONTS:
        out += "@font-face{font-family:'%s';font-style:normal;font-display:swap;font-weight:%s;src:url(assets/fonts/%s) format('woff2')%s}\n" % (fam, w, f, ';unicode-range:' + ur if ur else '')
    return out

def page():
    nav = [('#about', 'About', 'পরিচিতি'), ('#programme', 'Programme', 'অনুষ্ঠানসূচি'), ('#speakers', 'Speakers', 'বক্তা'), ('#venue', 'Venue', 'ভেন্যু'), ('#partners', 'Partners', 'সহযোগী')]
    comp = f'<a href="{REG}#competitions">{t("Competitions", "প্রতিযোগিতা")}</a>'
    links = ''.join(f'<a href="{h}">{t(e, b)}</a>' for h, e, b in nav) + comp
    reg = t("Register now", "রেজিস্টার করো")
    sheet = ''.join(f'<a href="{h}">{t(e, b)}</a>' for h, e, b in nav) + comp + f'<a class="btn" href="{REG}#competitions">{reg}</a>'
    toggle = '<div class="lang" role="group" aria-label="Language / ভাষা"><button type="button" data-l="en" aria-pressed="true" lang="en">EN</button><button type="button" data-l="bn" aria-pressed="false" lang="bn">বাংলা</button></div>'
    css = open(os.path.join(SRC, 'style.css')).read()
    js = open(os.path.join(SRC, 'app.js')).read()
    desc = "Alokbortika 2027: Lighting the Last Mile. A one-day healthcare stakeholder and recognition event on connected primary care, 9 January 2027 at RDRS, Rangpur, organised by Grameen HealthTech Limited."
    title_en = "Alokbortika 2027 · Lighting the Last Mile · 9 January, Rangpur"
    title_bn = "আলোকবর্তিকা ২০২৭ · আলো পৌঁছাক শেষ প্রান্তে · ৯ জানুয়ারি, রংপুর"
    body = hero() + leads() + about() + numbers() + evidence() + climb() + road() + programme() + people() + competitions() + venue() + partners() + closing()
    return f'''<!doctype html>
<html lang="en" class="no-js" data-start="{EVENT['date_iso']}" data-title-en="{H(title_en)}" data-title-bn="{H(title_bn)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H(title_en)}</title>
<script>(function(d){{d.className='js';var l='en';try{{l=sessionStorage.getItem('alokbortika.site.lang')==='bn'?'bn':'en'}}catch(e){{}}d.setAttribute('data-lang',l);d.lang=l;if(l==='bn')document.title=d.getAttribute('data-title-bn')}})(document.documentElement)</script>
<meta name="description" content="{H(desc)}">
<meta property="og:title" content="Alokbortika 2027 · Lighting the Last Mile">
<meta property="og:description" content="{H(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#BFE9FA">
<link rel="preload" href="assets/fonts/schibsted-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/logo.webp" as="image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='30' fill='%2301BADC' stroke='%230B1220' stroke-width='4'/%3E%3Cpath d='M32 12c6 8 8 14 2 22h-6c-5-6-2-14 4-22z' fill='%23FFCD00' stroke='%230B1220' stroke-width='3'/%3E%3Cpath d='M26 36h12l-4 18h-4z' fill='%23A93391' stroke='%230B1220' stroke-width='3'/%3E%3C/svg%3E">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Event","name":"Alokbortika 2027: Lighting the Last Mile","startDate":"2027-01-09T10:00:00+06:00","endDate":"2027-01-09T17:00:00+06:00","eventAttendanceMode":"https://schema.org/MixedEventAttendanceMode","eventStatus":"https://schema.org/EventScheduled","location":{{"@type":"Place","name":"RDRS","address":"Rangpur, Bangladesh"}},"organizer":{{"@type":"Organization","name":"Grameen HealthTech Limited"}},"inLanguage":["en","bn"],"description":"{H(desc)}"}}</script>
<style>
{fontface()}:root{{--logo:url(assets/logo.webp)}}
.logo-bg{{display:block;background:var(--logo) center/contain no-repeat}}
{css}</style>
</head>
<body>
<a class="skip" href="#main">{t("Skip to content", "মূল অংশে যান")}</a>
<header class="nav"><div class="wrap">
  <a class="brand" href="#top" aria-label="Alokbortika 2027, back to top"><span class="logo-bg" aria-hidden="true" style="width:53px;height:52px;flex:none"></span><span>{t("Alokbortika 2027", "আলোকবর্তিকা ২০২৭")}<small>{t("9 Jan · RDRS, Rangpur", "৯ জানুয়ারি · আরডিআরএস, রংপুর")}</small></span></a>
  <nav class="links" aria-label="Main">{links}</nav>
  <div class="nav-end">{toggle}<a class="btn" href="{REG}#competitions">{reg}</a>
  <button class="burger" type="button" aria-label="Menu" aria-controls="sheet" aria-expanded="false">{ICON['menu']}</button></div>
</div></header>
<nav class="sheet" id="sheet" aria-label="Mobile">{sheet}</nav>
<main id="main">
{body}
</main>
{footer()}
<script>
{js}</script>
</body>
</html>'''

if __name__ == '__main__':
    out = page()
    open(os.path.join(SITE, 'index.html'), 'w').write(out)
    print('index.html', len(out) // 1024, 'KB')
    if MISSING: print('MISSING BN:', sorted(MISSING))
