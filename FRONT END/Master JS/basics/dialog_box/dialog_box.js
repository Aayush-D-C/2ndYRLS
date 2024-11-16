// Confirm dialog
var choice = confirm("Do you want to say your name?");
if (choice === false) {
    document.write("Why do you deny it?");
} else {
    // Prompt for name
    var name = prompt("Enter your name:", "Type your name here");
    if (name) {  // Check if user provided a name
        alert("Your name is: " + name);
    } else {
        alert("No name entered.");
    }
}
