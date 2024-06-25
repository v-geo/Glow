<<<<<<< HEAD
import { sendNewUserProf } from './ajax/send-new-userprofile.js';
import { UploadProf, Profile_URL } from './modal/upload-profile.js'; 

=======
>>>>>>> 81396d173fbc83a724cab1e1868c7a58497b0e17
let Modal1 = document.getElementById('PopUp-Container1');
let Modal2 = document.getElementById('PopUp-Container2');
let Modal3 = document.getElementById('PopUp-Container3');
let Modal1Button = document.getElementById('Modal1-Button');
<<<<<<< HEAD
let Modal3Button = document.getElementById('Modal3-Button');
let cameraprof = document.getElementById('camera-prof');
let PopUpOverlay = document.getElementById('PopUp-Overlay');
let nwsubmit = document.getElementById('nw-submit');
let nwProfilepic = document.getElementById('nw-profilepic');
let nwfname = document.getElementById('nw-fname');
let nwlname = document.getElementById('nw-lname');
let nwgender = document.getElementById('nw-gender');
let nwbirthday = document.getElementById('nw-birthday');
let messagebox = document.getElementById('message-box');

let firstname = nwfname.value.trim();
let lastname = nwlname.value.trim();
let birthday = nwbirthday.value.trim();
let gender = nwgender.value.trim();
let Profile_url = ''; 
let Modals = [Modal1, Modal2, Modal3];


PopUpOverlay.style.display = "flex";

cameraprof.addEventListener('click', async () => {
    UploadProf(); 
});

Modal1Button.addEventListener('click', async () => {
    const { switchModal } = await import("./modal/new-user.js");
    switchModal(Modal2, Modals);
});


nwfname.addEventListener('input', function () {
    firstname = nwfname.value; 
});

nwbirthday.addEventListener('input', function () {
    birthday = nwbirthday.value; 
});
nwlname.addEventListener('input', function () {
    lastname = nwlname.value;
});

nwgender.addEventListener('change', function () {
    gender = nwgender.value; 
});

function calculateAge(birthday) {
    const today = new Date();
    const birthDate = new Date(birthday);
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}

nwbirthday.addEventListener('input', function () {
    birthday = nwbirthday.value.trim();

    if (birthday !== '') {
        const age = calculateAge(birthday);
        if (age < 13) {
            messagebox.textContent = "You must be at least 13 years old to create an account.";
            nwbirthday.value = ''; 
            return;
        }
    }
});

nwsubmit.addEventListener('click', async () => {

    if (firstname === '') {
        messagebox.textContent = "First name is required";
        return; 
    }
    if (lastname === '') {
        messagebox.textContent = "Last name is required";
        return;
    }
    if (birthday === '') {
        messagebox.textContent = "Birthday is required";
        return; 
    }
    if (gender === '') {
        messagebox.textContent = "Gender is required";
        return; 
    }

    const age = calculateAge(birthday);
    if (age < 13) {
        messagebox.textContent = "You must be at least 13 years old to create an account.";
        return;
    }

    Profile_url = Profile_URL(); 
    
    let nwObject = {
        firstname: firstname,
        lastname: lastname,
        gender: gender,
        profile: Profile_url || '../static/images/default-avatar-profile-picture-male-icon.png',
        birthday: birthday,
    };

    console.log(nwObject);
    sendNewUserProf(nwObject);
    
});
=======
let cameraprof = document.getElementById('camera-prof');
let PopUpOverlay = document.getElementById('PopUp-Overlay');

let Modals = [Modal1, Modal2, Modal3];
PopUpOverlay.style.display = "flex";

cameraprof.addEventListener('click', async () => {
    const { UploadProf } = await import ("./modal/upload-profile.js");
    UploadProf();
});


Modal1Button.addEventListener('click', async() =>{
    const { switchModal } = await import ("./modal/new-user.js")

    switchModal(Modal2, Modals);
})



>>>>>>> 81396d173fbc83a724cab1e1868c7a58497b0e17
