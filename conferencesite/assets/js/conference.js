//Workshop B in session 1 covers both the session 1 and session 2 time period, so a session 2 workshop can not be selected
// along with workshop B.  This validates that a selection in session 2 is not allowed if workshop B in session 1 is choosen.
function checkIfB(){
    var workshop1El = document.getElementsByName('workshop1');  // get the radiobuttons from the first session
    var workshop2El = document.getElementsByName('workshop2'); // get the radio buttons from the second session
    var errorMessage = "The \'Investigations Involving Automobile Media\' workshop from session 1 is an all day workshop." +
        "  You can't choose a workshop in session 2 if you will be participating in " +
        "\'Investigations Involving Automobile Media\'";

    workshop2El[0].required = true; // if workshop B is not selected then one workshop in each session must be taken

    if(workshop1El[1].checked) {
        workshop2El[0].required = false;  // if workshop B is selected, a workshop selection in session 2 is not required
        //check to see if a workshop in session 2 has been selected
        for(var j = 0; j < workshop2El.length; j++){
            if(workshop2El[j].checked) {
                errorMessageWindow(errorMessage, 400, 500);

                workshop2El[j].checked = false; //deselect the selected workshop in session 2
            }
        }
    }
}

//According to the requirements, workshop F in session 2 and workshop H in session 3 must be taken together.  This
//function verifies that a participant chooses F and H only when the other is choosen as well.
function checkIfF(){
    var workshop3El = document.getElementsByName('workshop3');  // get the radio buttons from session 3
    var workshop2El = document.getElementsByName('workshop2'); //get the radio buttons from session 2
    var errorMessage = "The \'Security of Biometrics\' workshop from session 2 and the  " +
        "\'Identification and Authentication of Incidents\' workshop from session 3 must be taken together.";

    //if either workshops F or H are selected without the other being selected
        if((workshop2El[2].checked && !workshop3El[1].checked) || (workshop3El[1].checked && !workshop2El[2].checked)){
            //alert("The \'Security of Biometrics\' workshop from session 2 and the  " +
             //   "\'Identification and Authentication of Incidents\' workshop from session 3 must be taken together." )
            errorMessageWindow(errorMessage, 400, 500);
                for(var j = 0; j < workshop3El.length; j++) {
                    workshop3El[j].checked = false; // clear the selected radio button
                }
        }


}

function errorMessageWindow(errorMessage, h, w){
    var top = (screen.height/2)-(h/2);  //center horizontally
    var left = (screen.width/2)-(h/2);  //center vertically
    var errorWindow = window.open("", "", "height="+h+",width="+w+",top="+top+", left="+left+",menubar=no,resizable=0,status=yes,toolbar=no");
    errorWindow.document.writeln("<body bgcolor='#a9a9a9'>");
    errorWindow.document.writeln("</body>");
    errorWindow.document.write(errorMessage);
    errorWindow.document.writeln("<br> <br> <br>");
    errorWindow.document.write("<input type='button' value='close' onclick='window.close()'>");
}

function storeCookie(){

    var stringToStore = getRegValues();                         //get string value for cookie
    document.cookie = "123456=" + stringToStore + "; path=/";  //set cookie
}

function getRegValues(){
    var cookieStringObject = {};   //create an empty javascript object to hold the information for each form field
    var regForm = document.getElementById('registrationForm');  // store the registration form name in a variable

    //add form fields to the object
    cookieStringObject.title = regForm.title.value;
    cookieStringObject.firstName = regForm.firstName.value;
    cookieStringObject.lastName = regForm.lastName.value;
    cookieStringObject.address1 = regForm.address1.value;
    cookieStringObject.address2 = regForm.address2.value;
    cookieStringObject.city = regForm.city.value;
    cookieStringObject.zipcode = regForm.zipcode.value;
    cookieStringObject.usrtel = regForm.usrtel.value;
    cookieStringObject.email = regForm.email.value;
    cookieStringObject.companyName = regForm.companyName.value;
    cookieStringObject.position = regForm.position.value;
    cookieStringObject.companyWebsite = regForm.companyWebsite.value;
    cookieStringObject.mealPlan = regForm.mealPlan.value;
    cookieStringObject.mealPlan2 = regForm.mealPlan2.value;
    cookieStringObject.billingFirst = regForm.billingFirst.value;
    cookieStringObject.billingLast = regForm.billingLast.value;
    cookieStringObject.cardType = regForm.cardType.value;
    cookieStringObject.cardNumber = regForm.cardNumber.value;
    cookieStringObject.csv = regForm.csv.value;
    cookieStringObject.expYear = regForm.expYear.value;
    cookieStringObject.expMonth = regForm.expMonth.value;
    cookieStringObject.workshop1 = regForm.workshop1.value;
    cookieStringObject.workshop2 =  regForm.workshop2.value;
    cookieStringObject.workshop3 = regForm.workshop3.value;

    //take the object and turn it into a string that can be used within the cookie key:value pair;
    //var jsonCookieString = JSON.stringify(cookieStringObject);

    return JSON.stringify(cookieStringObject);

}

