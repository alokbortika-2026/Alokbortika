# All event content lives here. Edit this file, then run build.py.
REG = "register.html"

EVENT = {
    "date_iso": "2027-01-09T10:00:00+06:00",
}

STATS = [
    ("~1M", "people reached through Grameen and Shukhee networks"),
    ("10,000+", "school, college and university students"),
    ("2,000+", "medical students from three Rangpur colleges"),
    ("200+", "specialist doctors and experts"),
    ("200+", "community pharmacies, with 600 link workers"),
    ("6", "countries on stage, in person and live"),
]

OOP = [("Bangladesh", 79.3), ("Nepal", 59.4), ("Sri Lanka", 54.8), ("Pakistan", 52.9),
       ("South Asia", 46.6), ("India", 43.9), ("World", 17.3)]

# root -> top
CLIMB = [
    ("~1M", "Community", "Patients, families and caregivers across Grameen communities"),
    ("10,000+", "Young changemakers", "School, college and university students with health ideas"),
    ("2,000+", "Medical students", "Prime, Rangpur Community and Rangpur Medical Colleges"),
    ("600", "Link workers", "With 200+ pharmacies as first-contact touchpoints"),
    ("200+", "Specialists", "Specialist doctors, nurses and public-health experts"),
    ("50", "Heads of department", "From all three Rangpur medical colleges"),
    ("20+", "Global experts", "DGHS leadership, JICA, PKSF and experts from 6 countries"),
]

PHASES = [
    ("2026-11-30", "2027-01-08", "From 30 Nov 2026", "Youth outreach", "10,000+ students",
     ["School, college and university outreach on community health",
      "Ideas on awareness, hygiene, nutrition and youth wellbeing",
      "9 young changemakers selected to pitch on stage"]),
    ("2026-11-30", "2027-01-08", "Before the event", "Medical college rounds", "2,000+ medical students",
     ["Campus rounds at Prime, Rangpur Community and Rangpur Medical Colleges",
      "Judged by up to 5 heads of department per college",
      "3 finalist teams go through to the Grand Final"]),
    ("2027-01-09", "2027-01-09", "9 Jan 2027", "Summit and Grand Final", "200+ specialists",
     ["Keynotes, six hybrid panels and the partner showcase",
      "Independent 5-member jury, 100-point rubric",
      "Alokbortika Awards for service and achievement"]),
    ("2027-01-10", "2027-01-20", "10 to 20 Jan 2027", "Amplify and follow up", "15+ newspapers",
     ["Official press release and media follow-up",
      "Highlights, interview clips and stakeholder bytes",
      "National Connected Primary Care agenda shared"]),
]

PANELS = {
    1: dict(room="Main Hall", time="2:00 to 2:30 PM", topic="Primary Healthcare", color="sky",
            title="Care Close to Home", sub="Making primary healthcare accessible for every family",
            q="How can pharmacies become trusted, regulated partners in primary care?",
            stat=("~69%", "of out-of-pocket spending goes on medicines")),
    2: dict(room="Main Hall", time="2:30 to 3:00 PM", topic="Women's Health", color="pop",
            title="Her Health, Her Voice", sub="Building trust in women's healthcare",
            q="What would make a rural woman confident to seek care digitally?",
            stat=("18.8%", "of women live with a mental health condition")),
    3: dict(room="Main Hall", time="3:00 to 3:30 PM", topic="Cross-Border Care", color="bolt",
            title="Care Without Borders", sub="Bringing quality treatment within reach",
            q="Which services must Bangladesh strengthen so families need not travel abroad?",
            stat=("US$5B", "estimated yearly spend on treatment abroad")),
    4: dict(room="Hallroom 2", time="2:00 to 2:30 PM", topic="Telenursing", color="mint",
            title="Nurses at the Heart of Care", sub="Reaching patients wherever they are",
            q="How can telenursing ease the doctor shortage while keeping care safe?",
            stat=("15", "health workers per 10,000 people, vs a 44.5 benchmark")),
    5: dict(room="Hallroom 2", time="2:30 to 3:00 PM", topic="Mind, Music & Healing", color="grape",
            title="Breaking the Silence", sub="Healing minds, ending stigma",
            q="What first step makes it safe to talk about mental health?",
            stat=("92%", "of adults with a mental health condition go untreated")),
    6: dict(room="Hallroom 2", time="3:00 to 3:30 PM", topic="Diabetes & Hypertension", color="coral",
            title="Beyond the Numbers", sub="Living well with diabetes and hypertension",
            q="How do we move from counting patients to keeping BP and sugar under control?",
            stat=("1 in 4", "adults has raised blood pressure")),
}

