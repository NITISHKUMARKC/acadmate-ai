// ========================================
// Tutor Elements
// ========================================

const askButton = getElement("askBtn");
const subjectSelect = getElement("subject");
const questionInput = getElement("question");


// ========================================
// Ask Button Click
// ========================================

askButton.addEventListener("click", async function () {

    // ========================================
    // Read User Input
    // ========================================

    const subject = subjectSelect.value.trim();
    const question = questionInput.value.trim();


    // ========================================
    // Input Validation
    // ========================================

    if (question === "") {

        showError("Please enter your question.");

        return;

    }


    // ========================================
    // Show Loading
    // ========================================

    showLoading();


    // ========================================
    // Send Request to FastAPI
    // ========================================

    const response = await fetch(
        "http://127.0.0.1:8000/ask",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                subject: subject,
                question: question
            })

        }
    );

    // Block 7 starts here...

});