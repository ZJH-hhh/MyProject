import $ from 'jquery';

export const getjobs = async () => {
    return $.ajax({
        url: 'http://127.0.0.1:8000/api/jobs/',
        type: 'GET',
    });
};

export const postjobs = (jobname, jobauthor) => {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/jobs/',
        type: 'POST',
        data: {
            name: jobname,
            author: jobauthor,
        },
    });
}