# name, role, org, country, panel, mode, focus, group
SPEAKERS = [
    ("Prof. Dr. Shah Md. Sarwar Jahan", "Professor of Medicine and Medicine Specialist", "Dinajpur Medical College & Hospital", "BD", 1, "In person", "When to visit a local doctor or pharmacy, and when to go to a hospital", "nat"),
    ("Prof. Dr. Abdul Wahed", "Professor of Paediatrics and Public Health", "", "BD", 1, "In person", "Keeping children healthy through care in the community", "nat"),
    ("Dr. Shah Ahasanul Imran", "Associate Professor & Head, Community Medicine & Public Health", "Rangpur Community Medical College", "BD", 1, "In person", "Early check-ups and disease prevention in the community", "nat"),
    ("Md. Fazlul Kader", "Managing Director", "Palli Karma-Sahayak Foundation (PKSF)", "Bangladesh", 1, "In person", "Bringing affordable healthcare to rural families", "intl"),
    ("Prof. Dr. Aziza Begum Lucy", "Professor, Gynaecology & Obstetrics", "Rangpur Community Medical College & Hospital", "BD", 2, "In person", "Helping women speak openly about their health concerns", "nat"),
    ("Prof. Dr. Halida Hanum Akhter", "Reproductive Health Epidemiologist, Obstetrician-Gynaecologist and Global Public Health Specialist", "", "BD", 2, "In person", "Safe motherhood and reproductive health for every woman", "nat"),
    ("Dr. David P. Hernandez", "Obstetrician-Gynaecologist and International Consultant", "MD, FACOG", "USA", 2, "Recorded message", "Respectful and confidential care for women worldwide", "intl"),
    ("Prof. Dr. Maruf Mollah", "Managing Director & Co-Founder, MalishaEdu; CEO, Belt & Road Healthcare Center", "MalishaEdu / BRHC", "China", 3, "Live virtual", "Getting specialist care without long and costly travel abroad", "intl"),
    ("Dr. Faiz H. Shah", "Executive Director, Yunus Center; Founding President, Yunus Thailand Foundation", "Asian Institute of Technology (AIT)", "Thailand", 3, "Live virtual", "Social business for affordable healthcare", "intl"),
    ("Dr. Bhattacharya", "Apollo Child Development Centre", "Apollo", "India", 3, "Virtual / in person", "Early support for children with developmental needs", "intl"),
    ("Dr. Krystal R. Sodaitis", "Chief Medical Officer", "ATRIO Health Plans", "USA", 3, "Recorded message", "Making quality healthcare affordable and accessible", "intl"),
    ("Prof. Michiko Moriyama", "Professor, Graduate School of Biomedical and Health Sciences", "Hiroshima University", "Japan", 4, "Live virtual", "How nurses in Japan support patients and families at home", "intl"),
    ("Ms. Yumi Okazaki", "Representative, Bangladesh Office", "JICA", "Japan", 4, "In person / virtual", "Japan and Bangladesh partnering to strengthen nursing", "intl"),
    ("Dr. Rehena Akter", "Principal", "Rangpur Community Nursing College", "BD", 4, "In person", "Training the next generation of nurses", "nat"),
    ("Brig. Gen. Dr. Md. Golam Rasul (LPR)", "Director", "Prime Medical College Hospital, Rangpur", "BD", 4, "In person", "The nurse's role in better patient care at hospitals", "nat"),
    ("Prof. Dr. Muhammad Abdul Monem", "Professor & Head, Department of Psychiatry", "Rangpur Community Medical College & Hospital", "BD", 5, "In person", "Mental illness is treatable, and it's okay to seek help", "nat"),
    ("Monica Yunus", "Co-Founder and Co-Executive Director", "Sing for Hope", "USA", 5, "Recorded message", "The healing power of music and the arts", "intl"),
    ("Dr. Madison Ngafeeson", "Business Professor, Leadership Coach and Founder", "LEAD Missions International", "USA", 5, "Recorded message", "Building inner strength and talking openly about mental health", "intl"),
    ("Prof. Dr. Md. Zakir Hossain", "Internal Medicine Specialist; Founder", "Hypertension and Research Centre, Rangpur", "BD", 6, "In person", "Controlling blood pressure in daily life", "nat"),
    ("Dr. Ratindra Nath Mondal", "Associate Professor of Medicine", "Prime Medical College & Hospital", "BD", 6, "In person", "Diet, exercise and medicine for managing diabetes", "nat"),
    ("Prof. Dr. Nawazesh Farid", "Professor of Cardiology", "Prime Medical College & Hospital", "BD", 6, "In person", "Protecting your heart when you have diabetes or high blood pressure", "nat"),
    ("Prof. Dr. S. M. G. Saklayen (Russel)", "Professor, Senior Consultant & Head, Vascular Surgery", "Ibrahim Cardiac Hospital & Research Institute, Dhaka", "BD", 6, "In person", "Foot care and preventing serious complications", "nat"),
]

