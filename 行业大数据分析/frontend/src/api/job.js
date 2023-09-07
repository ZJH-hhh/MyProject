import $ from 'jquery';

const header = 'http://127.0.0.1:8000/api/';

export function test() {
    return $.ajax({
        url: header + 'test/',
        type: 'GET',
        success: response => {
            return response;
        }
    })
}

export function assess() {
    return $.ajax({
        url: header + 'assess/',
        type: 'GET',
        success: response => {
            return response;
        }
    })
}

export function typeScore() {
    return $.ajax({
        url: header + 'typescore/',
        type: 'GET',
        success: response => {
            return response;
        }
    })
}