function getCookie(){
    var regNum = document.getElementById('registrationNumber');
    var regForm = document.getElementById('registrationForm');  // store the registration form name in a variable
    var cookieString = document.cookie;  // get the cookie
    var cookieArray;                     //array to hold name and value
    //if there is a semicolon delimited list, split apart the list
    if(cookieString.indexOf(';') > -1) {
        var seperateCookies = cookieString.split(';');
        cookieArray = seperateCookies[1].split("="); // split the retrieved cookie into its key and value and place in array
    }
    //if not, split at the key value pair
    else{
        cookieArray = cookieString.split("=");// split the retrieved cookie into its key and value and place in array
    }

    //If registration number is in cookie, fill form fields
    var cookieArrayName = cookieArray[0];
    if(regNum.value.trim() === cookieArrayName.trim()){
        var cookieStringObject = JSON.parse(cookieArray[1]);  //turn string into object
        //set the form fields using the object values
        regForm.title.value = cookieStringObject.title;
        regForm.firstName.value = cookieStringObject.firstName;
        regForm.lastName.value = cookieStringObject.lastName;
        regForm.address1.value = cookieStringObject.address1;
        regForm.address2.value = cookieStringObject.address2;
        regForm.city.value = cookieStringObject.city;
        regForm.zipcode.value = cookieStringObject.zipcode;
        regForm.usrtel.value = cookieStringObject.usrtel;
        regForm.email.value = cookieStringObject.email;
        regForm.companyName.value = cookieStringObject.companyName;
        regForm.position.value = cookieStringObject.position;
        regForm.companyWebsite.value = cookieStringObject.companyWebsite;
        regForm.mealPlan.value = cookieStringObject.mealPlan;
        regForm.mealPlan2.value = cookieStringObject.mealPlan2;
        regForm.billingFirst.value = cookieStringObject.billingFirst;
        regForm.billingLast.value = cookieStringObject.billingLast;
        regForm.cardType.value = cookieStringObject.cardType;
        regForm.cardNumber.value = cookieStringObject.cardNumber;
        regForm.csv.value = cookieStringObject.csv;
        regForm.expYear.value = cookieStringObject.expYear;
        regForm.expMonth.value = cookieStringObject.expMonth;
        regForm.workshop1.value = cookieStringObject.workshop1;
        regForm.workshop2.value = cookieStringObject.workshop2;
        regForm.workshop3.value = cookieStringObject.workshop3;

    }
    else if(!(regNum.value === "")){
        alert("Sorry, there is no match for that registration number.");
        regNum.value = "";
    }

}// end function
//hold each session div in a variable
session1El = document.getElementById('session1');
session2El = document.getElementById('session2');
session3El = document.getElementById('session3');
var registration = document.getElementById('registrationNumber');


//add the event listeners to listen for when a button is selected
session1El.addEventListener('change', checkIfB, false);  //check if workshop B is chosen
session2El.addEventListener('change', checkIfB, false);  //ensure workshop B not chosen
session2El.addEventListener('change', checkIfF, false); //check if workshop F and H selected together
session3El.addEventListener('change', checkIfF, false);  //check if workshop F and H selected together
document.getElementById('registrationForm').addEventListener("submit", storeCookie, false);  //when form submitted store cookie
registration.addEventListener('blur', getCookie, false);  // when registration number is entered compare to cookie