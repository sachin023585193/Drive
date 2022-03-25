const form = document.getElementById('form');
const upload_btn = document.getElementById('upload');
const input = document.getElementById('input');
const collapse_btn = document.getElementById('collapse-btn');

upload_btn.addEventListener('click', (e) => {
    e.preventDefault();
    input.click();
});

let formdata;
form.addEventListener('change', (e) => {
    // console.log(e.target.files);
    if (document.querySelector('.collapse.show#collapse') == null) collapse_btn.click();
    let input = document.querySelector('input[name="files"]');
    let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    for (let i = 0; i < input.files.length; i++) {
        formdata = new FormData();
        let { name, size } = input.files[i];
        console.log(name.split('.')[name.split('.').length - 1]);
        formdata.append('csrfmiddlewaretoken', csrf)
        formdata.append('file', input.files[i])
        formdata.append('name', name)
        formdata.append('size', size)
        formdata.append('extension', name.split('.')[name.split('.').length - 1]) //extension of file being sent
        upload(name, formdata)
    }
    // data = {
    //     method: 'POST',
    //     credentials: 'same-origin',
    //     body: formdata,
    // }
    // fetch('', data).then(data => console.log(data))

});

let percent_completed;
let progress_html;
let abort_button;
let request;
const progress_contaienr = document.querySelector('.progress-container');

function upload(name, datas) {
    let file_progress = document.createElement('div');
    file_progress.classList.add('file-progress');
    progress_contaienr.appendChild(file_progress);
    request = new XMLHttpRequest();
    request.open('POST', '');
    // console.log(request);
    request.onload = function(e) {
        //  console.log(e); 
    }
    request.upload.addEventListener('progress', ({ loaded, total }) => {
        percent_completed = (loaded / total) * 100;
        percent_completed = percent_completed.toFixed(1);

        progress_html = `
            <div class="file-name">${name}</div>
            <div class="progress-c">
                <div class="progress-bar" style="width: ${percent_completed}%;"></div>
                <div class="abort-pcompleted">
                    <div class="progress-num">${percent_completed}%</div>
                </div>
            </div>
        `
        if (percent_completed == 100) {
            progress_html = `
            <div class="file-name">${name}</div>
            <div class="progress-c">
                <div class="progress-bar" style="width: ${percent_completed}%;"></div>
                <div class="abort-pcompleted">
                    <div class="progress-num">${percent_completed}%</div>
                    <button title="Uploaded" class="abort-button text-success"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle-fill" viewBox="0 0 16 16">
                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
                  </svg></button>
                </div>
            </div>
        `
        }
        file_progress.innerHTML = progress_html;
        // console.log(percent_completed);
    })
    request.send(datas);
}