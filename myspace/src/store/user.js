import $ from 'jquery'
import jwt_decode from 'jwt-decode'

const modulesUser = {
    state: {
        id: '',
        username: '',
        photo: '',
        followCounter: 0,
        access: '',
        refresh: '',
        is_login: false,
    },
    getters: {
    },
    mutations: {
        updateUser(state, user) {
            state.id = user.id;
            state.username = user.username;
            state.photo = user.photo;
            state.followCounter = user.followCounter;
            state.access = user.access;
            state.refresh = user.refresh;
            state.is_login = user.is_login;
        },
        updateAccess(state, access) {
            state.access = access;
        },
        logout(state) {
            state.id = '';
            state.username = '';
            state.photo = '';
            state.followCounter = 0;
            state.access = '';
            state.refresh = '';
            state.is_login = false
        }
    },
    actions: {
        login(context, data) {
            $.ajax({
                url: 'https://app165.acapp.acwing.com.cn/api/token/',
                type: 'POST',
                data: {
                    username: data.username,
                    password: data.password,
                },
                success(response) {
                    const { access, refresh } = response;
                    const access_obj = jwt_decode(access);
                    setInterval(() => {
                        $.ajax({
                            url: 'https://app165.acapp.acwing.com.cn/api/token/refresh/',
                            type: 'POST',
                            data: {
                                refresh,
                            },
                            success(response) {
                                context.commit('updateAccess', response.access);
                            }
                        })
                    }, 4.5 * 6 * 1000);
                    $.ajax({
                        url: 'https://app165.acapp.acwing.com.cn/myspace/getinfo/',
                        type: 'GET',
                        data: {
                            user_id: access_obj.user_id,
                        },
                        headers: {
                            'Authorization': 'Bearer ' + access,
                        },
                        success(response) {
                            context.commit('updateUser', {
                                ...response,
                                access: access,
                                refresh: refresh,
                                is_login: true,
                            });
                            data.success();
                        },
                    });
                },
                error() {
                    data.error();
                }
            });
        }
    },
    modules: {
    }
}

export default modulesUser;