HONOUR = [
    ("Prime Medical College & Hospital", [("Prof. Dr. Md. Rabiul Islam Shah", "Principal"), ("Brig. Gen. Dr. Md. Golam Rasul (LPR)", "Director, Prime Medical College Hospital")]),
    ("Rangpur Community Medical College & Hospital", [("Prof. Dr. Md. Shariful Islam", "Principal"), ("Dr. Swapan Kumar Barman", "Hospital Director")]),
    ("Rangpur Medical College & Hospital", [("Prof. Dr. Md. Anowar Hossain", "Principal; Professor & Head, Surgery"), ("Brig. Gen. Ashiqur Rahman, MPH", "Director, Rangpur Medical College Hospital")]),
]

JURY = [
    ("Prof. Dr. Halida Hanum Akhter", "Jury Chair", "Reproductive Health Epidemiologist, Obstetrician-Gynaecologist and Global Public Health Specialist"),
    ("Prof. Dr. Shah Md. Sarwar Jahan", "Member", "Professor of Medicine, Dinajpur Medical College & Hospital"),
    ("Prof. Dr. S. M. G. Saklayen (Russel)", "Member", "Head of Vascular Surgery, Ibrahim Cardiac Hospital & Research Institute"),
    ("Prof. Dr. Md. Zakir Hossain", "Member", "Internal Medicine Specialist; Founder, Hypertension and Research Centre, Rangpur"),
    ("Prof. Dr. Abdul Wahed", "Member", "Professor of Paediatrics and Public Health"),
]

RUBRIC = [
    (25, "Public health relevance", "A real primary-care problem in the community, aligned with UHC and SDG 3"),
    (20, "Evidence and approach", "Sound reasoning, credible data and a clear, ethical method"),
    (20, "Feasibility and sustainability", "Realistic in Bangladesh, affordable and able to scale"),
    (20, "Equity and people-centred care", "Reaches women, children, the elderly, the poor and remote communities"),
    (15, "Presentation and Q&A", "Clarity, teamwork, time-keeping and quality of answers"),
]

GOVERNANCE = [
    ("Independent", "Grand Final jurors are not faculty of the three competing colleges."),
    ("Conflict-free", "Every judge signs a declaration and abstains from any team they're linked to."),
    ("Scored alone", "Each judge scores on the common rubric before any discussion."),
    ("Clear tie-break", "Highest public-health relevance score first, then the Jury Chair's decision."),
    ("Transparent", "Score sheets are kept by the organisers and every team gets written feedback."),
]

