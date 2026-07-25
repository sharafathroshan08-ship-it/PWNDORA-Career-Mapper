// ======================================================
// PWNDORA AI
// SCRIPT PART 1
// ======================================================

const API_URL = "http://127.0.0.1:5000/analyze";

// ------------------------------------------------------
// ELEMENTS
// ------------------------------------------------------

const landingPage = document.getElementById("landing");
const uploadPage = document.getElementById("upload");
const loadingScreen = document.getElementById("loadingScreen");
const dashboard = document.getElementById("dashboard");

const startBtn = document.getElementById("startBtn");
const uploadBtn = document.getElementById("uploadBtn");

const resumeInput = document.getElementById("resume");

const progressBar = document.getElementById("progressBar");
const loadingTitle = document.getElementById("loadingTitle");
const status = document.getElementById("status");

// ------------------------------------------------------
// INITIAL STATE
// ------------------------------------------------------

dashboard.classList.add("hidden");
loadingScreen.classList.add("hidden");

// ------------------------------------------------------
// START ANALYSIS
// ------------------------------------------------------

startBtn.addEventListener("click", () => {

    uploadPage.scrollIntoView({

        behavior: "smooth"

    });

});

// ------------------------------------------------------
// ANALYZE BUTTON
// ------------------------------------------------------

uploadBtn.addEventListener("click", analyzeResume);

// ------------------------------------------------------
// MAIN FUNCTION
// ------------------------------------------------------

async function analyzeResume() {

    if (resumeInput.files.length === 0) {

        alert("Please choose a PDF resume.");

        return;

    }

    loadingScreen.classList.remove("hidden");

    startLoadingAnimation();

    const formData = new FormData();

    formData.append(

        "resume",

        resumeInput.files[0]

    );

    try {

        const response = await fetch(

            API_URL,

            {

                method: "POST",

                body: formData

            }

        );

        const data = await response.json();

        if (!data.success) {

            loadingScreen.classList.add("hidden");

            status.innerText = data.message;

            return;

        }

        window.report = data;

        loadingScreen.classList.add("hidden");

        dashboard.classList.remove("hidden");

        dashboard.scrollIntoView({

            behavior: "smooth"

        });

        loadDashboard(data);

    }

    catch(error){

        console.error(error);

        loadingScreen.classList.add("hidden");

        status.innerText = "Unable to connect backend.";

    }

}

// ------------------------------------------------------
// LOADING ANIMATION
// ------------------------------------------------------

function startLoadingAnimation(){

    const messages=[

        "Initializing PWNDORA AI...",

        "Reading Resume...",

        "Extracting Skills...",

        "Mapping Cyber Skills...",

        "Calculating Domain Scores...",

        "Finding Best Roles...",

        "Running Gap Analysis...",

        "Building Learning Roadmap...",

        "Preparing Final Report..."

    ];

    let progress = 0;

    let index = 0;

    progressBar.style.width = "0%";

    loadingTitle.innerText = messages[0];

    const timer = setInterval(()=>{

        progress += 12;

        progressBar.style.width = progress + "%";

        if(index < messages.length-1){

            index++;

            loadingTitle.innerText = messages[index];

        }

        if(progress >= 100){

            clearInterval(timer);

        }

    },400);

}
// ======================================================
// SCRIPT PART 2
// Dashboard + Sidebar + Analytics
// ======================================================

// ---------------------------
// SIDEBAR NAVIGATION
// ---------------------------

const sidebarItems = document.querySelectorAll(".sidebar li");

const pages = {

    home: document.getElementById("homePage"),

    resume: document.getElementById("resumePage"),

    domains: document.getElementById("domainPage"),

    roles: document.getElementById("rolePage"),

    gaps: document.getElementById("gapPage"),

    roadmap: document.getElementById("roadmapPage"),

    report: document.getElementById("reportPage")

};

