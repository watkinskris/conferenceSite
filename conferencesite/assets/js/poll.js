//Say thank you in an alert box after the user has submitted their vote
function voteThankYou(){
    var pollButtonEl = document.getElementsByName("pollButton");  //get all radio buttons with name pollButton
    var objectName;         //name of the equipment user is voting for
    var itemSelected;       //index number of the object voted for
    var voteCount = 0;


    //check to see which item has been selected
    for(var i = 0; i < pollButtonEl.length; i++){
        if(pollButtonEl[i].checked){
            itemSelected = i;
        }
    }
    // take the index number of the selected item and turn it into the items string name
    switch(itemSelected){
        case 0:
            objectName = "The Universal Forensic Extraction Device";
            voteCount = Number((document.getElementById('fedVotes').innerHTML)) + 1;
            document.getElementById('fedVotes').innerHTML = voteCount.toString();
            break;
        case 1:
            objectName = "Digital Mobile Device Kit";
            voteCount = Number((document.getElementById('dmdkVotes').innerHTML)) + 1;
            document.getElementById('dmdkVotes').innerHTML = voteCount.toString();
            break;
        case 2:
            objectName = "Electrostatic Dissipation Bags";
            voteCount = Number((document.getElementById('ebVotes').innerHTML)) + 1;
            document.getElementById('ebVotes').innerHTML = voteCount.toString();
            break;
        case 3:
            objectName = "Write Blocker";
            voteCount = Number((document.getElementById('wbVotes').innerHTML)) + 1;
            document.getElementById('wbVotes').innerHTML = voteCount.toString();
            break;
        default:
            objectName = "none";
    }

    storeCookie();
    alert("Thank you for voting for: "  + objectName + "!");
}

/* retrieves the cookie from the browser if there is one and seperates the key from the value.

   param:  pollCookie - holds the cookie retrieved from the browser
           cookieArray - holds the cookie broken at "="
           seperateCookies - array to hold the cookie after it is split at the ";"
           totals - the value portion of the key value pair in the array

   return:  totals - the value of the cookie
 */

function getCookie(){
    var pollCookie = document.cookie;
    var cookieArray = [];
    var totals = "";
    var keyName = "voteTotals";

    //if there is not a cookie on the page go back to the calling function
    if(pollCookie === ""){
        return totals;
    }
    //else check to see if there are semi colons in the cookie
    else if(pollCookie.indexOf(';') > -1) {
        var seperateCookies = pollCookie.split(';');
        for(var j = 0; j < seperateCookies.length; j++) {
            cookieArray = seperateCookies[j].split("="); // split the retrieved cookie into its key and value and place in array
            var name = cookieArray[0];

            if(name.trim() === keyName.trim()){
                break;
            }//end if
        }//end for
    }//end else if

    //if not, split at the key value pair
    else{
        cookieArray = pollCookie.split("=");// split the retrieved cookie into its key and value and place in array
    }

    for(var i = 0; i < cookieArray.length; i++){
        if(cookieArray[i].trim() === keyName.trim()){
            i++;
            totals = cookieArray[i];
        }// end if
    }//end for

    return totals;
}//end function

/* retrieves the number of votes from each item and stores it in an object

   param:  voteCountObject - an object to hold the values of the vote counts
           votes - an array that will hold the references to the divs holding the vote totals
           objectField - variable to hold the name of the id of the item whose vote total is being collected

   return:  a stringified JSON object
 */

function getCookieValues(){
    var voteCountObject = {};
    var votes = document.getElementsByClassName('voteNumbers');

    for(var i = 0; i < votes.length; i++){
        var itemId = votes[i].getAttribute('id');

        voteCountObject[itemId] = votes[i].innerHTML;
    }
    return JSON.stringify(voteCountObject);
}

/* Accepts the stringified JSON object containing the id of the items and thier vote totals and stores the cookie in the browser

   param:  stringToStore - string parameter holding the stringified JSON object with key value pairs of vote totals

 */

function storeCookie() {
    var stringToStore = getCookieValues();
    document.cookie = "voteTotals=" + stringToStore;

}

function loadVoteTotals(){
    var totals = getCookie();
    var voteContainer = document.getElementsByClassName('voteNumbers');
    var itemId = "";

    if(totals === "") {
        for (var i = 0; i < voteContainer.length; i++) {
            itemId = voteContainer[i].getAttribute('id');
            document.getElementById(itemId).textContent = '0';
        }
    }
    else {
        var cookieStringObject = JSON.parse(totals);

        for (var j = 0; j < voteContainer.length; j++) {
            itemId = voteContainer[j].getAttribute('id');
            document.getElementById(itemId).textContent = cookieStringObject[itemId];
        }
    }
}

window.addEventListener('load', loadVoteTotals, false);
//get submit button from poll page
//var submitButton = document.getElementById('pollSubmit');

//listen for the submit button being pushed
//submitButton.addEventListener('click', voteThankYou, false);
document.getElementById("pollForm").addEventListener("submit", voteThankYou, false);

