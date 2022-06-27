const video = document.querySelector('#video');
const canvas = document.querySelector('#canvas');
const context = canvas.getContext('2d');

let faces = [];


window.addEventListener('load', ev => {
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices
            .getUserMedia({ video: true, audio: false })
            .then(stream => {
                video.srcObject = stream;
                sendImage();
            })
            .catch(error => {
                alert("Stream not started.");
            });
    }
    window.requestAnimationFrame(renderFrame);
});

function renderFrame() {
    if (video.readyState === video.HAVE_ENOUGH_DATA) {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0);
        faces.forEach(({ x, y, w, h, label, score }) => {
            context.strokeRect(x, y, w, h);
            context.fillText(`${label} (${score})`, x + 5, y + 15);
        });
    }
    window.requestAnimationFrame(renderFrame);
}

function sendImage() {
    const dataURL = canvas.toDataURL();
    axios.post('/api/image', { dataURL })
        .then(response => handleData(response.data))
        .catch(error => handleError(error));
}

function handleData(data) {
    faces = data;
    sendImage();
}

function handleError(error) {
    faces = [];
    setTimeout(sendImage, 1000);
}