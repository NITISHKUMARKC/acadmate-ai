// ========================================
// Tutor Elements
// ========================================

const askButton = getElement("askBtn");
const subjectSelect = getElement("subject");
const questionInput = getElement("question");

// ========================================
// Ask Button Click Event
// ========================================

askButton.addEventListener("click", async function () {

    // ------------------------------------
    // Read User Input
    // ------------------------------------

    const subject = subjectSelect.value.trim();
    const question = questionInput.value.trim();

    // ------------------------------------
    // Input Validation
    // ------------------------------------

    if (question === "") {

        showError("Please enter your question.");

        return;

    }

    // ------------------------------------
    // Show Loading Message
    // ------------------------------------

    showLoading();

    try {

        // ------------------------------------
        // Send Request to Backend
        // ------------------------------------

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

        // ------------------------------------
        // Convert Response to JSON
        // ------------------------------------

        const result = await response.json();

        // ------------------------------------
        // Check Response Status
        // ------------------------------------

        if (response.ok) {

            updateAnswer(result.answer);

        } else {

            showError(result.detail || "Something went wrong.");

        }

    }

    // ------------------------------------
    // Handle Connection Errors
    // ------------------------------------

    catch (error) {

        console.error(error);

        showError("Unable to connect to the backend server.");

    }

});