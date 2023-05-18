import $ from 'jquery';

export const getjobs = () => {
    // let res;
    $.ajax({
        url: 'http://127.0.0.1:8000/api/jobs/',
        type: 'GET',
        success(response) {
            console.log(response);
        }
    });

    // return res;
}

export const postjobs = (jobname, jobauthor) => {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/jobs/',
        type: 'POST',
        data: {
            name: jobname,
            author: jobauthor,
        },
        succecss(response) {
            console.log(response);
        }
    });
}