// ========================================
// Shared Utility Functions
// ========================================

function getElement(id) {
    return document.getElementById(id);
}

function updateAnswer(message) {
    getElement("answer").innerHTML = message;
}

function showLoading() {
    updateAnswer("Loading...");
}

function showError(message) {
    updateAnswer(message);
}