sidebarItems.forEach(item=>{

    item.addEventListener("click",()=>{

        sidebarItems.forEach(i=>i.classList.remove("active"));

        item.classList.add("active");

        document.querySelectorAll(".page").forEach(page=>{

            page.classList.remove("active");

        });

        const selected = pages[item.dataset.page];

        if(selected){

            selected.classList.add("active");

        }

    });

});

// ---------------------------
// MAIN DASHBOARD
// ---------------------------

function loadDashboard(data){

    loadAnalytics(data.analytics);

    loadAISummary(data.ai_summary);

    loadResumeOverview(data.parsed_resume);

}

// ---------------------------
// ANALYTICS
// ---------------------------

function loadAnalytics(analytics){

    document.getElementById("careerReadiness").innerText =

        analytics.career_readiness + "%";

    document.getElementById("skillCoverage").innerText =

        analytics.skill_coverage + "%";

}

// ---------------------------
// AI SUMMARY
// ---------------------------

function loadAISummary(summary){

    document.getElementById("aiSummary").innerHTML = `

        <p>${summary.recommendation}</p>

        <br>

        <strong>

            Readiness :

            ${summary.readiness_level}

        </strong>

    `;

    const strengthList =

        document.getElementById("strengthList");

    const weaknessList =

        document.getElementById("weaknessList");

    strengthList.innerHTML = "";

    weaknessList.innerHTML = "";

    summary.strengths.forEach(item=>{

        strengthList.innerHTML += `

            <li>✅ ${item}</li>

        `;

    });

    summary.weaknesses.forEach(item=>{

        weaknessList.innerHTML += `

            <li>⚠️ ${item}</li>

        `;

    });

}

// ---------------------------
// RESUME OVERVIEW
// ---------------------------

function loadResumeOverview(resume){

    const info =

        document.getElementById("resumeInfo");

    info.innerHTML = `

        <p>

            <b>Matched Skills :</b>

            ${resume.matched_skills.length}

        </p>

        <p>

            <b>Matched Tools :</b>

            ${resume.matched_tools.length}

        </p>

        <p>

            <b>Matched Certificates :</b>

            ${resume.matched_certificates.length}

        </p>

    `;

    loadMatchedSkills(resume.matched_skills);

    loadMatchedTools(resume.matched_tools);

    loadMatchedCertificates(resume.matched_certificates);

}

// ---------------------------
// MATCHED SKILLS
// ---------------------------

function loadMatchedSkills(skills){

    const container =

        document.getElementById("matchedSkills");

    container.innerHTML = "";

    skills.forEach(skill=>{

        container.innerHTML += `

            <span class="skill-tag">

                ${skill.skill}

            </span>

        `;

    });

}

// ---------------------------
// MATCHED TOOLS
// ---------------------------

function loadMatchedTools(tools){

    const container =

        document.getElementById("matchedTools");

    container.innerHTML = "";

    tools.forEach(tool=>{

        container.innerHTML += `

            <span class="skill-tag">

                ${tool}

            </span>

        `;

    });

}

// ---------------------------
// MATCHED CERTIFICATES
// ---------------------------

function loadMatchedCertificates(certs){

    const container =

        document.getElementById("matchedCertificates");

    container.innerHTML = "";

    certs.forEach(cert=>{

        container.innerHTML += `

            <span class="skill-tag">

                ${cert}

            </span>

        `;

    });

}
// ======================================================
// SCRIPT PART 3
// Domains • Roles • Gap Analysis • Roadmap
// ======================================================

// ---------------------------
// DOMAIN SCORES
// ---------------------------

function loadDomains(mapping){

    const container = document.getElementById("domainContainer");

    container.innerHTML = "";

    let bestScore = -1;
    let bestDomain = "--";

    mapping.domain_scores.forEach(item=>{

        if(item.score > bestScore){

            bestScore = item.score;
            bestDomain = item.domain;

        }

        container.innerHTML += `

            <div>

                <h3>${item.domain}</h3>

                <h2>${item.score}</h2>

            </div>

        `;

    });

    document.getElementById("bestDomain").innerText = bestDomain;

}