LOCAL_JUDGES = [
    ("Prime Medical College & Hospital", [
        ("Prof. Dr. Md. Noor Islam", "Chair · Head, Medicine & Gastroenterology"),
        ("Dr. Tamanna Hamid", "Head, Community Medicine"),
        ("Prof. Dr. Chanchal Kumar Mondol", "Head, Paediatrics"),
        ("Prof. Dr. Mst. Kamrun Nahaer", "Professor, Gynaecology & Obstetrics"),
        ("Prof. Dr. Bimal Chandra Roy", "Head, Surgery")]),
    ("Rangpur Community Medical College & Hospital", [
        ("Prof. Dr. Md. Ghulam Yusuf", "Chair · Head, Medicine"),
        ("Dr. Shah Ahasanul Imran", "Head, Community Medicine & Public Health"),
        ("Prof. Dr. Ranjit Basak", "Head, Paediatrics"),
        ("Prof. Dr. Anisa Begum", "Head, Gynaecology & Obstetrics"),
        ("Prof. Dr. Muhammad Abdul Monem", "Head, Psychiatry")]),
    ("Rangpur Medical College & Hospital", [
        ("Prof. Dr. Devendra Nath Sarkar", "Chair · Head, Medicine"),
        ("Prof. Dr. Samir Kumar Talukder", "Head, Endocrinology"),
        ("Prof. Dr. A. B. M. Mobasher Alam Suja", "Head, Nephrology"),
        ("Assoc. Prof. Dr. Haripada Sarkar", "Head, Cardiology"),
        ("Prof. Dr. Shafiqul Islam", "Head, Orthopaedic Surgery")]),
]

HODS = [
    ("Prime Medical College & Hospital", [
        ("Prof. Dr. Md. Noor Islam", "Medicine & Gastroenterology"), ("Prof. Dr. Bimal Chandra Roy", "Surgery"),
        ("Prof. Dr. Md. Shariful Haque", "Orthopaedics"), ("Prof. Dr. Mst. Kamrun Nahaer", "Gynaecology & Obstetrics"),
        ("Prof. Dr. Shahi Farzana Tasmin", "Gynaecology & Obstetrics"), ("Prof. Dr. Chanchal Kumar Mondol", "Paediatrics"),
        ("Prof. Dr. Md. Abdul Azim", "ENT"), ("Dr. Md. Rafiqul Islam", "Ophthalmology"),
        ("Dr. Md. Golam Hossain", "Cardiology"), ("Dr. Khandker Anjumanara Begum", "Psychiatry"),
        ("Dr. Md. Mohiuddin", "Anaesthesiology"), ("Dr. Maruna Yesmeen", "Dermatology & Venereology"),
        ("Dr. Md. Mostafiger Rahman", "Urology"), ("Dr. Sharmin Akter Shathi", "Dental Unit"),
        ("Prof. Dr. Anjum Ara Begum", "Anatomy"), ("Prof. Dr. Md. Mominul Haque", "Physiology"),
        ("Prof. Dr. Md. Rashidul Hasan", "Biochemistry"), ("Prof. Dr. Md. Sohorab Hossain Bhuiyan", "Pathology"),
        ("Prof. Dr. Md. Khairuzzaman", "Microbiology"), ("Dr. Farhana Haque", "Pharmacology"),
        ("Dr. Tamanna Hamid", "Community Medicine"), ("Dr. Md. Amir Uddin", "Forensic Medicine")]),
    ("Rangpur Community Medical College & Hospital", [
        ("Prof. Dr. Md. Ghulam Yusuf", "Medicine"), ("Prof. Dr. Md. Jabed Akhtar", "Surgery"),
        ("Dr. Mriganko Bhattacharjee", "Orthopaedics"), ("Prof. Dr. Anisa Begum", "Gynaecology & Obstetrics"),
        ("Prof. Dr. Ranjit Basak", "Paediatrics"), ("Prof. Dr. Md. Azharul Islam (Azad)", "Cardiology"),
        ("Dr. Md. Feroz Hossen", "ENT"), ("Dr. Md. Masudul Haque", "Ophthalmology"),
        ("Prof. Dr. Md. Rezaul Alam", "Dermatology & Venereology"), ("Prof. Dr. Sadrul Islam Talukder", "Anaesthesiology"),
        ("Prof. Dr. Muhammad Abdul Monem", "Psychiatry"), ("Prof. Dr. Md. Mosabber Hossain", "Urology"),
        ("Prof. Dr. Shamsun-Nahar", "Anatomy"), ("Prof. Dr. Chandra Rani Sarkar", "Physiology"),
        ("Prof. Dr. Md. Abdur Rahim", "Vice-Principal; Biochemistry"), ("Prof. Dr. Beauty Saha", "Pharmacology & Therapeutics"),
        ("Prof. Dr. Md. Ahsan Habib", "Pathology"), ("Dr. Mst. Arefa Aktar", "Microbiology"),
        ("Dr. Shah Ahasanul Imran", "Community Medicine & Public Health"), ("Dr. Nusrat Afroz", "Forensic Medicine")]),
    ("Rangpur Medical College & Hospital", [
        ("Prof. Dr. Md. Anowar Hossain", "Principal; Surgery"), ("Prof. Dr. Devendra Nath Sarkar", "Medicine"),
        ("Prof. Dr. Shafiqul Islam", "Orthopaedic Surgery"), ("Assoc. Prof. Dr. Haripada Sarkar", "Cardiology"),
        ("Prof. Dr. Samir Kumar Talukder", "Endocrinology"), ("Prof. Dr. A. B. M. Mobasher Alam Suja", "Nephrology"),
        ("Dr. Prashant Roy", "Neurology"), ("Prof. Dr. A. M. Al-Rabbani", "ENT")]),
]

