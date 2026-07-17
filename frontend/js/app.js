// ========================================
// Shared Utility Functions
// Used by:
// - tutor.js
// - calculator.js
// - tracker.js
// ========================================



// ========================================
// Update Answer Box
// ========================================

function updateAnswer(message) {

    document.getElementById("answer").innerHTML = message;

}



// ========================================
// Show Loading Message
// ========================================

function showLoading() {

    updateAnswer("Loading...");

}



// ========================================
// Show Error Message
// ========================================

function showError(message) {

    updateAnswer("❌ " + message);

}



// ========================================
// Clear Answer Box
// ========================================

function clearAnswer() {

    updateAnswer("");

}



// ========================================
// Get HTML Element by ID
// ========================================

function getElement(id) {

    return document.getElementById(id);

}