function getButtonChoice(radioButtonName) {
    var buttonChoiceEl = document.getElementsByName(radioButtonName);  //get all radio buttons with name passed in from listener
    var itemSelected = "";       //index number of the object voted for


//check to see which item has been selected
    for (var i = 0; i < buttonChoiceEl.length; i++) {
        if (buttonChoiceEl[i].checked) {
            itemSelected = buttonChoiceEl[i].value;
        }
    }
    return itemSelected;
}

function openListPage(radioButtonName){
    var buttonSelected = getButtonChoice(radioButtonName);

    if(buttonSelected === ""){
        alert("No selection has been made.  Please choose which list you would like to view before submitting")
    }
    else{
        window.open("participantlists/" + buttonSelected + ".html", "_blank", "location=0");
    }
}
function goToRegistrantPage(){
    window.open("participantlists/allConference.html", "_blank", "location=0");
}

document.getElementById('workshopListChoice').addEventListener("submit", function(){
    openListPage("workshopChoice");
    }, false);
document.getElementById('mealListForm').addEventListener("submit", function(){
    openListPage("mealChoice");
    }, false);
document.getElementById('allRegistrantsForm').addEventListener("submit", goToRegistrantPage, false);