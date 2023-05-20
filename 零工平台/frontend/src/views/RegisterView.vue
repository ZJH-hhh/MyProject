<template>
    <div class="register">
        <img src="https://img01.sc115.com/uploads3/sc/jpgs/2007/apic26734_sc115.com.jpg" alt="">
        <div class="row justify-content-md-center">
            <div class="col-4">
                <form @submit.prevent="register">
                    <div class="mb-3">
                        <label for="username" class="form-label">用户名</label>
                        <input v-model="username" type="texdt" class="form-control" id="username">
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">邮箱</label>
                        <input v-model="email" type="email" class="form-control" id="email">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">密码</label>
                        <input v-model="password" type="password" class="form-control" id="password">
                    </div>
                    <div class="mb-3">
                        <label for="password_confirm" class="form-label">确认密码</label>
                        <input v-model="password_confirm" type="password" class="form-control" id="password">
                    </div>
                    <div class="error-message">{{ error_message }}</div>
                    <button type="submit" class="btn btn-primary">注册</button>
                    <a class="login-btn" href="/gigplatform/login/">登录</a>
                </form>
            </div>
        </div>
    </div>
</template>
  
<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';
import $ from 'jquery';

export default {
    name: 'RegisterView',
    components: { // 表示在template中会用到哪些其他的组件
    },
    setup() {
        const store = useStore();
        let username = ref('');
        let email = ref('');
        let password = ref('');
        let password_confirm = ref('');
        let error_message = ref('');

        const register = () => {
            error_message.value = "";
            $.ajax({
                url: 'http://127.0.0.1:8000/api/register/',
                type: 'POST',
                data: {
                    username: username.value,
                    email: email.value,
                    password: password.value,
                    password_confirm: password_confirm.value,
                },
                success: response => {
                    if (response.result === 'success') {
                        store.dispatch("login", {
                            username: username.value,
                            password: password.value,
                            success() {
                                router.push({ name: 'home', });
                            },
                            error() {
                                error_message.value = '用户名或密码错误';
                            }
                        });
                    } else {
                        error_message.value = response.result;
                    }
                }
            })
        };

        return {
            username,
            email,
            password,
            password_confirm,
            error_message,
            register,
        }
    }
}
</script>
  
<style scoped>
.register {
    position: relative;
    display: inline-block;
}

button {
    width: 100%;
}

.error-message {
    color: red;
}

.login-btn {
    margin-top: 10px;
    float: right;
    cursor: pointer;
    text-decoration: none;
    color: black;
}

img {
    width: 100vw;
    height: 100vh;
}

.error-message {
    color: red;
}

.justify-content-md-center {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
  