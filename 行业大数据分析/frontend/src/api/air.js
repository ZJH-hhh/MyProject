import request from '@/utils/request'

export function getPopular(params) {
    return request({
        url: '/api/getpopular/',
        method: 'GET',
        params
    })
}