// ---------------------------
// RECOMMENDED ROLES
// ---------------------------

function loadRoles(roles){

    const container = document.getElementById("roleContainer");

    container.innerHTML = "";

    if(roles.length){

        document.getElementById("topRole").innerText = roles[0].role;

    }

    roles.forEach(role=>{

        container.innerHTML += `

            <div>

                <h3>${role.role}</h3>

                <p><b>Score :</b> ${role.score}</p>

            </div>

        `;

    });

}

// ---------------------------
// GAP ANALYSIS
// ---------------------------

function loadGap(gaps){

    const container = document.getElementById("gapContainer");

    container.innerHTML = "";

    gaps.forEach(gap=>{

        let color = "#3dd8ff";

        if(gap.priority === "High") color = "#ff5555";
        if(gap.priority === "Medium") color = "#ffc107";
        if(gap.priority === "Low") color = "#43d17d";

        container.innerHTML += `

            <div>

                <h3>${gap.skill}</h3>

                <p><b>Domain:</b> ${gap.domain}</p>

                <p style="color:${color}">

                    <b>Priority:</b> ${gap.priority}

                </p>

                <p><b>Difficulty:</b> ${gap.difficulty}</p>

            </div>

        `;

    });

}

// ---------------------------
// ROADMAP
// ---------------------------

function loadRoadmap(roadmap){

    const container = document.getElementById("roadmapContainer");

    container.innerHTML = "";

    Object.entries(roadmap).forEach(([level,skills])=>{

        let html = `

            <div class="dashboard-card">

                <h2>${level}</h2>

                <ul>

        `;

        if(skills.length===0){

            html += "<li>No recommendations.</li>";

        }else{

            skills.forEach(skill=>{

                html += `

                    <li>

                        ${skill.skill}

                        (${skill.domain})

                    </li>

                `;

            });

        }

        html += `

                </ul>

            </div>

        `;

        container.innerHTML += html;

    });

}

// ---------------------------
// UPDATE DASHBOARD
// ---------------------------

function loadDashboard(data){

    loadAnalytics(data.analytics);

    loadAISummary(data.ai_summary);

    loadResumeOverview(data.parsed_resume);

    loadDomains(data.mapping_result);

    loadRoles(data.recommended_roles);

    loadGap(data.gap_analysis);

    loadRoadmap(data.roadmap);

}
// ======================================================
// SCRIPT PART 4
// Report Download + Utilities
// ======================================================

// ---------------------------
// DOWNLOAD REPORT
// ---------------------------

const downloadButton = document.getElementById("downloadReport");

if(downloadButton){

    downloadButton.addEventListener("click", downloadReport);

}

function downloadReport(){

    if(!window.report){

        alert("Please analyze a resume first.");

        return;

    }

    const reportData = JSON.stringify(

        window.report.report,

        null,

        4

    );

    const blob = new Blob(

        [reportData],

        {

            type:"application/json"

        }

    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "PWNDORA_AI_Report.json";

    document.body.appendChild(a);

    a.click();

    document.body.removeChild(a);

    URL.revokeObjectURL(url);

}

// ---------------------------
// RESET STATUS
// ---------------------------

function clearStatus(){

    if(status){

        status.innerText = "";

    }

}

// ---------------------------
// FILE CHANGE
// ---------------------------

if(resumeInput){

    resumeInput.addEventListener("change",()=>{

        clearStatus();

    });

}

// ---------------------------
// KEYBOARD SHORTCUT
// ---------------------------

document.addEventListener("keydown",(event)=>{

    if(event.key==="Enter"){

        if(uploadPage.contains(document.activeElement)){

            analyzeResume();

        }

    }

});

// ---------------------------
// STARTUP
// ---------------------------

window.addEventListener("load",()=>{

    console.log("===================================");

    console.log("PWNDORA AI Frontend Loaded");

    console.log("Backend :",API_URL);

    console.log("Ready");

    console.log("===================================");

});