COMPETITIONS = [
    dict(key="idea", theme="idea", hash="idea-competition", name="Idea Competition",
         line="What kind of healthcare do you want for Bangladesh?",
         desc="Tell us what needs to change, and how, in a short video.",
         facts=[("Who", "School, college, university, medical, degree college and madrasa students"),
                ("Format", "A short video, made alone or in a team of up to 3"),
                ("Themes", "Digital healthcare, community care, health education, mental and child health")]),
    dict(key="cmk", theme="cmk", hash="changemaker", name="Become the Changemaker",
         line="Capture a story. Inspire a change.",
         desc="One photograph on healthcare, education, disease awareness or community development.",
         facts=[("Who", "Students from all six categories across Rangpur"),
                ("Format", "Your best original photo with a short caption"),
                ("Bonus", "Sign up to volunteer at the main event on 9 January")]),
    dict(key="case", theme="case", hash="case-study", name="Shukhee Case Study",
         line="How do we digitize the pharmacy?",
         desc="An inter-medical college challenge to rethink pharmacy services with digital tools.",
         facts=[("Who", "Medical college students only, in teams"),
                ("Format", "A written case study as PDF, PPT or PPTX"),
                ("The prize", "3 finalist teams pitch live at the Grand Final on 9 January")]),
]

TIERS = ["Title Sponsor", "Powered-by", "In Association", "Co-sponsor"]
BENEFITS = [
    ("Brand visibility", [
        ("Brand in every promotional material (30+)", [1, 1, 0, 0]),
        ("Brand in key promotional materials (10+)", [1, 1, 1, 1]),
        ("1 dedicated long banner at the venue", [1, 0, 0, 0]),
        ("Pre-event announcement on Shukhee social media", [1, 1, 1, 0]),
        ("Post-event PR coverage", [1, 1, 0, 0])]),
    ("Speaking and engagement", [
        ("1 keynote speech", [1, 0, 0, 0]),
        ("Panel discussion appearance", [1, 1, 0, 0]),
        ("Exclusive in-event announcement", [0, 0, 1, 0])]),
    ("On the day", [
        ("1 dedicated stall at the venue", [1, 1, 0, 0]),
        ("Exclusive branding in the lunch area", [0, 0, 1, 0]),
        ("Exclusive branding in the recreation area", [0, 0, 0, 1])]),
]
