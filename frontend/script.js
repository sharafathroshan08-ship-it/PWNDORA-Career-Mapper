// ======================================================
// PWNDORA Career Mapper
// Frontend Script - Part 1
// ======================================================

const API_URL = "http://127.0.0.1:5000/analyze";

const analyzeBtn = document.getElementById("analyzeBtn");
const resumeInput = document.getElementById("resume");

analyzeBtn.addEventListener("click", analyzeResume);

async function analyzeResume() {

    const file = resumeInput.files[0];

    if (!file) {
        alert("Please select a Resume PDF.");
        return;
    }

    analyzeBtn.disabled = true;
    analyzeBtn.innerText = "Analyzing...";

    const formData = new FormData();

    formData.append("resume", file);

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            body: formData

        });

        const report = await response.json();

        if (!report.success) {

            alert(report.message);

            analyzeBtn.disabled = false;
            analyzeBtn.innerText = "Analyze Resume";

            return;

        }

        loadDomains(report.mapping_result.domain_scores);

        loadRoles(report.recommended_roles);

        loadGap(report.gap_analysis);

        loadLearning(report.learning_path);

    }

    catch(error){

        console.error(error);

        alert("Unable to connect to Flask Backend.");

    }

    analyzeBtn.disabled = false;

    analyzeBtn.innerText = "Analyze Resume";

}
// ======================================================
// DOMAIN SCORES
// ======================================================

function loadDomains(domains) {

    const div = document.getElementById("domainScores");

    div.innerHTML = "";

    const maxScore = 3.0;

    domains.forEach(item => {

        const percent = Math.round((item.score / maxScore) * 100);

        div.innerHTML += `

        <div class="domain-card">

            <div class="domain-header">

                <span>${item.domain}</span>

                <strong>${item.score}</strong>

            </div>

            <div class="progress">

                <div class="progress-fill"
                     style="width:${percent}%">
                </div>

            </div>

        </div>

        `;

    });

}



// ======================================================
// ROLE RECOMMENDATIONS
// ======================================================

function loadRoles(roles) {

    const div = document.getElementById("roles");

    div.innerHTML = "";

    if (roles.length === 0)
        return;

    const best = roles[0];

    div.innerHTML += `

        <div class="best-role">

            <h3>🏆 Best Match</h3>

            <h2>${best.role}</h2>

            <p>

                Match Score :
                <strong>${best.score}</strong>

            </p>

        </div>

        <hr>

    `;

    roles.slice(1).forEach(role => {

        div.innerHTML += `

            <p>

                🎯 ${role.role}
                (${role.score})

            </p>

        `;

    });

}
// ======================================================
// GAP ANALYSIS
// ======================================================

function loadGap(gaps) {

    const div = document.getElementById("gap");

    div.innerHTML = "";

    if (!gaps || gaps.length === 0) {

        div.innerHTML = "<p>No skill gaps found.</p>";
        return;

    }

    gaps.slice(0, 10).forEach(skill => {

        div.innerHTML += `

            <p>

                ❌ ${skill.skill}

                <br>

                <small>
                    ${skill.priority}
                </small>

            </p>

            <hr>

        `;

    });

}



// ======================================================
// LEARNING PATH
// ======================================================

function loadLearning(path) {

    const div = document.getElementById("learning");

    div.innerHTML = "";

    if (!path) {

        div.innerHTML = "<p>No learning path available.</p>";

        return;

    }

    function addSection(title, labs) {

        if (!labs || labs.length === 0)
            return;

        div.innerHTML += `

            <h3>${title}</h3>

        `;

        labs.slice(0, 5).forEach(lab => {

            div.innerHTML += `

                <p>

                    🧪 ${lab.skill}

                    <br>

                    <small>

                        ${lab.hours} Hours

                    </small>

                </p>

            `;

        });

    }

    addSection("Foundation", path.foundation);

    addSection("Primary", path.primary);

    addSection("Stretch", path.stretch);

}
